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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'cs.aliyuncs.com',
            'cn-beijing-finance-1': 'cs.aliyuncs.com',
            'cn-beijing-finance-pop': 'cs.aliyuncs.com',
            'cn-beijing-gov-1': 'cs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cs.aliyuncs.com',
            'cn-edge-1': 'cs.aliyuncs.com',
            'cn-fujian': 'cs.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cs.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cs.aliyuncs.com',
            'cn-hangzhou-finance': 'cs-vpc.cn-hangzhou-finance.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cs.aliyuncs.com',
            'cn-hangzhou-test-306': 'cs.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cs.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'cs.aliyuncs.com',
            'cn-qingdao-nebula': 'cs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cs.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cs.aliyuncs.com',
            'cn-shanghai-finance-1': 'cs-vpc.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shanghai-inner': 'cs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cs.aliyuncs.com',
            'cn-shenzhen-finance-1': 'cs-vpc.cn-shenzhen-finance-1.aliyuncs.com',
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
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.next_token):
            query['next_token'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.ListTagResourcesResponse(),
            self.do_roarequest('ListTagResources', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/tags', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.next_token):
            query['next_token'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.ListTagResourcesResponse(),
            await self.do_roarequest_async('ListTagResources', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/tags', 'json', req, runtime)
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

    def untag_resources_with_options(
        self,
        request: cs20151215_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['resource_ids'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['tag_keys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.UntagResourcesResponse(),
            self.do_roarequest('UntagResources', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/tags', 'none', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cs20151215_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['resource_ids'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['tag_keys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.UntagResourcesResponse(),
            await self.do_roarequest_async('UntagResources', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/tags', 'none', req, runtime)
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

    def modify_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.instance_deletion_protection):
            body['instance_deletion_protection'] = request.instance_deletion_protection
        if not UtilClient.is_unset(request.ingress_domain_rebinding):
            body['ingress_domain_rebinding'] = request.ingress_domain_rebinding
        if not UtilClient.is_unset(request.ingress_loadbalancer_id):
            body['ingress_loadbalancer_id'] = request.ingress_loadbalancer_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterResponse(),
            self.do_roarequest('ModifyCluster', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/api/v2/clusters/{cluster_id}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.instance_deletion_protection):
            body['instance_deletion_protection'] = request.instance_deletion_protection
        if not UtilClient.is_unset(request.ingress_domain_rebinding):
            body['ingress_domain_rebinding'] = request.ingress_domain_rebinding
        if not UtilClient.is_unset(request.ingress_loadbalancer_id):
            body['ingress_loadbalancer_id'] = request.ingress_loadbalancer_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterResponse(),
            await self.do_roarequest_async('ModifyCluster', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/api/v2/clusters/{cluster_id}', 'json', req, runtime)
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

    def describe_cluster_attach_scripts_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.arch):
            body['arch'] = request.arch
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAttachScriptsResponse(),
            self.do_roarequest('DescribeClusterAttachScripts', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/attachscript', 'string', req, runtime)
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
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.arch):
            body['arch'] = request.arch
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAttachScriptsResponse(),
            await self.do_roarequest_async('DescribeClusterAttachScripts', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/attachscript', 'string', req, runtime)
        )

    def remove_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def remove_cluster_nodes_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def remove_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
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
        return TeaCore.from_map(
            cs20151215_models.RemoveClusterNodesResponse(),
            self.do_roarequest('RemoveClusterNodes', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/nodes/remove', 'none', req, runtime)
        )

    async def remove_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
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
        return TeaCore.from_map(
            cs20151215_models.RemoveClusterNodesResponse(),
            await self.do_roarequest_async('RemoveClusterNodes', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/nodes/remove', 'none', req, runtime)
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

    def describe_kubernetes_version_metadata_with_options(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.kubernetes_version):
            query['KubernetesVersion'] = request.kubernetes_version
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
            self.do_roarequest('DescribeKubernetesVersionMetadata', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v1/metadata/versions', 'array', req, runtime)
        )

    async def describe_kubernetes_version_metadata_with_options_async(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.kubernetes_version):
            query['KubernetesVersion'] = request.kubernetes_version
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
            await self.do_roarequest_async('DescribeKubernetesVersionMetadata', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v1/metadata/versions', 'array', req, runtime)
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

    def describe_cluster_logs_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterLogsResponse(),
            self.do_roarequest('DescribeClusterLogs', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/logs', 'array', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterLogsResponse(),
            await self.do_roarequest_async('DescribeClusterLogs', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/logs', 'array', req, runtime)
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

    def create_kubernetes_trigger_with_options(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateKubernetesTriggerResponse(),
            self.do_roarequest('CreateKubernetesTrigger', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/triggers', 'json', req, runtime)
        )

    async def create_kubernetes_trigger_with_options_async(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateKubernetesTriggerResponse(),
            await self.do_roarequest_async('CreateKubernetesTrigger', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/triggers', 'json', req, runtime)
        )

    def grant_permissions(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
    ) -> cs20151215_models.GrantPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_permissions_with_options(uid, request, headers, runtime)

    async def grant_permissions_async(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
    ) -> cs20151215_models.GrantPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_permissions_with_options_async(uid, request, headers, runtime)

    def grant_permissions_with_options(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GrantPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return TeaCore.from_map(
            cs20151215_models.GrantPermissionsResponse(),
            self.do_roarequest('GrantPermissions', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/permissions/users/{uid}', 'none', req, runtime)
        )

    async def grant_permissions_with_options_async(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GrantPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return TeaCore.from_map(
            cs20151215_models.GrantPermissionsResponse(),
            await self.do_roarequest_async('GrantPermissions', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/permissions/users/{uid}', 'none', req, runtime)
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

    def describe_cluster_detail_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterDetailResponse(),
            self.do_roarequest('DescribeClusterDetail', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterDetailResponse(),
            await self.do_roarequest_async('DescribeClusterDetail', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.PauseComponentUpgradeResponse(),
            self.do_roarequest('PauseComponentUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{clusterid}/components/{componentid}/pause', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.PauseComponentUpgradeResponse(),
            await self.do_roarequest_async('PauseComponentUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{clusterid}/components/{componentid}/pause', 'none', req, runtime)
        )

    def describe_clusters(
        self,
        request: cs20151215_models.DescribeClustersRequest,
    ) -> cs20151215_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_clusters_with_options(request, headers, runtime)

    async def describe_clusters_async(
        self,
        request: cs20151215_models.DescribeClustersRequest,
    ) -> cs20151215_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_clusters_with_options_async(request, headers, runtime)

    def describe_clusters_with_options(
        self,
        request: cs20151215_models.DescribeClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.cluster_type):
            query['clusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersResponse(),
            self.do_roarequest('DescribeClusters', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters', 'array', req, runtime)
        )

    async def describe_clusters_with_options_async(
        self,
        request: cs20151215_models.DescribeClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.cluster_type):
            query['clusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersResponse(),
            await self.do_roarequest_async('DescribeClusters', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters', 'array', req, runtime)
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

    def describe_user_permission_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserPermissionResponse(),
            self.do_roarequest('DescribeUserPermission', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/permissions/users/{uid}', 'array', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeUserPermissionResponse(),
            await self.do_roarequest_async('DescribeUserPermission', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/permissions/users/{uid}', 'array', req, runtime)
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
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.update_nodes):
            body['update_nodes'] = request.update_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterNodePoolResponse(),
            self.do_roarequest('ModifyClusterNodePool', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.update_nodes):
            body['update_nodes'] = request.update_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterNodePoolResponse(),
            await self.do_roarequest_async('ModifyClusterNodePool', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'json', req, runtime)
        )

    def resume_upgrade_cluster(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_upgrade_cluster_with_options(cluster_id, headers, runtime)

    async def resume_upgrade_cluster_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_upgrade_cluster_with_options_async(cluster_id, headers, runtime)

    def resume_upgrade_cluster_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeUpgradeClusterResponse(),
            self.do_roarequest('ResumeUpgradeCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/resume', 'none', req, runtime)
        )

    async def resume_upgrade_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeUpgradeClusterResponse(),
            await self.do_roarequest_async('ResumeUpgradeCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/resume', 'none', req, runtime)
        )

    def open_ack_service(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
    ) -> cs20151215_models.OpenAckServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_ack_service_with_options(request, headers, runtime)

    async def open_ack_service_async(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
    ) -> cs20151215_models.OpenAckServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_ack_service_with_options_async(request, headers, runtime)

    def open_ack_service_with_options(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.OpenAckServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.OpenAckServiceResponse(),
            self.do_roarequest('OpenAckService', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/service/open', 'json', req, runtime)
        )

    async def open_ack_service_with_options_async(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.OpenAckServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.OpenAckServiceResponse(),
            await self.do_roarequest_async('OpenAckService', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/service/open', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterNodePoolResponse(),
            self.do_roarequest('ScaleClusterNodePool', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterNodePoolResponse(),
            await self.do_roarequest_async('ScaleClusterNodePool', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolDetailResponse(),
            self.do_roarequest('DescribeClusterNodePoolDetail', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolDetailResponse(),
            await self.do_roarequest_async('DescribeClusterNodePoolDetail', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterNodePoolResponse(),
            self.do_roarequest('CreateClusterNodePool', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/nodepools', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterNodePoolResponse(),
            await self.do_roarequest_async('CreateClusterNodePool', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/nodepools', 'json', req, runtime)
        )

    def describe_cluster_user_kubeconfig(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_user_kubeconfig_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_user_kubeconfig_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_user_kubeconfig_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterUserKubeconfigResponse(),
            self.do_roarequest('DescribeClusterUserKubeconfig', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/k8s/{cluster_id}/user_config', 'json', req, runtime)
        )

    async def describe_cluster_user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterUserKubeconfigResponse(),
            await self.do_roarequest_async('DescribeClusterUserKubeconfig', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/k8s/{cluster_id}/user_config', 'json', req, runtime)
        )

    def scale_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
    ) -> cs20151215_models.ScaleClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_cluster_with_options(cluster_id, request, headers, runtime)

    async def scale_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
    ) -> cs20151215_models.ScaleClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_cluster_with_options_async(cluster_id, request, headers, runtime)

    def scale_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterResponse:
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
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterResponse(),
            self.do_roarequest('ScaleCluster', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/clusters/{cluster_id}', 'json', req, runtime)
        )

    async def scale_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterResponse:
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
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterResponse(),
            await self.do_roarequest_async('ScaleCluster', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/clusters/{cluster_id}', 'json', req, runtime)
        )

    def describe_cluster_addon_upgrade_status(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_upgrade_status_with_options(cluster_id, component_id, headers, runtime)

    async def describe_cluster_addon_upgrade_status_async(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_upgrade_status_with_options_async(cluster_id, component_id, headers, runtime)

    def describe_cluster_addon_upgrade_status_with_options(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
            self.do_roarequest('DescribeClusterAddonUpgradeStatus', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/components/{component_id}/upgradestatus', 'json', req, runtime)
        )

    async def describe_cluster_addon_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
            await self.do_roarequest_async('DescribeClusterAddonUpgradeStatus', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/components/{component_id}/upgradestatus', 'json', req, runtime)
        )

    def describe_addons(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
    ) -> cs20151215_models.DescribeAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_addons_with_options(request, headers, runtime)

    async def describe_addons_async(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
    ) -> cs20151215_models.DescribeAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_addons_with_options_async(request, headers, runtime)

    def describe_addons_with_options(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonsResponse(),
            self.do_roarequest('DescribeAddons', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/components/metadata', 'json', req, runtime)
        )

    async def describe_addons_with_options_async(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonsResponse(),
            await self.do_roarequest_async('DescribeAddons', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/components/metadata', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.unneeded_duration):
            body['unneeded_duration'] = request.unneeded_duration
        if not UtilClient.is_unset(request.utilization_threshold):
            body['utilization_threshold'] = request.utilization_threshold
        if not UtilClient.is_unset(request.gpu_utilization_threshold):
            body['gpu_utilization_threshold'] = request.gpu_utilization_threshold
        if not UtilClient.is_unset(request.scan_interval):
            body['scan_interval'] = request.scan_interval
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateAutoscalingConfigResponse(),
            self.do_roarequest('CreateAutoscalingConfig', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/cluster/{cluster_id}/autoscale/config/', 'none', req, runtime)
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
        if not UtilClient.is_unset(request.unneeded_duration):
            body['unneeded_duration'] = request.unneeded_duration
        if not UtilClient.is_unset(request.utilization_threshold):
            body['utilization_threshold'] = request.utilization_threshold
        if not UtilClient.is_unset(request.gpu_utilization_threshold):
            body['gpu_utilization_threshold'] = request.gpu_utilization_threshold
        if not UtilClient.is_unset(request.scan_interval):
            body['scan_interval'] = request.scan_interval
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateAutoscalingConfigResponse(),
            await self.do_roarequest_async('CreateAutoscalingConfig', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/cluster/{cluster_id}/autoscale/config/', 'none', req, runtime)
        )

    def create_cluster(
        self,
        request: cs20151215_models.CreateClusterRequest,
    ) -> cs20151215_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    async def create_cluster_async(
        self,
        request: cs20151215_models.CreateClusterRequest,
    ) -> cs20151215_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(request, headers, runtime)

    def create_cluster_with_options(
        self,
        request: cs20151215_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.cluster_type):
            body['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_spec):
            body['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        if not UtilClient.is_unset(request.pod_vswitch_ids):
            body['pod_vswitch_ids'] = request.pod_vswitch_ids
        if not UtilClient.is_unset(request.container_cidr):
            body['container_cidr'] = request.container_cidr
        if not UtilClient.is_unset(request.service_cidr):
            body['service_cidr'] = request.service_cidr
        if not UtilClient.is_unset(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['is_enterprise_security_group'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.snat_entry):
            body['snat_entry'] = request.snat_entry
        if not UtilClient.is_unset(request.endpoint_public_access):
            body['endpoint_public_access'] = request.endpoint_public_access
        if not UtilClient.is_unset(request.ssh_flags):
            body['ssh_flags'] = request.ssh_flags
        if not UtilClient.is_unset(request.timezone):
            body['timezone'] = request.timezone
        if not UtilClient.is_unset(request.node_cidr_mask):
            body['node_cidr_mask'] = request.node_cidr_mask
        if not UtilClient.is_unset(request.user_ca):
            body['user_ca'] = request.user_ca
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.cluster_domain):
            body['cluster_domain'] = request.cluster_domain
        if not UtilClient.is_unset(request.node_name_mode):
            body['node_name_mode'] = request.node_name_mode
        if not UtilClient.is_unset(request.custom_san):
            body['custom_san'] = request.custom_san
        if not UtilClient.is_unset(request.encryption_provider_key):
            body['encryption_provider_key'] = request.encryption_provider_key
        if not UtilClient.is_unset(request.service_account_issuer):
            body['service_account_issuer'] = request.service_account_issuer
        if not UtilClient.is_unset(request.api_audiences):
            body['api_audiences'] = request.api_audiences
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.addons):
            body['addons'] = request.addons
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.os_type):
            body['os_type'] = request.os_type
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.proxy_mode):
            body['proxy_mode'] = request.proxy_mode
        if not UtilClient.is_unset(request.node_port_range):
            body['node_port_range'] = request.node_port_range
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.master_count):
            body['master_count'] = request.master_count
        if not UtilClient.is_unset(request.master_vswitch_ids):
            body['master_vswitch_ids'] = request.master_vswitch_ids
        if not UtilClient.is_unset(request.master_instance_types):
            body['master_instance_types'] = request.master_instance_types
        if not UtilClient.is_unset(request.master_system_disk_category):
            body['master_system_disk_category'] = request.master_system_disk_category
        if not UtilClient.is_unset(request.master_system_disk_size):
            body['master_system_disk_size'] = request.master_system_disk_size
        if not UtilClient.is_unset(request.master_system_disk_snapshot_policy_id):
            body['master_system_disk_snapshot_policy_id'] = request.master_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.master_instance_charge_type):
            body['master_instance_charge_type'] = request.master_instance_charge_type
        if not UtilClient.is_unset(request.master_period_unit):
            body['master_period_unit'] = request.master_period_unit
        if not UtilClient.is_unset(request.master_period):
            body['master_period'] = request.master_period
        if not UtilClient.is_unset(request.master_auto_renew):
            body['master_auto_renew'] = request.master_auto_renew
        if not UtilClient.is_unset(request.master_auto_renew_period):
            body['master_auto_renew_period'] = request.master_auto_renew_period
        if not UtilClient.is_unset(request.num_of_nodes):
            body['num_of_nodes'] = request.num_of_nodes
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_vswitch_ids):
            body['worker_vswitch_ids'] = request.worker_vswitch_ids
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not UtilClient.is_unset(request.worker_system_disk_snapshot_policy_id):
            body['worker_system_disk_snapshot_policy_id'] = request.worker_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.service_discovery_types):
            body['service_discovery_types'] = request.service_discovery_types
        if not UtilClient.is_unset(request.nat_gateway):
            body['nat_gateway'] = request.nat_gateway
        if not UtilClient.is_unset(request.zone_id):
            body['zone_id'] = request.zone_id
        if not UtilClient.is_unset(request.profile):
            body['profile'] = request.profile
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.timeout_mins):
            body['timeout_mins'] = request.timeout_mins
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterResponse(),
            self.do_roarequest('CreateCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters', 'json', req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: cs20151215_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.cluster_type):
            body['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_spec):
            body['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        if not UtilClient.is_unset(request.pod_vswitch_ids):
            body['pod_vswitch_ids'] = request.pod_vswitch_ids
        if not UtilClient.is_unset(request.container_cidr):
            body['container_cidr'] = request.container_cidr
        if not UtilClient.is_unset(request.service_cidr):
            body['service_cidr'] = request.service_cidr
        if not UtilClient.is_unset(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['is_enterprise_security_group'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.snat_entry):
            body['snat_entry'] = request.snat_entry
        if not UtilClient.is_unset(request.endpoint_public_access):
            body['endpoint_public_access'] = request.endpoint_public_access
        if not UtilClient.is_unset(request.ssh_flags):
            body['ssh_flags'] = request.ssh_flags
        if not UtilClient.is_unset(request.timezone):
            body['timezone'] = request.timezone
        if not UtilClient.is_unset(request.node_cidr_mask):
            body['node_cidr_mask'] = request.node_cidr_mask
        if not UtilClient.is_unset(request.user_ca):
            body['user_ca'] = request.user_ca
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.cluster_domain):
            body['cluster_domain'] = request.cluster_domain
        if not UtilClient.is_unset(request.node_name_mode):
            body['node_name_mode'] = request.node_name_mode
        if not UtilClient.is_unset(request.custom_san):
            body['custom_san'] = request.custom_san
        if not UtilClient.is_unset(request.encryption_provider_key):
            body['encryption_provider_key'] = request.encryption_provider_key
        if not UtilClient.is_unset(request.service_account_issuer):
            body['service_account_issuer'] = request.service_account_issuer
        if not UtilClient.is_unset(request.api_audiences):
            body['api_audiences'] = request.api_audiences
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.addons):
            body['addons'] = request.addons
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.os_type):
            body['os_type'] = request.os_type
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.proxy_mode):
            body['proxy_mode'] = request.proxy_mode
        if not UtilClient.is_unset(request.node_port_range):
            body['node_port_range'] = request.node_port_range
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.master_count):
            body['master_count'] = request.master_count
        if not UtilClient.is_unset(request.master_vswitch_ids):
            body['master_vswitch_ids'] = request.master_vswitch_ids
        if not UtilClient.is_unset(request.master_instance_types):
            body['master_instance_types'] = request.master_instance_types
        if not UtilClient.is_unset(request.master_system_disk_category):
            body['master_system_disk_category'] = request.master_system_disk_category
        if not UtilClient.is_unset(request.master_system_disk_size):
            body['master_system_disk_size'] = request.master_system_disk_size
        if not UtilClient.is_unset(request.master_system_disk_snapshot_policy_id):
            body['master_system_disk_snapshot_policy_id'] = request.master_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.master_instance_charge_type):
            body['master_instance_charge_type'] = request.master_instance_charge_type
        if not UtilClient.is_unset(request.master_period_unit):
            body['master_period_unit'] = request.master_period_unit
        if not UtilClient.is_unset(request.master_period):
            body['master_period'] = request.master_period
        if not UtilClient.is_unset(request.master_auto_renew):
            body['master_auto_renew'] = request.master_auto_renew
        if not UtilClient.is_unset(request.master_auto_renew_period):
            body['master_auto_renew_period'] = request.master_auto_renew_period
        if not UtilClient.is_unset(request.num_of_nodes):
            body['num_of_nodes'] = request.num_of_nodes
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_vswitch_ids):
            body['worker_vswitch_ids'] = request.worker_vswitch_ids
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not UtilClient.is_unset(request.worker_system_disk_snapshot_policy_id):
            body['worker_system_disk_snapshot_policy_id'] = request.worker_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.service_discovery_types):
            body['service_discovery_types'] = request.service_discovery_types
        if not UtilClient.is_unset(request.nat_gateway):
            body['nat_gateway'] = request.nat_gateway
        if not UtilClient.is_unset(request.zone_id):
            body['zone_id'] = request.zone_id
        if not UtilClient.is_unset(request.profile):
            body['profile'] = request.profile
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.timeout_mins):
            body['timeout_mins'] = request.timeout_mins
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterResponse(),
            await self.do_roarequest_async('CreateCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.next_version):
            body['next_version'] = request.next_version
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterResponse(),
            self.do_roarequest('UpgradeCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade', 'none', req, runtime)
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
        if not UtilClient.is_unset(request.next_version):
            body['next_version'] = request.next_version
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterResponse(),
            await self.do_roarequest_async('UpgradeCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.CancelWorkflowResponse(),
            self.do_roarequest('CancelWorkflow', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/gs/workflow/{workflow_name}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.CancelWorkflowResponse(),
            await self.do_roarequest_async('CancelWorkflow', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/gs/workflow/{workflow_name}', 'none', req, runtime)
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

    def attach_instances_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.AttachInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.is_edge_worker):
            body['is_edge_worker'] = request.is_edge_worker
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesResponse(),
            self.do_roarequest('AttachInstances', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/attach', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.is_edge_worker):
            body['is_edge_worker'] = request.is_edge_worker
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesResponse(),
            await self.do_roarequest_async('AttachInstances', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/attach', 'json', req, runtime)
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

    def describe_templates_with_options(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        if not UtilClient.is_unset(request.page_num):
            query['page_num'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplatesResponse(),
            self.do_roarequest('DescribeTemplates', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/templates', 'json', req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        if not UtilClient.is_unset(request.page_num):
            query['page_num'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplatesResponse(),
            await self.do_roarequest_async('DescribeTemplates', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/templates', 'json', req, runtime)
        )

    def pause_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_cluster_upgrade_with_options(cluster_id, headers, runtime)

    async def pause_cluster_upgrade_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pause_cluster_upgrade_with_options_async(cluster_id, headers, runtime)

    def pause_cluster_upgrade_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.PauseClusterUpgradeResponse(),
            self.do_roarequest('PauseClusterUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/pause', 'none', req, runtime)
        )

    async def pause_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.PauseClusterUpgradeResponse(),
            await self.do_roarequest_async('PauseClusterUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/pause', 'none', req, runtime)
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

    def delete_template_with_options(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteTemplateResponse(),
            self.do_roarequest('DeleteTemplate', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/templates/{template_id}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DeleteTemplateResponse(),
            await self.do_roarequest_async('DeleteTemplate', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/templates/{template_id}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplateAttributeResponse(),
            self.do_roarequest('DescribeTemplateAttribute', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/templates/{template_id}', 'array', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplateAttributeResponse(),
            await self.do_roarequest_async('DescribeTemplateAttribute', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/templates/{template_id}', 'array', req, runtime)
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

    def create_template_with_options(
        self,
        request: cs20151215_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTemplateResponse(),
            self.do_roarequest('CreateTemplate', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/templates', 'json', req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: cs20151215_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTemplateResponse(),
            await self.do_roarequest_async('CreateTemplate', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/templates', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodesResponse(),
            self.do_roarequest('DescribeClusterNodes', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/nodes', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodesResponse(),
            await self.do_roarequest_async('DescribeClusterNodes', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/nodes', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.retain_all_resources):
            query['retain_all_resources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.keep_slb):
            query['keep_slb'] = request.keep_slb
        if not UtilClient.is_unset(request.retain_resources_shrink):
            query['retain_resources'] = request.retain_resources_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterResponse(),
            self.do_roarequest('DeleteCluster', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/clusters/{cluster_id}', 'none', req, runtime)
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
        if not UtilClient.is_unset(request.retain_all_resources):
            query['retain_all_resources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.keep_slb):
            query['keep_slb'] = request.keep_slb
        if not UtilClient.is_unset(request.retain_resources_shrink):
            query['retain_resources'] = request.retain_resources_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterResponse(),
            await self.do_roarequest_async('DeleteCluster', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/clusters/{cluster_id}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.CancelComponentUpgradeResponse(),
            self.do_roarequest('CancelComponentUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/{component_id}/cancel', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.CancelComponentUpgradeResponse(),
            await self.do_roarequest_async('CancelComponentUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/{component_id}/cancel', 'none', req, runtime)
        )

    def migrate_cluster(
        self,
        cluster_id: str,
    ) -> cs20151215_models.MigrateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_cluster_with_options(cluster_id, headers, runtime)

    async def migrate_cluster_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.MigrateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.migrate_cluster_with_options_async(cluster_id, headers, runtime)

    def migrate_cluster_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.MigrateClusterResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.MigrateClusterResponse(),
            self.do_roarequest('MigrateCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/migrate', 'none', req, runtime)
        )

    async def migrate_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.MigrateClusterResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.MigrateClusterResponse(),
            await self.do_roarequest_async('MigrateCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/migrate', 'none', req, runtime)
        )

    def describe_cluster_addons_version(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_version_with_options(cluster_id, headers, runtime)

    async def describe_cluster_addons_version_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addons_version_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_addons_version_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsVersionResponse(),
            self.do_roarequest('DescribeClusterAddonsVersion', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/components/version', 'json', req, runtime)
        )

    async def describe_cluster_addons_version_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsVersionResponse(),
            await self.do_roarequest_async('DescribeClusterAddonsVersion', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/components/version', 'json', req, runtime)
        )

    def describe_external_agent(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_external_agent_with_options(cluster_id, request, headers, runtime)

    async def describe_external_agent_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_external_agent_with_options_async(cluster_id, request, headers, runtime)

    def describe_external_agent_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeExternalAgentResponse(),
            self.do_roarequest('DescribeExternalAgent', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/k8s/{cluster_id}/external/agent/deployment', 'json', req, runtime)
        )

    async def describe_external_agent_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeExternalAgentResponse(),
            await self.do_roarequest_async('DescribeExternalAgent', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/k8s/{cluster_id}/external/agent/deployment', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.UnInstallClusterAddonsResponse(),
            self.do_roarequest('UnInstallClusterAddons', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/uninstall', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.UnInstallClusterAddonsResponse(),
            await self.do_roarequest_async('UnInstallClusterAddons', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/uninstall', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ResumeComponentUpgradeResponse(),
            self.do_roarequest('ResumeComponentUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{clusterid}/components/{componentid}/resume', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ResumeComponentUpgradeResponse(),
            await self.do_roarequest_async('ResumeComponentUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{clusterid}/components/{componentid}/resume', 'none', req, runtime)
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

    def describe_clusters_v1with_options(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersV1Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersV1Response(),
            self.do_roarequest('DescribeClustersV1', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v1/clusters', 'json', req, runtime)
        )

    async def describe_clusters_v1with_options_async(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersV1Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersV1Response(),
            await self.do_roarequest_async('DescribeClustersV1', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v1/clusters', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterConfigurationResponse(),
            self.do_roarequest('ModifyClusterConfiguration', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/clusters/{cluster_id}/configuration', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterConfigurationResponse(),
            await self.do_roarequest_async('ModifyClusterConfiguration', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/clusters/{cluster_id}/configuration', 'none', req, runtime)
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

    def describe_task_info_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTaskInfoResponse(),
            self.do_roarequest('DescribeTaskInfo', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/tasks/{task_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeTaskInfoResponse(),
            await self.do_roarequest_async('DescribeTaskInfo', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/tasks/{task_id}', 'json', req, runtime)
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

    def descirbe_workflow_with_options(
        self,
        workflow_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescirbeWorkflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescirbeWorkflowResponse(),
            self.do_roarequest('DescirbeWorkflow', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/gs/workflow/{workflow_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescirbeWorkflowResponse(),
            await self.do_roarequest_async('DescirbeWorkflow', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/gs/workflow/{workflow_name}', 'json', req, runtime)
        )

    def cancel_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_cluster_upgrade_with_options(cluster_id, headers, runtime)

    async def cancel_cluster_upgrade_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_cluster_upgrade_with_options_async(cluster_id, headers, runtime)

    def cancel_cluster_upgrade_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.CancelClusterUpgradeResponse(),
            self.do_roarequest('CancelClusterUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/cancel', 'none', req, runtime)
        )

    async def cancel_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.CancelClusterUpgradeResponse(),
            await self.do_roarequest_async('CancelClusterUpgrade', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/cancel', 'none', req, runtime)
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

    def remove_workflow_with_options(
        self,
        workflow_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveWorkflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveWorkflowResponse(),
            self.do_roarequest('RemoveWorkflow', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/gs/workflow/{workflow_name}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.RemoveWorkflowResponse(),
            await self.do_roarequest_async('RemoveWorkflow', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/gs/workflow/{workflow_name}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.UpdateTemplateResponse(),
            self.do_roarequest('UpdateTemplate', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/templates/{template_id}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.UpdateTemplateResponse(),
            await self.do_roarequest_async('UpdateTemplate', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/templates/{template_id}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterAddonsResponse(),
            self.do_roarequest('UpgradeClusterAddons', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/upgrade', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterAddonsResponse(),
            await self.do_roarequest_async('UpgradeClusterAddons', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/upgrade', 'none', req, runtime)
        )

    def describe_cluster_namespaces(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_namespaces_with_options(cluster_id, headers, runtime)

    async def describe_cluster_namespaces_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_namespaces_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_namespaces_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNamespacesResponse(),
            self.do_roarequest('DescribeClusterNamespaces', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/k8s/{cluster_id}/namespaces', 'array', req, runtime)
        )

    async def describe_cluster_namespaces_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNamespacesResponse(),
            await self.do_roarequest_async('DescribeClusterNamespaces', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/k8s/{cluster_id}/namespaces', 'array', req, runtime)
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

    def delete_kubernetes_trigger_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteKubernetesTriggerResponse(),
            self.do_roarequest('DeleteKubernetesTrigger', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/triggers/revoke/{id}', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DeleteKubernetesTriggerResponse(),
            await self.do_roarequest_async('DeleteKubernetesTrigger', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/triggers/revoke/{id}', 'none', req, runtime)
        )

    def describe_user_quota(self) -> cs20151215_models.DescribeUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_quota_with_options(headers, runtime)

    async def describe_user_quota_async(self) -> cs20151215_models.DescribeUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_quota_with_options_async(headers, runtime)

    def describe_user_quota_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserQuotaResponse(),
            self.do_roarequest('DescribeUserQuota', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/quota', 'json', req, runtime)
        )

    async def describe_user_quota_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserQuotaResponse(),
            await self.do_roarequest_async('DescribeUserQuota', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/quota', 'json', req, runtime)
        )

    def delete_cluster_nodepool(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodepool_with_options(cluster_id, nodepool_id, headers, runtime)

    async def delete_cluster_nodepool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_nodepool_with_options_async(cluster_id, nodepool_id, headers, runtime)

    def delete_cluster_nodepool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodepoolResponse(),
            self.do_roarequest('DeleteClusterNodepool', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'none', req, runtime)
        )

    async def delete_cluster_nodepool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodepoolResponse(),
            await self.do_roarequest_async('DeleteClusterNodepool', '2015-12-15', 'HTTPS', 'DELETE', 'AK', f'/clusters/{cluster_id}/nodepools/{nodepool_id}', 'none', req, runtime)
        )

    def describe_cluster_addons_upgrade_status(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_upgrade_status_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_addons_upgrade_status_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addons_upgrade_status_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_addons_upgrade_status_with_options(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
            self.do_roarequest('DescribeClusterAddonsUpgradeStatus', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/components/upgradestatus', 'json', req, runtime)
        )

    async def describe_cluster_addons_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
            await self.do_roarequest_async('DescribeClusterAddonsUpgradeStatus', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/components/upgradestatus', 'json', req, runtime)
        )

    def describe_workflows(self) -> cs20151215_models.DescribeWorkflowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflows_with_options(headers, runtime)

    async def describe_workflows_async(self) -> cs20151215_models.DescribeWorkflowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_workflows_with_options_async(headers, runtime)

    def describe_workflows_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeWorkflowsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeWorkflowsResponse(),
            self.do_roarequest('DescribeWorkflows', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/gs/workflows', 'json', req, runtime)
        )

    async def describe_workflows_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeWorkflowsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeWorkflowsResponse(),
            await self.do_roarequest_async('DescribeWorkflows', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/gs/workflows', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.InstallClusterAddonsResponse(),
            self.do_roarequest('InstallClusterAddons', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/install', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.InstallClusterAddonsResponse(),
            await self.do_roarequest_async('InstallClusterAddons', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/components/install', 'none', req, runtime)
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

    def describe_cluster_node_pools_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolsResponse(),
            self.do_roarequest('DescribeClusterNodePools', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/nodepools', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolsResponse(),
            await self.do_roarequest_async('DescribeClusterNodePools', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/nodepools', 'json', req, runtime)
        )

    def describe_cluster_v2user_kubeconfig(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_v2user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_v2user_kubeconfig_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_v2user_kubeconfig_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_v2user_kubeconfig_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
            self.do_roarequest('DescribeClusterV2UserKubeconfig', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v2/k8s/{cluster_id}/user_config', 'json', req, runtime)
        )

    async def describe_cluster_v2user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
            await self.do_roarequest_async('DescribeClusterV2UserKubeconfig', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v2/k8s/{cluster_id}/user_config', 'json', req, runtime)
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

    def start_workflow_with_options(
        self,
        request: cs20151215_models.StartWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartWorkflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.workflow_type):
            body['workflow_type'] = request.workflow_type
        if not UtilClient.is_unset(request.service):
            body['service'] = request.service
        if not UtilClient.is_unset(request.mapping_oss_region):
            body['mapping_oss_region'] = request.mapping_oss_region
        if not UtilClient.is_unset(request.mapping_fastq_first_filename):
            body['mapping_fastq_first_filename'] = request.mapping_fastq_first_filename
        if not UtilClient.is_unset(request.mapping_fastq_second_filename):
            body['mapping_fastq_second_filename'] = request.mapping_fastq_second_filename
        if not UtilClient.is_unset(request.mapping_bucket_name):
            body['mapping_bucket_name'] = request.mapping_bucket_name
        if not UtilClient.is_unset(request.mapping_fastq_path):
            body['mapping_fastq_path'] = request.mapping_fastq_path
        if not UtilClient.is_unset(request.mapping_reference_path):
            body['mapping_reference_path'] = request.mapping_reference_path
        if not UtilClient.is_unset(request.mapping_is_mark_dup):
            body['mapping_is_mark_dup'] = request.mapping_is_mark_dup
        if not UtilClient.is_unset(request.mapping_bam_out_path):
            body['mapping_bam_out_path'] = request.mapping_bam_out_path
        if not UtilClient.is_unset(request.mapping_bam_out_filename):
            body['mapping_bam_out_filename'] = request.mapping_bam_out_filename
        if not UtilClient.is_unset(request.wgs_oss_region):
            body['wgs_oss_region'] = request.wgs_oss_region
        if not UtilClient.is_unset(request.wgs_fastq_first_filename):
            body['wgs_fastq_first_filename'] = request.wgs_fastq_first_filename
        if not UtilClient.is_unset(request.wgs_fastq_second_filename):
            body['wgs_fastq_second_filename'] = request.wgs_fastq_second_filename
        if not UtilClient.is_unset(request.wgs_bucket_name):
            body['wgs_bucket_name'] = request.wgs_bucket_name
        if not UtilClient.is_unset(request.wgs_fastq_path):
            body['wgs_fastq_path'] = request.wgs_fastq_path
        if not UtilClient.is_unset(request.wgs_reference_path):
            body['wgs_reference_path'] = request.wgs_reference_path
        if not UtilClient.is_unset(request.wgs_vcf_out_path):
            body['wgs_vcf_out_path'] = request.wgs_vcf_out_path
        if not UtilClient.is_unset(request.wgs_vcf_out_filename):
            body['wgs_vcf_out_filename'] = request.wgs_vcf_out_filename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.StartWorkflowResponse(),
            self.do_roarequest('StartWorkflow', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/gs/workflow', 'json', req, runtime)
        )

    async def start_workflow_with_options_async(
        self,
        request: cs20151215_models.StartWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartWorkflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.workflow_type):
            body['workflow_type'] = request.workflow_type
        if not UtilClient.is_unset(request.service):
            body['service'] = request.service
        if not UtilClient.is_unset(request.mapping_oss_region):
            body['mapping_oss_region'] = request.mapping_oss_region
        if not UtilClient.is_unset(request.mapping_fastq_first_filename):
            body['mapping_fastq_first_filename'] = request.mapping_fastq_first_filename
        if not UtilClient.is_unset(request.mapping_fastq_second_filename):
            body['mapping_fastq_second_filename'] = request.mapping_fastq_second_filename
        if not UtilClient.is_unset(request.mapping_bucket_name):
            body['mapping_bucket_name'] = request.mapping_bucket_name
        if not UtilClient.is_unset(request.mapping_fastq_path):
            body['mapping_fastq_path'] = request.mapping_fastq_path
        if not UtilClient.is_unset(request.mapping_reference_path):
            body['mapping_reference_path'] = request.mapping_reference_path
        if not UtilClient.is_unset(request.mapping_is_mark_dup):
            body['mapping_is_mark_dup'] = request.mapping_is_mark_dup
        if not UtilClient.is_unset(request.mapping_bam_out_path):
            body['mapping_bam_out_path'] = request.mapping_bam_out_path
        if not UtilClient.is_unset(request.mapping_bam_out_filename):
            body['mapping_bam_out_filename'] = request.mapping_bam_out_filename
        if not UtilClient.is_unset(request.wgs_oss_region):
            body['wgs_oss_region'] = request.wgs_oss_region
        if not UtilClient.is_unset(request.wgs_fastq_first_filename):
            body['wgs_fastq_first_filename'] = request.wgs_fastq_first_filename
        if not UtilClient.is_unset(request.wgs_fastq_second_filename):
            body['wgs_fastq_second_filename'] = request.wgs_fastq_second_filename
        if not UtilClient.is_unset(request.wgs_bucket_name):
            body['wgs_bucket_name'] = request.wgs_bucket_name
        if not UtilClient.is_unset(request.wgs_fastq_path):
            body['wgs_fastq_path'] = request.wgs_fastq_path
        if not UtilClient.is_unset(request.wgs_reference_path):
            body['wgs_reference_path'] = request.wgs_reference_path
        if not UtilClient.is_unset(request.wgs_vcf_out_path):
            body['wgs_vcf_out_path'] = request.wgs_vcf_out_path
        if not UtilClient.is_unset(request.wgs_vcf_out_filename):
            body['wgs_vcf_out_filename'] = request.wgs_vcf_out_filename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.StartWorkflowResponse(),
            await self.do_roarequest_async('StartWorkflow', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/gs/workflow', 'json', req, runtime)
        )

    def scale_out_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_out_cluster_with_options(cluster_id, request, headers, runtime)

    async def scale_out_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_out_cluster_with_options_async(cluster_id, request, headers, runtime)

    def scale_out_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleOutClusterResponse(),
            self.do_roarequest('ScaleOutCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}', 'json', req, runtime)
        )

    async def scale_out_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleOutClusterResponse(),
            await self.do_roarequest_async('ScaleOutCluster', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/api/v2/clusters/{cluster_id}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEventsResponse(),
            self.do_roarequest('DescribeEvents', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/events', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEventsResponse(),
            await self.do_roarequest_async('DescribeEvents', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/events', 'json', req, runtime)
        )

    def update_k8s_cluster_user_config_expire(
        self,
        cluster_id: str,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_cluster_user_config_expire_with_options(cluster_id, headers, runtime)

    async def update_k8s_cluster_user_config_expire_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_cluster_user_config_expire_with_options_async(cluster_id, headers, runtime)

    def update_k8s_cluster_user_config_expire_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
            self.do_roarequest('UpdateK8sClusterUserConfigExpire', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/k8s/{cluster_id}/user_config/expire', 'none', req, runtime)
        )

    async def update_k8s_cluster_user_config_expire_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
            await self.do_roarequest_async('UpdateK8sClusterUserConfigExpire', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/k8s/{cluster_id}/user_config/expire', 'none', req, runtime)
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

    def tag_resources_with_options(
        self,
        request: cs20151215_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['resource_ids'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.TagResourcesResponse(),
            self.do_roarequest('TagResources', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/tags', 'none', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cs20151215_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['resource_ids'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.TagResourcesResponse(),
            await self.do_roarequest_async('TagResources', '2015-12-15', 'HTTPS', 'PUT', 'AK', f'/tags', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterTagsResponse(),
            self.do_roarequest('ModifyClusterTags', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/tags', 'none', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterTagsResponse(),
            await self.do_roarequest_async('ModifyClusterTags', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/tags', 'none', req, runtime)
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

    def get_kubernetes_trigger_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.GetKubernetesTriggerResponse(),
            self.do_roarequest('GetKubernetesTrigger', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/triggers/{cluster_id}', 'array', req, runtime)
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
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cs20151215_models.GetKubernetesTriggerResponse(),
            await self.do_roarequest_async('GetKubernetesTrigger', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/triggers/{cluster_id}', 'array', req, runtime)
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

    def get_upgrade_status_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.GetUpgradeStatusResponse(),
            self.do_roarequest('GetUpgradeStatus', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/status', 'json', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.GetUpgradeStatusResponse(),
            await self.do_roarequest_async('GetUpgradeStatus', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/api/v2/clusters/{cluster_id}/upgrade/status', 'json', req, runtime)
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

    def describe_cluster_resources_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterResourcesResponse(),
            self.do_roarequest('DescribeClusterResources', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/resources', 'array', req, runtime)
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
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterResourcesResponse(),
            await self.do_roarequest_async('DescribeClusterResources', '2015-12-15', 'HTTPS', 'GET', 'AK', f'/clusters/{cluster_id}/resources', 'array', req, runtime)
        )

    def delete_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def delete_cluster_nodes_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def delete_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodesResponse(),
            self.do_roarequest('DeleteClusterNodes', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/nodes', 'none', req, runtime)
        )

    async def delete_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodesResponse(),
            await self.do_roarequest_async('DeleteClusterNodes', '2015-12-15', 'HTTPS', 'POST', 'AK', f'/clusters/{cluster_id}/nodes', 'none', req, runtime)
        )
