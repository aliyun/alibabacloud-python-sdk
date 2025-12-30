# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ehpc20240730 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('ehpc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_nodes_with_options(
        self,
        tmp_req: main_models.AttachNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachNodesResponse:
        tmp_req.validate()
        request = main_models.AttachNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_node):
            request.compute_node_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_nodes_with_options_async(
        self,
        tmp_req: main_models.AttachNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachNodesResponse:
        tmp_req.validate()
        request = main_models.AttachNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_node):
            request.compute_node_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_nodes(
        self,
        request: main_models.AttachNodesRequest,
    ) -> main_models.AttachNodesResponse:
        runtime = RuntimeOptions()
        return self.attach_nodes_with_options(request, runtime)

    async def attach_nodes_async(
        self,
        request: main_models.AttachNodesRequest,
    ) -> main_models.AttachNodesResponse:
        runtime = RuntimeOptions()
        return await self.attach_nodes_with_options_async(request, runtime)

    def attach_shared_storages_with_options(
        self,
        tmp_req: main_models.AttachSharedStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachSharedStoragesResponse:
        tmp_req.validate()
        request = main_models.AttachSharedStoragesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.shared_storages):
            request.shared_storages_shrink = Utils.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachSharedStorages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachSharedStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_shared_storages_with_options_async(
        self,
        tmp_req: main_models.AttachSharedStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachSharedStoragesResponse:
        tmp_req.validate()
        request = main_models.AttachSharedStoragesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.shared_storages):
            request.shared_storages_shrink = Utils.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachSharedStorages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachSharedStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_shared_storages(
        self,
        request: main_models.AttachSharedStoragesRequest,
    ) -> main_models.AttachSharedStoragesResponse:
        runtime = RuntimeOptions()
        return self.attach_shared_storages_with_options(request, runtime)

    async def attach_shared_storages_async(
        self,
        request: main_models.AttachSharedStoragesRequest,
    ) -> main_models.AttachSharedStoragesResponse:
        runtime = RuntimeOptions()
        return await self.attach_shared_storages_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        tmp_req.validate()
        request = main_models.CreateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_packages):
            request.additional_packages_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        if not DaraCore.is_null(tmp_req.addons):
            request.addons_shrink = Utils.array_to_string_with_specified_style(tmp_req.addons, 'Addons', 'json')
        if not DaraCore.is_null(tmp_req.cluster_credentials):
            request.cluster_credentials_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_credentials, 'ClusterCredentials', 'json')
        if not DaraCore.is_null(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not DaraCore.is_null(tmp_req.manager):
            request.manager_shrink = Utils.array_to_string_with_specified_style(tmp_req.manager, 'Manager', 'json')
        if not DaraCore.is_null(tmp_req.queues):
            request.queues_shrink = Utils.array_to_string_with_specified_style(tmp_req.queues, 'Queues', 'json')
        if not DaraCore.is_null(tmp_req.shared_storages):
            request.shared_storages_shrink = Utils.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.additional_packages_shrink):
            query['AdditionalPackages'] = request.additional_packages_shrink
        if not DaraCore.is_null(request.addons_shrink):
            query['Addons'] = request.addons_shrink
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not DaraCore.is_null(request.cluster_credentials_shrink):
            query['ClusterCredentials'] = request.cluster_credentials_shrink
        if not DaraCore.is_null(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not DaraCore.is_null(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_vswitch_id):
            query['ClusterVSwitchId'] = request.cluster_vswitch_id
        if not DaraCore.is_null(request.cluster_vpc_id):
            query['ClusterVpcId'] = request.cluster_vpc_id
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.is_enterprise_security_group):
            query['IsEnterpriseSecurityGroup'] = request.is_enterprise_security_group
        if not DaraCore.is_null(request.manager_shrink):
            query['Manager'] = request.manager_shrink
        if not DaraCore.is_null(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not DaraCore.is_null(request.max_count):
            query['MaxCount'] = request.max_count
        if not DaraCore.is_null(request.queues_shrink):
            query['Queues'] = request.queues_shrink
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        tmp_req.validate()
        request = main_models.CreateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_packages):
            request.additional_packages_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        if not DaraCore.is_null(tmp_req.addons):
            request.addons_shrink = Utils.array_to_string_with_specified_style(tmp_req.addons, 'Addons', 'json')
        if not DaraCore.is_null(tmp_req.cluster_credentials):
            request.cluster_credentials_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_credentials, 'ClusterCredentials', 'json')
        if not DaraCore.is_null(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not DaraCore.is_null(tmp_req.manager):
            request.manager_shrink = Utils.array_to_string_with_specified_style(tmp_req.manager, 'Manager', 'json')
        if not DaraCore.is_null(tmp_req.queues):
            request.queues_shrink = Utils.array_to_string_with_specified_style(tmp_req.queues, 'Queues', 'json')
        if not DaraCore.is_null(tmp_req.shared_storages):
            request.shared_storages_shrink = Utils.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.additional_packages_shrink):
            query['AdditionalPackages'] = request.additional_packages_shrink
        if not DaraCore.is_null(request.addons_shrink):
            query['Addons'] = request.addons_shrink
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not DaraCore.is_null(request.cluster_credentials_shrink):
            query['ClusterCredentials'] = request.cluster_credentials_shrink
        if not DaraCore.is_null(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not DaraCore.is_null(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_vswitch_id):
            query['ClusterVSwitchId'] = request.cluster_vswitch_id
        if not DaraCore.is_null(request.cluster_vpc_id):
            query['ClusterVpcId'] = request.cluster_vpc_id
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.is_enterprise_security_group):
            query['IsEnterpriseSecurityGroup'] = request.is_enterprise_security_group
        if not DaraCore.is_null(request.manager_shrink):
            query['Manager'] = request.manager_shrink
        if not DaraCore.is_null(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not DaraCore.is_null(request.max_count):
            query['MaxCount'] = request.max_count
        if not DaraCore.is_null(request.queues_shrink):
            query['Queues'] = request.queues_shrink
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp_req: main_models.CreateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        tmp_req.validate()
        request = main_models.CreateJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_spec):
            request.job_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        tmp_req: main_models.CreateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        tmp_req.validate()
        request = main_models.CreateJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_spec):
            request.job_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_nodes_with_options(
        self,
        tmp_req: main_models.CreateNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodesResponse:
        tmp_req.validate()
        request = main_models.CreateNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_node):
            request.compute_node_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        if not DaraCore.is_null(tmp_req.hostnames):
            request.hostnames_shrink = Utils.array_to_string_with_specified_style(tmp_req.hostnames, 'Hostnames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not DaraCore.is_null(request.hpcinter_connect):
            query['HPCInterConnect'] = request.hpcinter_connect
        if not DaraCore.is_null(request.hostname_prefix):
            query['HostnamePrefix'] = request.hostname_prefix
        if not DaraCore.is_null(request.hostname_suffix):
            query['HostnameSuffix'] = request.hostname_suffix
        if not DaraCore.is_null(request.hostnames_shrink):
            query['Hostnames'] = request.hostnames_shrink
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.ram_role):
            query['RamRole'] = request.ram_role
        if not DaraCore.is_null(request.reserved_node_pool_id):
            query['ReservedNodePoolId'] = request.reserved_node_pool_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nodes_with_options_async(
        self,
        tmp_req: main_models.CreateNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodesResponse:
        tmp_req.validate()
        request = main_models.CreateNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compute_node):
            request.compute_node_shrink = Utils.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        if not DaraCore.is_null(tmp_req.hostnames):
            request.hostnames_shrink = Utils.array_to_string_with_specified_style(tmp_req.hostnames, 'Hostnames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not DaraCore.is_null(request.hpcinter_connect):
            query['HPCInterConnect'] = request.hpcinter_connect
        if not DaraCore.is_null(request.hostname_prefix):
            query['HostnamePrefix'] = request.hostname_prefix
        if not DaraCore.is_null(request.hostname_suffix):
            query['HostnameSuffix'] = request.hostname_suffix
        if not DaraCore.is_null(request.hostnames_shrink):
            query['Hostnames'] = request.hostnames_shrink
        if not DaraCore.is_null(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.ram_role):
            query['RamRole'] = request.ram_role
        if not DaraCore.is_null(request.reserved_node_pool_id):
            query['ReservedNodePoolId'] = request.reserved_node_pool_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nodes(
        self,
        request: main_models.CreateNodesRequest,
    ) -> main_models.CreateNodesResponse:
        runtime = RuntimeOptions()
        return self.create_nodes_with_options(request, runtime)

    async def create_nodes_async(
        self,
        request: main_models.CreateNodesRequest,
    ) -> main_models.CreateNodesResponse:
        runtime = RuntimeOptions()
        return await self.create_nodes_with_options_async(request, runtime)

    def create_queue_with_options(
        self,
        tmp_req: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        tmp_req.validate()
        request = main_models.CreateQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue):
            request.queue_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        tmp_req: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        tmp_req.validate()
        request = main_models.CreateQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue):
            request.queue_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_queue(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_users_with_options(
        self,
        tmp_req: main_models.CreateUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsersResponse:
        tmp_req.validate()
        request = main_models.CreateUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.user_shrink):
            query['User'] = request.user_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsers',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_users_with_options_async(
        self,
        tmp_req: main_models.CreateUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsersResponse:
        tmp_req.validate()
        request = main_models.CreateUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.user_shrink):
            query['User'] = request.user_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsers',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_users(
        self,
        request: main_models.CreateUsersRequest,
    ) -> main_models.CreateUsersResponse:
        runtime = RuntimeOptions()
        return self.create_users_with_options(request, runtime)

    async def create_users_async(
        self,
        request: main_models.CreateUsersRequest,
    ) -> main_models.CreateUsersResponse:
        runtime = RuntimeOptions()
        return await self.create_users_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_nodes_with_options(
        self,
        tmp_req: main_models.DeleteNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodesResponse:
        tmp_req.validate()
        request = main_models.DeleteNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nodes_with_options_async(
        self,
        tmp_req: main_models.DeleteNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodesResponse:
        tmp_req.validate()
        request = main_models.DeleteNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nodes(
        self,
        request: main_models.DeleteNodesRequest,
    ) -> main_models.DeleteNodesResponse:
        runtime = RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    async def delete_nodes_async(
        self,
        request: main_models.DeleteNodesRequest,
    ) -> main_models.DeleteNodesResponse:
        runtime = RuntimeOptions()
        return await self.delete_nodes_with_options_async(request, runtime)

    def delete_queues_with_options(
        self,
        tmp_req: main_models.DeleteQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueuesResponse:
        tmp_req.validate()
        request = main_models.DeleteQueuesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueues',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queues_with_options_async(
        self,
        tmp_req: main_models.DeleteQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueuesResponse:
        tmp_req.validate()
        request = main_models.DeleteQueuesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueues',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_queues(
        self,
        request: main_models.DeleteQueuesRequest,
    ) -> main_models.DeleteQueuesResponse:
        runtime = RuntimeOptions()
        return self.delete_queues_with_options(request, runtime)

    async def delete_queues_async(
        self,
        request: main_models.DeleteQueuesRequest,
    ) -> main_models.DeleteQueuesResponse:
        runtime = RuntimeOptions()
        return await self.delete_queues_with_options_async(request, runtime)

    def delete_users_with_options(
        self,
        tmp_req: main_models.DeleteUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsersResponse:
        tmp_req.validate()
        request = main_models.DeleteUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsers',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_users_with_options_async(
        self,
        tmp_req: main_models.DeleteUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsersResponse:
        tmp_req.validate()
        request = main_models.DeleteUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsers',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_users(
        self,
        request: main_models.DeleteUsersRequest,
    ) -> main_models.DeleteUsersResponse:
        runtime = RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: main_models.DeleteUsersRequest,
    ) -> main_models.DeleteUsersResponse:
        runtime = RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def describe_addon_template_with_options(
        self,
        request: main_models.DescribeAddonTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddonTemplate',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addon_template_with_options_async(
        self,
        request: main_models.DescribeAddonTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddonTemplate',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addon_template(
        self,
        request: main_models.DescribeAddonTemplateRequest,
    ) -> main_models.DescribeAddonTemplateResponse:
        runtime = RuntimeOptions()
        return self.describe_addon_template_with_options(request, runtime)

    async def describe_addon_template_async(
        self,
        request: main_models.DescribeAddonTemplateRequest,
    ) -> main_models.DescribeAddonTemplateResponse:
        runtime = RuntimeOptions()
        return await self.describe_addon_template_with_options_async(request, runtime)

    def detach_shared_storages_with_options(
        self,
        tmp_req: main_models.DetachSharedStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachSharedStoragesResponse:
        tmp_req.validate()
        request = main_models.DetachSharedStoragesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.shared_storages):
            request.shared_storages_shrink = Utils.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachSharedStorages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachSharedStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_shared_storages_with_options_async(
        self,
        tmp_req: main_models.DetachSharedStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachSharedStoragesResponse:
        tmp_req.validate()
        request = main_models.DetachSharedStoragesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.shared_storages):
            request.shared_storages_shrink = Utils.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachSharedStorages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachSharedStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_shared_storages(
        self,
        request: main_models.DetachSharedStoragesRequest,
    ) -> main_models.DetachSharedStoragesResponse:
        runtime = RuntimeOptions()
        return self.detach_shared_storages_with_options(request, runtime)

    async def detach_shared_storages_async(
        self,
        request: main_models.DetachSharedStoragesRequest,
    ) -> main_models.DetachSharedStoragesResponse:
        runtime = RuntimeOptions()
        return await self.detach_shared_storages_with_options_async(request, runtime)

    def get_addon_with_options(
        self,
        request: main_models.GetAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_id):
            query['AddonId'] = request.addon_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddon',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_with_options_async(
        self,
        request: main_models.GetAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_id):
            query['AddonId'] = request.addon_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAddon',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon(
        self,
        request: main_models.GetAddonRequest,
    ) -> main_models.GetAddonResponse:
        runtime = RuntimeOptions()
        return self.get_addon_with_options(request, runtime)

    async def get_addon_async(
        self,
        request: main_models.GetAddonRequest,
    ) -> main_models.GetAddonResponse:
        runtime = RuntimeOptions()
        return await self.get_addon_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: main_models.GetClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: main_models.GetClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: main_models.GetClusterRequest,
    ) -> main_models.GetClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_common_log_detail_with_options(
        self,
        request: main_models.GetCommonLogDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommonLogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.hidden_process):
            query['HiddenProcess'] = request.hidden_process
        if not DaraCore.is_null(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommonLogDetail',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommonLogDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_common_log_detail_with_options_async(
        self,
        request: main_models.GetCommonLogDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommonLogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.hidden_process):
            query['HiddenProcess'] = request.hidden_process
        if not DaraCore.is_null(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommonLogDetail',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommonLogDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_common_log_detail(
        self,
        request: main_models.GetCommonLogDetailRequest,
    ) -> main_models.GetCommonLogDetailResponse:
        runtime = RuntimeOptions()
        return self.get_common_log_detail_with_options(request, runtime)

    async def get_common_log_detail_async(
        self,
        request: main_models.GetCommonLogDetailRequest,
    ) -> main_models.GetCommonLogDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_common_log_detail_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: main_models.GetJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: main_models.GetJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def get_job_log_with_options(
        self,
        request: main_models.GetJobLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobLog',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_log_with_options_async(
        self,
        request: main_models.GetJobLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobLog',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_log(
        self,
        request: main_models.GetJobLogRequest,
    ) -> main_models.GetJobLogResponse:
        runtime = RuntimeOptions()
        return self.get_job_log_with_options(request, runtime)

    async def get_job_log_async(
        self,
        request: main_models.GetJobLogRequest,
    ) -> main_models.GetJobLogResponse:
        runtime = RuntimeOptions()
        return await self.get_job_log_with_options_async(request, runtime)

    def get_queue_with_options(
        self,
        request: main_models.GetQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueue',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_with_options_async(
        self,
        request: main_models.GetQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueue',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue(
        self,
        request: main_models.GetQueueRequest,
    ) -> main_models.GetQueueResponse:
        runtime = RuntimeOptions()
        return self.get_queue_with_options(request, runtime)

    async def get_queue_async(
        self,
        request: main_models.GetQueueRequest,
    ) -> main_models.GetQueueResponse:
        runtime = RuntimeOptions()
        return await self.get_queue_with_options_async(request, runtime)

    def install_addon_with_options(
        self,
        request: main_models.InstallAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.resources_spec):
            query['ResourcesSpec'] = request.resources_spec
        if not DaraCore.is_null(request.services_spec):
            query['ServicesSpec'] = request.services_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallAddon',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_addon_with_options_async(
        self,
        request: main_models.InstallAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.resources_spec):
            query['ResourcesSpec'] = request.resources_spec
        if not DaraCore.is_null(request.services_spec):
            query['ServicesSpec'] = request.services_spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallAddon',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_addon(
        self,
        request: main_models.InstallAddonRequest,
    ) -> main_models.InstallAddonResponse:
        runtime = RuntimeOptions()
        return self.install_addon_with_options(request, runtime)

    async def install_addon_async(
        self,
        request: main_models.InstallAddonRequest,
    ) -> main_models.InstallAddonResponse:
        runtime = RuntimeOptions()
        return await self.install_addon_with_options_async(request, runtime)

    def install_softwares_with_options(
        self,
        tmp_req: main_models.InstallSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallSoftwaresResponse:
        tmp_req.validate()
        request = main_models.InstallSoftwaresShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_packages):
            request.additional_packages_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_softwares_with_options_async(
        self,
        tmp_req: main_models.InstallSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallSoftwaresResponse:
        tmp_req.validate()
        request = main_models.InstallSoftwaresShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_packages):
            request.additional_packages_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_softwares(
        self,
        request: main_models.InstallSoftwaresRequest,
    ) -> main_models.InstallSoftwaresResponse:
        runtime = RuntimeOptions()
        return self.install_softwares_with_options(request, runtime)

    async def install_softwares_async(
        self,
        request: main_models.InstallSoftwaresRequest,
    ) -> main_models.InstallSoftwaresResponse:
        runtime = RuntimeOptions()
        return await self.install_softwares_with_options_async(request, runtime)

    def list_addon_templates_with_options(
        self,
        request: main_models.ListAddonTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_names):
            query['AddonNames'] = request.addon_names
        if not DaraCore.is_null(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddonTemplates',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addon_templates_with_options_async(
        self,
        request: main_models.ListAddonTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_names):
            query['AddonNames'] = request.addon_names
        if not DaraCore.is_null(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddonTemplates',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addon_templates(
        self,
        request: main_models.ListAddonTemplatesRequest,
    ) -> main_models.ListAddonTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_addon_templates_with_options(request, runtime)

    async def list_addon_templates_async(
        self,
        request: main_models.ListAddonTemplatesRequest,
    ) -> main_models.ListAddonTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_addon_templates_with_options_async(request, runtime)

    def list_addons_with_options(
        self,
        tmp_req: main_models.ListAddonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        tmp_req.validate()
        request = main_models.ListAddonsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addon_ids):
            request.addon_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.addon_ids, 'AddonIds', 'json')
        query = {}
        if not DaraCore.is_null(request.addon_ids_shrink):
            query['AddonIds'] = request.addon_ids_shrink
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        tmp_req: main_models.ListAddonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        tmp_req.validate()
        request = main_models.ListAddonsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.addon_ids):
            request.addon_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.addon_ids, 'AddonIds', 'json')
        query = {}
        if not DaraCore.is_null(request.addon_ids_shrink):
            query['AddonIds'] = request.addon_ids_shrink
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.list_addons_with_options(request, runtime)

    async def list_addons_async(
        self,
        request: main_models.ListAddonsRequest,
    ) -> main_models.ListAddonsResponse:
        runtime = RuntimeOptions()
        return await self.list_addons_with_options_async(request, runtime)

    def list_available_file_systems_with_options(
        self,
        request: main_models.ListAvailableFileSystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableFileSystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableFileSystems',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_file_systems_with_options_async(
        self,
        request: main_models.ListAvailableFileSystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableFileSystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableFileSystems',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_file_systems(
        self,
        request: main_models.ListAvailableFileSystemsRequest,
    ) -> main_models.ListAvailableFileSystemsResponse:
        runtime = RuntimeOptions()
        return self.list_available_file_systems_with_options(request, runtime)

    async def list_available_file_systems_async(
        self,
        request: main_models.ListAvailableFileSystemsRequest,
    ) -> main_models.ListAvailableFileSystemsResponse:
        runtime = RuntimeOptions()
        return await self.list_available_file_systems_with_options_async(request, runtime)

    def list_available_images_with_options(
        self,
        tmp_req: main_models.ListAvailableImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableImagesResponse:
        tmp_req.validate()
        request = main_models.ListAvailableImagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.directory_service):
            request.directory_service_shrink = Utils.array_to_string_with_specified_style(tmp_req.directory_service, 'DirectoryService', 'json')
        if not DaraCore.is_null(tmp_req.scheduler):
            request.scheduler_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler, 'Scheduler', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableImages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_images_with_options_async(
        self,
        tmp_req: main_models.ListAvailableImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableImagesResponse:
        tmp_req.validate()
        request = main_models.ListAvailableImagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.directory_service):
            request.directory_service_shrink = Utils.array_to_string_with_specified_style(tmp_req.directory_service, 'DirectoryService', 'json')
        if not DaraCore.is_null(tmp_req.scheduler):
            request.scheduler_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler, 'Scheduler', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableImages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_images(
        self,
        request: main_models.ListAvailableImagesRequest,
    ) -> main_models.ListAvailableImagesResponse:
        runtime = RuntimeOptions()
        return self.list_available_images_with_options(request, runtime)

    async def list_available_images_async(
        self,
        request: main_models.ListAvailableImagesRequest,
    ) -> main_models.ListAvailableImagesResponse:
        runtime = RuntimeOptions()
        return await self.list_available_images_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        tmp_req: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        tmp_req.validate()
        request = main_models.ListClustersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cluster_ids):
            request.cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        if not DaraCore.is_null(tmp_req.cluster_names):
            request.cluster_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_names, 'ClusterNames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not DaraCore.is_null(request.cluster_names_shrink):
            query['ClusterNames'] = request.cluster_names_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        tmp_req: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        tmp_req.validate()
        request = main_models.ListClustersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cluster_ids):
            request.cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        if not DaraCore.is_null(tmp_req.cluster_names):
            request.cluster_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_names, 'ClusterNames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not DaraCore.is_null(request.cluster_names_shrink):
            query['ClusterNames'] = request.cluster_names_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_common_logs_with_options(
        self,
        tmp_req: main_models.ListCommonLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonLogsResponse:
        tmp_req.validate()
        request = main_models.ListCommonLogsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_name):
            request.action_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_name, 'ActionName', 'json')
        query = {}
        if not DaraCore.is_null(request.action_name_shrink):
            query['ActionName'] = request.action_name_shrink
        if not DaraCore.is_null(request.action_status):
            query['ActionStatus'] = request.action_status
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.is_reverse):
            query['IsReverse'] = request.is_reverse
        if not DaraCore.is_null(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.operator_uid):
            query['OperatorUid'] = request.operator_uid
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonLogs',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_logs_with_options_async(
        self,
        tmp_req: main_models.ListCommonLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonLogsResponse:
        tmp_req.validate()
        request = main_models.ListCommonLogsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.action_name):
            request.action_name_shrink = Utils.array_to_string_with_specified_style(tmp_req.action_name, 'ActionName', 'json')
        query = {}
        if not DaraCore.is_null(request.action_name_shrink):
            query['ActionName'] = request.action_name_shrink
        if not DaraCore.is_null(request.action_status):
            query['ActionStatus'] = request.action_status
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.is_reverse):
            query['IsReverse'] = request.is_reverse
        if not DaraCore.is_null(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.operator_uid):
            query['OperatorUid'] = request.operator_uid
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonLogs',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_logs(
        self,
        request: main_models.ListCommonLogsRequest,
    ) -> main_models.ListCommonLogsResponse:
        runtime = RuntimeOptions()
        return self.list_common_logs_with_options(request, runtime)

    async def list_common_logs_async(
        self,
        request: main_models.ListCommonLogsRequest,
    ) -> main_models.ListCommonLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_common_logs_with_options_async(request, runtime)

    def list_installed_softwares_with_options(
        self,
        request: main_models.ListInstalledSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstalledSoftwaresResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstalledSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstalledSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_installed_softwares_with_options_async(
        self,
        request: main_models.ListInstalledSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstalledSoftwaresResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstalledSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstalledSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_installed_softwares(
        self,
        request: main_models.ListInstalledSoftwaresRequest,
    ) -> main_models.ListInstalledSoftwaresResponse:
        runtime = RuntimeOptions()
        return self.list_installed_softwares_with_options(request, runtime)

    async def list_installed_softwares_async(
        self,
        request: main_models.ListInstalledSoftwaresRequest,
    ) -> main_models.ListInstalledSoftwaresResponse:
        runtime = RuntimeOptions()
        return await self.list_installed_softwares_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        tmp_req: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        tmp_req.validate()
        request = main_models.ListJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_filter):
            request.job_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_filter, 'JobFilter', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_filter_shrink):
            query['JobFilter'] = request.job_filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        tmp_req: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        tmp_req.validate()
        request = main_models.ListJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_filter):
            request.job_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_filter, 'JobFilter', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_filter_shrink):
            query['JobFilter'] = request.job_filter_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hostnames):
            request.hostnames_shrink = Utils.array_to_string_with_specified_style(tmp_req.hostnames, 'Hostnames', 'json')
        if not DaraCore.is_null(tmp_req.private_ip_address):
            request.private_ip_address_shrink = Utils.array_to_string_with_specified_style(tmp_req.private_ip_address, 'PrivateIpAddress', 'json')
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.hostnames_shrink):
            query['Hostnames'] = request.hostnames_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip_address_shrink):
            query['PrivateIpAddress'] = request.private_ip_address_shrink
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.sequence):
            query['Sequence'] = request.sequence
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status_shrink):
            query['Status'] = request.status_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hostnames):
            request.hostnames_shrink = Utils.array_to_string_with_specified_style(tmp_req.hostnames, 'Hostnames', 'json')
        if not DaraCore.is_null(tmp_req.private_ip_address):
            request.private_ip_address_shrink = Utils.array_to_string_with_specified_style(tmp_req.private_ip_address, 'PrivateIpAddress', 'json')
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.hostnames_shrink):
            query['Hostnames'] = request.hostnames_shrink
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip_address_shrink):
            query['PrivateIpAddress'] = request.private_ip_address_shrink
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not DaraCore.is_null(request.sequence):
            query['Sequence'] = request.sequence
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status_shrink):
            query['Status'] = request.status_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        tmp_req: main_models.ListQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueuesResponse:
        tmp_req.validate()
        request = main_models.ListQueuesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueues',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queues_with_options_async(
        self,
        tmp_req: main_models.ListQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueuesResponse:
        tmp_req.validate()
        request = main_models.ListQueuesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue_names):
            request.queue_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueues',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queues(
        self,
        request: main_models.ListQueuesRequest,
    ) -> main_models.ListQueuesResponse:
        runtime = RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: main_models.ListQueuesRequest,
    ) -> main_models.ListQueuesResponse:
        runtime = RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.spec_code):
            query['SpecCode'] = request.spec_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.spec_code):
            query['SpecCode'] = request.spec_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_shared_storages_with_options(
        self,
        request: main_models.ListSharedStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedStoragesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedStorages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_storages_with_options_async(
        self,
        request: main_models.ListSharedStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedStoragesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedStorages',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_storages(
        self,
        request: main_models.ListSharedStoragesRequest,
    ) -> main_models.ListSharedStoragesResponse:
        runtime = RuntimeOptions()
        return self.list_shared_storages_with_options(request, runtime)

    async def list_shared_storages_async(
        self,
        request: main_models.ListSharedStoragesRequest,
    ) -> main_models.ListSharedStoragesResponse:
        runtime = RuntimeOptions()
        return await self.list_shared_storages_with_options_async(request, runtime)

    def list_softwares_with_options(
        self,
        request: main_models.ListSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSoftwaresResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_softwares_with_options_async(
        self,
        request: main_models.ListSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSoftwaresResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_softwares(
        self,
        request: main_models.ListSoftwaresRequest,
    ) -> main_models.ListSoftwaresResponse:
        runtime = RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    async def list_softwares_async(
        self,
        request: main_models.ListSoftwaresRequest,
    ) -> main_models.ListSoftwaresResponse:
        runtime = RuntimeOptions()
        return await self.list_softwares_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def stop_jobs_with_options(
        self,
        tmp_req: main_models.StopJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopJobsResponse:
        tmp_req.validate()
        request = main_models.StopJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopJobs',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_jobs_with_options_async(
        self,
        tmp_req: main_models.StopJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopJobsResponse:
        tmp_req.validate()
        request = main_models.StopJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_ids):
            request.job_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopJobs',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_jobs(
        self,
        request: main_models.StopJobsRequest,
    ) -> main_models.StopJobsResponse:
        runtime = RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    async def stop_jobs_async(
        self,
        request: main_models.StopJobsRequest,
    ) -> main_models.StopJobsResponse:
        runtime = RuntimeOptions()
        return await self.stop_jobs_with_options_async(request, runtime)

    def un_install_addon_with_options(
        self,
        request: main_models.UnInstallAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnInstallAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_id):
            query['AddonId'] = request.addon_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnInstallAddon',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnInstallAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_install_addon_with_options_async(
        self,
        request: main_models.UnInstallAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnInstallAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_id):
            query['AddonId'] = request.addon_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnInstallAddon',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnInstallAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_install_addon(
        self,
        request: main_models.UnInstallAddonRequest,
    ) -> main_models.UnInstallAddonResponse:
        runtime = RuntimeOptions()
        return self.un_install_addon_with_options(request, runtime)

    async def un_install_addon_async(
        self,
        request: main_models.UnInstallAddonRequest,
    ) -> main_models.UnInstallAddonResponse:
        runtime = RuntimeOptions()
        return await self.un_install_addon_with_options_async(request, runtime)

    def uninstall_softwares_with_options(
        self,
        tmp_req: main_models.UninstallSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallSoftwaresResponse:
        tmp_req.validate()
        request = main_models.UninstallSoftwaresShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_packages):
            request.additional_packages_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_softwares_with_options_async(
        self,
        tmp_req: main_models.UninstallSoftwaresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallSoftwaresResponse:
        tmp_req.validate()
        request = main_models.UninstallSoftwaresShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.additional_packages):
            request.additional_packages_shrink = Utils.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallSoftwares',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_softwares(
        self,
        request: main_models.UninstallSoftwaresRequest,
    ) -> main_models.UninstallSoftwaresResponse:
        runtime = RuntimeOptions()
        return self.uninstall_softwares_with_options(request, runtime)

    async def uninstall_softwares_async(
        self,
        request: main_models.UninstallSoftwaresRequest,
    ) -> main_models.UninstallSoftwaresResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_softwares_with_options_async(request, runtime)

    def update_cluster_with_options(
        self,
        tmp_req: main_models.UpdateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterResponse:
        tmp_req.validate()
        request = main_models.UpdateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not DaraCore.is_null(tmp_req.monitor_spec):
            request.monitor_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_spec, 'MonitorSpec', 'json')
        if not DaraCore.is_null(tmp_req.scheduler_spec):
            request.scheduler_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler_spec, 'SchedulerSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not DaraCore.is_null(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.enable_scale_in):
            query['EnableScaleIn'] = request.enable_scale_in
        if not DaraCore.is_null(request.enable_scale_out):
            query['EnableScaleOut'] = request.enable_scale_out
        if not DaraCore.is_null(request.grow_interval):
            query['GrowInterval'] = request.grow_interval
        if not DaraCore.is_null(request.idle_interval):
            query['IdleInterval'] = request.idle_interval
        if not DaraCore.is_null(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not DaraCore.is_null(request.max_count):
            query['MaxCount'] = request.max_count
        if not DaraCore.is_null(request.monitor_spec_shrink):
            query['MonitorSpec'] = request.monitor_spec_shrink
        if not DaraCore.is_null(request.scheduler_spec_shrink):
            query['SchedulerSpec'] = request.scheduler_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        tmp_req: main_models.UpdateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterResponse:
        tmp_req.validate()
        request = main_models.UpdateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not DaraCore.is_null(tmp_req.monitor_spec):
            request.monitor_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_spec, 'MonitorSpec', 'json')
        if not DaraCore.is_null(tmp_req.scheduler_spec):
            request.scheduler_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.scheduler_spec, 'SchedulerSpec', 'json')
        query = {}
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not DaraCore.is_null(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.enable_scale_in):
            query['EnableScaleIn'] = request.enable_scale_in
        if not DaraCore.is_null(request.enable_scale_out):
            query['EnableScaleOut'] = request.enable_scale_out
        if not DaraCore.is_null(request.grow_interval):
            query['GrowInterval'] = request.grow_interval
        if not DaraCore.is_null(request.idle_interval):
            query['IdleInterval'] = request.idle_interval
        if not DaraCore.is_null(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not DaraCore.is_null(request.max_count):
            query['MaxCount'] = request.max_count
        if not DaraCore.is_null(request.monitor_spec_shrink):
            query['MonitorSpec'] = request.monitor_spec_shrink
        if not DaraCore.is_null(request.scheduler_spec_shrink):
            query['SchedulerSpec'] = request.scheduler_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCluster',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster(
        self,
        request: main_models.UpdateClusterRequest,
    ) -> main_models.UpdateClusterResponse:
        runtime = RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    async def update_cluster_async(
        self,
        request: main_models.UpdateClusterRequest,
    ) -> main_models.UpdateClusterResponse:
        runtime = RuntimeOptions()
        return await self.update_cluster_with_options_async(request, runtime)

    def update_nodes_with_options(
        self,
        tmp_req: main_models.UpdateNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodesResponse:
        tmp_req.validate()
        request = main_models.UpdateNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instances):
            request.instances_shrink = Utils.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instances_shrink):
            query['Instances'] = request.instances_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nodes_with_options_async(
        self,
        tmp_req: main_models.UpdateNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodesResponse:
        tmp_req.validate()
        request = main_models.UpdateNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instances):
            request.instances_shrink = Utils.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instances_shrink):
            query['Instances'] = request.instances_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodes',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nodes(
        self,
        request: main_models.UpdateNodesRequest,
    ) -> main_models.UpdateNodesResponse:
        runtime = RuntimeOptions()
        return self.update_nodes_with_options(request, runtime)

    async def update_nodes_async(
        self,
        request: main_models.UpdateNodesRequest,
    ) -> main_models.UpdateNodesResponse:
        runtime = RuntimeOptions()
        return await self.update_nodes_with_options_async(request, runtime)

    def update_queue_with_options(
        self,
        tmp_req: main_models.UpdateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQueueResponse:
        tmp_req.validate()
        request = main_models.UpdateQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue):
            request.queue_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQueue',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_queue_with_options_async(
        self,
        tmp_req: main_models.UpdateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQueueResponse:
        tmp_req.validate()
        request = main_models.UpdateQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.queue):
            request.queue_shrink = Utils.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQueue',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_queue(
        self,
        request: main_models.UpdateQueueRequest,
    ) -> main_models.UpdateQueueResponse:
        runtime = RuntimeOptions()
        return self.update_queue_with_options(request, runtime)

    async def update_queue_async(
        self,
        request: main_models.UpdateQueueRequest,
    ) -> main_models.UpdateQueueResponse:
        runtime = RuntimeOptions()
        return await self.update_queue_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2024-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
