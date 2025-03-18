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
        """
        @summary Adds existing Elastic Compute Service (ECS) instances to a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AttachInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def attach_instances_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.AttachInstancesResponse:
        """
        @summary Adds existing Elastic Compute Service (ECS) instances to a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AttachInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def attach_instances(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
    ) -> cs20151215_models.AttachInstancesResponse:
        """
        @summary Adds existing Elastic Compute Service (ECS) instances to a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_instances_with_options(cluster_id, request, headers, runtime)

    async def attach_instances_async(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
    ) -> cs20151215_models.AttachInstancesResponse:
        """
        @summary Adds existing Elastic Compute Service (ECS) instances to a Container Service for Kubernetes (ACK) cluster.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        """
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
        """
        @summary Adds existing nodes to a specific node pool. You can add existing ECS instances to a specific node pool in a Container Service for Kubernetes (ACK) cluster as worker nodes. You can also add removed worker nodes back to the node pool.
        
        @param request: AttachInstancesToNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesToNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesToNodePoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesToNodePoolResponse(),
                self.execute(params, req, runtime)
            )

    async def attach_instances_to_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.AttachInstancesToNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.AttachInstancesToNodePoolResponse:
        """
        @summary Adds existing nodes to a specific node pool. You can add existing ECS instances to a specific node pool in a Container Service for Kubernetes (ACK) cluster as worker nodes. You can also add removed worker nodes back to the node pool.
        
        @param request: AttachInstancesToNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesToNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesToNodePoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.AttachInstancesToNodePoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def attach_instances_to_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.AttachInstancesToNodePoolRequest,
    ) -> cs20151215_models.AttachInstancesToNodePoolResponse:
        """
        @summary Adds existing nodes to a specific node pool. You can add existing ECS instances to a specific node pool in a Container Service for Kubernetes (ACK) cluster as worker nodes. You can also add removed worker nodes back to the node pool.
        
        @param request: AttachInstancesToNodePoolRequest
        @return: AttachInstancesToNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_instances_to_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def attach_instances_to_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.AttachInstancesToNodePoolRequest,
    ) -> cs20151215_models.AttachInstancesToNodePoolResponse:
        """
        @summary Adds existing nodes to a specific node pool. You can add existing ECS instances to a specific node pool in a Container Service for Kubernetes (ACK) cluster as worker nodes. You can also add removed worker nodes back to the node pool.
        
        @param request: AttachInstancesToNodePoolRequest
        @return: AttachInstancesToNodePoolResponse
        """
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
        @deprecated OpenAPI CancelClusterUpgrade is deprecated
        
        @summary You can call the CancelClusterUpgrade operation to cancel the update of a cluster.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelClusterUpgradeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelClusterUpgradeResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        """
        @deprecated OpenAPI CancelClusterUpgrade is deprecated
        
        @summary You can call the CancelClusterUpgrade operation to cancel the update of a cluster.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelClusterUpgradeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelClusterUpgradeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        """
        @deprecated OpenAPI CancelClusterUpgrade is deprecated
        
        @summary You can call the CancelClusterUpgrade operation to cancel the update of a cluster.
        
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
        @deprecated OpenAPI CancelClusterUpgrade is deprecated
        
        @summary You can call the CancelClusterUpgrade operation to cancel the update of a cluster.
        
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
        """
        @deprecated OpenAPI CancelComponentUpgrade is deprecated
        
        @summary You can call the CancelComponentUpgrade operation to cancel the update of a component.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelComponentUpgradeResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelComponentUpgradeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelComponentUpgradeResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_component_upgrade_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelComponentUpgradeResponse:
        """
        @deprecated OpenAPI CancelComponentUpgrade is deprecated
        
        @summary You can call the CancelComponentUpgrade operation to cancel the update of a component.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelComponentUpgradeResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelComponentUpgradeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelComponentUpgradeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_component_upgrade(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.CancelComponentUpgradeResponse:
        """
        @deprecated OpenAPI CancelComponentUpgrade is deprecated
        
        @summary You can call the CancelComponentUpgrade operation to cancel the update of a component.
        
        @return: CancelComponentUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_component_upgrade_with_options(cluster_id, component_id, headers, runtime)

    async def cancel_component_upgrade_async(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.CancelComponentUpgradeResponse:
        """
        @deprecated OpenAPI CancelComponentUpgrade is deprecated
        
        @summary You can call the CancelComponentUpgrade operation to cancel the update of a component.
        
        @return: CancelComponentUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_component_upgrade_with_options_async(cluster_id, component_id, headers, runtime)

    def cancel_operation_plan_with_options(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        """
        @summary You can call the CancelOperationPlan operation to cancel a pending auto O\\\\\\\\\\\\&M plan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelOperationPlanResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelOperationPlanResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelOperationPlanResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_operation_plan_with_options_async(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        """
        @summary You can call the CancelOperationPlan operation to cancel a pending auto O\\\\\\\\\\\\&M plan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelOperationPlanResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelOperationPlanResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelOperationPlanResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_operation_plan(
        self,
        plan_id: str,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        """
        @summary You can call the CancelOperationPlan operation to cancel a pending auto O\\\\\\\\\\\\&M plan.
        
        @return: CancelOperationPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_operation_plan_with_options(plan_id, headers, runtime)

    async def cancel_operation_plan_async(
        self,
        plan_id: str,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        """
        @summary You can call the CancelOperationPlan operation to cancel a pending auto O\\\\\\\\\\\\&M plan.
        
        @return: CancelOperationPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_operation_plan_with_options_async(plan_id, headers, runtime)

    def cancel_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelTaskResponse:
        """
        @summary Cancels the execution of a cluster task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelTaskResponse:
        """
        @summary Cancels the execution of a cluster task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CancelTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CancelTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_task(
        self,
        task_id: str,
    ) -> cs20151215_models.CancelTaskResponse:
        """
        @summary Cancels the execution of a cluster task.
        
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(task_id, headers, runtime)

    async def cancel_task_async(
        self,
        task_id: str,
    ) -> cs20151215_models.CancelTaskResponse:
        """
        @summary Cancels the execution of a cluster task.
        
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(task_id, headers, runtime)

    def check_control_plane_log_enable_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        """
        @summary Queries the current log configuration of control plane components, including the log retention period and the log collection component. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube API Server, Kube Scheduler, Kube Controller Manager, and Cloud Controller Manager.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckControlPlaneLogEnableResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CheckControlPlaneLogEnableResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CheckControlPlaneLogEnableResponse(),
                self.execute(params, req, runtime)
            )

    async def check_control_plane_log_enable_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        """
        @summary Queries the current log configuration of control plane components, including the log retention period and the log collection component. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube API Server, Kube Scheduler, Kube Controller Manager, and Cloud Controller Manager.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckControlPlaneLogEnableResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CheckControlPlaneLogEnableResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CheckControlPlaneLogEnableResponse(),
                await self.execute_async(params, req, runtime)
            )

    def check_control_plane_log_enable(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        """
        @summary Queries the current log configuration of control plane components, including the log retention period and the log collection component. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube API Server, Kube Scheduler, Kube Controller Manager, and Cloud Controller Manager.
        
        @return: CheckControlPlaneLogEnableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_control_plane_log_enable_with_options(cluster_id, headers, runtime)

    async def check_control_plane_log_enable_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        """
        @summary Queries the current log configuration of control plane components, including the log retention period and the log collection component. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube API Server, Kube Scheduler, Kube Controller Manager, and Cloud Controller Manager.
        
        @return: CheckControlPlaneLogEnableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_control_plane_log_enable_with_options_async(cluster_id, headers, runtime)

    def check_service_role_with_options(
        self,
        request: cs20151215_models.CheckServiceRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CheckServiceRoleResponse:
        """
        @summary Checks whether the specified service roles are granted to Container Service for Kubernetes (ACK) within the current Alibaba Cloud account. ACK can access other cloud services, such as Elastic Compute Service (ECS), Object Storage Service (OSS), File Storage NAS (NAS), and Server Load Balancer (SLB), only after ACK is assigned the required service roles.
        
        @param request: CheckServiceRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.roles):
            body['roles'] = request.roles
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckServiceRole',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/ram/check-service-role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CheckServiceRoleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CheckServiceRoleResponse(),
                self.execute(params, req, runtime)
            )

    async def check_service_role_with_options_async(
        self,
        request: cs20151215_models.CheckServiceRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CheckServiceRoleResponse:
        """
        @summary Checks whether the specified service roles are granted to Container Service for Kubernetes (ACK) within the current Alibaba Cloud account. ACK can access other cloud services, such as Elastic Compute Service (ECS), Object Storage Service (OSS), File Storage NAS (NAS), and Server Load Balancer (SLB), only after ACK is assigned the required service roles.
        
        @param request: CheckServiceRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.roles):
            body['roles'] = request.roles
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckServiceRole',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/ram/check-service-role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CheckServiceRoleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CheckServiceRoleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def check_service_role(
        self,
        request: cs20151215_models.CheckServiceRoleRequest,
    ) -> cs20151215_models.CheckServiceRoleResponse:
        """
        @summary Checks whether the specified service roles are granted to Container Service for Kubernetes (ACK) within the current Alibaba Cloud account. ACK can access other cloud services, such as Elastic Compute Service (ECS), Object Storage Service (OSS), File Storage NAS (NAS), and Server Load Balancer (SLB), only after ACK is assigned the required service roles.
        
        @param request: CheckServiceRoleRequest
        @return: CheckServiceRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_service_role_with_options(request, headers, runtime)

    async def check_service_role_async(
        self,
        request: cs20151215_models.CheckServiceRoleRequest,
    ) -> cs20151215_models.CheckServiceRoleResponse:
        """
        @summary Checks whether the specified service roles are granted to Container Service for Kubernetes (ACK) within the current Alibaba Cloud account. ACK can access other cloud services, such as Elastic Compute Service (ECS), Object Storage Service (OSS), File Storage NAS (NAS), and Server Load Balancer (SLB), only after ACK is assigned the required service roles.
        
        @param request: CheckServiceRoleRequest
        @return: CheckServiceRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_service_role_with_options_async(request, headers, runtime)

    def clean_cluster_user_permissions_with_options(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.CleanClusterUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CleanClusterUserPermissionsResponse:
        """
        @summary Deletes kubeconfig files that may pose potential risks from a user and revokes Role-Based Access Control (RBAC) permissions on a cluster.
        
        @description >
        To call this operation, make sure that you have the AliyunCSFullAccess permission.
        You cannot revoke the permissions of an Alibaba Cloud account.
        You cannot revoke the permissions of the account that you use to call this operation.
        
        @param request: CleanClusterUserPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CleanClusterUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CleanClusterUserPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/cluster/{OpenApiUtilClient.get_encode_param(cluster_id)}/user/{OpenApiUtilClient.get_encode_param(uid)}/permissions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CleanClusterUserPermissionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CleanClusterUserPermissionsResponse(),
                self.execute(params, req, runtime)
            )

    async def clean_cluster_user_permissions_with_options_async(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.CleanClusterUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CleanClusterUserPermissionsResponse:
        """
        @summary Deletes kubeconfig files that may pose potential risks from a user and revokes Role-Based Access Control (RBAC) permissions on a cluster.
        
        @description >
        To call this operation, make sure that you have the AliyunCSFullAccess permission.
        You cannot revoke the permissions of an Alibaba Cloud account.
        You cannot revoke the permissions of the account that you use to call this operation.
        
        @param request: CleanClusterUserPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CleanClusterUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CleanClusterUserPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/cluster/{OpenApiUtilClient.get_encode_param(cluster_id)}/user/{OpenApiUtilClient.get_encode_param(uid)}/permissions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CleanClusterUserPermissionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CleanClusterUserPermissionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def clean_cluster_user_permissions(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.CleanClusterUserPermissionsRequest,
    ) -> cs20151215_models.CleanClusterUserPermissionsResponse:
        """
        @summary Deletes kubeconfig files that may pose potential risks from a user and revokes Role-Based Access Control (RBAC) permissions on a cluster.
        
        @description >
        To call this operation, make sure that you have the AliyunCSFullAccess permission.
        You cannot revoke the permissions of an Alibaba Cloud account.
        You cannot revoke the permissions of the account that you use to call this operation.
        
        @param request: CleanClusterUserPermissionsRequest
        @return: CleanClusterUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clean_cluster_user_permissions_with_options(cluster_id, uid, request, headers, runtime)

    async def clean_cluster_user_permissions_async(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.CleanClusterUserPermissionsRequest,
    ) -> cs20151215_models.CleanClusterUserPermissionsResponse:
        """
        @summary Deletes kubeconfig files that may pose potential risks from a user and revokes Role-Based Access Control (RBAC) permissions on a cluster.
        
        @description >
        To call this operation, make sure that you have the AliyunCSFullAccess permission.
        You cannot revoke the permissions of an Alibaba Cloud account.
        You cannot revoke the permissions of the account that you use to call this operation.
        
        @param request: CleanClusterUserPermissionsRequest
        @return: CleanClusterUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clean_cluster_user_permissions_with_options_async(cluster_id, uid, request, headers, runtime)

    def clean_user_permissions_with_options(
        self,
        uid: str,
        tmp_req: cs20151215_models.CleanUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CleanUserPermissionsResponse:
        """
        @summary You can call the CleanUserPermissions operation to delete the kubeconfig files of the specified users and revoke the relevant Role-Based Access Control (RBAC) permissions. This API operation is suitable for scenarios where employees have resigned or the accounts of employees are locked.
        
        @description > - To call this operation, make sure that you have the AliyunCSFullAccess permission.
        > - You cannot revoke the permissions of an Alibaba Cloud account.
        > - You cannot revoke the permissions of the account that you use to call this operation.
        
        @param tmp_req: CleanUserPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CleanUserPermissionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.CleanUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CleanUserPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/users/{OpenApiUtilClient.get_encode_param(uid)}/permissions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CleanUserPermissionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CleanUserPermissionsResponse(),
                self.execute(params, req, runtime)
            )

    async def clean_user_permissions_with_options_async(
        self,
        uid: str,
        tmp_req: cs20151215_models.CleanUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CleanUserPermissionsResponse:
        """
        @summary You can call the CleanUserPermissions operation to delete the kubeconfig files of the specified users and revoke the relevant Role-Based Access Control (RBAC) permissions. This API operation is suitable for scenarios where employees have resigned or the accounts of employees are locked.
        
        @description > - To call this operation, make sure that you have the AliyunCSFullAccess permission.
        > - You cannot revoke the permissions of an Alibaba Cloud account.
        > - You cannot revoke the permissions of the account that you use to call this operation.
        
        @param tmp_req: CleanUserPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CleanUserPermissionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.CleanUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CleanUserPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/users/{OpenApiUtilClient.get_encode_param(uid)}/permissions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CleanUserPermissionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CleanUserPermissionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def clean_user_permissions(
        self,
        uid: str,
        request: cs20151215_models.CleanUserPermissionsRequest,
    ) -> cs20151215_models.CleanUserPermissionsResponse:
        """
        @summary You can call the CleanUserPermissions operation to delete the kubeconfig files of the specified users and revoke the relevant Role-Based Access Control (RBAC) permissions. This API operation is suitable for scenarios where employees have resigned or the accounts of employees are locked.
        
        @description > - To call this operation, make sure that you have the AliyunCSFullAccess permission.
        > - You cannot revoke the permissions of an Alibaba Cloud account.
        > - You cannot revoke the permissions of the account that you use to call this operation.
        
        @param request: CleanUserPermissionsRequest
        @return: CleanUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clean_user_permissions_with_options(uid, request, headers, runtime)

    async def clean_user_permissions_async(
        self,
        uid: str,
        request: cs20151215_models.CleanUserPermissionsRequest,
    ) -> cs20151215_models.CleanUserPermissionsResponse:
        """
        @summary You can call the CleanUserPermissions operation to delete the kubeconfig files of the specified users and revoke the relevant Role-Based Access Control (RBAC) permissions. This API operation is suitable for scenarios where employees have resigned or the accounts of employees are locked.
        
        @description > - To call this operation, make sure that you have the AliyunCSFullAccess permission.
        > - You cannot revoke the permissions of an Alibaba Cloud account.
        > - You cannot revoke the permissions of the account that you use to call this operation.
        
        @param request: CleanUserPermissionsRequest
        @return: CleanUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clean_user_permissions_with_options_async(uid, request, headers, runtime)

    def create_autoscaling_config_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        """
        @summary Creates a scaling configuration to allow the system to scale resources based on the given scaling rules. When you create a scaling configuration, you can specify the scaling metrics, thresholds, scaling order, and scaling interval.
        
        @param request: CreateAutoscalingConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoscalingConfigResponse
        """
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
        if not UtilClient.is_unset(request.priorities):
            body['priorities'] = request.priorities
        if not UtilClient.is_unset(request.recycle_node_deletion_enabled):
            body['recycle_node_deletion_enabled'] = request.recycle_node_deletion_enabled
        if not UtilClient.is_unset(request.scale_down_enabled):
            body['scale_down_enabled'] = request.scale_down_enabled
        if not UtilClient.is_unset(request.scale_up_from_zero):
            body['scale_up_from_zero'] = request.scale_up_from_zero
        if not UtilClient.is_unset(request.scaler_type):
            body['scaler_type'] = request.scaler_type
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateAutoscalingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateAutoscalingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def create_autoscaling_config_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        """
        @summary Creates a scaling configuration to allow the system to scale resources based on the given scaling rules. When you create a scaling configuration, you can specify the scaling metrics, thresholds, scaling order, and scaling interval.
        
        @param request: CreateAutoscalingConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoscalingConfigResponse
        """
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
        if not UtilClient.is_unset(request.priorities):
            body['priorities'] = request.priorities
        if not UtilClient.is_unset(request.recycle_node_deletion_enabled):
            body['recycle_node_deletion_enabled'] = request.recycle_node_deletion_enabled
        if not UtilClient.is_unset(request.scale_down_enabled):
            body['scale_down_enabled'] = request.scale_down_enabled
        if not UtilClient.is_unset(request.scale_up_from_zero):
            body['scale_up_from_zero'] = request.scale_up_from_zero
        if not UtilClient.is_unset(request.scaler_type):
            body['scaler_type'] = request.scaler_type
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateAutoscalingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateAutoscalingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_autoscaling_config(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        """
        @summary Creates a scaling configuration to allow the system to scale resources based on the given scaling rules. When you create a scaling configuration, you can specify the scaling metrics, thresholds, scaling order, and scaling interval.
        
        @param request: CreateAutoscalingConfigRequest
        @return: CreateAutoscalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_autoscaling_config_with_options(cluster_id, request, headers, runtime)

    async def create_autoscaling_config_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        """
        @summary Creates a scaling configuration to allow the system to scale resources based on the given scaling rules. When you create a scaling configuration, you can specify the scaling metrics, thresholds, scaling order, and scaling interval.
        
        @param request: CreateAutoscalingConfigRequest
        @return: CreateAutoscalingConfigResponse
        """
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
        @summary Creates a Container Service for Kubernetes (ACK) cluster. For example, you can create an ACK managed cluster, ACK Serverless cluster, ACK Edge cluster, or registered cluster. When you create an ACK cluster, you need to configure the cluster information, components, and cloud resources used by ACK.
        
        @description ### [](#-openapi-)Generate API request parameters in the ACK console
        When you fail to create an ACK cluster by calling the CreateCluster operation due to invalid parameter settings, you can generate valid API request parameters in the ACK console. Procedure:
        1.  Log on to the [ACK console](javascript:void\\(0\\)). In the left-side navigation pane, click *Clusters**.
        2.  On the *Cluster** page, click **Cluster Templates**.
        3.  In the Select Cluster Template dialog box, select the type of cluster that you want to create and click Create. Then, configure the cluster setting parameters.
        4.  After you configure the cluster parameters, click *Generate API Request Parameters** in the **Confirm Order** step.
        The API request parameters are displayed in the API Request Parameters dialog box.
        
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
        if not UtilClient.is_unset(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['auto_renew_period'] = request.auto_renew_period
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
        if not UtilClient.is_unset(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
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
        if not UtilClient.is_unset(request.load_balancer_id):
            body['load_balancer_id'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_spec):
            body['load_balancer_spec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.logging_type):
            body['logging_type'] = request.logging_type
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
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
        if not UtilClient.is_unset(request.operation_policy):
            body['operation_policy'] = request.operation_policy
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
        if not UtilClient.is_unset(request.security_hardening_os):
            body['security_hardening_os'] = request.security_hardening_os
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
        if not UtilClient.is_unset(request.zone_ids):
            body['zone_ids'] = request.zone_ids
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def create_cluster_with_options_async(
        self,
        request: cs20151215_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterResponse:
        """
        @summary Creates a Container Service for Kubernetes (ACK) cluster. For example, you can create an ACK managed cluster, ACK Serverless cluster, ACK Edge cluster, or registered cluster. When you create an ACK cluster, you need to configure the cluster information, components, and cloud resources used by ACK.
        
        @description ### [](#-openapi-)Generate API request parameters in the ACK console
        When you fail to create an ACK cluster by calling the CreateCluster operation due to invalid parameter settings, you can generate valid API request parameters in the ACK console. Procedure:
        1.  Log on to the [ACK console](javascript:void\\(0\\)). In the left-side navigation pane, click *Clusters**.
        2.  On the *Cluster** page, click **Cluster Templates**.
        3.  In the Select Cluster Template dialog box, select the type of cluster that you want to create and click Create. Then, configure the cluster setting parameters.
        4.  After you configure the cluster parameters, click *Generate API Request Parameters** in the **Confirm Order** step.
        The API request parameters are displayed in the API Request Parameters dialog box.
        
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
        if not UtilClient.is_unset(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['auto_renew_period'] = request.auto_renew_period
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
        if not UtilClient.is_unset(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
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
        if not UtilClient.is_unset(request.load_balancer_id):
            body['load_balancer_id'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_spec):
            body['load_balancer_spec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.logging_type):
            body['logging_type'] = request.logging_type
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
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
        if not UtilClient.is_unset(request.operation_policy):
            body['operation_policy'] = request.operation_policy
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
        if not UtilClient.is_unset(request.security_hardening_os):
            body['security_hardening_os'] = request.security_hardening_os
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
        if not UtilClient.is_unset(request.zone_ids):
            body['zone_ids'] = request.zone_ids
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_cluster(
        self,
        request: cs20151215_models.CreateClusterRequest,
    ) -> cs20151215_models.CreateClusterResponse:
        """
        @summary Creates a Container Service for Kubernetes (ACK) cluster. For example, you can create an ACK managed cluster, ACK Serverless cluster, ACK Edge cluster, or registered cluster. When you create an ACK cluster, you need to configure the cluster information, components, and cloud resources used by ACK.
        
        @description ### [](#-openapi-)Generate API request parameters in the ACK console
        When you fail to create an ACK cluster by calling the CreateCluster operation due to invalid parameter settings, you can generate valid API request parameters in the ACK console. Procedure:
        1.  Log on to the [ACK console](javascript:void\\(0\\)). In the left-side navigation pane, click *Clusters**.
        2.  On the *Cluster** page, click **Cluster Templates**.
        3.  In the Select Cluster Template dialog box, select the type of cluster that you want to create and click Create. Then, configure the cluster setting parameters.
        4.  After you configure the cluster parameters, click *Generate API Request Parameters** in the **Confirm Order** step.
        The API request parameters are displayed in the API Request Parameters dialog box.
        
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
        @summary Creates a Container Service for Kubernetes (ACK) cluster. For example, you can create an ACK managed cluster, ACK Serverless cluster, ACK Edge cluster, or registered cluster. When you create an ACK cluster, you need to configure the cluster information, components, and cloud resources used by ACK.
        
        @description ### [](#-openapi-)Generate API request parameters in the ACK console
        When you fail to create an ACK cluster by calling the CreateCluster operation due to invalid parameter settings, you can generate valid API request parameters in the ACK console. Procedure:
        1.  Log on to the [ACK console](javascript:void\\(0\\)). In the left-side navigation pane, click *Clusters**.
        2.  On the *Cluster** page, click **Cluster Templates**.
        3.  In the Select Cluster Template dialog box, select the type of cluster that you want to create and click Create. Then, configure the cluster setting parameters.
        4.  After you configure the cluster parameters, click *Generate API Request Parameters** in the **Confirm Order** step.
        The API request parameters are displayed in the API Request Parameters dialog box.
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(request, headers, runtime)

    def create_cluster_diagnosis_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterDiagnosisResponse:
        """
        @summary Starts a cluster diagnostic.
        
        @param request: CreateClusterDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterDiagnosisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterDiagnosis',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/diagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateClusterDiagnosisResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateClusterDiagnosisResponse(),
                self.execute(params, req, runtime)
            )

    async def create_cluster_diagnosis_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterDiagnosisResponse:
        """
        @summary Starts a cluster diagnostic.
        
        @param request: CreateClusterDiagnosisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterDiagnosisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterDiagnosis',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/diagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateClusterDiagnosisResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateClusterDiagnosisResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_cluster_diagnosis(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterDiagnosisRequest,
    ) -> cs20151215_models.CreateClusterDiagnosisResponse:
        """
        @summary Starts a cluster diagnostic.
        
        @param request: CreateClusterDiagnosisRequest
        @return: CreateClusterDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_diagnosis_with_options(cluster_id, request, headers, runtime)

    async def create_cluster_diagnosis_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterDiagnosisRequest,
    ) -> cs20151215_models.CreateClusterDiagnosisResponse:
        """
        @summary Starts a cluster diagnostic.
        
        @param request: CreateClusterDiagnosisRequest
        @return: CreateClusterDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_diagnosis_with_options_async(cluster_id, request, headers, runtime)

    def create_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        """
        @summary Creates a node pool for a Container Service for Kubernetes (ACK) cluster. You can use node pools to facilitate node management. For example, you can schedule, configure, or maintain nodes by node pool, and enable auto scaling for a node pool. We recommend that you use a managed node pool, which can help automate specific O\\\\\\&M tasks for nodes, such as Common Vulnerabilities and Exposures (CVE) patching and node repair. This reduces your O\\\\\\&M workload.
        
        @param request: CreateClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterNodePoolResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.host_network):
            body['host_network'] = request.host_network
        if not UtilClient.is_unset(request.interconnect_config):
            body['interconnect_config'] = request.interconnect_config
        if not UtilClient.is_unset(request.interconnect_mode):
            body['interconnect_mode'] = request.interconnect_mode
        if not UtilClient.is_unset(request.intranet):
            body['intranet'] = request.intranet
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateClusterNodePoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateClusterNodePoolResponse(),
                self.execute(params, req, runtime)
            )

    async def create_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        """
        @summary Creates a node pool for a Container Service for Kubernetes (ACK) cluster. You can use node pools to facilitate node management. For example, you can schedule, configure, or maintain nodes by node pool, and enable auto scaling for a node pool. We recommend that you use a managed node pool, which can help automate specific O\\\\\\&M tasks for nodes, such as Common Vulnerabilities and Exposures (CVE) patching and node repair. This reduces your O\\\\\\&M workload.
        
        @param request: CreateClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterNodePoolResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.host_network):
            body['host_network'] = request.host_network
        if not UtilClient.is_unset(request.interconnect_config):
            body['interconnect_config'] = request.interconnect_config
        if not UtilClient.is_unset(request.interconnect_mode):
            body['interconnect_mode'] = request.interconnect_mode
        if not UtilClient.is_unset(request.intranet):
            body['intranet'] = request.intranet
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateClusterNodePoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateClusterNodePoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_cluster_node_pool(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        """
        @summary Creates a node pool for a Container Service for Kubernetes (ACK) cluster. You can use node pools to facilitate node management. For example, you can schedule, configure, or maintain nodes by node pool, and enable auto scaling for a node pool. We recommend that you use a managed node pool, which can help automate specific O\\\\\\&M tasks for nodes, such as Common Vulnerabilities and Exposures (CVE) patching and node repair. This reduces your O\\\\\\&M workload.
        
        @param request: CreateClusterNodePoolRequest
        @return: CreateClusterNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_node_pool_with_options(cluster_id, request, headers, runtime)

    async def create_cluster_node_pool_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        """
        @summary Creates a node pool for a Container Service for Kubernetes (ACK) cluster. You can use node pools to facilitate node management. For example, you can schedule, configure, or maintain nodes by node pool, and enable auto scaling for a node pool. We recommend that you use a managed node pool, which can help automate specific O\\\\\\&M tasks for nodes, such as Common Vulnerabilities and Exposures (CVE) patching and node repair. This reduces your O\\\\\\&M workload.
        
        @param request: CreateClusterNodePoolRequest
        @return: CreateClusterNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_node_pool_with_options_async(cluster_id, request, headers, runtime)

    def create_edge_machine_with_options(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        """
        @summary You can call the CreateEdgeMachine operation to activate a cloud-native box.
        
        @param request: CreateEdgeMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeMachineResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateEdgeMachineResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateEdgeMachineResponse(),
                self.execute(params, req, runtime)
            )

    async def create_edge_machine_with_options_async(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        """
        @summary You can call the CreateEdgeMachine operation to activate a cloud-native box.
        
        @param request: CreateEdgeMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeMachineResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateEdgeMachineResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateEdgeMachineResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_edge_machine(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        """
        @summary You can call the CreateEdgeMachine operation to activate a cloud-native box.
        
        @param request: CreateEdgeMachineRequest
        @return: CreateEdgeMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_edge_machine_with_options(request, headers, runtime)

    async def create_edge_machine_async(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        """
        @summary You can call the CreateEdgeMachine operation to activate a cloud-native box.
        
        @param request: CreateEdgeMachineRequest
        @return: CreateEdgeMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_edge_machine_with_options_async(request, headers, runtime)

    def create_kubernetes_trigger_with_options(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        """
        @deprecated OpenAPI CreateKubernetesTrigger is deprecated
        
        @summary You can call the CreateKubernetesTrigger operation to create a trigger for an application.
        
        @param request: CreateKubernetesTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKubernetesTriggerResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateKubernetesTriggerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateKubernetesTriggerResponse(),
                self.execute(params, req, runtime)
            )

    async def create_kubernetes_trigger_with_options_async(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        """
        @deprecated OpenAPI CreateKubernetesTrigger is deprecated
        
        @summary You can call the CreateKubernetesTrigger operation to create a trigger for an application.
        
        @param request: CreateKubernetesTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKubernetesTriggerResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateKubernetesTriggerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateKubernetesTriggerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_kubernetes_trigger(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        """
        @deprecated OpenAPI CreateKubernetesTrigger is deprecated
        
        @summary You can call the CreateKubernetesTrigger operation to create a trigger for an application.
        
        @param request: CreateKubernetesTriggerRequest
        @return: CreateKubernetesTriggerResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_kubernetes_trigger_with_options(request, headers, runtime)

    async def create_kubernetes_trigger_async(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        """
        @deprecated OpenAPI CreateKubernetesTrigger is deprecated
        
        @summary You can call the CreateKubernetesTrigger operation to create a trigger for an application.
        
        @param request: CreateKubernetesTriggerRequest
        @return: CreateKubernetesTriggerResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_kubernetes_trigger_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: cs20151215_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTemplateResponse:
        """
        @summary Creates an orchestration template. An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can use orchestration templates to manage resources in Kubernetes clusters and automate resource deployment, such as pods, Services, Deployments, ConfigMaps, and persistent volumes (PVs).
        
        @param request: CreateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def create_template_with_options_async(
        self,
        request: cs20151215_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTemplateResponse:
        """
        @summary Creates an orchestration template. An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can use orchestration templates to manage resources in Kubernetes clusters and automate resource deployment, such as pods, Services, Deployments, ConfigMaps, and persistent volumes (PVs).
        
        @param request: CreateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_template(
        self,
        request: cs20151215_models.CreateTemplateRequest,
    ) -> cs20151215_models.CreateTemplateResponse:
        """
        @summary Creates an orchestration template. An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can use orchestration templates to manage resources in Kubernetes clusters and automate resource deployment, such as pods, Services, Deployments, ConfigMaps, and persistent volumes (PVs).
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: cs20151215_models.CreateTemplateRequest,
    ) -> cs20151215_models.CreateTemplateResponse:
        """
        @summary Creates an orchestration template. An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can use orchestration templates to manage resources in Kubernetes clusters and automate resource deployment, such as pods, Services, Deployments, ConfigMaps, and persistent volumes (PVs).
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
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
        """
        @summary Creates a trigger for an application to redeploy the application pods when specific conditions are met.
        
        @param request: CreateTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateTriggerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateTriggerResponse(),
                self.execute(params, req, runtime)
            )

    async def create_trigger_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTriggerResponse:
        """
        @summary Creates a trigger for an application to redeploy the application pods when specific conditions are met.
        
        @param request: CreateTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.CreateTriggerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.CreateTriggerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_trigger(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateTriggerRequest,
    ) -> cs20151215_models.CreateTriggerResponse:
        """
        @summary Creates a trigger for an application to redeploy the application pods when specific conditions are met.
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(cluster_id, request, headers, runtime)

    async def create_trigger_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateTriggerRequest,
    ) -> cs20151215_models.CreateTriggerResponse:
        """
        @summary Creates a trigger for an application to redeploy the application pods when specific conditions are met.
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_trigger_with_options_async(cluster_id, request, headers, runtime)

    def delete_alert_contact_with_options(
        self,
        tmp_req: cs20151215_models.DeleteAlertContactRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactResponse:
        """
        @summary Deletes one or more ACK alert contacts.
        
        @param tmp_req: DeleteAlertContactRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertContactResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteAlertContactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_ids):
            request.contact_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_ids, 'contact_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.contact_ids_shrink):
            query['contact_ids'] = request.contact_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
            body_type='array'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_alert_contact_with_options_async(
        self,
        tmp_req: cs20151215_models.DeleteAlertContactRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactResponse:
        """
        @summary Deletes one or more ACK alert contacts.
        
        @param tmp_req: DeleteAlertContactRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertContactResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteAlertContactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_ids):
            request.contact_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_ids, 'contact_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.contact_ids_shrink):
            query['contact_ids'] = request.contact_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
            body_type='array'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_alert_contact(
        self,
        request: cs20151215_models.DeleteAlertContactRequest,
    ) -> cs20151215_models.DeleteAlertContactResponse:
        """
        @summary Deletes one or more ACK alert contacts.
        
        @param request: DeleteAlertContactRequest
        @return: DeleteAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_with_options(request, headers, runtime)

    async def delete_alert_contact_async(
        self,
        request: cs20151215_models.DeleteAlertContactRequest,
    ) -> cs20151215_models.DeleteAlertContactResponse:
        """
        @summary Deletes one or more ACK alert contacts.
        
        @param request: DeleteAlertContactRequest
        @return: DeleteAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_alert_contact_with_options_async(request, headers, runtime)

    def delete_alert_contact_group_with_options(
        self,
        tmp_req: cs20151215_models.DeleteAlertContactGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactGroupResponse:
        """
        @summary Deletes an ACK alert contact group.
        
        @param tmp_req: DeleteAlertContactGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertContactGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteAlertContactGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_group_ids):
            request.contact_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_group_ids, 'contact_group_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids_shrink):
            query['contact_group_ids'] = request.contact_group_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
            body_type='array'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_alert_contact_group_with_options_async(
        self,
        tmp_req: cs20151215_models.DeleteAlertContactGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactGroupResponse:
        """
        @summary Deletes an ACK alert contact group.
        
        @param tmp_req: DeleteAlertContactGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertContactGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteAlertContactGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact_group_ids):
            request.contact_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_group_ids, 'contact_group_ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids_shrink):
            query['contact_group_ids'] = request.contact_group_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
            body_type='array'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteAlertContactGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_alert_contact_group(
        self,
        request: cs20151215_models.DeleteAlertContactGroupRequest,
    ) -> cs20151215_models.DeleteAlertContactGroupResponse:
        """
        @summary Deletes an ACK alert contact group.
        
        @param request: DeleteAlertContactGroupRequest
        @return: DeleteAlertContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_group_with_options(request, headers, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: cs20151215_models.DeleteAlertContactGroupRequest,
    ) -> cs20151215_models.DeleteAlertContactGroupResponse:
        """
        @summary Deletes an ACK alert contact group.
        
        @param request: DeleteAlertContactGroupRequest
        @return: DeleteAlertContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_alert_contact_group_with_options_async(request, headers, runtime)

    def delete_cluster_with_options(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterResponse:
        """
        @summary You can call the DeleteCluster operation to delete a cluster and specify whether to delete or retain the relevant cluster resources. Before you delete a cluster, you must manually delete workloads in the cluster, such as Deployments, StatefulSets, Jobs, and CronJobs. Otherwise, you may fail to delete the cluster.
        
        @description Warning:
        Subscription ECS instances and Lingjun nodes in a cluster cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release the resources. For more information, see \\<a href="{0}" target="_blank">Rules for deleting clusters and releasing nodes\\</a>.
        If the SLB instance of the API server uses the subscription billing method, it cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release it.
        By default, virtual private clouds (VPCs), vSwitches, security groups, and RAM roles are retained if they are used by other resources. To avoid unnecessary costs, we recommend that you manually release the resources.
        Elastic container instances created on virtual nodes are automatically released.
        Some resources created together with a cluster are not automatically released when the cluster is deleted. After the cluster is deleted, you are still charged for the resources. Release or retain the resources based on your actual needs. The resources include Simple Log Service projects automatically created by the cluster and dynamically provisioned disks.
        
        @param tmp_req: DeleteClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_options):
            request.delete_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_options, 'delete_options', 'json')
        if not UtilClient.is_unset(tmp_req.retain_resources):
            request.retain_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_resources, 'retain_resources', 'json')
        query = {}
        if not UtilClient.is_unset(request.delete_options_shrink):
            query['delete_options'] = request.delete_options_shrink
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_cluster_with_options_async(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterResponse:
        """
        @summary You can call the DeleteCluster operation to delete a cluster and specify whether to delete or retain the relevant cluster resources. Before you delete a cluster, you must manually delete workloads in the cluster, such as Deployments, StatefulSets, Jobs, and CronJobs. Otherwise, you may fail to delete the cluster.
        
        @description Warning:
        Subscription ECS instances and Lingjun nodes in a cluster cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release the resources. For more information, see \\<a href="{0}" target="_blank">Rules for deleting clusters and releasing nodes\\</a>.
        If the SLB instance of the API server uses the subscription billing method, it cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release it.
        By default, virtual private clouds (VPCs), vSwitches, security groups, and RAM roles are retained if they are used by other resources. To avoid unnecessary costs, we recommend that you manually release the resources.
        Elastic container instances created on virtual nodes are automatically released.
        Some resources created together with a cluster are not automatically released when the cluster is deleted. After the cluster is deleted, you are still charged for the resources. Release or retain the resources based on your actual needs. The resources include Simple Log Service projects automatically created by the cluster and dynamically provisioned disks.
        
        @param tmp_req: DeleteClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_options):
            request.delete_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_options, 'delete_options', 'json')
        if not UtilClient.is_unset(tmp_req.retain_resources):
            request.retain_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_resources, 'retain_resources', 'json')
        query = {}
        if not UtilClient.is_unset(request.delete_options_shrink):
            query['delete_options'] = request.delete_options_shrink
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterRequest,
    ) -> cs20151215_models.DeleteClusterResponse:
        """
        @summary You can call the DeleteCluster operation to delete a cluster and specify whether to delete or retain the relevant cluster resources. Before you delete a cluster, you must manually delete workloads in the cluster, such as Deployments, StatefulSets, Jobs, and CronJobs. Otherwise, you may fail to delete the cluster.
        
        @description Warning:
        Subscription ECS instances and Lingjun nodes in a cluster cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release the resources. For more information, see \\<a href="{0}" target="_blank">Rules for deleting clusters and releasing nodes\\</a>.
        If the SLB instance of the API server uses the subscription billing method, it cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release it.
        By default, virtual private clouds (VPCs), vSwitches, security groups, and RAM roles are retained if they are used by other resources. To avoid unnecessary costs, we recommend that you manually release the resources.
        Elastic container instances created on virtual nodes are automatically released.
        Some resources created together with a cluster are not automatically released when the cluster is deleted. After the cluster is deleted, you are still charged for the resources. Release or retain the resources based on your actual needs. The resources include Simple Log Service projects automatically created by the cluster and dynamically provisioned disks.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_with_options(cluster_id, request, headers, runtime)

    async def delete_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterRequest,
    ) -> cs20151215_models.DeleteClusterResponse:
        """
        @summary You can call the DeleteCluster operation to delete a cluster and specify whether to delete or retain the relevant cluster resources. Before you delete a cluster, you must manually delete workloads in the cluster, such as Deployments, StatefulSets, Jobs, and CronJobs. Otherwise, you may fail to delete the cluster.
        
        @description Warning:
        Subscription ECS instances and Lingjun nodes in a cluster cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release the resources. For more information, see \\<a href="{0}" target="_blank">Rules for deleting clusters and releasing nodes\\</a>.
        If the SLB instance of the API server uses the subscription billing method, it cannot be automatically released. To avoid unnecessary costs, we recommend that you manually release it.
        By default, virtual private clouds (VPCs), vSwitches, security groups, and RAM roles are retained if they are used by other resources. To avoid unnecessary costs, we recommend that you manually release the resources.
        Elastic container instances created on virtual nodes are automatically released.
        Some resources created together with a cluster are not automatically released when the cluster is deleted. After the cluster is deleted, you are still charged for the resources. Release or retain the resources based on your actual needs. The resources include Simple Log Service projects automatically created by the cluster and dynamically provisioned disks.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
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
        """
        @summary null
        
        @param request: DeleteClusterNodepoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterNodepoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodepoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodepoolResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_cluster_nodepool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DeleteClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        """
        @summary null
        
        @param request: DeleteClusterNodepoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterNodepoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodepoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodepoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_cluster_nodepool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DeleteClusterNodepoolRequest,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        """
        @summary null
        
        @param request: DeleteClusterNodepoolRequest
        @return: DeleteClusterNodepoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodepool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def delete_cluster_nodepool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DeleteClusterNodepoolRequest,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        """
        @summary null
        
        @param request: DeleteClusterNodepoolRequest
        @return: DeleteClusterNodepoolResponse
        """
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
        @summary Removes nodes from a Container Service for Kubernetes (ACK) cluster. When you remove nodes, you can specify whether to release the Elastic Compute Service (ECS) instances and drain the nodes. When you remove nodes, pods on the nodes are migrated. This may adversely affect your businesses. We recommend that you back up data and perform this operation during off-peak hours.
        
        @description    When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        When you remove a node, the system sets the status of the node to Unschedulable.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodesResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        """
        @summary Removes nodes from a Container Service for Kubernetes (ACK) cluster. When you remove nodes, you can specify whether to release the Elastic Compute Service (ECS) instances and drain the nodes. When you remove nodes, pods on the nodes are migrated. This may adversely affect your businesses. We recommend that you back up data and perform this operation during off-peak hours.
        
        @description    When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        When you remove a node, the system sets the status of the node to Unschedulable.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteClusterNodesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        """
        @summary Removes nodes from a Container Service for Kubernetes (ACK) cluster. When you remove nodes, you can specify whether to release the Elastic Compute Service (ECS) instances and drain the nodes. When you remove nodes, pods on the nodes are migrated. This may adversely affect your businesses. We recommend that you back up data and perform this operation during off-peak hours.
        
        @description    When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        When you remove a node, the system sets the status of the node to Unschedulable.
        
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
        @summary Removes nodes from a Container Service for Kubernetes (ACK) cluster. When you remove nodes, you can specify whether to release the Elastic Compute Service (ECS) instances and drain the nodes. When you remove nodes, pods on the nodes are migrated. This may adversely affect your businesses. We recommend that you back up data and perform this operation during off-peak hours.
        
        @description    When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        When you remove a node, the system sets the status of the node to Unschedulable.
        
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
        """
        @summary You can call the DeleteEdgeMachine operation to delete a cloud-native box.
        
        @param request: DeleteEdgeMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeMachineResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteEdgeMachineResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteEdgeMachineResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_edge_machine_with_options_async(
        self,
        edge_machineid: str,
        request: cs20151215_models.DeleteEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteEdgeMachineResponse:
        """
        @summary You can call the DeleteEdgeMachine operation to delete a cloud-native box.
        
        @param request: DeleteEdgeMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeMachineResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteEdgeMachineResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteEdgeMachineResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_edge_machine(
        self,
        edge_machineid: str,
        request: cs20151215_models.DeleteEdgeMachineRequest,
    ) -> cs20151215_models.DeleteEdgeMachineResponse:
        """
        @summary You can call the DeleteEdgeMachine operation to delete a cloud-native box.
        
        @param request: DeleteEdgeMachineRequest
        @return: DeleteEdgeMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_edge_machine_with_options(edge_machineid, request, headers, runtime)

    async def delete_edge_machine_async(
        self,
        edge_machineid: str,
        request: cs20151215_models.DeleteEdgeMachineRequest,
    ) -> cs20151215_models.DeleteEdgeMachineResponse:
        """
        @summary You can call the DeleteEdgeMachine operation to delete a cloud-native box.
        
        @param request: DeleteEdgeMachineRequest
        @return: DeleteEdgeMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_edge_machine_with_options_async(edge_machineid, request, headers, runtime)

    def delete_kubernetes_trigger_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        """
        @deprecated OpenAPI DeleteKubernetesTrigger is deprecated
        
        @summary You can call the DeleteKubernetesTrigger operation to delete an application trigger by trigger ID
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKubernetesTriggerResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteKubernetesTriggerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteKubernetesTriggerResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_kubernetes_trigger_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        """
        @deprecated OpenAPI DeleteKubernetesTrigger is deprecated
        
        @summary You can call the DeleteKubernetesTrigger operation to delete an application trigger by trigger ID
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKubernetesTriggerResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteKubernetesTriggerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteKubernetesTriggerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_kubernetes_trigger(
        self,
        id: str,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        """
        @deprecated OpenAPI DeleteKubernetesTrigger is deprecated
        
        @summary You can call the DeleteKubernetesTrigger operation to delete an application trigger by trigger ID
        
        @return: DeleteKubernetesTriggerResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_kubernetes_trigger_with_options(id, headers, runtime)

    async def delete_kubernetes_trigger_async(
        self,
        id: str,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        """
        @deprecated OpenAPI DeleteKubernetesTrigger is deprecated
        
        @summary You can call the DeleteKubernetesTrigger operation to delete an application trigger by trigger ID
        
        @return: DeleteKubernetesTriggerResponse
        Deprecated
        """
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
        """
        @summary Deletes policy instances in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeletePolicyInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeletePolicyInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeletePolicyInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeletePolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeletePolicyInstanceResponse:
        """
        @summary Deletes policy instances in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeletePolicyInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeletePolicyInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeletePolicyInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeletePolicyInstanceRequest,
    ) -> cs20151215_models.DeletePolicyInstanceResponse:
        """
        @summary Deletes policy instances in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeletePolicyInstanceRequest
        @return: DeletePolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def delete_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeletePolicyInstanceRequest,
    ) -> cs20151215_models.DeletePolicyInstanceResponse:
        """
        @summary Deletes policy instances in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeletePolicyInstanceRequest
        @return: DeletePolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def delete_template_with_options(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTemplateResponse:
        """
        @summary Deletes the orchestration templates that you no longer need.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_template_with_options_async(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTemplateResponse:
        """
        @summary Deletes the orchestration templates that you no longer need.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_template(
        self,
        template_id: str,
    ) -> cs20151215_models.DeleteTemplateResponse:
        """
        @summary Deletes the orchestration templates that you no longer need.
        
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(template_id, headers, runtime)

    async def delete_template_async(
        self,
        template_id: str,
    ) -> cs20151215_models.DeleteTemplateResponse:
        """
        @summary Deletes the orchestration templates that you no longer need.
        
        @return: DeleteTemplateResponse
        """
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
        """
        @summary Deletes an application trigger.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteTriggerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteTriggerResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_trigger_with_options_async(
        self,
        cluster_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTriggerResponse:
        """
        @summary Deletes an application trigger.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeleteTriggerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeleteTriggerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_trigger(
        self,
        cluster_id: str,
        id: str,
    ) -> cs20151215_models.DeleteTriggerResponse:
        """
        @summary Deletes an application trigger.
        
        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(cluster_id, id, headers, runtime)

    async def delete_trigger_async(
        self,
        cluster_id: str,
        id: str,
    ) -> cs20151215_models.DeleteTriggerResponse:
        """
        @summary Deletes an application trigger.
        
        @return: DeleteTriggerResponse
        """
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
        """
        @summary Deploys a policy in the specified namespaces of a specific Container Service for Kubernetes (ACK) cluster. You can create and deploy a security policy by specifying the policy type, action of the policy such as alerting or denying, and namespaces to which the policy applies.
        
        @param request: DeployPolicyInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployPolicyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeployPolicyInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeployPolicyInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def deploy_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeployPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeployPolicyInstanceResponse:
        """
        @summary Deploys a policy in the specified namespaces of a specific Container Service for Kubernetes (ACK) cluster. You can create and deploy a security policy by specifying the policy type, action of the policy such as alerting or denying, and namespaces to which the policy applies.
        
        @param request: DeployPolicyInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployPolicyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DeployPolicyInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DeployPolicyInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def deploy_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeployPolicyInstanceRequest,
    ) -> cs20151215_models.DeployPolicyInstanceResponse:
        """
        @summary Deploys a policy in the specified namespaces of a specific Container Service for Kubernetes (ACK) cluster. You can create and deploy a security policy by specifying the policy type, action of the policy such as alerting or denying, and namespaces to which the policy applies.
        
        @param request: DeployPolicyInstanceRequest
        @return: DeployPolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def deploy_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeployPolicyInstanceRequest,
    ) -> cs20151215_models.DeployPolicyInstanceResponse:
        """
        @summary Deploys a policy in the specified namespaces of a specific Container Service for Kubernetes (ACK) cluster. You can create and deploy a security policy by specifying the policy type, action of the policy such as alerting or denying, and namespaces to which the policy applies.
        
        @param request: DeployPolicyInstanceRequest
        @return: DeployPolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def describe_addon_with_options(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonResponse:
        """
        @summary Queries the information about a component based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, cluster version, and component name. The information includes whether the component is managed, the component type, supported custom parameter schema, compatible operating system architecture, and earliest supported cluster version.
        
        @param request: DescribeAddonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddonResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_addon_with_options_async(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonResponse:
        """
        @summary Queries the information about a component based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, cluster version, and component name. The information includes whether the component is managed, the component type, supported custom parameter schema, compatible operating system architecture, and earliest supported cluster version.
        
        @param request: DescribeAddonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddonResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_addon(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
    ) -> cs20151215_models.DescribeAddonResponse:
        """
        @summary Queries the information about a component based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, cluster version, and component name. The information includes whether the component is managed, the component type, supported custom parameter schema, compatible operating system architecture, and earliest supported cluster version.
        
        @param request: DescribeAddonRequest
        @return: DescribeAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_addon_with_options(addon_name, request, headers, runtime)

    async def describe_addon_async(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
    ) -> cs20151215_models.DescribeAddonResponse:
        """
        @summary Queries the information about a component based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, cluster version, and component name. The information includes whether the component is managed, the component type, supported custom parameter schema, compatible operating system architecture, and earliest supported cluster version.
        
        @param request: DescribeAddonRequest
        @return: DescribeAddonResponse
        """
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
        @deprecated OpenAPI DescribeAddons is deprecated
        
        @summary You can call the DescribeAddons operation to query the details about all components that are supported by Container Service for Kubernetes (ACK).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_addons_with_options_async(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonsResponse:
        """
        @deprecated OpenAPI DescribeAddons is deprecated
        
        @summary You can call the DescribeAddons operation to query the details about all components that are supported by Container Service for Kubernetes (ACK).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeAddonsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_addons(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
    ) -> cs20151215_models.DescribeAddonsResponse:
        """
        @deprecated OpenAPI DescribeAddons is deprecated
        
        @summary You can call the DescribeAddons operation to query the details about all components that are supported by Container Service for Kubernetes (ACK).
        
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
        @deprecated OpenAPI DescribeAddons is deprecated
        
        @summary You can call the DescribeAddons operation to query the details about all components that are supported by Container Service for Kubernetes (ACK).
        
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
        @deprecated OpenAPI DescribeClusterAddonInstance is deprecated
        
        @summary You can call the DescribeClusterAddonInstance operation to query the information about a cluster component, including the version, status, and configuration of the component.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_addon_instance_with_options_async(
        self,
        cluster_id: str,
        addon_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonInstanceResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonInstance is deprecated
        
        @summary You can call the DescribeClusterAddonInstance operation to query the information about a cluster component, including the version, status, and configuration of the component.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_addon_instance(
        self,
        cluster_id: str,
        addon_name: str,
    ) -> cs20151215_models.DescribeClusterAddonInstanceResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonInstance is deprecated
        
        @summary You can call the DescribeClusterAddonInstance operation to query the information about a cluster component, including the version, status, and configuration of the component.
        
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
        @deprecated OpenAPI DescribeClusterAddonInstance is deprecated
        
        @summary You can call the DescribeClusterAddonInstance operation to query the information about a cluster component, including the version, status, and configuration of the component.
        
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
        request: cs20151215_models.DescribeClusterAddonMetadataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonMetadata is deprecated
        
        @summary You can call the DescribeClusterAddonMetadata operation to query the metadata of a component version. The metadata includes the component version and available parameters.
        
        @param request: DescribeClusterAddonMetadataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonMetadataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonMetadataResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_addon_metadata_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.DescribeClusterAddonMetadataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonMetadata is deprecated
        
        @summary You can call the DescribeClusterAddonMetadata operation to query the metadata of a component version. The metadata includes the component version and available parameters.
        
        @param request: DescribeClusterAddonMetadataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonMetadataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonMetadataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_addon_metadata(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.DescribeClusterAddonMetadataRequest,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonMetadata is deprecated
        
        @summary You can call the DescribeClusterAddonMetadata operation to query the metadata of a component version. The metadata includes the component version and available parameters.
        
        @param request: DescribeClusterAddonMetadataRequest
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_metadata_with_options(cluster_id, component_id, request, headers, runtime)

    async def describe_cluster_addon_metadata_async(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.DescribeClusterAddonMetadataRequest,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonMetadata is deprecated
        
        @summary You can call the DescribeClusterAddonMetadata operation to query the metadata of a component version. The metadata includes the component version and available parameters.
        
        @param request: DescribeClusterAddonMetadataRequest
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_metadata_with_options_async(cluster_id, component_id, request, headers, runtime)

    def describe_cluster_addon_upgrade_status_with_options(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonUpgradeStatus operation to query the update progress of a cluster component.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_addon_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonUpgradeStatus operation to query the update progress of a cluster component.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_addon_upgrade_status(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonUpgradeStatus operation to query the update progress of a cluster component.
        
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
        @deprecated OpenAPI DescribeClusterAddonUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonUpgradeStatus operation to query the update progress of a cluster component.
        
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
        @deprecated OpenAPI DescribeClusterAddonsUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonsUpgradeStatus operation to query the update progress of a component by component name.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_addons_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonsUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonsUpgradeStatus operation to query the update progress of a component by component name.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_addons_upgrade_status(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonsUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonsUpgradeStatus operation to query the update progress of a component by component name.
        
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
        @deprecated OpenAPI DescribeClusterAddonsUpgradeStatus is deprecated
        
        @summary You can call the DescribeClusterAddonsUpgradeStatus operation to query the update progress of a component by component name.
        
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
        @deprecated OpenAPI DescribeClusterAddonsVersion is deprecated
        
        @summary You can call the DescribeClusterAddonsVersion operation to query the details about all components in a cluster by cluster ID.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsVersionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsVersionResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_addons_version_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonsVersion is deprecated
        
        @summary You can call the DescribeClusterAddonsVersion operation to query the details about all components in a cluster by cluster ID.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsVersionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAddonsVersionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_addons_version(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        """
        @deprecated OpenAPI DescribeClusterAddonsVersion is deprecated
        
        @summary You can call the DescribeClusterAddonsVersion operation to query the details about all components in a cluster by cluster ID.
        
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
        @deprecated OpenAPI DescribeClusterAddonsVersion is deprecated
        
        @summary You can call the DescribeClusterAddonsVersion operation to query the details about all components in a cluster by cluster ID.
        
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
        """
        @summary Queries the scripts used to add existing nodes to a Container Service for Kubernetes (ACK) cluster. ACK allows you to manually add existing Elastic Compute Service (ECS) instances to an ACK cluster as worker nodes or re-add worker nodes that you remove from the cluster to a node pool.
        
        @param request: DescribeClusterAttachScriptsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAttachScriptsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.arch):
            body['arch'] = request.arch
        if not UtilClient.is_unset(request.expired):
            body['expired'] = request.expired
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAttachScriptsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAttachScriptsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_attach_scripts_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        """
        @summary Queries the scripts used to add existing nodes to a Container Service for Kubernetes (ACK) cluster. ACK allows you to manually add existing Elastic Compute Service (ECS) instances to an ACK cluster as worker nodes or re-add worker nodes that you remove from the cluster to a node pool.
        
        @param request: DescribeClusterAttachScriptsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAttachScriptsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.arch):
            body['arch'] = request.arch
        if not UtilClient.is_unset(request.expired):
            body['expired'] = request.expired
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAttachScriptsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterAttachScriptsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_attach_scripts(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        """
        @summary Queries the scripts used to add existing nodes to a Container Service for Kubernetes (ACK) cluster. ACK allows you to manually add existing Elastic Compute Service (ECS) instances to an ACK cluster as worker nodes or re-add worker nodes that you remove from the cluster to a node pool.
        
        @param request: DescribeClusterAttachScriptsRequest
        @return: DescribeClusterAttachScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_attach_scripts_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_attach_scripts_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        """
        @summary Queries the scripts used to add existing nodes to a Container Service for Kubernetes (ACK) cluster. ACK allows you to manually add existing Elastic Compute Service (ECS) instances to an ACK cluster as worker nodes or re-add worker nodes that you remove from the cluster to a node pool.
        
        @param request: DescribeClusterAttachScriptsRequest
        @return: DescribeClusterAttachScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_attach_scripts_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_detail_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        """
        @summary You can call the DescribeClusterDetail operation to query the details of a Container Service for Kubernetes (ACK) cluster by cluster ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterDetailResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_detail_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        """
        @summary You can call the DescribeClusterDetail operation to query the details of a Container Service for Kubernetes (ACK) cluster by cluster ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterDetailResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_detail(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        """
        @summary You can call the DescribeClusterDetail operation to query the details of a Container Service for Kubernetes (ACK) cluster by cluster ID.
        
        @return: DescribeClusterDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_detail_with_options(cluster_id, headers, runtime)

    async def describe_cluster_detail_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        """
        @summary You can call the DescribeClusterDetail operation to query the details of a Container Service for Kubernetes (ACK) cluster by cluster ID.
        
        @return: DescribeClusterDetailResponse
        """
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
        """
        @summary Queries events and event details in a Container Service for Kubernetes (ACK) cluster, including the severity level, status, and start time of each event. Events are generated when clusters created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeClusterEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterEventsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterEventsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterEventsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_events_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterEventsResponse:
        """
        @summary Queries events and event details in a Container Service for Kubernetes (ACK) cluster, including the severity level, status, and start time of each event. Events are generated when clusters created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeClusterEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterEventsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterEventsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterEventsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_events(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterEventsRequest,
    ) -> cs20151215_models.DescribeClusterEventsResponse:
        """
        @summary Queries events and event details in a Container Service for Kubernetes (ACK) cluster, including the severity level, status, and start time of each event. Events are generated when clusters created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeClusterEventsRequest
        @return: DescribeClusterEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_events_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_events_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterEventsRequest,
    ) -> cs20151215_models.DescribeClusterEventsResponse:
        """
        @summary Queries events and event details in a Container Service for Kubernetes (ACK) cluster, including the severity level, status, and start time of each event. Events are generated when clusters created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeClusterEventsRequest
        @return: DescribeClusterEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_events_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_logs_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        """
        @summary Queries the cluster log to help analyze cluster issues and locate the cause.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterLogsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterLogsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterLogsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_logs_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        """
        @summary Queries the cluster log to help analyze cluster issues and locate the cause.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterLogsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterLogsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterLogsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_logs(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        """
        @summary Queries the cluster log to help analyze cluster issues and locate the cause.
        
        @return: DescribeClusterLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_logs_with_options(cluster_id, headers, runtime)

    async def describe_cluster_logs_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        """
        @summary Queries the cluster log to help analyze cluster issues and locate the cause.
        
        @return: DescribeClusterLogsResponse
        """
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
        """
        @summary You can call the DescribeClusterNodePoolDetail.html operation to query the details about a node pool in a cluster by node pool ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNodePoolDetailResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_node_pool_detail_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolDetailResponse:
        """
        @summary You can call the DescribeClusterNodePoolDetail.html operation to query the details about a node pool in a cluster by node pool ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNodePoolDetailResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_node_pool_detail(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> cs20151215_models.DescribeClusterNodePoolDetailResponse:
        """
        @summary You can call the DescribeClusterNodePoolDetail.html operation to query the details about a node pool in a cluster by node pool ID.
        
        @return: DescribeClusterNodePoolDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pool_detail_with_options(cluster_id, nodepool_id, headers, runtime)

    async def describe_cluster_node_pool_detail_async(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> cs20151215_models.DescribeClusterNodePoolDetailResponse:
        """
        @summary You can call the DescribeClusterNodePoolDetail.html operation to query the details about a node pool in a cluster by node pool ID.
        
        @return: DescribeClusterNodePoolDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_node_pool_detail_with_options_async(cluster_id, nodepool_id, headers, runtime)

    def describe_cluster_node_pools_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodePoolsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        """
        @summary Queries the information about all node pools in a cluster.
        
        @param request: DescribeClusterNodePoolsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNodePoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nodepool_name):
            query['NodepoolName'] = request.nodepool_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_node_pools_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodePoolsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        """
        @summary Queries the information about all node pools in a cluster.
        
        @param request: DescribeClusterNodePoolsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNodePoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nodepool_name):
            query['NodepoolName'] = request.nodepool_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodePoolsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_node_pools(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodePoolsRequest,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        """
        @summary Queries the information about all node pools in a cluster.
        
        @param request: DescribeClusterNodePoolsRequest
        @return: DescribeClusterNodePoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pools_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_node_pools_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodePoolsRequest,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        """
        @summary Queries the information about all node pools in a cluster.
        
        @param request: DescribeClusterNodePoolsRequest
        @return: DescribeClusterNodePoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_node_pools_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        """
        @summary null
        
        @param request: DescribeClusterNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNodesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        """
        @summary null
        
        @param request: DescribeClusterNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNodesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterNodesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        """
        @summary null
        
        @param request: DescribeClusterNodesRequest
        @return: DescribeClusterNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_nodes_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        """
        @summary null
        
        @param request: DescribeClusterNodesRequest
        @return: DescribeClusterNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_resources_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        """
        @summary You can call the DescribeClusterResources operation to query all resources in a cluster by cluster ID.
        
        @param request: DescribeClusterResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_addon_resources):
            query['with_addon_resources'] = request.with_addon_resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_resources_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        """
        @summary You can call the DescribeClusterResources operation to query all resources in a cluster by cluster ID.
        
        @param request: DescribeClusterResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_addon_resources):
            query['with_addon_resources'] = request.with_addon_resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_resources(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterResourcesRequest,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        """
        @summary You can call the DescribeClusterResources operation to query all resources in a cluster by cluster ID.
        
        @param request: DescribeClusterResourcesRequest
        @return: DescribeClusterResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_resources_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_resources_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterResourcesRequest,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        """
        @summary You can call the DescribeClusterResources operation to query all resources in a cluster by cluster ID.
        
        @param request: DescribeClusterResourcesRequest
        @return: DescribeClusterResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_resources_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_tasks_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        """
        @summary Queries tasks in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DescribeClusterTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterTasksResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_tasks_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        """
        @summary Queries tasks in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DescribeClusterTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterTasksResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_tasks(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        """
        @summary Queries tasks in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DescribeClusterTasksRequest
        @return: DescribeClusterTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_tasks_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_tasks_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        """
        @summary Queries tasks in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DescribeClusterTasksRequest
        @return: DescribeClusterTasksResponse
        """
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
        @summary Kubeconfig files store identity and authentication information that is used by clients to access Container Service for Kubernetes (ACK) clusters. To use a kubectl client to manage an ACK cluster, you need to use the corresponding kubeconfig file to connect to the ACK cluster. We recommend that you keep kubeconfig files confidential and revoke kubeconfig files that are not in use. This helps prevent data leaks caused by the disclosure of kubeconfig files.
        
        @description >  The default validity period of a kubeconfig file is 3 years. 180 days before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the kubeconfig file is valid for 3 years. The previous kubeconfig file still remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterUserKubeconfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterUserKubeconfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        """
        @summary Kubeconfig files store identity and authentication information that is used by clients to access Container Service for Kubernetes (ACK) clusters. To use a kubectl client to manage an ACK cluster, you need to use the corresponding kubeconfig file to connect to the ACK cluster. We recommend that you keep kubeconfig files confidential and revoke kubeconfig files that are not in use. This helps prevent data leaks caused by the disclosure of kubeconfig files.
        
        @description >  The default validity period of a kubeconfig file is 3 years. 180 days before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the kubeconfig file is valid for 3 years. The previous kubeconfig file still remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterUserKubeconfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterUserKubeconfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_user_kubeconfig(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        """
        @summary Kubeconfig files store identity and authentication information that is used by clients to access Container Service for Kubernetes (ACK) clusters. To use a kubectl client to manage an ACK cluster, you need to use the corresponding kubeconfig file to connect to the ACK cluster. We recommend that you keep kubeconfig files confidential and revoke kubeconfig files that are not in use. This helps prevent data leaks caused by the disclosure of kubeconfig files.
        
        @description >  The default validity period of a kubeconfig file is 3 years. 180 days before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the kubeconfig file is valid for 3 years. The previous kubeconfig file still remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
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
        @summary Kubeconfig files store identity and authentication information that is used by clients to access Container Service for Kubernetes (ACK) clusters. To use a kubectl client to manage an ACK cluster, you need to use the corresponding kubeconfig file to connect to the ACK cluster. We recommend that you keep kubeconfig files confidential and revoke kubeconfig files that are not in use. This helps prevent data leaks caused by the disclosure of kubeconfig files.
        
        @description >  The default validity period of a kubeconfig file is 3 years. 180 days before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the kubeconfig file is valid for 3 years. The previous kubeconfig file still remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
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
        @deprecated OpenAPI DescribeClusterV2UserKubeconfig is deprecated
        
        @summary 获取集群kubeconfig接口
        
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
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_v2user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        """
        @deprecated OpenAPI DescribeClusterV2UserKubeconfig is deprecated
        
        @summary 获取集群kubeconfig接口
        
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
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_v2user_kubeconfig(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        """
        @deprecated OpenAPI DescribeClusterV2UserKubeconfig is deprecated
        
        @summary 获取集群kubeconfig接口
        
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
        @deprecated OpenAPI DescribeClusterV2UserKubeconfig is deprecated
        
        @summary 获取集群kubeconfig接口
        
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
        """
        @summary Queries the security vulnerability details of a cluster by cluster ID. The details include vulnerability name, vulnerability type, and vulnerability severity. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterVulsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterVulsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterVulsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_vuls_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterVulsResponse:
        """
        @summary Queries the security vulnerability details of a cluster by cluster ID. The details include vulnerability name, vulnerability type, and vulnerability severity. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterVulsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterVulsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClusterVulsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_vuls(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterVulsResponse:
        """
        @summary Queries the security vulnerability details of a cluster by cluster ID. The details include vulnerability name, vulnerability type, and vulnerability severity. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @return: DescribeClusterVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_vuls_with_options(cluster_id, headers, runtime)

    async def describe_cluster_vuls_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterVulsResponse:
        """
        @summary Queries the security vulnerability details of a cluster by cluster ID. The details include vulnerability name, vulnerability type, and vulnerability severity. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @return: DescribeClusterVulsResponse
        """
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
        @deprecated OpenAPI DescribeClusters is deprecated
        
        @summary Queries all the clusters that belong to the current Alibaba Cloud account, including Kubernetes clusters and Swarm clusters.
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_clusters_with_options_async(
        self,
        request: cs20151215_models.DescribeClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersResponse:
        """
        @deprecated OpenAPI DescribeClusters is deprecated
        
        @summary Queries all the clusters that belong to the current Alibaba Cloud account, including Kubernetes clusters and Swarm clusters.
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_clusters(
        self,
        request: cs20151215_models.DescribeClustersRequest,
    ) -> cs20151215_models.DescribeClustersResponse:
        """
        @deprecated OpenAPI DescribeClusters is deprecated
        
        @summary Queries all the clusters that belong to the current Alibaba Cloud account, including Kubernetes clusters and Swarm clusters.
        
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
        @deprecated OpenAPI DescribeClusters is deprecated
        
        @summary Queries all the clusters that belong to the current Alibaba Cloud account, including Kubernetes clusters and Swarm clusters.
        
        @param request: DescribeClustersRequest
        @return: DescribeClustersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_clusters_with_options_async(request, headers, runtime)

    def describe_clusters_for_region_with_options(
        self,
        region_id: str,
        request: cs20151215_models.DescribeClustersForRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersForRegionResponse:
        """
        @summary Queries all clusters in a specified region.
        
        @param request: DescribeClustersForRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersForRegionResponse
        """
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersForRegion',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/regions/{OpenApiUtilClient.get_encode_param(region_id)}/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersForRegionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersForRegionResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_clusters_for_region_with_options_async(
        self,
        region_id: str,
        request: cs20151215_models.DescribeClustersForRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersForRegionResponse:
        """
        @summary Queries all clusters in a specified region.
        
        @param request: DescribeClustersForRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersForRegionResponse
        """
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersForRegion',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/regions/{OpenApiUtilClient.get_encode_param(region_id)}/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersForRegionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersForRegionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_clusters_for_region(
        self,
        region_id: str,
        request: cs20151215_models.DescribeClustersForRegionRequest,
    ) -> cs20151215_models.DescribeClustersForRegionResponse:
        """
        @summary Queries all clusters in a specified region.
        
        @param request: DescribeClustersForRegionRequest
        @return: DescribeClustersForRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_clusters_for_region_with_options(region_id, request, headers, runtime)

    async def describe_clusters_for_region_async(
        self,
        region_id: str,
        request: cs20151215_models.DescribeClustersForRegionRequest,
    ) -> cs20151215_models.DescribeClustersForRegionResponse:
        """
        @summary Queries all clusters in a specified region.
        
        @param request: DescribeClustersForRegionRequest
        @return: DescribeClustersForRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_clusters_for_region_with_options_async(region_id, request, headers, runtime)

    def describe_clusters_v1with_options(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersV1Response:
        """
        @summary Queries the details about Container Service for Kubernetes (ACK) clusters of specified types or specifications within an account.
        
        @param request: DescribeClustersV1Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersV1Response
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersV1Response(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersV1Response(),
                self.execute(params, req, runtime)
            )

    async def describe_clusters_v1with_options_async(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersV1Response:
        """
        @summary Queries the details about Container Service for Kubernetes (ACK) clusters of specified types or specifications within an account.
        
        @param request: DescribeClustersV1Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersV1Response
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersV1Response(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeClustersV1Response(),
                await self.execute_async(params, req, runtime)
            )

    def describe_clusters_v1(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
    ) -> cs20151215_models.DescribeClustersV1Response:
        """
        @summary Queries the details about Container Service for Kubernetes (ACK) clusters of specified types or specifications within an account.
        
        @param request: DescribeClustersV1Request
        @return: DescribeClustersV1Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_clusters_v1with_options(request, headers, runtime)

    async def describe_clusters_v1_async(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
    ) -> cs20151215_models.DescribeClustersV1Response:
        """
        @summary Queries the details about Container Service for Kubernetes (ACK) clusters of specified types or specifications within an account.
        
        @param request: DescribeClustersV1Request
        @return: DescribeClustersV1Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_clusters_v1with_options_async(request, headers, runtime)

    def describe_edge_machine_active_process_with_options(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        """
        @deprecated OpenAPI DescribeEdgeMachineActiveProcess is deprecated
        
        @summary You can call the DescribeEdgeMachineActiveProcess operation to query the activation progress of a cloud-native box.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachineActiveProcessResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineActiveProcessResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineActiveProcessResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_edge_machine_active_process_with_options_async(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        """
        @deprecated OpenAPI DescribeEdgeMachineActiveProcess is deprecated
        
        @summary You can call the DescribeEdgeMachineActiveProcess operation to query the activation progress of a cloud-native box.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachineActiveProcessResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineActiveProcessResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineActiveProcessResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_edge_machine_active_process(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        """
        @deprecated OpenAPI DescribeEdgeMachineActiveProcess is deprecated
        
        @summary You can call the DescribeEdgeMachineActiveProcess operation to query the activation progress of a cloud-native box.
        
        @return: DescribeEdgeMachineActiveProcessResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_active_process_with_options(edge_machineid, headers, runtime)

    async def describe_edge_machine_active_process_async(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        """
        @deprecated OpenAPI DescribeEdgeMachineActiveProcess is deprecated
        
        @summary You can call the DescribeEdgeMachineActiveProcess operation to query the activation progress of a cloud-native box.
        
        @return: DescribeEdgeMachineActiveProcessResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machine_active_process_with_options_async(edge_machineid, headers, runtime)

    def describe_edge_machine_models_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        """
        @summary You can call the DescribeEdgeMachineModels operation to query the cloud-native box models.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachineModelsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineModelsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineModelsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_edge_machine_models_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        """
        @summary You can call the DescribeEdgeMachineModels operation to query the cloud-native box models.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachineModelsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineModelsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineModelsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_edge_machine_models(self) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        """
        @summary You can call the DescribeEdgeMachineModels operation to query the cloud-native box models.
        
        @return: DescribeEdgeMachineModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_models_with_options(headers, runtime)

    async def describe_edge_machine_models_async(self) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        """
        @summary You can call the DescribeEdgeMachineModels operation to query the cloud-native box models.
        
        @return: DescribeEdgeMachineModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machine_models_with_options_async(headers, runtime)

    def describe_edge_machine_tunnel_config_detail_with_options(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        """
        @summary You can call the DescribeEdgeMachineTunnelConfigDetail operation to obtain the SSH token of a cloud-native box.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachineTunnelConfigDetailResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_edge_machine_tunnel_config_detail_with_options_async(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        """
        @summary You can call the DescribeEdgeMachineTunnelConfigDetail operation to obtain the SSH token of a cloud-native box.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachineTunnelConfigDetailResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_edge_machine_tunnel_config_detail(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        """
        @summary You can call the DescribeEdgeMachineTunnelConfigDetail operation to obtain the SSH token of a cloud-native box.
        
        @return: DescribeEdgeMachineTunnelConfigDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_tunnel_config_detail_with_options(edge_machineid, headers, runtime)

    async def describe_edge_machine_tunnel_config_detail_async(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        """
        @summary You can call the DescribeEdgeMachineTunnelConfigDetail operation to obtain the SSH token of a cloud-native box.
        
        @return: DescribeEdgeMachineTunnelConfigDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machine_tunnel_config_detail_with_options_async(edge_machineid, headers, runtime)

    def describe_edge_machines_with_options(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        """
        @summary You can call the DescribeEdgeMachines operation to query a list of cloud-native boxes.
        
        @param request: DescribeEdgeMachinesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachinesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachinesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachinesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_edge_machines_with_options_async(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        """
        @summary You can call the DescribeEdgeMachines operation to query a list of cloud-native boxes.
        
        @param request: DescribeEdgeMachinesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeMachinesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachinesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEdgeMachinesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_edge_machines(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        """
        @summary You can call the DescribeEdgeMachines operation to query a list of cloud-native boxes.
        
        @param request: DescribeEdgeMachinesRequest
        @return: DescribeEdgeMachinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machines_with_options(request, headers, runtime)

    async def describe_edge_machines_async(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        """
        @summary You can call the DescribeEdgeMachines operation to query a list of cloud-native boxes.
        
        @param request: DescribeEdgeMachinesRequest
        @return: DescribeEdgeMachinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machines_with_options_async(request, headers, runtime)

    def describe_events_with_options(
        self,
        request: cs20151215_models.DescribeEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEventsResponse:
        """
        @summary Queries the detailed information about a type of events, including the severity level, status, and time. Events are generated when clusters are created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_events_with_options_async(
        self,
        request: cs20151215_models.DescribeEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEventsResponse:
        """
        @summary Queries the detailed information about a type of events, including the severity level, status, and time. Events are generated when clusters are created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_events(
        self,
        request: cs20151215_models.DescribeEventsRequest,
    ) -> cs20151215_models.DescribeEventsResponse:
        """
        @summary Queries the detailed information about a type of events, including the severity level, status, and time. Events are generated when clusters are created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeEventsRequest
        @return: DescribeEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_events_with_options(request, headers, runtime)

    async def describe_events_async(
        self,
        request: cs20151215_models.DescribeEventsRequest,
    ) -> cs20151215_models.DescribeEventsResponse:
        """
        @summary Queries the detailed information about a type of events, including the severity level, status, and time. Events are generated when clusters are created, modified, and updated, node pools are created and scaled out, and components are installed.
        
        @param request: DescribeEventsRequest
        @return: DescribeEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_events_with_options_async(request, headers, runtime)

    def describe_events_for_region_with_options(
        self,
        region_id: str,
        request: cs20151215_models.DescribeEventsForRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEventsForRegionResponse:
        """
        @summary Queries all events in a specified region.
        
        @param request: DescribeEventsForRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsForRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventsForRegion',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/regions/{OpenApiUtilClient.get_encode_param(region_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsForRegionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsForRegionResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_events_for_region_with_options_async(
        self,
        region_id: str,
        request: cs20151215_models.DescribeEventsForRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEventsForRegionResponse:
        """
        @summary Queries all events in a specified region.
        
        @param request: DescribeEventsForRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEventsForRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventsForRegion',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/regions/{OpenApiUtilClient.get_encode_param(region_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsForRegionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeEventsForRegionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_events_for_region(
        self,
        region_id: str,
        request: cs20151215_models.DescribeEventsForRegionRequest,
    ) -> cs20151215_models.DescribeEventsForRegionResponse:
        """
        @summary Queries all events in a specified region.
        
        @param request: DescribeEventsForRegionRequest
        @return: DescribeEventsForRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_events_for_region_with_options(region_id, request, headers, runtime)

    async def describe_events_for_region_async(
        self,
        region_id: str,
        request: cs20151215_models.DescribeEventsForRegionRequest,
    ) -> cs20151215_models.DescribeEventsForRegionResponse:
        """
        @summary Queries all events in a specified region.
        
        @param request: DescribeEventsForRegionRequest
        @return: DescribeEventsForRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_events_for_region_with_options_async(region_id, request, headers, runtime)

    def describe_external_agent_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        """
        @deprecated OpenAPI DescribeExternalAgent is deprecated
        
        @summary Queries the proxy configurations of a registered cluster by cluster ID.
        
        @description For more information, see [Register an external Kubernetes cluster](https://help.aliyun.com/document_detail/121053.html).
        
        @param request: DescribeExternalAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExternalAgentResponse
        Deprecated
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeExternalAgentResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeExternalAgentResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_external_agent_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        """
        @deprecated OpenAPI DescribeExternalAgent is deprecated
        
        @summary Queries the proxy configurations of a registered cluster by cluster ID.
        
        @description For more information, see [Register an external Kubernetes cluster](https://help.aliyun.com/document_detail/121053.html).
        
        @param request: DescribeExternalAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExternalAgentResponse
        Deprecated
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeExternalAgentResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeExternalAgentResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_external_agent(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        """
        @deprecated OpenAPI DescribeExternalAgent is deprecated
        
        @summary Queries the proxy configurations of a registered cluster by cluster ID.
        
        @description For more information, see [Register an external Kubernetes cluster](https://help.aliyun.com/document_detail/121053.html).
        
        @param request: DescribeExternalAgentRequest
        @return: DescribeExternalAgentResponse
        Deprecated
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
        @deprecated OpenAPI DescribeExternalAgent is deprecated
        
        @summary Queries the proxy configurations of a registered cluster by cluster ID.
        
        @description For more information, see [Register an external Kubernetes cluster](https://help.aliyun.com/document_detail/121053.html).
        
        @param request: DescribeExternalAgentRequest
        @return: DescribeExternalAgentResponse
        Deprecated
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
        """
        @summary Queries the detailed information about Kubernetes versions, including the version number, release date, expiration date, compatible OSs, and runtime.
        
        @param request: DescribeKubernetesVersionMetadataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKubernetesVersionMetadataResponse
        """
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
        if not UtilClient.is_unset(request.query_upgradable_version):
            query['QueryUpgradableVersion'] = request.query_upgradable_version
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_kubernetes_version_metadata_with_options_async(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        """
        @summary Queries the detailed information about Kubernetes versions, including the version number, release date, expiration date, compatible OSs, and runtime.
        
        @param request: DescribeKubernetesVersionMetadataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKubernetesVersionMetadataResponse
        """
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
        if not UtilClient.is_unset(request.query_upgradable_version):
            query['QueryUpgradableVersion'] = request.query_upgradable_version
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_kubernetes_version_metadata(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        """
        @summary Queries the detailed information about Kubernetes versions, including the version number, release date, expiration date, compatible OSs, and runtime.
        
        @param request: DescribeKubernetesVersionMetadataRequest
        @return: DescribeKubernetesVersionMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_kubernetes_version_metadata_with_options(request, headers, runtime)

    async def describe_kubernetes_version_metadata_async(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        """
        @summary Queries the detailed information about Kubernetes versions, including the version number, release date, expiration date, compatible OSs, and runtime.
        
        @param request: DescribeKubernetesVersionMetadataRequest
        @return: DescribeKubernetesVersionMetadataResponse
        """
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
        """
        @summary Queries the vulnerability information of a node pool, such as vulnerability names and severity levels, by specifying the ID of the node pool. We recommend that you periodically scan node pools for vulnerabilities to enhance cluster security.
        
        @param request: DescribeNodePoolVulsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodePoolVulsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeNodePoolVulsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeNodePoolVulsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_node_pool_vuls_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DescribeNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeNodePoolVulsResponse:
        """
        @summary Queries the vulnerability information of a node pool, such as vulnerability names and severity levels, by specifying the ID of the node pool. We recommend that you periodically scan node pools for vulnerabilities to enhance cluster security.
        
        @param request: DescribeNodePoolVulsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodePoolVulsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeNodePoolVulsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeNodePoolVulsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_node_pool_vuls(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DescribeNodePoolVulsRequest,
    ) -> cs20151215_models.DescribeNodePoolVulsResponse:
        """
        @summary Queries the vulnerability information of a node pool, such as vulnerability names and severity levels, by specifying the ID of the node pool. We recommend that you periodically scan node pools for vulnerabilities to enhance cluster security.
        
        @param request: DescribeNodePoolVulsRequest
        @return: DescribeNodePoolVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_node_pool_vuls_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def describe_node_pool_vuls_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DescribeNodePoolVulsRequest,
    ) -> cs20151215_models.DescribeNodePoolVulsResponse:
        """
        @summary Queries the vulnerability information of a node pool, such as vulnerability names and severity levels, by specifying the ID of the node pool. We recommend that you periodically scan node pools for vulnerabilities to enhance cluster security.
        
        @param request: DescribeNodePoolVulsRequest
        @return: DescribeNodePoolVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_node_pool_vuls_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def describe_policies_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePoliciesResponse:
        """
        @summary Queries a list of security policies. Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePoliciesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePoliciesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePoliciesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_policies_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePoliciesResponse:
        """
        @summary Queries a list of security policies. Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePoliciesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePoliciesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePoliciesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_policies(self) -> cs20151215_models.DescribePoliciesResponse:
        """
        @summary Queries a list of security policies. Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment.
        
        @return: DescribePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policies_with_options(headers, runtime)

    async def describe_policies_async(self) -> cs20151215_models.DescribePoliciesResponse:
        """
        @summary Queries a list of security policies. Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment.
        
        @return: DescribePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policies_with_options_async(headers, runtime)

    def describe_policy_details_with_options(
        self,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        """
        @summary Queries the detailed information about a policy. The information includes the content, action, and severity level of the policy. Container Service for Kubernetes (ACK) provides the following types of predefined security policies: Compliance, Infra, K8s-general, and pod security policy (PSP). These policies ensure that containers are running in the production environment in a secure manner.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyDetailsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_policy_details_with_options_async(
        self,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        """
        @summary Queries the detailed information about a policy. The information includes the content, action, and severity level of the policy. Container Service for Kubernetes (ACK) provides the following types of predefined security policies: Compliance, Infra, K8s-general, and pod security policy (PSP). These policies ensure that containers are running in the production environment in a secure manner.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyDetailsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_policy_details(
        self,
        policy_name: str,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        """
        @summary Queries the detailed information about a policy. The information includes the content, action, and severity level of the policy. Container Service for Kubernetes (ACK) provides the following types of predefined security policies: Compliance, Infra, K8s-general, and pod security policy (PSP). These policies ensure that containers are running in the production environment in a secure manner.
        
        @return: DescribePolicyDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_details_with_options(policy_name, headers, runtime)

    async def describe_policy_details_async(
        self,
        policy_name: str,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        """
        @summary Queries the detailed information about a policy. The information includes the content, action, and severity level of the policy. Container Service for Kubernetes (ACK) provides the following types of predefined security policies: Compliance, Infra, K8s-general, and pod security policy (PSP). These policies ensure that containers are running in the production environment in a secure manner.
        
        @return: DescribePolicyDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policy_details_with_options_async(policy_name, headers, runtime)

    def describe_policy_governance_in_cluster_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment. You can call the DescribePolicyGovernanceInCluster operation to query the details of policies for an ACK cluster. For example, you can query the number of policies that are enabled per severity level, the audit logs of policies, and the blocking and alerting information.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyGovernanceInClusterResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyGovernanceInClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyGovernanceInClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_policy_governance_in_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment. You can call the DescribePolicyGovernanceInCluster operation to query the details of policies for an ACK cluster. For example, you can query the number of policies that are enabled per severity level, the audit logs of policies, and the blocking and alerting information.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyGovernanceInClusterResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyGovernanceInClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyGovernanceInClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_policy_governance_in_cluster(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment. You can call the DescribePolicyGovernanceInCluster operation to query the details of policies for an ACK cluster. For example, you can query the number of policies that are enabled per severity level, the audit logs of policies, and the blocking and alerting information.
        
        @return: DescribePolicyGovernanceInClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_governance_in_cluster_with_options(cluster_id, headers, runtime)

    async def describe_policy_governance_in_cluster_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) clusters offer a variety of built-in container security policies, such as Compliance, Infra, K8s-general, and pod security policy (PSP). You can use these policies to ensure the security of containers running in a production environment. You can call the DescribePolicyGovernanceInCluster operation to query the details of policies for an ACK cluster. For example, you can query the number of policies that are enabled per severity level, the audit logs of policies, and the blocking and alerting information.
        
        @return: DescribePolicyGovernanceInClusterResponse
        """
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
        """
        @summary Queries the detailed information about policy instances of the specified type in a Container Service for Kubernetes (ACK) cluster, such as the policy description and severity level. You can choose a type of security policy for an ACK cluster, specify the action and applicable scope of the policy, and then create and deploy a policy instance.
        
        @param request: DescribePolicyInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_policy_instances_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribePolicyInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyInstancesResponse:
        """
        @summary Queries the detailed information about policy instances of the specified type in a Container Service for Kubernetes (ACK) cluster, such as the policy description and severity level. You can choose a type of security policy for an ACK cluster, specify the action and applicable scope of the policy, and then create and deploy a policy instance.
        
        @param request: DescribePolicyInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_policy_instances(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribePolicyInstancesRequest,
    ) -> cs20151215_models.DescribePolicyInstancesResponse:
        """
        @summary Queries the detailed information about policy instances of the specified type in a Container Service for Kubernetes (ACK) cluster, such as the policy description and severity level. You can choose a type of security policy for an ACK cluster, specify the action and applicable scope of the policy, and then create and deploy a policy instance.
        
        @param request: DescribePolicyInstancesRequest
        @return: DescribePolicyInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_with_options(cluster_id, request, headers, runtime)

    async def describe_policy_instances_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribePolicyInstancesRequest,
    ) -> cs20151215_models.DescribePolicyInstancesResponse:
        """
        @summary Queries the detailed information about policy instances of the specified type in a Container Service for Kubernetes (ACK) cluster, such as the policy description and severity level. You can choose a type of security policy for an ACK cluster, specify the action and applicable scope of the policy, and then create and deploy a policy instance.
        
        @param request: DescribePolicyInstancesRequest
        @return: DescribePolicyInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policy_instances_with_options_async(cluster_id, request, headers, runtime)

    def describe_policy_instances_status_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries the deployment of policy instances in the current Container Service for Kubernetes (ACK) cluster, including the number of policy instances of each type and the number of policy types of each severity level.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesStatusResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_policy_instances_status_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries the deployment of policy instances in the current Container Service for Kubernetes (ACK) cluster, including the number of policy instances of each type and the number of policy types of each severity level.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesStatusResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribePolicyInstancesStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_policy_instances_status(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries the deployment of policy instances in the current Container Service for Kubernetes (ACK) cluster, including the number of policy instances of each type and the number of policy types of each severity level.
        
        @return: DescribePolicyInstancesStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_status_with_options(cluster_id, headers, runtime)

    async def describe_policy_instances_status_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries the deployment of policy instances in the current Container Service for Kubernetes (ACK) cluster, including the number of policy instances of each type and the number of policy types of each severity level.
        
        @return: DescribePolicyInstancesStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policy_instances_status_with_options_async(cluster_id, headers, runtime)

    def describe_resources_delete_protection_with_options(
        self,
        cluster_id: str,
        resource_type: str,
        request: cs20151215_models.DescribeResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeResourcesDeleteProtectionResponse:
        """
        @summary Queries whether the deletion protection feature is enabled for the specified resources. The resources that you can query include namespaces and Services.
        
        @param request: DescribeResourcesDeleteProtectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourcesDeleteProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resources):
            query['resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcesDeleteProtection',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_type)}/protection',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeResourcesDeleteProtectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeResourcesDeleteProtectionResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_resources_delete_protection_with_options_async(
        self,
        cluster_id: str,
        resource_type: str,
        request: cs20151215_models.DescribeResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeResourcesDeleteProtectionResponse:
        """
        @summary Queries whether the deletion protection feature is enabled for the specified resources. The resources that you can query include namespaces and Services.
        
        @param request: DescribeResourcesDeleteProtectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourcesDeleteProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resources):
            query['resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcesDeleteProtection',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_type)}/protection',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeResourcesDeleteProtectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeResourcesDeleteProtectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_resources_delete_protection(
        self,
        cluster_id: str,
        resource_type: str,
        request: cs20151215_models.DescribeResourcesDeleteProtectionRequest,
    ) -> cs20151215_models.DescribeResourcesDeleteProtectionResponse:
        """
        @summary Queries whether the deletion protection feature is enabled for the specified resources. The resources that you can query include namespaces and Services.
        
        @param request: DescribeResourcesDeleteProtectionRequest
        @return: DescribeResourcesDeleteProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resources_delete_protection_with_options(cluster_id, resource_type, request, headers, runtime)

    async def describe_resources_delete_protection_async(
        self,
        cluster_id: str,
        resource_type: str,
        request: cs20151215_models.DescribeResourcesDeleteProtectionRequest,
    ) -> cs20151215_models.DescribeResourcesDeleteProtectionResponse:
        """
        @summary Queries whether the deletion protection feature is enabled for the specified resources. The resources that you can query include namespaces and Services.
        
        @param request: DescribeResourcesDeleteProtectionRequest
        @return: DescribeResourcesDeleteProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resources_delete_protection_with_options_async(cluster_id, resource_type, request, headers, runtime)

    def describe_subaccount_k8s_cluster_user_config_with_options(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.DescribeSubaccountK8sClusterUserConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse:
        """
        @summary Queries or issues the kubeconfig credentials of a Resource Access Management (RAM) user or RAM role of the account. If you are the permission manager of a Container Service for Kubernetes (ACK) cluster, you can issue the kubeconfig credentials to a specific RAM user or RAM role of the account by using the Alibaba Cloud account. The kubeconfig credentials, which are used to connect to the ACK cluster, contain the identity information about the RAM user or RAM role.
        
        @description You can call this operation only by using an Alibaba Cloud account.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse(),
                self.execute(params, req, runtime)
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
        @summary Queries or issues the kubeconfig credentials of a Resource Access Management (RAM) user or RAM role of the account. If you are the permission manager of a Container Service for Kubernetes (ACK) cluster, you can issue the kubeconfig credentials to a specific RAM user or RAM role of the account by using the Alibaba Cloud account. The kubeconfig credentials, which are used to connect to the ACK cluster, contain the identity information about the RAM user or RAM role.
        
        @description You can call this operation only by using an Alibaba Cloud account.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_subaccount_k8s_cluster_user_config(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.DescribeSubaccountK8sClusterUserConfigRequest,
    ) -> cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse:
        """
        @summary Queries or issues the kubeconfig credentials of a Resource Access Management (RAM) user or RAM role of the account. If you are the permission manager of a Container Service for Kubernetes (ACK) cluster, you can issue the kubeconfig credentials to a specific RAM user or RAM role of the account by using the Alibaba Cloud account. The kubeconfig credentials, which are used to connect to the ACK cluster, contain the identity information about the RAM user or RAM role.
        
        @description You can call this operation only by using an Alibaba Cloud account.
        
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
        @summary Queries or issues the kubeconfig credentials of a Resource Access Management (RAM) user or RAM role of the account. If you are the permission manager of a Container Service for Kubernetes (ACK) cluster, you can issue the kubeconfig credentials to a specific RAM user or RAM role of the account by using the Alibaba Cloud account. The kubeconfig credentials, which are used to connect to the ACK cluster, contain the identity information about the RAM user or RAM role.
        
        @description You can call this operation only by using an Alibaba Cloud account.
        
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
        """
        @summary Queries detailed information about a task, such as the task type, status, and progress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskInfoResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTaskInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTaskInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_task_info_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        """
        @summary Queries detailed information about a task, such as the task type, status, and progress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskInfoResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTaskInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTaskInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_task_info(
        self,
        task_id: str,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        """
        @summary Queries detailed information about a task, such as the task type, status, and progress.
        
        @return: DescribeTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_info_with_options(task_id, headers, runtime)

    async def describe_task_info_async(
        self,
        task_id: str,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        """
        @summary Queries detailed information about a task, such as the task type, status, and progress.
        
        @return: DescribeTaskInfoResponse
        """
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
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplateAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateAttributeResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplateAttributeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplateAttributeResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_template_attribute_with_options_async(
        self,
        template_id: str,
        request: cs20151215_models.DescribeTemplateAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplateAttributeResponse:
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplateAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateAttributeResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplateAttributeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplateAttributeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_template_attribute(
        self,
        template_id: str,
        request: cs20151215_models.DescribeTemplateAttributeRequest,
    ) -> cs20151215_models.DescribeTemplateAttributeResponse:
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplateAttributeRequest
        @return: DescribeTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_template_attribute_with_options(template_id, request, headers, runtime)

    async def describe_template_attribute_async(
        self,
        template_id: str,
        request: cs20151215_models.DescribeTemplateAttributeRequest,
    ) -> cs20151215_models.DescribeTemplateAttributeResponse:
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplateAttributeRequest
        @return: DescribeTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_template_attribute_with_options_async(template_id, request, headers, runtime)

    def describe_templates_with_options(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplatesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplatesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplatesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_templates_with_options_async(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplatesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplatesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTemplatesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_templates(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplatesRequest
        @return: DescribeTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(request, headers, runtime)

    async def describe_templates_async(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        """
        @summary An orchestration template defines and describes a group of Kubernetes resources. It declaratively describes the configuration of an application or how an application runs. You can call the DescribeTemplates API operation to query orchestration templates and their detailed information, including access permissions, YAML content, and labels.
        
        @param request: DescribeTemplatesRequest
        @return: DescribeTemplatesResponse
        """
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
        """
        @summary Queries triggers that match specific conditions.
        
        @param request: DescribeTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTriggerResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTriggerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTriggerResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_trigger_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTriggerResponse:
        """
        @summary Queries triggers that match specific conditions.
        
        @param request: DescribeTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTriggerResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeTriggerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeTriggerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_trigger(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeTriggerRequest,
    ) -> cs20151215_models.DescribeTriggerResponse:
        """
        @summary Queries triggers that match specific conditions.
        
        @param request: DescribeTriggerRequest
        @return: DescribeTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_trigger_with_options(cluster_id, request, headers, runtime)

    async def describe_trigger_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeTriggerRequest,
    ) -> cs20151215_models.DescribeTriggerResponse:
        """
        @summary Queries triggers that match specific conditions.
        
        @param request: DescribeTriggerRequest
        @return: DescribeTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_trigger_with_options_async(cluster_id, request, headers, runtime)

    def describe_user_cluster_namespaces_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        """
        @summary You can use Kubernetes namespaces to limit users from accessing resources in a Container Service for Kubernetes (ACK) cluster. Users that are granted Role-Based Access Control (RBAC) permissions only on one namespace cannot access resources in other namespaces. Queries the RBAC permissions that are granted to the current Resource Access Management (RAM) user or RAM role on an ACK cluster.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserClusterNamespacesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeUserClusterNamespacesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeUserClusterNamespacesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_user_cluster_namespaces_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        """
        @summary You can use Kubernetes namespaces to limit users from accessing resources in a Container Service for Kubernetes (ACK) cluster. Users that are granted Role-Based Access Control (RBAC) permissions only on one namespace cannot access resources in other namespaces. Queries the RBAC permissions that are granted to the current Resource Access Management (RAM) user or RAM role on an ACK cluster.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserClusterNamespacesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeUserClusterNamespacesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeUserClusterNamespacesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_user_cluster_namespaces(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        """
        @summary You can use Kubernetes namespaces to limit users from accessing resources in a Container Service for Kubernetes (ACK) cluster. Users that are granted Role-Based Access Control (RBAC) permissions only on one namespace cannot access resources in other namespaces. Queries the RBAC permissions that are granted to the current Resource Access Management (RAM) user or RAM role on an ACK cluster.
        
        @return: DescribeUserClusterNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_cluster_namespaces_with_options(cluster_id, headers, runtime)

    async def describe_user_cluster_namespaces_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        """
        @summary You can use Kubernetes namespaces to limit users from accessing resources in a Container Service for Kubernetes (ACK) cluster. Users that are granted Role-Based Access Control (RBAC) permissions only on one namespace cannot access resources in other namespaces. Queries the RBAC permissions that are granted to the current Resource Access Management (RAM) user or RAM role on an ACK cluster.
        
        @return: DescribeUserClusterNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_cluster_namespaces_with_options_async(cluster_id, headers, runtime)

    def describe_user_permission_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        """
        @summary In an Container Service for Kubernetes (ACK) cluster, you can create and specify different Resource Access Management (RAM) users or roles to have different access permissions. This ensures access control and resource isolation. You can call the DescribeUserPermission operation to query the permissions that are granted to a RAM user or RAM role on ACK clusters, including the resources that are allowed to access, the scope of the permissions, the predefined role, and the permission source.
        
        @description *Precautions**:
        If you call this operation as a Resource Access Management (RAM) user or by assuming a RAM role, only the permissions granted on the clusters on which the current account has the role-based access control (RBAC) administrator permissions are returned. If you want to query the permissions on all clusters, you must use an account that has the RBAC administrator permissions on all clusters.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserPermissionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeUserPermissionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeUserPermissionResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_user_permission_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        """
        @summary In an Container Service for Kubernetes (ACK) cluster, you can create and specify different Resource Access Management (RAM) users or roles to have different access permissions. This ensures access control and resource isolation. You can call the DescribeUserPermission operation to query the permissions that are granted to a RAM user or RAM role on ACK clusters, including the resources that are allowed to access, the scope of the permissions, the predefined role, and the permission source.
        
        @description *Precautions**:
        If you call this operation as a Resource Access Management (RAM) user or by assuming a RAM role, only the permissions granted on the clusters on which the current account has the role-based access control (RBAC) administrator permissions are returned. If you want to query the permissions on all clusters, you must use an account that has the RBAC administrator permissions on all clusters.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserPermissionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeUserPermissionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeUserPermissionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_user_permission(
        self,
        uid: str,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        """
        @summary In an Container Service for Kubernetes (ACK) cluster, you can create and specify different Resource Access Management (RAM) users or roles to have different access permissions. This ensures access control and resource isolation. You can call the DescribeUserPermission operation to query the permissions that are granted to a RAM user or RAM role on ACK clusters, including the resources that are allowed to access, the scope of the permissions, the predefined role, and the permission source.
        
        @description *Precautions**:
        If you call this operation as a Resource Access Management (RAM) user or by assuming a RAM role, only the permissions granted on the clusters on which the current account has the role-based access control (RBAC) administrator permissions are returned. If you want to query the permissions on all clusters, you must use an account that has the RBAC administrator permissions on all clusters.
        
        @return: DescribeUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_permission_with_options(uid, headers, runtime)

    async def describe_user_permission_async(
        self,
        uid: str,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        """
        @summary In an Container Service for Kubernetes (ACK) cluster, you can create and specify different Resource Access Management (RAM) users or roles to have different access permissions. This ensures access control and resource isolation. You can call the DescribeUserPermission operation to query the permissions that are granted to a RAM user or RAM role on ACK clusters, including the resources that are allowed to access, the scope of the permissions, the predefined role, and the permission source.
        
        @description *Precautions**:
        If you call this operation as a Resource Access Management (RAM) user or by assuming a RAM role, only the permissions granted on the clusters on which the current account has the role-based access control (RBAC) administrator permissions are returned. If you want to query the permissions on all clusters, you must use an account that has the RBAC administrator permissions on all clusters.
        
        @return: DescribeUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_permission_with_options_async(uid, headers, runtime)

    def describe_user_quota_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserQuotaResponse:
        """
        @summary Queries quotas related to Container Service for Kubernetes (ACK) clusters, node pools, and nodes. To increase a quota, submit an application in the Quota Center console.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserQuotaResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeUserQuotaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeUserQuotaResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_user_quota_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserQuotaResponse:
        """
        @summary Queries quotas related to Container Service for Kubernetes (ACK) clusters, node pools, and nodes. To increase a quota, submit an application in the Quota Center console.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserQuotaResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.DescribeUserQuotaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.DescribeUserQuotaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_user_quota(self) -> cs20151215_models.DescribeUserQuotaResponse:
        """
        @summary Queries quotas related to Container Service for Kubernetes (ACK) clusters, node pools, and nodes. To increase a quota, submit an application in the Quota Center console.
        
        @return: DescribeUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_quota_with_options(headers, runtime)

    async def describe_user_quota_async(self) -> cs20151215_models.DescribeUserQuotaResponse:
        """
        @summary Queries quotas related to Container Service for Kubernetes (ACK) clusters, node pools, and nodes. To increase a quota, submit an application in the Quota Center console.
        
        @return: DescribeUserQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_quota_with_options_async(headers, runtime)

    def edge_cluster_add_edge_machine_with_options(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        """
        @deprecated OpenAPI EdgeClusterAddEdgeMachine is deprecated
        
        @summary You can call the EdgeClusterAddEdgeMachine operation to add a cloud-native box to a Container Service for Kubernetes (ACK) Edge cluster.
        
        @param request: EdgeClusterAddEdgeMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EdgeClusterAddEdgeMachineResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.EdgeClusterAddEdgeMachineResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.EdgeClusterAddEdgeMachineResponse(),
                self.execute(params, req, runtime)
            )

    async def edge_cluster_add_edge_machine_with_options_async(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        """
        @deprecated OpenAPI EdgeClusterAddEdgeMachine is deprecated
        
        @summary You can call the EdgeClusterAddEdgeMachine operation to add a cloud-native box to a Container Service for Kubernetes (ACK) Edge cluster.
        
        @param request: EdgeClusterAddEdgeMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EdgeClusterAddEdgeMachineResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.EdgeClusterAddEdgeMachineResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.EdgeClusterAddEdgeMachineResponse(),
                await self.execute_async(params, req, runtime)
            )

    def edge_cluster_add_edge_machine(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        """
        @deprecated OpenAPI EdgeClusterAddEdgeMachine is deprecated
        
        @summary You can call the EdgeClusterAddEdgeMachine operation to add a cloud-native box to a Container Service for Kubernetes (ACK) Edge cluster.
        
        @param request: EdgeClusterAddEdgeMachineRequest
        @return: EdgeClusterAddEdgeMachineResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.edge_cluster_add_edge_machine_with_options(clusterid, edge_machineid, request, headers, runtime)

    async def edge_cluster_add_edge_machine_async(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        """
        @deprecated OpenAPI EdgeClusterAddEdgeMachine is deprecated
        
        @summary You can call the EdgeClusterAddEdgeMachine operation to add a cloud-native box to a Container Service for Kubernetes (ACK) Edge cluster.
        
        @param request: EdgeClusterAddEdgeMachineRequest
        @return: EdgeClusterAddEdgeMachineResponse
        Deprecated
        """
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
        @summary Patches node vulnerabilities in a node pool to enhance node security. Cloud Security provided by Alibaba Cloud periodically scans Elastic Compute Service (ECS) instances for vulnerabilities and provides suggestions on how to patch the detected vulnerabilities. Vulnerability patching may require node restarts. Make sure that your cluster has sufficient idle nodes for node draining.
        
        @description 1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.FixNodePoolVulsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.FixNodePoolVulsResponse(),
                self.execute(params, req, runtime)
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
        @summary Patches node vulnerabilities in a node pool to enhance node security. Cloud Security provided by Alibaba Cloud periodically scans Elastic Compute Service (ECS) instances for vulnerabilities and provides suggestions on how to patch the detected vulnerabilities. Vulnerability patching may require node restarts. Make sure that your cluster has sufficient idle nodes for node draining.
        
        @description 1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.FixNodePoolVulsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.FixNodePoolVulsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def fix_node_pool_vuls(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.FixNodePoolVulsRequest,
    ) -> cs20151215_models.FixNodePoolVulsResponse:
        """
        @summary Patches node vulnerabilities in a node pool to enhance node security. Cloud Security provided by Alibaba Cloud periodically scans Elastic Compute Service (ECS) instances for vulnerabilities and provides suggestions on how to patch the detected vulnerabilities. Vulnerability patching may require node restarts. Make sure that your cluster has sufficient idle nodes for node draining.
        
        @description 1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
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
        @summary Patches node vulnerabilities in a node pool to enhance node security. Cloud Security provided by Alibaba Cloud periodically scans Elastic Compute Service (ECS) instances for vulnerabilities and provides suggestions on how to patch the detected vulnerabilities. Vulnerability patching may require node restarts. Make sure that your cluster has sufficient idle nodes for node draining.
        
        @description 1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
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
        """
        @summary You can call the GetClusterAddonInstance operation to query the information of a component instance in a cluster, including the version, configurations, and log status of the component instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterAddonInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterAddonInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterAddonInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def get_cluster_addon_instance_with_options_async(
        self,
        cluster_id: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterAddonInstanceResponse:
        """
        @summary You can call the GetClusterAddonInstance operation to query the information of a component instance in a cluster, including the version, configurations, and log status of the component instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterAddonInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterAddonInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterAddonInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_cluster_addon_instance(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> cs20151215_models.GetClusterAddonInstanceResponse:
        """
        @summary You can call the GetClusterAddonInstance operation to query the information of a component instance in a cluster, including the version, configurations, and log status of the component instance.
        
        @return: GetClusterAddonInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_addon_instance_with_options(cluster_id, instance_name, headers, runtime)

    async def get_cluster_addon_instance_async(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> cs20151215_models.GetClusterAddonInstanceResponse:
        """
        @summary You can call the GetClusterAddonInstance operation to query the information of a component instance in a cluster, including the version, configurations, and log status of the component instance.
        
        @return: GetClusterAddonInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_addon_instance_with_options_async(cluster_id, instance_name, headers, runtime)

    def get_cluster_audit_project_with_options(
        self,
        clusterid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterAuditProjectResponse:
        """
        @summary You can call the GetClusterAuditProject operation to check whether the cluster has API Server auditing enabled and the corresponding Simple Log Service project that stores API Server audit logs.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterAuditProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterAuditProject',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/audit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterAuditProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterAuditProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def get_cluster_audit_project_with_options_async(
        self,
        clusterid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterAuditProjectResponse:
        """
        @summary You can call the GetClusterAuditProject operation to check whether the cluster has API Server auditing enabled and the corresponding Simple Log Service project that stores API Server audit logs.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterAuditProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterAuditProject',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/audit',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterAuditProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterAuditProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_cluster_audit_project(
        self,
        clusterid: str,
    ) -> cs20151215_models.GetClusterAuditProjectResponse:
        """
        @summary You can call the GetClusterAuditProject operation to check whether the cluster has API Server auditing enabled and the corresponding Simple Log Service project that stores API Server audit logs.
        
        @return: GetClusterAuditProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_audit_project_with_options(clusterid, headers, runtime)

    async def get_cluster_audit_project_async(
        self,
        clusterid: str,
    ) -> cs20151215_models.GetClusterAuditProjectResponse:
        """
        @summary You can call the GetClusterAuditProject operation to check whether the cluster has API Server auditing enabled and the corresponding Simple Log Service project that stores API Server audit logs.
        
        @return: GetClusterAuditProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_audit_project_with_options_async(clusterid, headers, runtime)

    def get_cluster_check_with_options(
        self,
        cluster_id: str,
        check_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterCheckResponse:
        """
        @summary Queries a cluster check task by cluster ID and task ID. You can view the status, check items, creation time, and end time of the task. Container Intelligence Service (CIS) provides a variety of Kubernetes cluster check features, including cluster update check, cluster migration check, component installation check, component update check, and node pool check.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterCheckResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterCheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterCheckResponse(),
                self.execute(params, req, runtime)
            )

    async def get_cluster_check_with_options_async(
        self,
        cluster_id: str,
        check_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterCheckResponse:
        """
        @summary Queries a cluster check task by cluster ID and task ID. You can view the status, check items, creation time, and end time of the task. Container Intelligence Service (CIS) provides a variety of Kubernetes cluster check features, including cluster update check, cluster migration check, component installation check, component update check, and node pool check.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterCheckResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterCheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterCheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_cluster_check(
        self,
        cluster_id: str,
        check_id: str,
    ) -> cs20151215_models.GetClusterCheckResponse:
        """
        @summary Queries a cluster check task by cluster ID and task ID. You can view the status, check items, creation time, and end time of the task. Container Intelligence Service (CIS) provides a variety of Kubernetes cluster check features, including cluster update check, cluster migration check, component installation check, component update check, and node pool check.
        
        @return: GetClusterCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_check_with_options(cluster_id, check_id, headers, runtime)

    async def get_cluster_check_async(
        self,
        cluster_id: str,
        check_id: str,
    ) -> cs20151215_models.GetClusterCheckResponse:
        """
        @summary Queries a cluster check task by cluster ID and task ID. You can view the status, check items, creation time, and end time of the task. Container Intelligence Service (CIS) provides a variety of Kubernetes cluster check features, including cluster update check, cluster migration check, component installation check, component update check, and node pool check.
        
        @return: GetClusterCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_check_with_options_async(cluster_id, check_id, headers, runtime)

    def get_cluster_diagnosis_check_items_with_options(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisCheckItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterDiagnosisCheckItemsResponse:
        """
        @summary Queries cluster diagnostic items.
        
        @param request: GetClusterDiagnosisCheckItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterDiagnosisCheckItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDiagnosisCheckItems',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/diagnosis/{OpenApiUtilClient.get_encode_param(diagnosis_id)}/check_items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisCheckItemsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisCheckItemsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_cluster_diagnosis_check_items_with_options_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisCheckItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterDiagnosisCheckItemsResponse:
        """
        @summary Queries cluster diagnostic items.
        
        @param request: GetClusterDiagnosisCheckItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterDiagnosisCheckItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDiagnosisCheckItems',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/diagnosis/{OpenApiUtilClient.get_encode_param(diagnosis_id)}/check_items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisCheckItemsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisCheckItemsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_cluster_diagnosis_check_items(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisCheckItemsRequest,
    ) -> cs20151215_models.GetClusterDiagnosisCheckItemsResponse:
        """
        @summary Queries cluster diagnostic items.
        
        @param request: GetClusterDiagnosisCheckItemsRequest
        @return: GetClusterDiagnosisCheckItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_diagnosis_check_items_with_options(cluster_id, diagnosis_id, request, headers, runtime)

    async def get_cluster_diagnosis_check_items_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisCheckItemsRequest,
    ) -> cs20151215_models.GetClusterDiagnosisCheckItemsResponse:
        """
        @summary Queries cluster diagnostic items.
        
        @param request: GetClusterDiagnosisCheckItemsRequest
        @return: GetClusterDiagnosisCheckItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_diagnosis_check_items_with_options_async(cluster_id, diagnosis_id, request, headers, runtime)

    def get_cluster_diagnosis_result_with_options(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterDiagnosisResultResponse:
        """
        @summary Queries cluster diagnostic results.
        
        @param request: GetClusterDiagnosisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterDiagnosisResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDiagnosisResult',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/diagnosis/{OpenApiUtilClient.get_encode_param(diagnosis_id)}/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_cluster_diagnosis_result_with_options_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterDiagnosisResultResponse:
        """
        @summary Queries cluster diagnostic results.
        
        @param request: GetClusterDiagnosisResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterDiagnosisResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDiagnosisResult',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/diagnosis/{OpenApiUtilClient.get_encode_param(diagnosis_id)}/result',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetClusterDiagnosisResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_cluster_diagnosis_result(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisResultRequest,
    ) -> cs20151215_models.GetClusterDiagnosisResultResponse:
        """
        @summary Queries cluster diagnostic results.
        
        @param request: GetClusterDiagnosisResultRequest
        @return: GetClusterDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_diagnosis_result_with_options(cluster_id, diagnosis_id, request, headers, runtime)

    async def get_cluster_diagnosis_result_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: cs20151215_models.GetClusterDiagnosisResultRequest,
    ) -> cs20151215_models.GetClusterDiagnosisResultResponse:
        """
        @summary Queries cluster diagnostic results.
        
        @param request: GetClusterDiagnosisResultRequest
        @return: GetClusterDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_diagnosis_result_with_options_async(cluster_id, diagnosis_id, request, headers, runtime)

    def get_kubernetes_trigger_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        """
        @deprecated OpenAPI GetKubernetesTrigger is deprecated
        
        @summary You can call the GetKubernetesTrigger operationto query the triggers of an application by application name.
        
        @param request: GetKubernetesTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKubernetesTriggerResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetKubernetesTriggerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetKubernetesTriggerResponse(),
                self.execute(params, req, runtime)
            )

    async def get_kubernetes_trigger_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        """
        @deprecated OpenAPI GetKubernetesTrigger is deprecated
        
        @summary You can call the GetKubernetesTrigger operationto query the triggers of an application by application name.
        
        @param request: GetKubernetesTriggerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKubernetesTriggerResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetKubernetesTriggerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetKubernetesTriggerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_kubernetes_trigger(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        """
        @deprecated OpenAPI GetKubernetesTrigger is deprecated
        
        @summary You can call the GetKubernetesTrigger operationto query the triggers of an application by application name.
        
        @param request: GetKubernetesTriggerRequest
        @return: GetKubernetesTriggerResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_kubernetes_trigger_with_options(cluster_id, request, headers, runtime)

    async def get_kubernetes_trigger_async(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        """
        @deprecated OpenAPI GetKubernetesTrigger is deprecated
        
        @summary You can call the GetKubernetesTrigger operationto query the triggers of an application by application name.
        
        @param request: GetKubernetesTriggerRequest
        @return: GetKubernetesTriggerResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_kubernetes_trigger_with_options_async(cluster_id, request, headers, runtime)

    def get_upgrade_status_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        """
        @deprecated OpenAPI GetUpgradeStatus is deprecated
        
        @summary You can call the GetUpgradeStatus operation to query the update progress of a cluster by cluster ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUpgradeStatusResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetUpgradeStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetUpgradeStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def get_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        """
        @deprecated OpenAPI GetUpgradeStatus is deprecated
        
        @summary You can call the GetUpgradeStatus operation to query the update progress of a cluster by cluster ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUpgradeStatusResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GetUpgradeStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GetUpgradeStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_upgrade_status(
        self,
        cluster_id: str,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        """
        @deprecated OpenAPI GetUpgradeStatus is deprecated
        
        @summary You can call the GetUpgradeStatus operation to query the update progress of a cluster by cluster ID.
        
        @return: GetUpgradeStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_upgrade_status_with_options(cluster_id, headers, runtime)

    async def get_upgrade_status_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        """
        @deprecated OpenAPI GetUpgradeStatus is deprecated
        
        @summary You can call the GetUpgradeStatus operation to query the update progress of a cluster by cluster ID.
        
        @return: GetUpgradeStatusResponse
        Deprecated
        """
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
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        If you use a Resource Access Management (RAM) user to call the operation, make sure that the RAM user has the permissions to modify the permissions of other RAM users or RAM roles. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned after you call the operation. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](https://help.aliyun.com/document_detail/119035.html).
        If you update full permissions, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GrantPermissionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GrantPermissionsResponse(),
                self.execute(params, req, runtime)
            )

    async def grant_permissions_with_options_async(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GrantPermissionsResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        If you use a Resource Access Management (RAM) user to call the operation, make sure that the RAM user has the permissions to modify the permissions of other RAM users or RAM roles. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned after you call the operation. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](https://help.aliyun.com/document_detail/119035.html).
        If you update full permissions, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.GrantPermissionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.GrantPermissionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def grant_permissions(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
    ) -> cs20151215_models.GrantPermissionsResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        If you use a Resource Access Management (RAM) user to call the operation, make sure that the RAM user has the permissions to modify the permissions of other RAM users or RAM roles. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned after you call the operation. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](https://help.aliyun.com/document_detail/119035.html).
        If you update full permissions, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation.
        
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
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        If you use a Resource Access Management (RAM) user to call the operation, make sure that the RAM user has the permissions to modify the permissions of other RAM users or RAM roles. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned after you call the operation. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](https://help.aliyun.com/document_detail/119035.html).
        If you update full permissions, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation.
        
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
        """
        @summary Installs a component by specifying the name and version of the component. To enhance Kubernetes capabilities, you can install a variety of components in Container Service for Kubernetes (ACK) clusters, such as fully-managed core components and application, logging and monitoring, network, storage, and security group components.
        
        @param request: InstallClusterAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallClusterAddonsResponse
        """
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.InstallClusterAddonsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.InstallClusterAddonsResponse(),
                self.execute(params, req, runtime)
            )

    async def install_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.InstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.InstallClusterAddonsResponse:
        """
        @summary Installs a component by specifying the name and version of the component. To enhance Kubernetes capabilities, you can install a variety of components in Container Service for Kubernetes (ACK) clusters, such as fully-managed core components and application, logging and monitoring, network, storage, and security group components.
        
        @param request: InstallClusterAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallClusterAddonsResponse
        """
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.InstallClusterAddonsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.InstallClusterAddonsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def install_cluster_addons(
        self,
        cluster_id: str,
        request: cs20151215_models.InstallClusterAddonsRequest,
    ) -> cs20151215_models.InstallClusterAddonsResponse:
        """
        @summary Installs a component by specifying the name and version of the component. To enhance Kubernetes capabilities, you can install a variety of components in Container Service for Kubernetes (ACK) clusters, such as fully-managed core components and application, logging and monitoring, network, storage, and security group components.
        
        @param request: InstallClusterAddonsRequest
        @return: InstallClusterAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def install_cluster_addons_async(
        self,
        cluster_id: str,
        request: cs20151215_models.InstallClusterAddonsRequest,
    ) -> cs20151215_models.InstallClusterAddonsResponse:
        """
        @summary Installs a component by specifying the name and version of the component. To enhance Kubernetes capabilities, you can install a variety of components in Container Service for Kubernetes (ACK) clusters, such as fully-managed core components and application, logging and monitoring, network, storage, and security group components.
        
        @param request: InstallClusterAddonsRequest
        @return: InstallClusterAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def list_addons_with_options(
        self,
        request: cs20151215_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListAddonsResponse:
        """
        @summary Queries the available components based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, and cluster version and queries the detailed information about a component. The information includes whether the component is managed, the supported custom parameter schema, and compatible operating system architecture.
        
        @param request: ListAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListAddonsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListAddonsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_addons_with_options_async(
        self,
        request: cs20151215_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListAddonsResponse:
        """
        @summary Queries the available components based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, and cluster version and queries the detailed information about a component. The information includes whether the component is managed, the supported custom parameter schema, and compatible operating system architecture.
        
        @param request: ListAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListAddonsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListAddonsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_addons(
        self,
        request: cs20151215_models.ListAddonsRequest,
    ) -> cs20151215_models.ListAddonsResponse:
        """
        @summary Queries the available components based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, and cluster version and queries the detailed information about a component. The information includes whether the component is managed, the supported custom parameter schema, and compatible operating system architecture.
        
        @param request: ListAddonsRequest
        @return: ListAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_addons_with_options(request, headers, runtime)

    async def list_addons_async(
        self,
        request: cs20151215_models.ListAddonsRequest,
    ) -> cs20151215_models.ListAddonsResponse:
        """
        @summary Queries the available components based on specific conditions such as the region, cluster type, cluster subtype defined by cluster profile, and cluster version and queries the detailed information about a component. The information includes whether the component is managed, the supported custom parameter schema, and compatible operating system architecture.
        
        @param request: ListAddonsRequest
        @return: ListAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_addons_with_options_async(request, headers, runtime)

    def list_cluster_addon_instances_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        """
        @summary Queries the component instances that are running in the specified cluster and the information about the component instances. The information includes the component version and status.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterAddonInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListClusterAddonInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListClusterAddonInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_cluster_addon_instances_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        """
        @summary Queries the component instances that are running in the specified cluster and the information about the component instances. The information includes the component version and status.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterAddonInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListClusterAddonInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListClusterAddonInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_cluster_addon_instances(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        """
        @summary Queries the component instances that are running in the specified cluster and the information about the component instances. The information includes the component version and status.
        
        @return: ListClusterAddonInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_addon_instances_with_options(cluster_id, headers, runtime)

    async def list_cluster_addon_instances_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        """
        @summary Queries the component instances that are running in the specified cluster and the information about the component instances. The information includes the component version and status.
        
        @return: ListClusterAddonInstancesResponse
        """
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
        """
        @summary You can call the ListClusterChecks operation to query all the cluster check results of a cluster.
        
        @param request: ListClusterChecksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterChecksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target):
            query['target'] = request.target
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListClusterChecksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListClusterChecksResponse(),
                self.execute(params, req, runtime)
            )

    async def list_cluster_checks_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterChecksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterChecksResponse:
        """
        @summary You can call the ListClusterChecks operation to query all the cluster check results of a cluster.
        
        @param request: ListClusterChecksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterChecksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target):
            query['target'] = request.target
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListClusterChecksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListClusterChecksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_cluster_checks(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterChecksRequest,
    ) -> cs20151215_models.ListClusterChecksResponse:
        """
        @summary You can call the ListClusterChecks operation to query all the cluster check results of a cluster.
        
        @param request: ListClusterChecksRequest
        @return: ListClusterChecksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_checks_with_options(cluster_id, request, headers, runtime)

    async def list_cluster_checks_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterChecksRequest,
    ) -> cs20151215_models.ListClusterChecksResponse:
        """
        @summary You can call the ListClusterChecks operation to query all the cluster check results of a cluster.
        
        @param request: ListClusterChecksRequest
        @return: ListClusterChecksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_checks_with_options_async(cluster_id, request, headers, runtime)

    def list_cluster_kubeconfig_states_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterKubeconfigStatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterKubeconfigStatesResponse:
        """
        @summary Queries the kubeconfig files that are issued to users for the current cluster and the status of the kubeconfig files.
        
        @description > - To call this operation, make sure that you have ram:ListUsers and ram:ListRoles permissions.
        > - To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListClusterKubeconfigStatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterKubeconfigStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterKubeconfigStates',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/kubeconfig/states',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListClusterKubeconfigStatesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListClusterKubeconfigStatesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_cluster_kubeconfig_states_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterKubeconfigStatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterKubeconfigStatesResponse:
        """
        @summary Queries the kubeconfig files that are issued to users for the current cluster and the status of the kubeconfig files.
        
        @description > - To call this operation, make sure that you have ram:ListUsers and ram:ListRoles permissions.
        > - To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListClusterKubeconfigStatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterKubeconfigStatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterKubeconfigStates',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/kubeconfig/states',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListClusterKubeconfigStatesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListClusterKubeconfigStatesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_cluster_kubeconfig_states(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterKubeconfigStatesRequest,
    ) -> cs20151215_models.ListClusterKubeconfigStatesResponse:
        """
        @summary Queries the kubeconfig files that are issued to users for the current cluster and the status of the kubeconfig files.
        
        @description > - To call this operation, make sure that you have ram:ListUsers and ram:ListRoles permissions.
        > - To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListClusterKubeconfigStatesRequest
        @return: ListClusterKubeconfigStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_kubeconfig_states_with_options(cluster_id, request, headers, runtime)

    async def list_cluster_kubeconfig_states_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterKubeconfigStatesRequest,
    ) -> cs20151215_models.ListClusterKubeconfigStatesResponse:
        """
        @summary Queries the kubeconfig files that are issued to users for the current cluster and the status of the kubeconfig files.
        
        @description > - To call this operation, make sure that you have ram:ListUsers and ram:ListRoles permissions.
        > - To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListClusterKubeconfigStatesRequest
        @return: ListClusterKubeconfigStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_kubeconfig_states_with_options_async(cluster_id, request, headers, runtime)

    def list_operation_plans_with_options(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListOperationPlansResponse:
        """
        @summary Queries the automated maintenance schedules of a cluster.
        
        @param request: ListOperationPlansRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationPlansResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListOperationPlansResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListOperationPlansResponse(),
                self.execute(params, req, runtime)
            )

    async def list_operation_plans_with_options_async(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListOperationPlansResponse:
        """
        @summary Queries the automated maintenance schedules of a cluster.
        
        @param request: ListOperationPlansRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationPlansResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListOperationPlansResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListOperationPlansResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_operation_plans(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
    ) -> cs20151215_models.ListOperationPlansResponse:
        """
        @summary Queries the automated maintenance schedules of a cluster.
        
        @param request: ListOperationPlansRequest
        @return: ListOperationPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_operation_plans_with_options(request, headers, runtime)

    async def list_operation_plans_async(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
    ) -> cs20151215_models.ListOperationPlansResponse:
        """
        @summary Queries the automated maintenance schedules of a cluster.
        
        @param request: ListOperationPlansRequest
        @return: ListOperationPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_operation_plans_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: cs20151215_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListTagResourcesResponse:
        """
        @summary Queries resource labels and the detailed information, such as the key-value pairs of the labels and the clusters to which the labels are added. You can use labels to classify and manage Container Service for Kubernetes (ACK) clusters in order to meet monitoring, cost analysis, and tenant isolation requirements.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: cs20151215_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListTagResourcesResponse:
        """
        @summary Queries resource labels and the detailed information, such as the key-value pairs of the labels and the clusters to which the labels are added. You can use labels to classify and manage Container Service for Kubernetes (ACK) clusters in order to meet monitoring, cost analysis, and tenant isolation requirements.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: cs20151215_models.ListTagResourcesRequest,
    ) -> cs20151215_models.ListTagResourcesResponse:
        """
        @summary Queries resource labels and the detailed information, such as the key-value pairs of the labels and the clusters to which the labels are added. You can use labels to classify and manage Container Service for Kubernetes (ACK) clusters in order to meet monitoring, cost analysis, and tenant isolation requirements.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: cs20151215_models.ListTagResourcesRequest,
    ) -> cs20151215_models.ListTagResourcesResponse:
        """
        @summary Queries resource labels and the detailed information, such as the key-value pairs of the labels and the clusters to which the labels are added. You can use labels to classify and manage Container Service for Kubernetes (ACK) clusters in order to meet monitoring, cost analysis, and tenant isolation requirements.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_user_kube_config_states_with_options(
        self,
        uid: str,
        request: cs20151215_models.ListUserKubeConfigStatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListUserKubeConfigStatesResponse:
        """
        @summary You can call the ListUserKubeConfigStates operation to query the status of the kubeconfig files of all clusters managed by the current user.
        
        @description >  To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListUserKubeConfigStatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserKubeConfigStatesResponse
        """
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
            action='ListUserKubeConfigStates',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/users/{OpenApiUtilClient.get_encode_param(uid)}/kubeconfig/states',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListUserKubeConfigStatesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListUserKubeConfigStatesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_user_kube_config_states_with_options_async(
        self,
        uid: str,
        request: cs20151215_models.ListUserKubeConfigStatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListUserKubeConfigStatesResponse:
        """
        @summary You can call the ListUserKubeConfigStates operation to query the status of the kubeconfig files of all clusters managed by the current user.
        
        @description >  To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListUserKubeConfigStatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserKubeConfigStatesResponse
        """
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
            action='ListUserKubeConfigStates',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/users/{OpenApiUtilClient.get_encode_param(uid)}/kubeconfig/states',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ListUserKubeConfigStatesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ListUserKubeConfigStatesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_user_kube_config_states(
        self,
        uid: str,
        request: cs20151215_models.ListUserKubeConfigStatesRequest,
    ) -> cs20151215_models.ListUserKubeConfigStatesResponse:
        """
        @summary You can call the ListUserKubeConfigStates operation to query the status of the kubeconfig files of all clusters managed by the current user.
        
        @description >  To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListUserKubeConfigStatesRequest
        @return: ListUserKubeConfigStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_kube_config_states_with_options(uid, request, headers, runtime)

    async def list_user_kube_config_states_async(
        self,
        uid: str,
        request: cs20151215_models.ListUserKubeConfigStatesRequest,
    ) -> cs20151215_models.ListUserKubeConfigStatesResponse:
        """
        @summary You can call the ListUserKubeConfigStates operation to query the status of the kubeconfig files of all clusters managed by the current user.
        
        @description >  To call this operation, make sure that you have the AliyunCSFullAccess permissions.
        
        @param request: ListUserKubeConfigStatesRequest
        @return: ListUserKubeConfigStatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_kube_config_states_with_options_async(uid, request, headers, runtime)

    def migrate_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.MigrateClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) Pro clusters are developed based on ACK Basic clusters. ACK Pro clusters provide all benefits of ACK managed clusters, such as fully-managed control planes and control plane high availability. In addition, ACK Pro clusters provide you with enhanced reliability, security, and schedulability. ACK Pro clusters are covered by the SLA that supports compensation clauses. ACK Pro clusters are suitable for large-scale businesses that require high stability and security in production environments. We recommend that you migrate from ACK Basic clusters to ACK Pro clusters.
        
        @param request: MigrateClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateClusterResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.MigrateClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.MigrateClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def migrate_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.MigrateClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) Pro clusters are developed based on ACK Basic clusters. ACK Pro clusters provide all benefits of ACK managed clusters, such as fully-managed control planes and control plane high availability. In addition, ACK Pro clusters provide you with enhanced reliability, security, and schedulability. ACK Pro clusters are covered by the SLA that supports compensation clauses. ACK Pro clusters are suitable for large-scale businesses that require high stability and security in production environments. We recommend that you migrate from ACK Basic clusters to ACK Pro clusters.
        
        @param request: MigrateClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateClusterResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.MigrateClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.MigrateClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def migrate_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
    ) -> cs20151215_models.MigrateClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) Pro clusters are developed based on ACK Basic clusters. ACK Pro clusters provide all benefits of ACK managed clusters, such as fully-managed control planes and control plane high availability. In addition, ACK Pro clusters provide you with enhanced reliability, security, and schedulability. ACK Pro clusters are covered by the SLA that supports compensation clauses. ACK Pro clusters are suitable for large-scale businesses that require high stability and security in production environments. We recommend that you migrate from ACK Basic clusters to ACK Pro clusters.
        
        @param request: MigrateClusterRequest
        @return: MigrateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_cluster_with_options(cluster_id, request, headers, runtime)

    async def migrate_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
    ) -> cs20151215_models.MigrateClusterResponse:
        """
        @summary Container Service for Kubernetes (ACK) Pro clusters are developed based on ACK Basic clusters. ACK Pro clusters provide all benefits of ACK managed clusters, such as fully-managed control planes and control plane high availability. In addition, ACK Pro clusters provide you with enhanced reliability, security, and schedulability. ACK Pro clusters are covered by the SLA that supports compensation clauses. ACK Pro clusters are suitable for large-scale businesses that require high stability and security in production environments. We recommend that you migrate from ACK Basic clusters to ACK Pro clusters.
        
        @param request: MigrateClusterRequest
        @return: MigrateClusterResponse
        """
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
        """
        @summary You can call the ModifyCluster operation to modify the cluster configurations by cluster ID.
        
        @param request: ModifyClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.api_server_custom_cert_sans):
            body['api_server_custom_cert_sans'] = request.api_server_custom_cert_sans
        if not UtilClient.is_unset(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.cluster_name):
            body['cluster_name'] = request.cluster_name
        if not UtilClient.is_unset(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
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
        if not UtilClient.is_unset(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not UtilClient.is_unset(request.system_events_logging):
            body['system_events_logging'] = request.system_events_logging
        if not UtilClient.is_unset(request.timezone):
            body['timezone'] = request.timezone
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterResponse:
        """
        @summary You can call the ModifyCluster operation to modify the cluster configurations by cluster ID.
        
        @param request: ModifyClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.api_server_custom_cert_sans):
            body['api_server_custom_cert_sans'] = request.api_server_custom_cert_sans
        if not UtilClient.is_unset(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.cluster_name):
            body['cluster_name'] = request.cluster_name
        if not UtilClient.is_unset(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
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
        if not UtilClient.is_unset(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not UtilClient.is_unset(request.system_events_logging):
            body['system_events_logging'] = request.system_events_logging
        if not UtilClient.is_unset(request.timezone):
            body['timezone'] = request.timezone
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
    ) -> cs20151215_models.ModifyClusterResponse:
        """
        @summary You can call the ModifyCluster operation to modify the cluster configurations by cluster ID.
        
        @param request: ModifyClusterRequest
        @return: ModifyClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
    ) -> cs20151215_models.ModifyClusterResponse:
        """
        @summary You can call the ModifyCluster operation to modify the cluster configurations by cluster ID.
        
        @param request: ModifyClusterRequest
        @return: ModifyClusterResponse
        """
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
        @summary Modifies the configuration of a cluster component. This operation may affect your businesses. We recommend that you assess the impact, back up data, and perform the operation during off-peak hours.
        
        @description You can call this API operation to modify the component parameters of an ACK Basic cluster or the control plane parameters of an ACK Pro cluster:
        To view the component parameters of an ACK Basic cluster, call the DescribeClusterAddonMetadata API operation. For more information, see [Query the metadata of a cluster component](https://help.aliyun.com/document_detail/2667944.html).
        To view the control plane parameters of an ACK Pro cluster, see [Customize the control plane parameters of an ACK Pro cluster](https://help.aliyun.com/document_detail/199588.html).
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterAddonResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterAddonResponse(),
                self.execute(params, req, runtime)
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
        @summary Modifies the configuration of a cluster component. This operation may affect your businesses. We recommend that you assess the impact, back up data, and perform the operation during off-peak hours.
        
        @description You can call this API operation to modify the component parameters of an ACK Basic cluster or the control plane parameters of an ACK Pro cluster:
        To view the component parameters of an ACK Basic cluster, call the DescribeClusterAddonMetadata API operation. For more information, see [Query the metadata of a cluster component](https://help.aliyun.com/document_detail/2667944.html).
        To view the control plane parameters of an ACK Pro cluster, see [Customize the control plane parameters of an ACK Pro cluster](https://help.aliyun.com/document_detail/199588.html).
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterAddonResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterAddonResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_cluster_addon(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.ModifyClusterAddonRequest,
    ) -> cs20151215_models.ModifyClusterAddonResponse:
        """
        @summary Modifies the configuration of a cluster component. This operation may affect your businesses. We recommend that you assess the impact, back up data, and perform the operation during off-peak hours.
        
        @description You can call this API operation to modify the component parameters of an ACK Basic cluster or the control plane parameters of an ACK Pro cluster:
        To view the component parameters of an ACK Basic cluster, call the DescribeClusterAddonMetadata API operation. For more information, see [Query the metadata of a cluster component](https://help.aliyun.com/document_detail/2667944.html).
        To view the control plane parameters of an ACK Pro cluster, see [Customize the control plane parameters of an ACK Pro cluster](https://help.aliyun.com/document_detail/199588.html).
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
        @summary Modifies the configuration of a cluster component. This operation may affect your businesses. We recommend that you assess the impact, back up data, and perform the operation during off-peak hours.
        
        @description You can call this API operation to modify the component parameters of an ACK Basic cluster or the control plane parameters of an ACK Pro cluster:
        To view the component parameters of an ACK Basic cluster, call the DescribeClusterAddonMetadata API operation. For more information, see [Query the metadata of a cluster component](https://help.aliyun.com/document_detail/2667944.html).
        To view the control plane parameters of an ACK Pro cluster, see [Customize the control plane parameters of an ACK Pro cluster](https://help.aliyun.com/document_detail/199588.html).
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
        """
        @deprecated OpenAPI ModifyClusterConfiguration is deprecated
        
        @summary This API operation applies only to Container Service for Kubernetes (ACK) managed clusters.
        
        @param request: ModifyClusterConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterConfigurationResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterConfigurationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterConfigurationResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_cluster_configuration_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterConfigurationResponse:
        """
        @deprecated OpenAPI ModifyClusterConfiguration is deprecated
        
        @summary This API operation applies only to Container Service for Kubernetes (ACK) managed clusters.
        
        @param request: ModifyClusterConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterConfigurationResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterConfigurationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterConfigurationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_cluster_configuration(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterConfigurationRequest,
    ) -> cs20151215_models.ModifyClusterConfigurationResponse:
        """
        @deprecated OpenAPI ModifyClusterConfiguration is deprecated
        
        @summary This API operation applies only to Container Service for Kubernetes (ACK) managed clusters.
        
        @param request: ModifyClusterConfigurationRequest
        @return: ModifyClusterConfigurationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_configuration_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_configuration_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterConfigurationRequest,
    ) -> cs20151215_models.ModifyClusterConfigurationResponse:
        """
        @deprecated OpenAPI ModifyClusterConfiguration is deprecated
        
        @summary This API operation applies only to Container Service for Kubernetes (ACK) managed clusters.
        
        @param request: ModifyClusterConfigurationRequest
        @return: ModifyClusterConfigurationResponse
        Deprecated
        """
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
        """
        @summary You can call the ModifyClusterNodePool operation to modify the configuration of a node pool with the specified node pool ID.
        
        @param request: ModifyClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterNodePoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterNodePoolResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterNodePoolResponse:
        """
        @summary You can call the ModifyClusterNodePool operation to modify the configuration of a node pool with the specified node pool ID.
        
        @param request: ModifyClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterNodePoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterNodePoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyClusterNodePoolRequest,
    ) -> cs20151215_models.ModifyClusterNodePoolResponse:
        """
        @summary You can call the ModifyClusterNodePool operation to modify the configuration of a node pool with the specified node pool ID.
        
        @param request: ModifyClusterNodePoolRequest
        @return: ModifyClusterNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def modify_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyClusterNodePoolRequest,
    ) -> cs20151215_models.ModifyClusterNodePoolResponse:
        """
        @summary You can call the ModifyClusterNodePool operation to modify the configuration of a node pool with the specified node pool ID.
        
        @param request: ModifyClusterNodePoolRequest
        @return: ModifyClusterNodePoolResponse
        """
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
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\\\\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the ModifyClusterTags operation to modify the labels of a cluster.
        
        @param request: ModifyClusterTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterTagsResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_cluster_tags_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterTagsResponse:
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\\\\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the ModifyClusterTags operation to modify the labels of a cluster.
        
        @param request: ModifyClusterTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyClusterTagsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_cluster_tags(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterTagsRequest,
    ) -> cs20151215_models.ModifyClusterTagsResponse:
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\\\\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the ModifyClusterTags operation to modify the labels of a cluster.
        
        @param request: ModifyClusterTagsRequest
        @return: ModifyClusterTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_tags_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_tags_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterTagsRequest,
    ) -> cs20151215_models.ModifyClusterTagsResponse:
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\\\\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the ModifyClusterTags operation to modify the labels of a cluster.
        
        @param request: ModifyClusterTagsRequest
        @return: ModifyClusterTagsResponse
        """
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
        @summary Modifies the configuration of a node pool, such as the kubelet configuration and node rolling update configuration. After you modify the node pool configuration, nodes are batch updated and the kubelet on each node is restarted. This may adversely affect the nodes and workloads. We recommend that you perform this operation during off-peak hours.
        
        @description >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
        @param request: ModifyNodePoolNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolNodeConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.containerd_config):
            body['containerd_config'] = request.containerd_config
        if not UtilClient.is_unset(request.kubelet_config):
            body['kubelet_config'] = request.kubelet_config
        if not UtilClient.is_unset(request.os_config):
            body['os_config'] = request.os_config
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyNodePoolNodeConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyNodePoolNodeConfigResponse(),
                self.execute(params, req, runtime)
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
        @summary Modifies the configuration of a node pool, such as the kubelet configuration and node rolling update configuration. After you modify the node pool configuration, nodes are batch updated and the kubelet on each node is restarted. This may adversely affect the nodes and workloads. We recommend that you perform this operation during off-peak hours.
        
        @description >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
        @param request: ModifyNodePoolNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolNodeConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.containerd_config):
            body['containerd_config'] = request.containerd_config
        if not UtilClient.is_unset(request.kubelet_config):
            body['kubelet_config'] = request.kubelet_config
        if not UtilClient.is_unset(request.os_config):
            body['os_config'] = request.os_config
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyNodePoolNodeConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyNodePoolNodeConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_node_pool_node_config(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyNodePoolNodeConfigRequest,
    ) -> cs20151215_models.ModifyNodePoolNodeConfigResponse:
        """
        @summary Modifies the configuration of a node pool, such as the kubelet configuration and node rolling update configuration. After you modify the node pool configuration, nodes are batch updated and the kubelet on each node is restarted. This may adversely affect the nodes and workloads. We recommend that you perform this operation during off-peak hours.
        
        @description >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
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
        @summary Modifies the configuration of a node pool, such as the kubelet configuration and node rolling update configuration. After you modify the node pool configuration, nodes are batch updated and the kubelet on each node is restarted. This may adversely affect the nodes and workloads. We recommend that you perform this operation during off-peak hours.
        
        @description >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
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
        """
        @summary Updates a policy in a specific Container Service for Kubernetes (ACK) cluster. You can modify the action of the policy such as alerting or denying and namespaces to which the policy applies.
        
        @param request: ModifyPolicyInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyPolicyInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyPolicyInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.ModifyPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyPolicyInstanceResponse:
        """
        @summary Updates a policy in a specific Container Service for Kubernetes (ACK) cluster. You can modify the action of the policy such as alerting or denying and namespaces to which the policy applies.
        
        @param request: ModifyPolicyInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ModifyPolicyInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ModifyPolicyInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.ModifyPolicyInstanceRequest,
    ) -> cs20151215_models.ModifyPolicyInstanceResponse:
        """
        @summary Updates a policy in a specific Container Service for Kubernetes (ACK) cluster. You can modify the action of the policy such as alerting or denying and namespaces to which the policy applies.
        
        @param request: ModifyPolicyInstanceRequest
        @return: ModifyPolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def modify_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.ModifyPolicyInstanceRequest,
    ) -> cs20151215_models.ModifyPolicyInstanceResponse:
        """
        @summary Updates a policy in a specific Container Service for Kubernetes (ACK) cluster. You can modify the action of the policy such as alerting or denying and namespaces to which the policy applies.
        
        @param request: ModifyPolicyInstanceRequest
        @return: ModifyPolicyInstanceResponse
        """
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
        @summary When you use Container Service for Kubernetes (ACK) for the first time, you must activate ACK by using an Alibaba Cloud account or RAM user with the required permissions and complete ACK authorization.
        
        @description    You can activate ACK by using Alibaba Cloud accounts.
        To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.OpenAckServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.OpenAckServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def open_ack_service_with_options_async(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.OpenAckServiceResponse:
        """
        @summary When you use Container Service for Kubernetes (ACK) for the first time, you must activate ACK by using an Alibaba Cloud account or RAM user with the required permissions and complete ACK authorization.
        
        @description    You can activate ACK by using Alibaba Cloud accounts.
        To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.OpenAckServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.OpenAckServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def open_ack_service(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
    ) -> cs20151215_models.OpenAckServiceResponse:
        """
        @summary When you use Container Service for Kubernetes (ACK) for the first time, you must activate ACK by using an Alibaba Cloud account or RAM user with the required permissions and complete ACK authorization.
        
        @description    You can activate ACK by using Alibaba Cloud accounts.
        To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
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
        @summary When you use Container Service for Kubernetes (ACK) for the first time, you must activate ACK by using an Alibaba Cloud account or RAM user with the required permissions and complete ACK authorization.
        
        @description    You can activate ACK by using Alibaba Cloud accounts.
        To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
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
        @deprecated OpenAPI PauseClusterUpgrade is deprecated
        
        @summary You can call the PauseClusterUpgrade operation to pause the update of a Container Service for Kubernetes (ACK) cluster.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.PauseClusterUpgradeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.PauseClusterUpgradeResponse(),
                self.execute(params, req, runtime)
            )

    async def pause_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        """
        @deprecated OpenAPI PauseClusterUpgrade is deprecated
        
        @summary You can call the PauseClusterUpgrade operation to pause the update of a Container Service for Kubernetes (ACK) cluster.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.PauseClusterUpgradeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.PauseClusterUpgradeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def pause_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        """
        @deprecated OpenAPI PauseClusterUpgrade is deprecated
        
        @summary You can call the PauseClusterUpgrade operation to pause the update of a Container Service for Kubernetes (ACK) cluster.
        
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
        @deprecated OpenAPI PauseClusterUpgrade is deprecated
        
        @summary You can call the PauseClusterUpgrade operation to pause the update of a Container Service for Kubernetes (ACK) cluster.
        
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
        """
        @deprecated OpenAPI PauseComponentUpgrade is deprecated
        
        @summary You can call the PauseComponentUpgrade operation to pause the update of a component.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseComponentUpgradeResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.PauseComponentUpgradeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.PauseComponentUpgradeResponse(),
                self.execute(params, req, runtime)
            )

    async def pause_component_upgrade_with_options_async(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseComponentUpgradeResponse:
        """
        @deprecated OpenAPI PauseComponentUpgrade is deprecated
        
        @summary You can call the PauseComponentUpgrade operation to pause the update of a component.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseComponentUpgradeResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.PauseComponentUpgradeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.PauseComponentUpgradeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def pause_component_upgrade(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.PauseComponentUpgradeResponse:
        """
        @deprecated OpenAPI PauseComponentUpgrade is deprecated
        
        @summary You can call the PauseComponentUpgrade operation to pause the update of a component.
        
        @return: PauseComponentUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    async def pause_component_upgrade_async(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.PauseComponentUpgradeResponse:
        """
        @deprecated OpenAPI PauseComponentUpgrade is deprecated
        
        @summary You can call the PauseComponentUpgrade operation to pause the update of a component.
        
        @return: PauseComponentUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pause_component_upgrade_with_options_async(clusterid, componentid, headers, runtime)

    def pause_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseTaskResponse:
        """
        @summary Pauses an on-going task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.PauseTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.PauseTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def pause_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseTaskResponse:
        """
        @summary Pauses an on-going task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.PauseTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.PauseTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def pause_task(
        self,
        task_id: str,
    ) -> cs20151215_models.PauseTaskResponse:
        """
        @summary Pauses an on-going task.
        
        @return: PauseTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_task_with_options(task_id, headers, runtime)

    async def pause_task_async(
        self,
        task_id: str,
    ) -> cs20151215_models.PauseTaskResponse:
        """
        @summary Pauses an on-going task.
        
        @return: PauseTaskResponse
        """
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
        @deprecated OpenAPI RemoveClusterNodes is deprecated
        
        @summary You can call the RemoveClusterNodes operation to remove nodes from a Container Service for Kubernetes (ACK) cluster.
        
        @description ***\
        When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        Nodes remain in the Unschedulable state when they are being removed.
        You can remove only worker nodes. You cannot remove master nodes.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RemoveClusterNodesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RemoveClusterNodesResponse(),
                self.execute(params, req, runtime)
            )

    async def remove_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        """
        @deprecated OpenAPI RemoveClusterNodes is deprecated
        
        @summary You can call the RemoveClusterNodes operation to remove nodes from a Container Service for Kubernetes (ACK) cluster.
        
        @description ***\
        When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        Nodes remain in the Unschedulable state when they are being removed.
        You can remove only worker nodes. You cannot remove master nodes.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RemoveClusterNodesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RemoveClusterNodesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        """
        @deprecated OpenAPI RemoveClusterNodes is deprecated
        
        @summary You can call the RemoveClusterNodes operation to remove nodes from a Container Service for Kubernetes (ACK) cluster.
        
        @description ***\
        When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        Nodes remain in the Unschedulable state when they are being removed.
        You can remove only worker nodes. You cannot remove master nodes.
        
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
        @deprecated OpenAPI RemoveClusterNodes is deprecated
        
        @summary You can call the RemoveClusterNodes operation to remove nodes from a Container Service for Kubernetes (ACK) cluster.
        
        @description ***\
        When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        Nodes remain in the Unschedulable state when they are being removed.
        You can remove only worker nodes. You cannot remove master nodes.
        
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
        @summary Removes nodes from a node pool.
        
        @description    When you remove a node, the pods on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        Nodes remain in the Unschedulable state when they are being removed.
        The system removes only worker nodes. It does not remove master nodes.
        Even if you set the `release_node` parameter to `true`, subscription nodes are not released. You must release the subscription nodes in the [ECS console](https://ecs.console.aliyun.com/) after you remove the nodes.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RemoveNodePoolNodesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RemoveNodePoolNodesResponse(),
                self.execute(params, req, runtime)
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
        @summary Removes nodes from a node pool.
        
        @description    When you remove a node, the pods on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        Nodes remain in the Unschedulable state when they are being removed.
        The system removes only worker nodes. It does not remove master nodes.
        Even if you set the `release_node` parameter to `true`, subscription nodes are not released. You must release the subscription nodes in the [ECS console](https://ecs.console.aliyun.com/) after you remove the nodes.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RemoveNodePoolNodesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RemoveNodePoolNodesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_node_pool_nodes(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RemoveNodePoolNodesRequest,
    ) -> cs20151215_models.RemoveNodePoolNodesResponse:
        """
        @summary Removes nodes from a node pool.
        
        @description    When you remove a node, the pods on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        Nodes remain in the Unschedulable state when they are being removed.
        The system removes only worker nodes. It does not remove master nodes.
        Even if you set the `release_node` parameter to `true`, subscription nodes are not released. You must release the subscription nodes in the [ECS console](https://ecs.console.aliyun.com/) after you remove the nodes.
        
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
        @summary Removes nodes from a node pool.
        
        @description    When you remove a node, the pods on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        The operation may have unexpected risks. Back up the data before you perform this operation.
        Nodes remain in the Unschedulable state when they are being removed.
        The system removes only worker nodes. It does not remove master nodes.
        Even if you set the `release_node` parameter to `true`, subscription nodes are not released. You must release the subscription nodes in the [ECS console](https://ecs.console.aliyun.com/) after you remove the nodes.
        
        @param request: RemoveNodePoolNodesRequest
        @return: RemoveNodePoolNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_node_pool_nodes_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def repair_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        """
        @summary Repairs a node pool.
        
        @param request: RepairClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RepairClusterNodePoolResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.operations):
            body['operations'] = request.operations
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RepairClusterNodePoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RepairClusterNodePoolResponse(),
                self.execute(params, req, runtime)
            )

    async def repair_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        """
        @summary Repairs a node pool.
        
        @param request: RepairClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RepairClusterNodePoolResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.operations):
            body['operations'] = request.operations
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RepairClusterNodePoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RepairClusterNodePoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def repair_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        """
        @summary Repairs a node pool.
        
        @param request: RepairClusterNodePoolRequest
        @return: RepairClusterNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.repair_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def repair_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        """
        @summary Repairs a node pool.
        
        @param request: RepairClusterNodePoolRequest
        @return: RepairClusterNodePoolResponse
        """
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
        """
        @deprecated OpenAPI ResumeComponentUpgrade is deprecated
        
        @summary You can call the ResumeComponentUpgrade operation to resume the update of a component.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeComponentUpgradeResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ResumeComponentUpgradeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ResumeComponentUpgradeResponse(),
                self.execute(params, req, runtime)
            )

    async def resume_component_upgrade_with_options_async(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeComponentUpgradeResponse:
        """
        @deprecated OpenAPI ResumeComponentUpgrade is deprecated
        
        @summary You can call the ResumeComponentUpgrade operation to resume the update of a component.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeComponentUpgradeResponse
        Deprecated
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ResumeComponentUpgradeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ResumeComponentUpgradeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def resume_component_upgrade(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.ResumeComponentUpgradeResponse:
        """
        @deprecated OpenAPI ResumeComponentUpgrade is deprecated
        
        @summary You can call the ResumeComponentUpgrade operation to resume the update of a component.
        
        @return: ResumeComponentUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    async def resume_component_upgrade_async(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.ResumeComponentUpgradeResponse:
        """
        @deprecated OpenAPI ResumeComponentUpgrade is deprecated
        
        @summary You can call the ResumeComponentUpgrade operation to resume the update of a component.
        
        @return: ResumeComponentUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_component_upgrade_with_options_async(clusterid, componentid, headers, runtime)

    def resume_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeTaskResponse:
        """
        @summary Resumes a task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ResumeTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ResumeTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def resume_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeTaskResponse:
        """
        @summary Resumes a task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ResumeTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ResumeTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def resume_task(
        self,
        task_id: str,
    ) -> cs20151215_models.ResumeTaskResponse:
        """
        @summary Resumes a task.
        
        @return: ResumeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_task_with_options(task_id, headers, runtime)

    async def resume_task_async(
        self,
        task_id: str,
    ) -> cs20151215_models.ResumeTaskResponse:
        """
        @summary Resumes a task.
        
        @return: ResumeTaskResponse
        """
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
        @deprecated OpenAPI ResumeUpgradeCluster is deprecated
        
        @summary You can call the ResumeUpgradeCluster operation to resume the update of a cluster by cluster ID.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ResumeUpgradeClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ResumeUpgradeClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def resume_upgrade_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        """
        @deprecated OpenAPI ResumeUpgradeCluster is deprecated
        
        @summary You can call the ResumeUpgradeCluster operation to resume the update of a cluster by cluster ID.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ResumeUpgradeClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ResumeUpgradeClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def resume_upgrade_cluster(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        """
        @deprecated OpenAPI ResumeUpgradeCluster is deprecated
        
        @summary You can call the ResumeUpgradeCluster operation to resume the update of a cluster by cluster ID.
        
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
        @deprecated OpenAPI ResumeUpgradeCluster is deprecated
        
        @summary You can call the ResumeUpgradeCluster operation to resume the update of a cluster by cluster ID.
        
        @return: ResumeUpgradeClusterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_upgrade_cluster_with_options_async(cluster_id, headers, runtime)

    def revoke_k8s_cluster_kube_config_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RevokeK8sClusterKubeConfigResponse:
        """
        @summary You can call the RevokeK8sClusterKubeConfig operation to revoke the kubeconfig file of a cluster that belongs to the current Alibaba Cloud account or RAM user. After the kubeconfig file is revoked, the cluster generates a new kubeconfig file, and the original kubeconfig file becomes invalid.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeK8sClusterKubeConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RevokeK8sClusterKubeConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/certs',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RevokeK8sClusterKubeConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RevokeK8sClusterKubeConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def revoke_k8s_cluster_kube_config_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RevokeK8sClusterKubeConfigResponse:
        """
        @summary You can call the RevokeK8sClusterKubeConfig operation to revoke the kubeconfig file of a cluster that belongs to the current Alibaba Cloud account or RAM user. After the kubeconfig file is revoked, the cluster generates a new kubeconfig file, and the original kubeconfig file becomes invalid.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeK8sClusterKubeConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RevokeK8sClusterKubeConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/certs',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RevokeK8sClusterKubeConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RevokeK8sClusterKubeConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def revoke_k8s_cluster_kube_config(
        self,
        cluster_id: str,
    ) -> cs20151215_models.RevokeK8sClusterKubeConfigResponse:
        """
        @summary You can call the RevokeK8sClusterKubeConfig operation to revoke the kubeconfig file of a cluster that belongs to the current Alibaba Cloud account or RAM user. After the kubeconfig file is revoked, the cluster generates a new kubeconfig file, and the original kubeconfig file becomes invalid.
        
        @return: RevokeK8sClusterKubeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_k8s_cluster_kube_config_with_options(cluster_id, headers, runtime)

    async def revoke_k8s_cluster_kube_config_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.RevokeK8sClusterKubeConfigResponse:
        """
        @summary You can call the RevokeK8sClusterKubeConfig operation to revoke the kubeconfig file of a cluster that belongs to the current Alibaba Cloud account or RAM user. After the kubeconfig file is revoked, the cluster generates a new kubeconfig file, and the original kubeconfig file becomes invalid.
        
        @return: RevokeK8sClusterKubeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_k8s_cluster_kube_config_with_options_async(cluster_id, headers, runtime)

    def run_cluster_check_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RunClusterCheckResponse:
        """
        @summary Container Intelligence Service (CIS) provides a variety of cluster check capabilities to allow you to perform cluster update check, cluster migration check, component installation check, component update check, and node pool check. A precheck is automatically triggered before an update, migration, or installation is performed. You can perform changes only if the cluster passes the precheck. You can also manually call the RunClusterCheck operation to initiate cluster checks. We recommend that you periodically check and maintain your cluster to mitigate potential risks.
        
        @param request: RunClusterCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunClusterCheckResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RunClusterCheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RunClusterCheckResponse(),
                self.execute(params, req, runtime)
            )

    async def run_cluster_check_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RunClusterCheckResponse:
        """
        @summary Container Intelligence Service (CIS) provides a variety of cluster check capabilities to allow you to perform cluster update check, cluster migration check, component installation check, component update check, and node pool check. A precheck is automatically triggered before an update, migration, or installation is performed. You can perform changes only if the cluster passes the precheck. You can also manually call the RunClusterCheck operation to initiate cluster checks. We recommend that you periodically check and maintain your cluster to mitigate potential risks.
        
        @param request: RunClusterCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunClusterCheckResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.RunClusterCheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.RunClusterCheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_cluster_check(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
    ) -> cs20151215_models.RunClusterCheckResponse:
        """
        @summary Container Intelligence Service (CIS) provides a variety of cluster check capabilities to allow you to perform cluster update check, cluster migration check, component installation check, component update check, and node pool check. A precheck is automatically triggered before an update, migration, or installation is performed. You can perform changes only if the cluster passes the precheck. You can also manually call the RunClusterCheck operation to initiate cluster checks. We recommend that you periodically check and maintain your cluster to mitigate potential risks.
        
        @param request: RunClusterCheckRequest
        @return: RunClusterCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_cluster_check_with_options(cluster_id, request, headers, runtime)

    async def run_cluster_check_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
    ) -> cs20151215_models.RunClusterCheckResponse:
        """
        @summary Container Intelligence Service (CIS) provides a variety of cluster check capabilities to allow you to perform cluster update check, cluster migration check, component installation check, component update check, and node pool check. A precheck is automatically triggered before an update, migration, or installation is performed. You can perform changes only if the cluster passes the precheck. You can also manually call the RunClusterCheck operation to initiate cluster checks. We recommend that you periodically check and maintain your cluster to mitigate potential risks.
        
        @param request: RunClusterCheckRequest
        @return: RunClusterCheckResponse
        """
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
        @deprecated OpenAPI ScaleCluster is deprecated
        
        @summary 扩容Kubernetes集群
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def scale_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterResponse:
        """
        @deprecated OpenAPI ScaleCluster is deprecated
        
        @summary 扩容Kubernetes集群
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def scale_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
    ) -> cs20151215_models.ScaleClusterResponse:
        """
        @deprecated OpenAPI ScaleCluster is deprecated
        
        @summary 扩容Kubernetes集群
        
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
        @deprecated OpenAPI ScaleCluster is deprecated
        
        @summary 扩容Kubernetes集群
        
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
        """
        @summary Scales out a node pool.
        
        @param request: ScaleClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleClusterNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterNodePoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterNodePoolResponse(),
                self.execute(params, req, runtime)
            )

    async def scale_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ScaleClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterNodePoolResponse:
        """
        @summary Scales out a node pool.
        
        @param request: ScaleClusterNodePoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleClusterNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterNodePoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScaleClusterNodePoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def scale_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ScaleClusterNodePoolRequest,
    ) -> cs20151215_models.ScaleClusterNodePoolResponse:
        """
        @summary Scales out a node pool.
        
        @param request: ScaleClusterNodePoolRequest
        @return: ScaleClusterNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def scale_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ScaleClusterNodePoolRequest,
    ) -> cs20151215_models.ScaleClusterNodePoolResponse:
        """
        @summary Scales out a node pool.
        
        @param request: ScaleClusterNodePoolRequest
        @return: ScaleClusterNodePoolResponse
        """
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
        @summary You can call the ScaleOutCluster operation to scale out a cluster by cluster ID.
        
        @description *\
        ***The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](https://help.aliyun.com/document_detail/184928.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScaleOutClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScaleOutClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def scale_out_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        """
        @summary You can call the ScaleOutCluster operation to scale out a cluster by cluster ID.
        
        @description *\
        ***The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](https://help.aliyun.com/document_detail/184928.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScaleOutClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScaleOutClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def scale_out_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        """
        @summary You can call the ScaleOutCluster operation to scale out a cluster by cluster ID.
        
        @description *\
        ***The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](https://help.aliyun.com/document_detail/184928.html).
        
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
        @summary You can call the ScaleOutCluster operation to scale out a cluster by cluster ID.
        
        @description *\
        ***The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](https://help.aliyun.com/document_detail/184928.html).
        
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
        """
        @summary Scans for vulnerabilities in a Container Service for Kubernetes (ACK) cluster, including workload vulnerabilities, third-party software vulnerabilities, CVE vulnerabilities, WebCMS vulnerabilities, and Windows vulnerabilities. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanClusterVulsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScanClusterVulsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScanClusterVulsResponse(),
                self.execute(params, req, runtime)
            )

    async def scan_cluster_vuls_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScanClusterVulsResponse:
        """
        @summary Scans for vulnerabilities in a Container Service for Kubernetes (ACK) cluster, including workload vulnerabilities, third-party software vulnerabilities, CVE vulnerabilities, WebCMS vulnerabilities, and Windows vulnerabilities. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanClusterVulsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.ScanClusterVulsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.ScanClusterVulsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def scan_cluster_vuls(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ScanClusterVulsResponse:
        """
        @summary Scans for vulnerabilities in a Container Service for Kubernetes (ACK) cluster, including workload vulnerabilities, third-party software vulnerabilities, CVE vulnerabilities, WebCMS vulnerabilities, and Windows vulnerabilities. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @return: ScanClusterVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scan_cluster_vuls_with_options(cluster_id, headers, runtime)

    async def scan_cluster_vuls_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ScanClusterVulsResponse:
        """
        @summary Scans for vulnerabilities in a Container Service for Kubernetes (ACK) cluster, including workload vulnerabilities, third-party software vulnerabilities, CVE vulnerabilities, WebCMS vulnerabilities, and Windows vulnerabilities. We recommend that you scan your cluster on a regular basis to ensure cluster security.
        
        @return: ScanClusterVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scan_cluster_vuls_with_options_async(cluster_id, headers, runtime)

    def start_alert_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.StartAlertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartAlertResponse:
        """
        @summary Activates the specified alert rule(s).
        
        @param request: StartAlertRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAlertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not UtilClient.is_unset(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.StartAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.StartAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def start_alert_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.StartAlertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartAlertResponse:
        """
        @summary Activates the specified alert rule(s).
        
        @param request: StartAlertRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAlertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not UtilClient.is_unset(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.StartAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.StartAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_alert(
        self,
        cluster_id: str,
        request: cs20151215_models.StartAlertRequest,
    ) -> cs20151215_models.StartAlertResponse:
        """
        @summary Activates the specified alert rule(s).
        
        @param request: StartAlertRequest
        @return: StartAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_alert_with_options(cluster_id, request, headers, runtime)

    async def start_alert_async(
        self,
        cluster_id: str,
        request: cs20151215_models.StartAlertRequest,
    ) -> cs20151215_models.StartAlertResponse:
        """
        @summary Activates the specified alert rule(s).
        
        @param request: StartAlertRequest
        @return: StartAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_alert_with_options_async(cluster_id, request, headers, runtime)

    def stop_alert_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.StopAlertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StopAlertResponse:
        """
        @summary You can call the StopAlert operation to disable an alert rule or an alert rule set in the alert center of Container Service for Kubernetes (ACK).
        
        @param request: StopAlertRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAlertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not UtilClient.is_unset(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.StopAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.StopAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_alert_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.StopAlertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StopAlertResponse:
        """
        @summary You can call the StopAlert operation to disable an alert rule or an alert rule set in the alert center of Container Service for Kubernetes (ACK).
        
        @param request: StopAlertRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAlertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not UtilClient.is_unset(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.StopAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.StopAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_alert(
        self,
        cluster_id: str,
        request: cs20151215_models.StopAlertRequest,
    ) -> cs20151215_models.StopAlertResponse:
        """
        @summary You can call the StopAlert operation to disable an alert rule or an alert rule set in the alert center of Container Service for Kubernetes (ACK).
        
        @param request: StopAlertRequest
        @return: StopAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_alert_with_options(cluster_id, request, headers, runtime)

    async def stop_alert_async(
        self,
        cluster_id: str,
        request: cs20151215_models.StopAlertRequest,
    ) -> cs20151215_models.StopAlertResponse:
        """
        @summary You can call the StopAlert operation to disable an alert rule or an alert rule set in the alert center of Container Service for Kubernetes (ACK).
        
        @param request: StopAlertRequest
        @return: StopAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_alert_with_options_async(cluster_id, request, headers, runtime)

    def sync_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        """
        @summary Synchronizes the information about a node pool, including the metadata and node information of the node pool.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncClusterNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.SyncClusterNodePoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.SyncClusterNodePoolResponse(),
                self.execute(params, req, runtime)
            )

    async def sync_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        """
        @summary Synchronizes the information about a node pool, including the metadata and node information of the node pool.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncClusterNodePoolResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.SyncClusterNodePoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.SyncClusterNodePoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def sync_cluster_node_pool(
        self,
        cluster_id: str,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        """
        @summary Synchronizes the information about a node pool, including the metadata and node information of the node pool.
        
        @return: SyncClusterNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_cluster_node_pool_with_options(cluster_id, headers, runtime)

    async def sync_cluster_node_pool_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        """
        @summary Synchronizes the information about a node pool, including the metadata and node information of the node pool.
        
        @return: SyncClusterNodePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sync_cluster_node_pool_with_options_async(cluster_id, headers, runtime)

    def tag_resources_with_options(
        self,
        request: cs20151215_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.TagResourcesResponse:
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the TagResources operation to add labels to a cluster.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: cs20151215_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.TagResourcesResponse:
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the TagResources operation to add labels to a cluster.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: cs20151215_models.TagResourcesRequest,
    ) -> cs20151215_models.TagResourcesResponse:
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the TagResources operation to add labels to a cluster.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: cs20151215_models.TagResourcesRequest,
    ) -> cs20151215_models.TagResourcesResponse:
        """
        @summary You can add labels in key-value pairs to clusters. This allows cluster developers or O\\&M engineers to classify and manage clusters in a more flexible manner. This also meets the requirements for monitoring, cost analysis, and tenant isolation. You can call the TagResources operation to add labels to a cluster.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
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
        """
        @summary Uninstalls components that you no longer need from a cluster. You must specify the name of the components and specify whether to release associated Alibaba Cloud resources from the cluster.
        
        @param request: UnInstallClusterAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnInstallClusterAddonsResponse
        """
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UnInstallClusterAddonsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UnInstallClusterAddonsResponse(),
                self.execute(params, req, runtime)
            )

    async def un_install_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UnInstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UnInstallClusterAddonsResponse:
        """
        @summary Uninstalls components that you no longer need from a cluster. You must specify the name of the components and specify whether to release associated Alibaba Cloud resources from the cluster.
        
        @param request: UnInstallClusterAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnInstallClusterAddonsResponse
        """
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UnInstallClusterAddonsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UnInstallClusterAddonsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def un_install_cluster_addons(
        self,
        cluster_id: str,
        request: cs20151215_models.UnInstallClusterAddonsRequest,
    ) -> cs20151215_models.UnInstallClusterAddonsResponse:
        """
        @summary Uninstalls components that you no longer need from a cluster. You must specify the name of the components and specify whether to release associated Alibaba Cloud resources from the cluster.
        
        @param request: UnInstallClusterAddonsRequest
        @return: UnInstallClusterAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def un_install_cluster_addons_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UnInstallClusterAddonsRequest,
    ) -> cs20151215_models.UnInstallClusterAddonsResponse:
        """
        @summary Uninstalls components that you no longer need from a cluster. You must specify the name of the components and specify whether to release associated Alibaba Cloud resources from the cluster.
        
        @param request: UnInstallClusterAddonsRequest
        @return: UnInstallClusterAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_install_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: cs20151215_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UntagResourcesResponse:
        """
        @summary If you no longer need the labels (key-value pairs) of a cluster, you can call the UntagResources operation to delete the labels.
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        tmp_req: cs20151215_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UntagResourcesResponse:
        """
        @summary If you no longer need the labels (key-value pairs) of a cluster, you can call the UntagResources operation to delete the labels.
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: cs20151215_models.UntagResourcesRequest,
    ) -> cs20151215_models.UntagResourcesResponse:
        """
        @summary If you no longer need the labels (key-value pairs) of a cluster, you can call the UntagResources operation to delete the labels.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: cs20151215_models.UntagResourcesRequest,
    ) -> cs20151215_models.UntagResourcesResponse:
        """
        @summary If you no longer need the labels (key-value pairs) of a cluster, you can call the UntagResources operation to delete the labels.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_cluster_audit_log_config_with_options(
        self,
        clusterid: str,
        request: cs20151215_models.UpdateClusterAuditLogConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateClusterAuditLogConfigResponse:
        """
        @summary You can call the UpdateClusterAuditLogConfig operation to enable or disable the audit log feature in a Container Service for Kubernetes (ACK) cluster and update the audit log configuration. This operation also allows you to record requests to the Kubernetes API and the responses, which can be used to trace cluster operation history and troubleshoot cluster issues.
        
        @description Before you call this operation, ensure that you understand the billing methods and pricing of [Simple Log Service](https://www.alibabacloud.com/product/log-service/pricing).
        
        @param request: UpdateClusterAuditLogConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.disable):
            body['disable'] = request.disable
        if not UtilClient.is_unset(request.sls_project_name):
            body['sls_project_name'] = request.sls_project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterAuditLogConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/audit_log',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateClusterAuditLogConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateClusterAuditLogConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def update_cluster_audit_log_config_with_options_async(
        self,
        clusterid: str,
        request: cs20151215_models.UpdateClusterAuditLogConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateClusterAuditLogConfigResponse:
        """
        @summary You can call the UpdateClusterAuditLogConfig operation to enable or disable the audit log feature in a Container Service for Kubernetes (ACK) cluster and update the audit log configuration. This operation also allows you to record requests to the Kubernetes API and the responses, which can be used to trace cluster operation history and troubleshoot cluster issues.
        
        @description Before you call this operation, ensure that you understand the billing methods and pricing of [Simple Log Service](https://www.alibabacloud.com/product/log-service/pricing).
        
        @param request: UpdateClusterAuditLogConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterAuditLogConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.disable):
            body['disable'] = request.disable
        if not UtilClient.is_unset(request.sls_project_name):
            body['sls_project_name'] = request.sls_project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterAuditLogConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/audit_log',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateClusterAuditLogConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateClusterAuditLogConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_cluster_audit_log_config(
        self,
        clusterid: str,
        request: cs20151215_models.UpdateClusterAuditLogConfigRequest,
    ) -> cs20151215_models.UpdateClusterAuditLogConfigResponse:
        """
        @summary You can call the UpdateClusterAuditLogConfig operation to enable or disable the audit log feature in a Container Service for Kubernetes (ACK) cluster and update the audit log configuration. This operation also allows you to record requests to the Kubernetes API and the responses, which can be used to trace cluster operation history and troubleshoot cluster issues.
        
        @description Before you call this operation, ensure that you understand the billing methods and pricing of [Simple Log Service](https://www.alibabacloud.com/product/log-service/pricing).
        
        @param request: UpdateClusterAuditLogConfigRequest
        @return: UpdateClusterAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_cluster_audit_log_config_with_options(clusterid, request, headers, runtime)

    async def update_cluster_audit_log_config_async(
        self,
        clusterid: str,
        request: cs20151215_models.UpdateClusterAuditLogConfigRequest,
    ) -> cs20151215_models.UpdateClusterAuditLogConfigResponse:
        """
        @summary You can call the UpdateClusterAuditLogConfig operation to enable or disable the audit log feature in a Container Service for Kubernetes (ACK) cluster and update the audit log configuration. This operation also allows you to record requests to the Kubernetes API and the responses, which can be used to trace cluster operation history and troubleshoot cluster issues.
        
        @description Before you call this operation, ensure that you understand the billing methods and pricing of [Simple Log Service](https://www.alibabacloud.com/product/log-service/pricing).
        
        @param request: UpdateClusterAuditLogConfigRequest
        @return: UpdateClusterAuditLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_cluster_audit_log_config_with_options_async(clusterid, request, headers, runtime)

    def update_contact_group_for_alert_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateContactGroupForAlertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        """
        @summary null
        
        @param request: UpdateContactGroupForAlertRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContactGroupForAlertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not UtilClient.is_unset(request.contact_group_ids):
            body['contact_group_ids'] = request.contact_group_ids
        if not UtilClient.is_unset(request.cr_name):
            body['cr_name'] = request.cr_name
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateContactGroupForAlertResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateContactGroupForAlertResponse(),
                self.execute(params, req, runtime)
            )

    async def update_contact_group_for_alert_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateContactGroupForAlertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        """
        @summary null
        
        @param request: UpdateContactGroupForAlertRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContactGroupForAlertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not UtilClient.is_unset(request.contact_group_ids):
            body['contact_group_ids'] = request.contact_group_ids
        if not UtilClient.is_unset(request.cr_name):
            body['cr_name'] = request.cr_name
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateContactGroupForAlertResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateContactGroupForAlertResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_contact_group_for_alert(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateContactGroupForAlertRequest,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        """
        @summary null
        
        @param request: UpdateContactGroupForAlertRequest
        @return: UpdateContactGroupForAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_contact_group_for_alert_with_options(cluster_id, request, headers, runtime)

    async def update_contact_group_for_alert_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateContactGroupForAlertRequest,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        """
        @summary null
        
        @param request: UpdateContactGroupForAlertRequest
        @return: UpdateContactGroupForAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_contact_group_for_alert_with_options_async(cluster_id, request, headers, runtime)

    def update_control_plane_log_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        """
        @summary Modifies the log configurations of control plane components. The configurations include the log retention period and components whose logs that you want to collect. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube-apiserver, kube-scheduler, Kubernetes controller manager, and cloud controller manager (CCM).
        
        @param request: UpdateControlPlaneLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateControlPlaneLogResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateControlPlaneLogResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateControlPlaneLogResponse(),
                self.execute(params, req, runtime)
            )

    async def update_control_plane_log_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        """
        @summary Modifies the log configurations of control plane components. The configurations include the log retention period and components whose logs that you want to collect. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube-apiserver, kube-scheduler, Kubernetes controller manager, and cloud controller manager (CCM).
        
        @param request: UpdateControlPlaneLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateControlPlaneLogResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateControlPlaneLogResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateControlPlaneLogResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_control_plane_log(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        """
        @summary Modifies the log configurations of control plane components. The configurations include the log retention period and components whose logs that you want to collect. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube-apiserver, kube-scheduler, Kubernetes controller manager, and cloud controller manager (CCM).
        
        @param request: UpdateControlPlaneLogRequest
        @return: UpdateControlPlaneLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_control_plane_log_with_options(cluster_id, request, headers, runtime)

    async def update_control_plane_log_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        """
        @summary Modifies the log configurations of control plane components. The configurations include the log retention period and components whose logs that you want to collect. Container Service for Kubernetes (ACK) managed clusters can collect the logs of control plane components and deliver the logs to projects in Simple Log Service. These control plane components include Kube-apiserver, kube-scheduler, Kubernetes controller manager, and cloud controller manager (CCM).
        
        @param request: UpdateControlPlaneLogRequest
        @return: UpdateControlPlaneLogResponse
        """
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
        @summary Sets the validity period of a kubeconfig file used by a Resource Access Management (RAM) user or RAM role to connect to a Container Service for Kubernetes (ACK) cluster. The validity period ranges from 1 to 876,000 hours. You can call this API operation when you customize configurations by using an Alibaba Cloud account. The default validity period of a kubeconfig file is three years.
        
        @description    You can call this operation only with an Alibaba Cloud account.
        If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
                self.execute(params, req, runtime)
            )

    async def update_k8s_cluster_user_config_expire_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateK8sClusterUserConfigExpireRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        """
        @summary Sets the validity period of a kubeconfig file used by a Resource Access Management (RAM) user or RAM role to connect to a Container Service for Kubernetes (ACK) cluster. The validity period ranges from 1 to 876,000 hours. You can call this API operation when you customize configurations by using an Alibaba Cloud account. The default validity period of a kubeconfig file is three years.
        
        @description    You can call this operation only with an Alibaba Cloud account.
        If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_k8s_cluster_user_config_expire(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateK8sClusterUserConfigExpireRequest,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        """
        @summary Sets the validity period of a kubeconfig file used by a Resource Access Management (RAM) user or RAM role to connect to a Container Service for Kubernetes (ACK) cluster. The validity period ranges from 1 to 876,000 hours. You can call this API operation when you customize configurations by using an Alibaba Cloud account. The default validity period of a kubeconfig file is three years.
        
        @description    You can call this operation only with an Alibaba Cloud account.
        If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
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
        @summary Sets the validity period of a kubeconfig file used by a Resource Access Management (RAM) user or RAM role to connect to a Container Service for Kubernetes (ACK) cluster. The validity period ranges from 1 to 876,000 hours. You can call this API operation when you customize configurations by using an Alibaba Cloud account. The default validity period of a kubeconfig file is three years.
        
        @description    You can call this operation only with an Alibaba Cloud account.
        If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
        @param request: UpdateK8sClusterUserConfigExpireRequest
        @return: UpdateK8sClusterUserConfigExpireResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_cluster_user_config_expire_with_options_async(cluster_id, request, headers, runtime)

    def update_resources_delete_protection_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateResourcesDeleteProtectionResponse:
        """
        @summary Updates the deletion protection status of the specified resources. You can enable or disable deletion protection for namespaces and Services. You can call this operation to enable deletion protection for namespaces or Services that involve businesses-critical and sensitive data to avoid incurring maintenance costs caused by accidental namespace or Service deletion.
        
        @param request: UpdateResourcesDeleteProtectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourcesDeleteProtectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_type):
            body['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.resources):
            body['resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourcesDeleteProtection',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/resources/protection',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateResourcesDeleteProtectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateResourcesDeleteProtectionResponse(),
                self.execute(params, req, runtime)
            )

    async def update_resources_delete_protection_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateResourcesDeleteProtectionResponse:
        """
        @summary Updates the deletion protection status of the specified resources. You can enable or disable deletion protection for namespaces and Services. You can call this operation to enable deletion protection for namespaces or Services that involve businesses-critical and sensitive data to avoid incurring maintenance costs caused by accidental namespace or Service deletion.
        
        @param request: UpdateResourcesDeleteProtectionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourcesDeleteProtectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_type):
            body['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.resources):
            body['resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourcesDeleteProtection',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/resources/protection',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateResourcesDeleteProtectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateResourcesDeleteProtectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_resources_delete_protection(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateResourcesDeleteProtectionRequest,
    ) -> cs20151215_models.UpdateResourcesDeleteProtectionResponse:
        """
        @summary Updates the deletion protection status of the specified resources. You can enable or disable deletion protection for namespaces and Services. You can call this operation to enable deletion protection for namespaces or Services that involve businesses-critical and sensitive data to avoid incurring maintenance costs caused by accidental namespace or Service deletion.
        
        @param request: UpdateResourcesDeleteProtectionRequest
        @return: UpdateResourcesDeleteProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resources_delete_protection_with_options(cluster_id, request, headers, runtime)

    async def update_resources_delete_protection_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateResourcesDeleteProtectionRequest,
    ) -> cs20151215_models.UpdateResourcesDeleteProtectionResponse:
        """
        @summary Updates the deletion protection status of the specified resources. You can enable or disable deletion protection for namespaces and Services. You can call this operation to enable deletion protection for namespaces or Services that involve businesses-critical and sensitive data to avoid incurring maintenance costs caused by accidental namespace or Service deletion.
        
        @param request: UpdateResourcesDeleteProtectionRequest
        @return: UpdateResourcesDeleteProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resources_delete_protection_with_options_async(cluster_id, request, headers, runtime)

    def update_template_with_options(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateTemplateResponse:
        """
        @summary Updates the configurations of an orchestration template. An orchestration template defines and describes a group of Container Service for Kubernetes (ACK) resources. An orchestration template describes the configurations of an application or how an application runs in a declarative manner.
        
        @param request: UpdateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def update_template_with_options_async(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateTemplateResponse:
        """
        @summary Updates the configurations of an orchestration template. An orchestration template defines and describes a group of Container Service for Kubernetes (ACK) resources. An orchestration template describes the configurations of an application or how an application runs in a declarative manner.
        
        @param request: UpdateTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_template(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
    ) -> cs20151215_models.UpdateTemplateResponse:
        """
        @summary Updates the configurations of an orchestration template. An orchestration template defines and describes a group of Container Service for Kubernetes (ACK) resources. An orchestration template describes the configurations of an application or how an application runs in a declarative manner.
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(template_id, request, headers, runtime)

    async def update_template_async(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
    ) -> cs20151215_models.UpdateTemplateResponse:
        """
        @summary Updates the configurations of an orchestration template. An orchestration template defines and describes a group of Container Service for Kubernetes (ACK) resources. An orchestration template describes the configurations of an application or how an application runs in a declarative manner.
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(template_id, request, headers, runtime)

    def update_user_permissions_with_options(
        self,
        uid: str,
        request: cs20151215_models.UpdateUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateUserPermissionsResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        You can update the permissions of a RAM user or RAM role on a cluster by using full update or incremental update. If you use full update, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation. If you use incremental update, you can grant permissions to or revoke permissions from the RAM user or RAM role on the cluster. In this case, only the permissions that you specify in the request parameters when you call the operation are granted or revoked, other permissions of the RAM user or RAM role on the cluster are not affected.
        
        @param request: UpdateUserPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateUserPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/permissions/users/{OpenApiUtilClient.get_encode_param(uid)}/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateUserPermissionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateUserPermissionsResponse(),
                self.execute(params, req, runtime)
            )

    async def update_user_permissions_with_options_async(
        self,
        uid: str,
        request: cs20151215_models.UpdateUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateUserPermissionsResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        You can update the permissions of a RAM user or RAM role on a cluster by using full update or incremental update. If you use full update, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation. If you use incremental update, you can grant permissions to or revoke permissions from the RAM user or RAM role on the cluster. In this case, only the permissions that you specify in the request parameters when you call the operation are granted or revoked, other permissions of the RAM user or RAM role on the cluster are not affected.
        
        @param request: UpdateUserPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateUserPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/permissions/users/{OpenApiUtilClient.get_encode_param(uid)}/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpdateUserPermissionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpdateUserPermissionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_user_permissions(
        self,
        uid: str,
        request: cs20151215_models.UpdateUserPermissionsRequest,
    ) -> cs20151215_models.UpdateUserPermissionsResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        You can update the permissions of a RAM user or RAM role on a cluster by using full update or incremental update. If you use full update, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation. If you use incremental update, you can grant permissions to or revoke permissions from the RAM user or RAM role on the cluster. In this case, only the permissions that you specify in the request parameters when you call the operation are granted or revoked, other permissions of the RAM user or RAM role on the cluster are not affected.
        
        @param request: UpdateUserPermissionsRequest
        @return: UpdateUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_permissions_with_options(uid, request, headers, runtime)

    async def update_user_permissions_async(
        self,
        uid: str,
        request: cs20151215_models.UpdateUserPermissionsRequest,
    ) -> cs20151215_models.UpdateUserPermissionsResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a Resource Access Management (RAM) user or RAM role. By default, you do not have the RBAC permissions on a Container Service for Kubernetes (ACK) cluster if you are not the cluster owner or you are not using an Alibaba Cloud account. You can call this operation to specify the resources that can be accessed, permission scope, and predefined roles. This helps you better manage the access control on resources in ACK clusters.
        
        @description *Precautions**:
        You can update the permissions of a RAM user or RAM role on a cluster by using full update or incremental update. If you use full update, the existing permissions of the RAM user or RAM role on the cluster are overwritten. You must specify all the permissions that you want to grant to the RAM user or RAM role in the request parameters when you call the operation. If you use incremental update, you can grant permissions to or revoke permissions from the RAM user or RAM role on the cluster. In this case, only the permissions that you specify in the request parameters when you call the operation are granted or revoked, other permissions of the RAM user or RAM role on the cluster are not affected.
        
        @param request: UpdateUserPermissionsRequest
        @return: UpdateUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_user_permissions_with_options_async(uid, request, headers, runtime)

    def upgrade_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterResponse:
        """
        @summary You can call the UpgradeCluster operation to upgrade a cluster by cluster ID.
        
        @description After successfully calling the UpgradeCluster interface, this API returns the `task_id` of the upgrade task. You can manage this operation task by calling the following task APIs:
        - [Call DescribeTaskInfo to query task details](https://help.aliyun.com/document_detail/2667985.html)
        - [Call PauseTask to pause a running task](https://help.aliyun.com/document_detail/2667986.html)
        - [Call ResumeTask to resume a task that has been paused](https://help.aliyun.com/document_detail/2667987.html)
        - [Call CancelTask to cancel a running task](https://help.aliyun.com/document_detail/2667988.html)
        
        @param request: UpgradeClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_name):
            body['component_name'] = request.component_name
        if not UtilClient.is_unset(request.master_only):
            body['master_only'] = request.master_only
        if not UtilClient.is_unset(request.next_version):
            body['next_version'] = request.next_version
        if not UtilClient.is_unset(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def upgrade_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterResponse:
        """
        @summary You can call the UpgradeCluster operation to upgrade a cluster by cluster ID.
        
        @description After successfully calling the UpgradeCluster interface, this API returns the `task_id` of the upgrade task. You can manage this operation task by calling the following task APIs:
        - [Call DescribeTaskInfo to query task details](https://help.aliyun.com/document_detail/2667985.html)
        - [Call PauseTask to pause a running task](https://help.aliyun.com/document_detail/2667986.html)
        - [Call ResumeTask to resume a task that has been paused](https://help.aliyun.com/document_detail/2667987.html)
        - [Call CancelTask to cancel a running task](https://help.aliyun.com/document_detail/2667988.html)
        
        @param request: UpgradeClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_name):
            body['component_name'] = request.component_name
        if not UtilClient.is_unset(request.master_only):
            body['master_only'] = request.master_only
        if not UtilClient.is_unset(request.next_version):
            body['next_version'] = request.next_version
        if not UtilClient.is_unset(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def upgrade_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
    ) -> cs20151215_models.UpgradeClusterResponse:
        """
        @summary You can call the UpgradeCluster operation to upgrade a cluster by cluster ID.
        
        @description After successfully calling the UpgradeCluster interface, this API returns the `task_id` of the upgrade task. You can manage this operation task by calling the following task APIs:
        - [Call DescribeTaskInfo to query task details](https://help.aliyun.com/document_detail/2667985.html)
        - [Call PauseTask to pause a running task](https://help.aliyun.com/document_detail/2667986.html)
        - [Call ResumeTask to resume a task that has been paused](https://help.aliyun.com/document_detail/2667987.html)
        - [Call CancelTask to cancel a running task](https://help.aliyun.com/document_detail/2667988.html)
        
        @param request: UpgradeClusterRequest
        @return: UpgradeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_with_options(cluster_id, request, headers, runtime)

    async def upgrade_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
    ) -> cs20151215_models.UpgradeClusterResponse:
        """
        @summary You can call the UpgradeCluster operation to upgrade a cluster by cluster ID.
        
        @description After successfully calling the UpgradeCluster interface, this API returns the `task_id` of the upgrade task. You can manage this operation task by calling the following task APIs:
        - [Call DescribeTaskInfo to query task details](https://help.aliyun.com/document_detail/2667985.html)
        - [Call PauseTask to pause a running task](https://help.aliyun.com/document_detail/2667986.html)
        - [Call ResumeTask to resume a task that has been paused](https://help.aliyun.com/document_detail/2667987.html)
        - [Call CancelTask to cancel a running task](https://help.aliyun.com/document_detail/2667988.html)
        
        @param request: UpgradeClusterRequest
        @return: UpgradeClusterResponse
        """
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
        """
        @summary Updates cluster components to use new features and patch vulnerabilities. You must update cluster components one after one and update a component only after the previous one is successfully updated. Before you update a component, we recommend that you read the update notes for each component. Cluster component updates may affect your businesses. Assess the impact, back up data, and perform the update during off-peak hours.
        
        @param request: UpgradeClusterAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterAddonsResponse
        """
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterAddonsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterAddonsResponse(),
                self.execute(params, req, runtime)
            )

    async def upgrade_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterAddonsResponse:
        """
        @summary Updates cluster components to use new features and patch vulnerabilities. You must update cluster components one after one and update a component only after the previous one is successfully updated. Before you update a component, we recommend that you read the update notes for each component. Cluster component updates may affect your businesses. Assess the impact, back up data, and perform the update during off-peak hours.
        
        @param request: UpgradeClusterAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterAddonsResponse
        """
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
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterAddonsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterAddonsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def upgrade_cluster_addons(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterAddonsRequest,
    ) -> cs20151215_models.UpgradeClusterAddonsResponse:
        """
        @summary Updates cluster components to use new features and patch vulnerabilities. You must update cluster components one after one and update a component only after the previous one is successfully updated. Before you update a component, we recommend that you read the update notes for each component. Cluster component updates may affect your businesses. Assess the impact, back up data, and perform the update during off-peak hours.
        
        @param request: UpgradeClusterAddonsRequest
        @return: UpgradeClusterAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def upgrade_cluster_addons_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterAddonsRequest,
    ) -> cs20151215_models.UpgradeClusterAddonsResponse:
        """
        @summary Updates cluster components to use new features and patch vulnerabilities. You must update cluster components one after one and update a component only after the previous one is successfully updated. Before you update a component, we recommend that you read the update notes for each component. Cluster component updates may affect your businesses. Assess the impact, back up data, and perform the update during off-peak hours.
        
        @param request: UpgradeClusterAddonsRequest
        @return: UpgradeClusterAddonsResponse
        """
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
        @summary You can call the UpgradeClusterNodepool operation to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @description This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
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
        if not UtilClient.is_unset(request.node_names):
            body['node_names'] = request.node_names
        if not UtilClient.is_unset(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterNodepoolResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterNodepoolResponse(),
                self.execute(params, req, runtime)
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
        @summary You can call the UpgradeClusterNodepool operation to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @description This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
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
        if not UtilClient.is_unset(request.node_names):
            body['node_names'] = request.node_names
        if not UtilClient.is_unset(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterNodepoolResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cs20151215_models.UpgradeClusterNodepoolResponse(),
                await self.execute_async(params, req, runtime)
            )

    def upgrade_cluster_nodepool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.UpgradeClusterNodepoolRequest,
    ) -> cs20151215_models.UpgradeClusterNodepoolResponse:
        """
        @summary You can call the UpgradeClusterNodepool operation to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @description This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
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
        @summary You can call the UpgradeClusterNodepool operation to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @description This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @param request: UpgradeClusterNodepoolRequest
        @return: UpgradeClusterNodepoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_cluster_nodepool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)
