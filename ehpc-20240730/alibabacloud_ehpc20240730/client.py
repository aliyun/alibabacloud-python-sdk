# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ehpc20240730 import models as ehpc20240730_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_nodes_with_options(
        self,
        tmp_req: ehpc20240730_models.AttachNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.AttachNodesResponse:
        """
        @summary Adds Elastic Compute Service (ECS) instances as compute nodes to Elastic High Performance Computing (E-HPC) clusters.
        
        @description The ECS instances must meet the following requirements:
        The ECS instances do not belong to any E-HPC cluster.
        The ECS instances reside in the same virtual private cloud (VPC) as the cluster.
        The ECS instances are in the Stopped state.
        Take of the following limits:
        You can specify multiple instance IDs to add them at a time. However, the instances must be of the same type.
        When an instance is added to the cluster, [the system disk is reset](https://help.aliyun.com/zh/ecs/user-guide/re-initialize-a-system-disk) by using the image specified by the input parameters.
        If the instance has data disks, they are not automatically created and mounted after the instance is added.
        The hostname of the instance remains the same. Therefore, you must ensure that the hostname of the instance to be added is different from the hostname of an existing node in the cluster.
        
        @param tmp_req: AttachNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.AttachNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.compute_node):
            request.compute_node_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.AttachNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_nodes_with_options_async(
        self,
        tmp_req: ehpc20240730_models.AttachNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.AttachNodesResponse:
        """
        @summary Adds Elastic Compute Service (ECS) instances as compute nodes to Elastic High Performance Computing (E-HPC) clusters.
        
        @description The ECS instances must meet the following requirements:
        The ECS instances do not belong to any E-HPC cluster.
        The ECS instances reside in the same virtual private cloud (VPC) as the cluster.
        The ECS instances are in the Stopped state.
        Take of the following limits:
        You can specify multiple instance IDs to add them at a time. However, the instances must be of the same type.
        When an instance is added to the cluster, [the system disk is reset](https://help.aliyun.com/zh/ecs/user-guide/re-initialize-a-system-disk) by using the image specified by the input parameters.
        If the instance has data disks, they are not automatically created and mounted after the instance is added.
        The hostname of the instance remains the same. Therefore, you must ensure that the hostname of the instance to be added is different from the hostname of an existing node in the cluster.
        
        @param tmp_req: AttachNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.AttachNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.compute_node):
            request.compute_node_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.AttachNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_nodes(
        self,
        request: ehpc20240730_models.AttachNodesRequest,
    ) -> ehpc20240730_models.AttachNodesResponse:
        """
        @summary Adds Elastic Compute Service (ECS) instances as compute nodes to Elastic High Performance Computing (E-HPC) clusters.
        
        @description The ECS instances must meet the following requirements:
        The ECS instances do not belong to any E-HPC cluster.
        The ECS instances reside in the same virtual private cloud (VPC) as the cluster.
        The ECS instances are in the Stopped state.
        Take of the following limits:
        You can specify multiple instance IDs to add them at a time. However, the instances must be of the same type.
        When an instance is added to the cluster, [the system disk is reset](https://help.aliyun.com/zh/ecs/user-guide/re-initialize-a-system-disk) by using the image specified by the input parameters.
        If the instance has data disks, they are not automatically created and mounted after the instance is added.
        The hostname of the instance remains the same. Therefore, you must ensure that the hostname of the instance to be added is different from the hostname of an existing node in the cluster.
        
        @param request: AttachNodesRequest
        @return: AttachNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_nodes_with_options(request, runtime)

    async def attach_nodes_async(
        self,
        request: ehpc20240730_models.AttachNodesRequest,
    ) -> ehpc20240730_models.AttachNodesResponse:
        """
        @summary Adds Elastic Compute Service (ECS) instances as compute nodes to Elastic High Performance Computing (E-HPC) clusters.
        
        @description The ECS instances must meet the following requirements:
        The ECS instances do not belong to any E-HPC cluster.
        The ECS instances reside in the same virtual private cloud (VPC) as the cluster.
        The ECS instances are in the Stopped state.
        Take of the following limits:
        You can specify multiple instance IDs to add them at a time. However, the instances must be of the same type.
        When an instance is added to the cluster, [the system disk is reset](https://help.aliyun.com/zh/ecs/user-guide/re-initialize-a-system-disk) by using the image specified by the input parameters.
        If the instance has data disks, they are not automatically created and mounted after the instance is added.
        The hostname of the instance remains the same. Therefore, you must ensure that the hostname of the instance to be added is different from the hostname of an existing node in the cluster.
        
        @param request: AttachNodesRequest
        @return: AttachNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_nodes_with_options_async(request, runtime)

    def attach_shared_storages_with_options(
        self,
        tmp_req: ehpc20240730_models.AttachSharedStoragesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.AttachSharedStoragesResponse:
        """
        @summary Attaches shared storage to an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        When you call this operation, take note of the following items:
        The file system that you want to attach must be created in advance in the same virtual private cloud (VPC) as the destination cluster. For more information, see [Create a file system](https://help.aliyun.com/document_detail/27530.html) and [Manage mount targets](https://help.aliyun.com/document_detail/27531.html).
        E-HPC clusters support Apsara File Storage NAS file systems.
        
        @param tmp_req: AttachSharedStoragesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachSharedStoragesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.AttachSharedStoragesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shared_storages):
            request.shared_storages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachSharedStorages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.AttachSharedStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_shared_storages_with_options_async(
        self,
        tmp_req: ehpc20240730_models.AttachSharedStoragesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.AttachSharedStoragesResponse:
        """
        @summary Attaches shared storage to an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        When you call this operation, take note of the following items:
        The file system that you want to attach must be created in advance in the same virtual private cloud (VPC) as the destination cluster. For more information, see [Create a file system](https://help.aliyun.com/document_detail/27530.html) and [Manage mount targets](https://help.aliyun.com/document_detail/27531.html).
        E-HPC clusters support Apsara File Storage NAS file systems.
        
        @param tmp_req: AttachSharedStoragesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachSharedStoragesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.AttachSharedStoragesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shared_storages):
            request.shared_storages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachSharedStorages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.AttachSharedStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_shared_storages(
        self,
        request: ehpc20240730_models.AttachSharedStoragesRequest,
    ) -> ehpc20240730_models.AttachSharedStoragesResponse:
        """
        @summary Attaches shared storage to an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        When you call this operation, take note of the following items:
        The file system that you want to attach must be created in advance in the same virtual private cloud (VPC) as the destination cluster. For more information, see [Create a file system](https://help.aliyun.com/document_detail/27530.html) and [Manage mount targets](https://help.aliyun.com/document_detail/27531.html).
        E-HPC clusters support Apsara File Storage NAS file systems.
        
        @param request: AttachSharedStoragesRequest
        @return: AttachSharedStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_shared_storages_with_options(request, runtime)

    async def attach_shared_storages_async(
        self,
        request: ehpc20240730_models.AttachSharedStoragesRequest,
    ) -> ehpc20240730_models.AttachSharedStoragesResponse:
        """
        @summary Attaches shared storage to an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        When you call this operation, take note of the following items:
        The file system that you want to attach must be created in advance in the same virtual private cloud (VPC) as the destination cluster. For more information, see [Create a file system](https://help.aliyun.com/document_detail/27530.html) and [Manage mount targets](https://help.aliyun.com/document_detail/27531.html).
        E-HPC clusters support Apsara File Storage NAS file systems.
        
        @param request: AttachSharedStoragesRequest
        @return: AttachSharedStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_shared_storages_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: ehpc20240730_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you call this operation, make sure that you are familiar with the billing and pricing of E-HPC. For more information, see [Overview](https://help.aliyun.com/document_detail/2842985.html).
        
        @param tmp_req: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_packages):
            request.additional_packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        if not UtilClient.is_unset(tmp_req.addons):
            request.addons_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addons, 'Addons', 'json')
        if not UtilClient.is_unset(tmp_req.cluster_credentials):
            request.cluster_credentials_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_credentials, 'ClusterCredentials', 'json')
        if not UtilClient.is_unset(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not UtilClient.is_unset(tmp_req.manager):
            request.manager_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.manager, 'Manager', 'json')
        if not UtilClient.is_unset(tmp_req.queues):
            request.queues_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queues, 'Queues', 'json')
        if not UtilClient.is_unset(tmp_req.shared_storages):
            request.shared_storages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.additional_packages_shrink):
            query['AdditionalPackages'] = request.additional_packages_shrink
        if not UtilClient.is_unset(request.addons_shrink):
            query['Addons'] = request.addons_shrink
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not UtilClient.is_unset(request.cluster_credentials_shrink):
            query['ClusterCredentials'] = request.cluster_credentials_shrink
        if not UtilClient.is_unset(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not UtilClient.is_unset(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_vswitch_id):
            query['ClusterVSwitchId'] = request.cluster_vswitch_id
        if not UtilClient.is_unset(request.cluster_vpc_id):
            query['ClusterVpcId'] = request.cluster_vpc_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            query['IsEnterpriseSecurityGroup'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.manager_shrink):
            query['Manager'] = request.manager_shrink
        if not UtilClient.is_unset(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not UtilClient.is_unset(request.max_count):
            query['MaxCount'] = request.max_count
        if not UtilClient.is_unset(request.queues_shrink):
            query['Queues'] = request.queues_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: ehpc20240730_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you call this operation, make sure that you are familiar with the billing and pricing of E-HPC. For more information, see [Overview](https://help.aliyun.com/document_detail/2842985.html).
        
        @param tmp_req: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_packages):
            request.additional_packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        if not UtilClient.is_unset(tmp_req.addons):
            request.addons_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addons, 'Addons', 'json')
        if not UtilClient.is_unset(tmp_req.cluster_credentials):
            request.cluster_credentials_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_credentials, 'ClusterCredentials', 'json')
        if not UtilClient.is_unset(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not UtilClient.is_unset(tmp_req.manager):
            request.manager_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.manager, 'Manager', 'json')
        if not UtilClient.is_unset(tmp_req.queues):
            request.queues_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queues, 'Queues', 'json')
        if not UtilClient.is_unset(tmp_req.shared_storages):
            request.shared_storages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.additional_packages_shrink):
            query['AdditionalPackages'] = request.additional_packages_shrink
        if not UtilClient.is_unset(request.addons_shrink):
            query['Addons'] = request.addons_shrink
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not UtilClient.is_unset(request.cluster_credentials_shrink):
            query['ClusterCredentials'] = request.cluster_credentials_shrink
        if not UtilClient.is_unset(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not UtilClient.is_unset(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not UtilClient.is_unset(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_vswitch_id):
            query['ClusterVSwitchId'] = request.cluster_vswitch_id
        if not UtilClient.is_unset(request.cluster_vpc_id):
            query['ClusterVpcId'] = request.cluster_vpc_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            query['IsEnterpriseSecurityGroup'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.manager_shrink):
            query['Manager'] = request.manager_shrink
        if not UtilClient.is_unset(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not UtilClient.is_unset(request.max_count):
            query['MaxCount'] = request.max_count
        if not UtilClient.is_unset(request.queues_shrink):
            query['Queues'] = request.queues_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: ehpc20240730_models.CreateClusterRequest,
    ) -> ehpc20240730_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you call this operation, make sure that you are familiar with the billing and pricing of E-HPC. For more information, see [Overview](https://help.aliyun.com/document_detail/2842985.html).
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: ehpc20240730_models.CreateClusterRequest,
    ) -> ehpc20240730_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you call this operation, make sure that you are familiar with the billing and pricing of E-HPC. For more information, see [Overview](https://help.aliyun.com/document_detail/2842985.html).
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp_req: ehpc20240730_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateJobResponse:
        """
        @summary Creates a job for a cluster.
        
        @description Before you call this operation, make sure that you understand the billing and [pricing](https://www.aliyun.com/price/product#/ecs/detail) of E-HPC.
        
        @param tmp_req: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_spec):
            request.job_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        tmp_req: ehpc20240730_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateJobResponse:
        """
        @summary Creates a job for a cluster.
        
        @description Before you call this operation, make sure that you understand the billing and [pricing](https://www.aliyun.com/price/product#/ecs/detail) of E-HPC.
        
        @param tmp_req: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_spec):
            request.job_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: ehpc20240730_models.CreateJobRequest,
    ) -> ehpc20240730_models.CreateJobResponse:
        """
        @summary Creates a job for a cluster.
        
        @description Before you call this operation, make sure that you understand the billing and [pricing](https://www.aliyun.com/price/product#/ecs/detail) of E-HPC.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: ehpc20240730_models.CreateJobRequest,
    ) -> ehpc20240730_models.CreateJobResponse:
        """
        @summary Creates a job for a cluster.
        
        @description Before you call this operation, make sure that you understand the billing and [pricing](https://www.aliyun.com/price/product#/ecs/detail) of E-HPC.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_nodes_with_options(
        self,
        tmp_req: ehpc20240730_models.CreateNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateNodesResponse:
        """
        @summary Creates compute nodes for an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)
        
        @param tmp_req: CreateNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.compute_node):
            request.compute_node_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.hpcinter_connect):
            query['HPCInterConnect'] = request.hpcinter_connect
        if not UtilClient.is_unset(request.hostname_prefix):
            query['HostnamePrefix'] = request.hostname_prefix
        if not UtilClient.is_unset(request.hostname_suffix):
            query['HostnameSuffix'] = request.hostname_suffix
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.reserved_node_pool_id):
            query['ReservedNodePoolId'] = request.reserved_node_pool_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nodes_with_options_async(
        self,
        tmp_req: ehpc20240730_models.CreateNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateNodesResponse:
        """
        @summary Creates compute nodes for an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)
        
        @param tmp_req: CreateNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.compute_node):
            request.compute_node_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compute_node, 'ComputeNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.compute_node_shrink):
            query['ComputeNode'] = request.compute_node_shrink
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.hpcinter_connect):
            query['HPCInterConnect'] = request.hpcinter_connect
        if not UtilClient.is_unset(request.hostname_prefix):
            query['HostnamePrefix'] = request.hostname_prefix
        if not UtilClient.is_unset(request.hostname_suffix):
            query['HostnameSuffix'] = request.hostname_suffix
        if not UtilClient.is_unset(request.keep_alive):
            query['KeepAlive'] = request.keep_alive
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.ram_role):
            query['RamRole'] = request.ram_role
        if not UtilClient.is_unset(request.reserved_node_pool_id):
            query['ReservedNodePoolId'] = request.reserved_node_pool_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nodes(
        self,
        request: ehpc20240730_models.CreateNodesRequest,
    ) -> ehpc20240730_models.CreateNodesResponse:
        """
        @summary Creates compute nodes for an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)
        
        @param request: CreateNodesRequest
        @return: CreateNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_nodes_with_options(request, runtime)

    async def create_nodes_async(
        self,
        request: ehpc20240730_models.CreateNodesRequest,
    ) -> ehpc20240730_models.CreateNodesResponse:
        """
        @summary Creates compute nodes for an Elastic High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)
        
        @param request: CreateNodesRequest
        @return: CreateNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_nodes_with_options_async(request, runtime)

    def create_queue_with_options(
        self,
        tmp_req: ehpc20240730_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateQueueResponse:
        """
        @summary Creates a queue for an Enterprise High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue):
            request.queue_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        tmp_req: ehpc20240730_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateQueueResponse:
        """
        @summary Creates a queue for an Enterprise High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue):
            request.queue_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_queue(
        self,
        request: ehpc20240730_models.CreateQueueRequest,
    ) -> ehpc20240730_models.CreateQueueResponse:
        """
        @summary Creates a queue for an Enterprise High Performance Computing (E-HPC) cluster.
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: ehpc20240730_models.CreateQueueRequest,
    ) -> ehpc20240730_models.CreateQueueResponse:
        """
        @summary Creates a queue for an Enterprise High Performance Computing (E-HPC) cluster.
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_users_with_options(
        self,
        tmp_req: ehpc20240730_models.CreateUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateUsersResponse:
        """
        @summary Adds users to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: CreateUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUsers',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_users_with_options_async(
        self,
        tmp_req: ehpc20240730_models.CreateUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.CreateUsersResponse:
        """
        @summary Adds users to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: CreateUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.CreateUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUsers',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.CreateUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_users(
        self,
        request: ehpc20240730_models.CreateUsersRequest,
    ) -> ehpc20240730_models.CreateUsersResponse:
        """
        @summary Adds users to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: CreateUsersRequest
        @return: CreateUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_users_with_options(request, runtime)

    async def create_users_async(
        self,
        request: ehpc20240730_models.CreateUsersRequest,
    ) -> ehpc20240730_models.CreateUsersResponse:
        """
        @summary Adds users to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: CreateUsersRequest
        @return: CreateUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_users_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: ehpc20240730_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteClusterResponse:
        """
        @summary Releases an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Make sure that data of the cluster to be deleted is backed up before you call this operation.
        > After a cluster is released, you cannot restore the data stored in the cluster. Exercise caution when you release a cluster.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: ehpc20240730_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteClusterResponse:
        """
        @summary Releases an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Make sure that data of the cluster to be deleted is backed up before you call this operation.
        > After a cluster is released, you cannot restore the data stored in the cluster. Exercise caution when you release a cluster.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: ehpc20240730_models.DeleteClusterRequest,
    ) -> ehpc20240730_models.DeleteClusterResponse:
        """
        @summary Releases an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Make sure that data of the cluster to be deleted is backed up before you call this operation.
        > After a cluster is released, you cannot restore the data stored in the cluster. Exercise caution when you release a cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: ehpc20240730_models.DeleteClusterRequest,
    ) -> ehpc20240730_models.DeleteClusterResponse:
        """
        @summary Releases an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Make sure that data of the cluster to be deleted is backed up before you call this operation.
        > After a cluster is released, you cannot restore the data stored in the cluster. Exercise caution when you release a cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_nodes_with_options(
        self,
        tmp_req: ehpc20240730_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteNodesResponse:
        """
        @summary Deletes compute nodes from an Enterprise High Performance Computing (E-HPC) cluster at a time.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param tmp_req: DeleteNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DeleteNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nodes_with_options_async(
        self,
        tmp_req: ehpc20240730_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteNodesResponse:
        """
        @summary Deletes compute nodes from an Enterprise High Performance Computing (E-HPC) cluster at a time.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param tmp_req: DeleteNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DeleteNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nodes(
        self,
        request: ehpc20240730_models.DeleteNodesRequest,
    ) -> ehpc20240730_models.DeleteNodesResponse:
        """
        @summary Deletes compute nodes from an Enterprise High Performance Computing (E-HPC) cluster at a time.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: DeleteNodesRequest
        @return: DeleteNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    async def delete_nodes_async(
        self,
        request: ehpc20240730_models.DeleteNodesRequest,
    ) -> ehpc20240730_models.DeleteNodesResponse:
        """
        @summary Deletes compute nodes from an Enterprise High Performance Computing (E-HPC) cluster at a time.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: DeleteNodesRequest
        @return: DeleteNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_nodes_with_options_async(request, runtime)

    def delete_queues_with_options(
        self,
        tmp_req: ehpc20240730_models.DeleteQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteQueuesResponse:
        """
        @summary Deletes queues from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a queue, you must delete all compute nodes in the queue.
        
        @param tmp_req: DeleteQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueuesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DeleteQueuesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueues',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queues_with_options_async(
        self,
        tmp_req: ehpc20240730_models.DeleteQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteQueuesResponse:
        """
        @summary Deletes queues from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a queue, you must delete all compute nodes in the queue.
        
        @param tmp_req: DeleteQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueuesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DeleteQueuesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueues',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_queues(
        self,
        request: ehpc20240730_models.DeleteQueuesRequest,
    ) -> ehpc20240730_models.DeleteQueuesResponse:
        """
        @summary Deletes queues from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a queue, you must delete all compute nodes in the queue.
        
        @param request: DeleteQueuesRequest
        @return: DeleteQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_queues_with_options(request, runtime)

    async def delete_queues_async(
        self,
        request: ehpc20240730_models.DeleteQueuesRequest,
    ) -> ehpc20240730_models.DeleteQueuesResponse:
        """
        @summary Deletes queues from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a queue, you must delete all compute nodes in the queue.
        
        @param request: DeleteQueuesRequest
        @return: DeleteQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_queues_with_options_async(request, runtime)

    def delete_users_with_options(
        self,
        tmp_req: ehpc20240730_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @param tmp_req: DeleteUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DeleteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUsers',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_users_with_options_async(
        self,
        tmp_req: ehpc20240730_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @param tmp_req: DeleteUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DeleteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUsers',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DeleteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_users(
        self,
        request: ehpc20240730_models.DeleteUsersRequest,
    ) -> ehpc20240730_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @param request: DeleteUsersRequest
        @return: DeleteUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: ehpc20240730_models.DeleteUsersRequest,
    ) -> ehpc20240730_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @param request: DeleteUsersRequest
        @return: DeleteUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def describe_addon_template_with_options(
        self,
        request: ehpc20240730_models.DescribeAddonTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DescribeAddonTemplateResponse:
        """
        @summary Queries the details of an addon template.
        
        @param request: DescribeAddonTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddonTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddonTemplate',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DescribeAddonTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addon_template_with_options_async(
        self,
        request: ehpc20240730_models.DescribeAddonTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DescribeAddonTemplateResponse:
        """
        @summary Queries the details of an addon template.
        
        @param request: DescribeAddonTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddonTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddonTemplate',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DescribeAddonTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addon_template(
        self,
        request: ehpc20240730_models.DescribeAddonTemplateRequest,
    ) -> ehpc20240730_models.DescribeAddonTemplateResponse:
        """
        @summary Queries the details of an addon template.
        
        @param request: DescribeAddonTemplateRequest
        @return: DescribeAddonTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_addon_template_with_options(request, runtime)

    async def describe_addon_template_async(
        self,
        request: ehpc20240730_models.DescribeAddonTemplateRequest,
    ) -> ehpc20240730_models.DescribeAddonTemplateResponse:
        """
        @summary Queries the details of an addon template.
        
        @param request: DescribeAddonTemplateRequest
        @return: DescribeAddonTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_addon_template_with_options_async(request, runtime)

    def detach_shared_storages_with_options(
        self,
        tmp_req: ehpc20240730_models.DetachSharedStoragesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DetachSharedStoragesResponse:
        """
        @summary Unmounts shared storage from the mount directory of a cluster.
        
        @param tmp_req: DetachSharedStoragesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachSharedStoragesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DetachSharedStoragesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shared_storages):
            request.shared_storages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachSharedStorages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DetachSharedStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_shared_storages_with_options_async(
        self,
        tmp_req: ehpc20240730_models.DetachSharedStoragesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.DetachSharedStoragesResponse:
        """
        @summary Unmounts shared storage from the mount directory of a cluster.
        
        @param tmp_req: DetachSharedStoragesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachSharedStoragesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.DetachSharedStoragesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shared_storages):
            request.shared_storages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared_storages, 'SharedStorages', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.shared_storages_shrink):
            query['SharedStorages'] = request.shared_storages_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachSharedStorages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.DetachSharedStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_shared_storages(
        self,
        request: ehpc20240730_models.DetachSharedStoragesRequest,
    ) -> ehpc20240730_models.DetachSharedStoragesResponse:
        """
        @summary Unmounts shared storage from the mount directory of a cluster.
        
        @param request: DetachSharedStoragesRequest
        @return: DetachSharedStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_shared_storages_with_options(request, runtime)

    async def detach_shared_storages_async(
        self,
        request: ehpc20240730_models.DetachSharedStoragesRequest,
    ) -> ehpc20240730_models.DetachSharedStoragesResponse:
        """
        @summary Unmounts shared storage from the mount directory of a cluster.
        
        @param request: DetachSharedStoragesRequest
        @return: DetachSharedStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_shared_storages_with_options_async(request, runtime)

    def get_addon_with_options(
        self,
        request: ehpc20240730_models.GetAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetAddonResponse:
        """
        @summary Queries the details of an installed addon.
        
        @param request: GetAddonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_id):
            query['AddonId'] = request.addon_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddon',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_addon_with_options_async(
        self,
        request: ehpc20240730_models.GetAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetAddonResponse:
        """
        @summary Queries the details of an installed addon.
        
        @param request: GetAddonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_id):
            query['AddonId'] = request.addon_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAddon',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_addon(
        self,
        request: ehpc20240730_models.GetAddonRequest,
    ) -> ehpc20240730_models.GetAddonResponse:
        """
        @summary Queries the details of an installed addon.
        
        @param request: GetAddonRequest
        @return: GetAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_addon_with_options(request, runtime)

    async def get_addon_async(
        self,
        request: ehpc20240730_models.GetAddonRequest,
    ) -> ehpc20240730_models.GetAddonResponse:
        """
        @summary Queries the details of an installed addon.
        
        @param request: GetAddonRequest
        @return: GetAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_addon_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: ehpc20240730_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetClusterResponse:
        """
        @summary Queries information about an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: ehpc20240730_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetClusterResponse:
        """
        @summary Queries information about an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: ehpc20240730_models.GetClusterRequest,
    ) -> ehpc20240730_models.GetClusterResponse:
        """
        @summary Queries information about an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: ehpc20240730_models.GetClusterRequest,
    ) -> ehpc20240730_models.GetClusterResponse:
        """
        @summary Queries information about an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_common_log_detail_with_options(
        self,
        request: ehpc20240730_models.GetCommonLogDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetCommonLogDetailResponse:
        """
        @summary Query logs based on a request ID. Logs for specific actions can be queried thanks to an Action-Stage-Method three-layer log splitting structure.
        
        @param request: GetCommonLogDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommonLogDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.hidden_process):
            query['HiddenProcess'] = request.hidden_process
        if not UtilClient.is_unset(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommonLogDetail',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetCommonLogDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_common_log_detail_with_options_async(
        self,
        request: ehpc20240730_models.GetCommonLogDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetCommonLogDetailResponse:
        """
        @summary Query logs based on a request ID. Logs for specific actions can be queried thanks to an Action-Stage-Method three-layer log splitting structure.
        
        @param request: GetCommonLogDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommonLogDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.hidden_process):
            query['HiddenProcess'] = request.hidden_process
        if not UtilClient.is_unset(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommonLogDetail',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetCommonLogDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_common_log_detail(
        self,
        request: ehpc20240730_models.GetCommonLogDetailRequest,
    ) -> ehpc20240730_models.GetCommonLogDetailResponse:
        """
        @summary Query logs based on a request ID. Logs for specific actions can be queried thanks to an Action-Stage-Method three-layer log splitting structure.
        
        @param request: GetCommonLogDetailRequest
        @return: GetCommonLogDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_common_log_detail_with_options(request, runtime)

    async def get_common_log_detail_async(
        self,
        request: ehpc20240730_models.GetCommonLogDetailRequest,
    ) -> ehpc20240730_models.GetCommonLogDetailResponse:
        """
        @summary Query logs based on a request ID. Logs for specific actions can be queried thanks to an Action-Stage-Method three-layer log splitting structure.
        
        @param request: GetCommonLogDetailRequest
        @return: GetCommonLogDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_common_log_detail_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: ehpc20240730_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @param request: GetJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: ehpc20240730_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @param request: GetJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        request: ehpc20240730_models.GetJobRequest,
    ) -> ehpc20240730_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: ehpc20240730_models.GetJobRequest,
    ) -> ehpc20240730_models.GetJobResponse:
        """
        @summary Obtains the details of a job.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def get_job_log_with_options(
        self,
        request: ehpc20240730_models.GetJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetJobLogResponse:
        """
        @summary Queries the output logs of a job, including standard output logs and error output logs.
        
        @description ## [](#)Usage notes
        Currently, only Slurm and PBS Pro schedulers for Standard Edition clusters are supported.
        
        @param request: GetJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobLog',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_log_with_options_async(
        self,
        request: ehpc20240730_models.GetJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetJobLogResponse:
        """
        @summary Queries the output logs of a job, including standard output logs and error output logs.
        
        @description ## [](#)Usage notes
        Currently, only Slurm and PBS Pro schedulers for Standard Edition clusters are supported.
        
        @param request: GetJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobLog',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_log(
        self,
        request: ehpc20240730_models.GetJobLogRequest,
    ) -> ehpc20240730_models.GetJobLogResponse:
        """
        @summary Queries the output logs of a job, including standard output logs and error output logs.
        
        @description ## [](#)Usage notes
        Currently, only Slurm and PBS Pro schedulers for Standard Edition clusters are supported.
        
        @param request: GetJobLogRequest
        @return: GetJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_log_with_options(request, runtime)

    async def get_job_log_async(
        self,
        request: ehpc20240730_models.GetJobLogRequest,
    ) -> ehpc20240730_models.GetJobLogResponse:
        """
        @summary Queries the output logs of a job, including standard output logs and error output logs.
        
        @description ## [](#)Usage notes
        Currently, only Slurm and PBS Pro schedulers for Standard Edition clusters are supported.
        
        @param request: GetJobLogRequest
        @return: GetJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_log_with_options_async(request, runtime)

    def get_queue_with_options(
        self,
        request: ehpc20240730_models.GetQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetQueueResponse:
        """
        @summary Queries the details of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueue',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_with_options_async(
        self,
        request: ehpc20240730_models.GetQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.GetQueueResponse:
        """
        @summary Queries the details of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueue',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.GetQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue(
        self,
        request: ehpc20240730_models.GetQueueRequest,
    ) -> ehpc20240730_models.GetQueueResponse:
        """
        @summary Queries the details of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetQueueRequest
        @return: GetQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_queue_with_options(request, runtime)

    async def get_queue_async(
        self,
        request: ehpc20240730_models.GetQueueRequest,
    ) -> ehpc20240730_models.GetQueueResponse:
        """
        @summary Queries the details of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: GetQueueRequest
        @return: GetQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_with_options_async(request, runtime)

    def install_addon_with_options(
        self,
        request: ehpc20240730_models.InstallAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.InstallAddonResponse:
        """
        @summary Installs an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into two types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: InstallAddonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resources_spec):
            query['ResourcesSpec'] = request.resources_spec
        if not UtilClient.is_unset(request.services_spec):
            query['ServicesSpec'] = request.services_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallAddon',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.InstallAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_addon_with_options_async(
        self,
        request: ehpc20240730_models.InstallAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.InstallAddonResponse:
        """
        @summary Installs an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into two types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: InstallAddonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resources_spec):
            query['ResourcesSpec'] = request.resources_spec
        if not UtilClient.is_unset(request.services_spec):
            query['ServicesSpec'] = request.services_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallAddon',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.InstallAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_addon(
        self,
        request: ehpc20240730_models.InstallAddonRequest,
    ) -> ehpc20240730_models.InstallAddonResponse:
        """
        @summary Installs an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into two types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: InstallAddonRequest
        @return: InstallAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_addon_with_options(request, runtime)

    async def install_addon_async(
        self,
        request: ehpc20240730_models.InstallAddonRequest,
    ) -> ehpc20240730_models.InstallAddonResponse:
        """
        @summary Installs an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into two types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: InstallAddonRequest
        @return: InstallAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_addon_with_options_async(request, runtime)

    def install_softwares_with_options(
        self,
        tmp_req: ehpc20240730_models.InstallSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.InstallSoftwaresResponse:
        """
        @summary Install software for the specified cluster.
        
        @description ## Interface Description
        When calling this interface, please note the following:
        - The cluster status must be `Running`.
        - If the cluster series is `Serverless`, ensure that there is at least one login node or compute node in the cluster; otherwise, software cannot be added to the target cluster.
        
        @param tmp_req: InstallSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallSoftwaresResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.InstallSoftwaresShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_packages):
            request.additional_packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.InstallSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_softwares_with_options_async(
        self,
        tmp_req: ehpc20240730_models.InstallSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.InstallSoftwaresResponse:
        """
        @summary Install software for the specified cluster.
        
        @description ## Interface Description
        When calling this interface, please note the following:
        - The cluster status must be `Running`.
        - If the cluster series is `Serverless`, ensure that there is at least one login node or compute node in the cluster; otherwise, software cannot be added to the target cluster.
        
        @param tmp_req: InstallSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallSoftwaresResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.InstallSoftwaresShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_packages):
            request.additional_packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.InstallSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_softwares(
        self,
        request: ehpc20240730_models.InstallSoftwaresRequest,
    ) -> ehpc20240730_models.InstallSoftwaresResponse:
        """
        @summary Install software for the specified cluster.
        
        @description ## Interface Description
        When calling this interface, please note the following:
        - The cluster status must be `Running`.
        - If the cluster series is `Serverless`, ensure that there is at least one login node or compute node in the cluster; otherwise, software cannot be added to the target cluster.
        
        @param request: InstallSoftwaresRequest
        @return: InstallSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_softwares_with_options(request, runtime)

    async def install_softwares_async(
        self,
        request: ehpc20240730_models.InstallSoftwaresRequest,
    ) -> ehpc20240730_models.InstallSoftwaresResponse:
        """
        @summary Install software for the specified cluster.
        
        @description ## Interface Description
        When calling this interface, please note the following:
        - The cluster status must be `Running`.
        - If the cluster series is `Serverless`, ensure that there is at least one login node or compute node in the cluster; otherwise, software cannot be added to the target cluster.
        
        @param request: InstallSoftwaresRequest
        @return: InstallSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_softwares_with_options_async(request, runtime)

    def list_addon_templates_with_options(
        self,
        request: ehpc20240730_models.ListAddonTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAddonTemplatesResponse:
        """
        @summary Queries supported addon templates.
        
        @param request: ListAddonTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_names):
            query['AddonNames'] = request.addon_names
        if not UtilClient.is_unset(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddonTemplates',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAddonTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addon_templates_with_options_async(
        self,
        request: ehpc20240730_models.ListAddonTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAddonTemplatesResponse:
        """
        @summary Queries supported addon templates.
        
        @param request: ListAddonTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_names):
            query['AddonNames'] = request.addon_names
        if not UtilClient.is_unset(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddonTemplates',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAddonTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addon_templates(
        self,
        request: ehpc20240730_models.ListAddonTemplatesRequest,
    ) -> ehpc20240730_models.ListAddonTemplatesResponse:
        """
        @summary Queries supported addon templates.
        
        @param request: ListAddonTemplatesRequest
        @return: ListAddonTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_addon_templates_with_options(request, runtime)

    async def list_addon_templates_async(
        self,
        request: ehpc20240730_models.ListAddonTemplatesRequest,
    ) -> ehpc20240730_models.ListAddonTemplatesResponse:
        """
        @summary Queries supported addon templates.
        
        @param request: ListAddonTemplatesRequest
        @return: ListAddonTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_addon_templates_with_options_async(request, runtime)

    def list_addons_with_options(
        self,
        tmp_req: ehpc20240730_models.ListAddonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAddonsResponse:
        """
        @summary Queries installed addons of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: ListAddonsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListAddonsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addon_ids):
            request.addon_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addon_ids, 'AddonIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.addon_ids_shrink):
            query['AddonIds'] = request.addon_ids_shrink
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        tmp_req: ehpc20240730_models.ListAddonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAddonsResponse:
        """
        @summary Queries installed addons of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: ListAddonsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddonsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListAddonsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addon_ids):
            request.addon_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addon_ids, 'AddonIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.addon_ids_shrink):
            query['AddonIds'] = request.addon_ids_shrink
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addons(
        self,
        request: ehpc20240730_models.ListAddonsRequest,
    ) -> ehpc20240730_models.ListAddonsResponse:
        """
        @summary Queries installed addons of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListAddonsRequest
        @return: ListAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_addons_with_options(request, runtime)

    async def list_addons_async(
        self,
        request: ehpc20240730_models.ListAddonsRequest,
    ) -> ehpc20240730_models.ListAddonsResponse:
        """
        @summary Queries installed addons of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListAddonsRequest
        @return: ListAddonsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_addons_with_options_async(request, runtime)

    def list_available_file_systems_with_options(
        self,
        request: ehpc20240730_models.ListAvailableFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAvailableFileSystemsResponse:
        """
        @summary Queries the file systems that can be attached in a region.
        
        @param request: ListAvailableFileSystemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableFileSystemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableFileSystems',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAvailableFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_file_systems_with_options_async(
        self,
        request: ehpc20240730_models.ListAvailableFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAvailableFileSystemsResponse:
        """
        @summary Queries the file systems that can be attached in a region.
        
        @param request: ListAvailableFileSystemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableFileSystemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableFileSystems',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAvailableFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_file_systems(
        self,
        request: ehpc20240730_models.ListAvailableFileSystemsRequest,
    ) -> ehpc20240730_models.ListAvailableFileSystemsResponse:
        """
        @summary Queries the file systems that can be attached in a region.
        
        @param request: ListAvailableFileSystemsRequest
        @return: ListAvailableFileSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_available_file_systems_with_options(request, runtime)

    async def list_available_file_systems_async(
        self,
        request: ehpc20240730_models.ListAvailableFileSystemsRequest,
    ) -> ehpc20240730_models.ListAvailableFileSystemsResponse:
        """
        @summary Queries the file systems that can be attached in a region.
        
        @param request: ListAvailableFileSystemsRequest
        @return: ListAvailableFileSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_available_file_systems_with_options_async(request, runtime)

    def list_available_images_with_options(
        self,
        tmp_req: ehpc20240730_models.ListAvailableImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAvailableImagesResponse:
        """
        @summary Queries images that are available for Elastic High Performance Computing (E-HPC) clusters.
        
        @param tmp_req: ListAvailableImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableImagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListAvailableImagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.directory_service):
            request.directory_service_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.directory_service, 'DirectoryService', 'json')
        if not UtilClient.is_unset(tmp_req.scheduler):
            request.scheduler_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler, 'Scheduler', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableImages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAvailableImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_images_with_options_async(
        self,
        tmp_req: ehpc20240730_models.ListAvailableImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListAvailableImagesResponse:
        """
        @summary Queries images that are available for Elastic High Performance Computing (E-HPC) clusters.
        
        @param tmp_req: ListAvailableImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableImagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListAvailableImagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.directory_service):
            request.directory_service_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.directory_service, 'DirectoryService', 'json')
        if not UtilClient.is_unset(tmp_req.scheduler):
            request.scheduler_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler, 'Scheduler', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableImages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListAvailableImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_images(
        self,
        request: ehpc20240730_models.ListAvailableImagesRequest,
    ) -> ehpc20240730_models.ListAvailableImagesResponse:
        """
        @summary Queries images that are available for Elastic High Performance Computing (E-HPC) clusters.
        
        @param request: ListAvailableImagesRequest
        @return: ListAvailableImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_available_images_with_options(request, runtime)

    async def list_available_images_async(
        self,
        request: ehpc20240730_models.ListAvailableImagesRequest,
    ) -> ehpc20240730_models.ListAvailableImagesResponse:
        """
        @summary Queries images that are available for Elastic High Performance Computing (E-HPC) clusters.
        
        @param request: ListAvailableImagesRequest
        @return: ListAvailableImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_available_images_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        tmp_req: ehpc20240730_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListClustersResponse:
        """
        @summary Queries all clusters of a user in each region.
        
        @param tmp_req: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.cluster_names):
            request.cluster_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_names, 'ClusterNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.cluster_names_shrink):
            query['ClusterNames'] = request.cluster_names_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        tmp_req: ehpc20240730_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListClustersResponse:
        """
        @summary Queries all clusters of a user in each region.
        
        @param tmp_req: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.cluster_names):
            request.cluster_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_names, 'ClusterNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.cluster_names_shrink):
            query['ClusterNames'] = request.cluster_names_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: ehpc20240730_models.ListClustersRequest,
    ) -> ehpc20240730_models.ListClustersResponse:
        """
        @summary Queries all clusters of a user in each region.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: ehpc20240730_models.ListClustersRequest,
    ) -> ehpc20240730_models.ListClustersResponse:
        """
        @summary Queries all clusters of a user in each region.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_common_logs_with_options(
        self,
        tmp_req: ehpc20240730_models.ListCommonLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListCommonLogsResponse:
        """
        @summary Queries the logs of a cluster that are generated within a time range.
        
        @param tmp_req: ListCommonLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommonLogsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListCommonLogsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_name):
            request.action_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_name, 'ActionName', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_name_shrink):
            query['ActionName'] = request.action_name_shrink
        if not UtilClient.is_unset(request.action_status):
            query['ActionStatus'] = request.action_status
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.is_reverse):
            query['IsReverse'] = request.is_reverse
        if not UtilClient.is_unset(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.operator_uid):
            query['OperatorUid'] = request.operator_uid
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommonLogs',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListCommonLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_logs_with_options_async(
        self,
        tmp_req: ehpc20240730_models.ListCommonLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListCommonLogsResponse:
        """
        @summary Queries the logs of a cluster that are generated within a time range.
        
        @param tmp_req: ListCommonLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommonLogsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListCommonLogsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_name):
            request.action_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_name, 'ActionName', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_name_shrink):
            query['ActionName'] = request.action_name_shrink
        if not UtilClient.is_unset(request.action_status):
            query['ActionStatus'] = request.action_status
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.is_reverse):
            query['IsReverse'] = request.is_reverse
        if not UtilClient.is_unset(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.operator_uid):
            query['OperatorUid'] = request.operator_uid
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommonLogs',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListCommonLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_logs(
        self,
        request: ehpc20240730_models.ListCommonLogsRequest,
    ) -> ehpc20240730_models.ListCommonLogsResponse:
        """
        @summary Queries the logs of a cluster that are generated within a time range.
        
        @param request: ListCommonLogsRequest
        @return: ListCommonLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_common_logs_with_options(request, runtime)

    async def list_common_logs_async(
        self,
        request: ehpc20240730_models.ListCommonLogsRequest,
    ) -> ehpc20240730_models.ListCommonLogsResponse:
        """
        @summary Queries the logs of a cluster that are generated within a time range.
        
        @param request: ListCommonLogsRequest
        @return: ListCommonLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_common_logs_with_options_async(request, runtime)

    def list_installed_softwares_with_options(
        self,
        request: ehpc20240730_models.ListInstalledSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListInstalledSoftwaresResponse:
        """
        @summary Queries the installed software of a cluster.
        
        @param request: ListInstalledSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstalledSoftwaresResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstalledSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListInstalledSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_installed_softwares_with_options_async(
        self,
        request: ehpc20240730_models.ListInstalledSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListInstalledSoftwaresResponse:
        """
        @summary Queries the installed software of a cluster.
        
        @param request: ListInstalledSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstalledSoftwaresResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstalledSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListInstalledSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_installed_softwares(
        self,
        request: ehpc20240730_models.ListInstalledSoftwaresRequest,
    ) -> ehpc20240730_models.ListInstalledSoftwaresResponse:
        """
        @summary Queries the installed software of a cluster.
        
        @param request: ListInstalledSoftwaresRequest
        @return: ListInstalledSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_installed_softwares_with_options(request, runtime)

    async def list_installed_softwares_async(
        self,
        request: ehpc20240730_models.ListInstalledSoftwaresRequest,
    ) -> ehpc20240730_models.ListInstalledSoftwaresResponse:
        """
        @summary Queries the installed software of a cluster.
        
        @param request: ListInstalledSoftwaresRequest
        @return: ListInstalledSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_installed_softwares_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        tmp_req: ehpc20240730_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param tmp_req: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_filter):
            request.job_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_filter, 'JobFilter', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_filter_shrink):
            query['JobFilter'] = request.job_filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        tmp_req: ehpc20240730_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param tmp_req: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_filter):
            request.job_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_filter, 'JobFilter', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_filter_shrink):
            query['JobFilter'] = request.job_filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: ehpc20240730_models.ListJobsRequest,
    ) -> ehpc20240730_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: ehpc20240730_models.ListJobsRequest,
    ) -> ehpc20240730_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: ehpc20240730_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListNodesResponse:
        """
        @summary Queries the nodes of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hostnames):
            request.hostnames_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hostnames, 'Hostnames', 'json')
        if not UtilClient.is_unset(tmp_req.private_ip_address):
            request.private_ip_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.private_ip_address, 'PrivateIpAddress', 'json')
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hostnames_shrink):
            query['Hostnames'] = request.hostnames_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip_address_shrink):
            query['PrivateIpAddress'] = request.private_ip_address_shrink
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.sequence):
            query['Sequence'] = request.sequence
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status_shrink):
            query['Status'] = request.status_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: ehpc20240730_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListNodesResponse:
        """
        @summary Queries the nodes of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hostnames):
            request.hostnames_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hostnames, 'Hostnames', 'json')
        if not UtilClient.is_unset(tmp_req.private_ip_address):
            request.private_ip_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.private_ip_address, 'PrivateIpAddress', 'json')
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hostnames_shrink):
            query['Hostnames'] = request.hostnames_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip_address_shrink):
            query['PrivateIpAddress'] = request.private_ip_address_shrink
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        if not UtilClient.is_unset(request.sequence):
            query['Sequence'] = request.sequence
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status_shrink):
            query['Status'] = request.status_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: ehpc20240730_models.ListNodesRequest,
    ) -> ehpc20240730_models.ListNodesResponse:
        """
        @summary Queries the nodes of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: ehpc20240730_models.ListNodesRequest,
    ) -> ehpc20240730_models.ListNodesResponse:
        """
        @summary Queries the nodes of an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        tmp_req: ehpc20240730_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListQueuesResponse:
        """
        @summary Queries queues in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: ListQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueuesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListQueuesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queues_with_options_async(
        self,
        tmp_req: ehpc20240730_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListQueuesResponse:
        """
        @summary Queries queues in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: ListQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueuesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.ListQueuesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue_names):
            request.queue_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue_names, 'QueueNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_names_shrink):
            query['QueueNames'] = request.queue_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queues(
        self,
        request: ehpc20240730_models.ListQueuesRequest,
    ) -> ehpc20240730_models.ListQueuesResponse:
        """
        @summary Queries queues in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListQueuesRequest
        @return: ListQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: ehpc20240730_models.ListQueuesRequest,
    ) -> ehpc20240730_models.ListQueuesResponse:
        """
        @summary Queries queues in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListQueuesRequest
        @return: ListQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def list_shared_storages_with_options(
        self,
        request: ehpc20240730_models.ListSharedStoragesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListSharedStoragesResponse:
        """
        @summary Queries the shared storage that is attached to a cluster.
        
        @param request: ListSharedStoragesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedStoragesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedStorages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListSharedStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_storages_with_options_async(
        self,
        request: ehpc20240730_models.ListSharedStoragesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListSharedStoragesResponse:
        """
        @summary Queries the shared storage that is attached to a cluster.
        
        @param request: ListSharedStoragesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedStoragesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedStorages',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListSharedStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_storages(
        self,
        request: ehpc20240730_models.ListSharedStoragesRequest,
    ) -> ehpc20240730_models.ListSharedStoragesResponse:
        """
        @summary Queries the shared storage that is attached to a cluster.
        
        @param request: ListSharedStoragesRequest
        @return: ListSharedStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shared_storages_with_options(request, runtime)

    async def list_shared_storages_async(
        self,
        request: ehpc20240730_models.ListSharedStoragesRequest,
    ) -> ehpc20240730_models.ListSharedStoragesResponse:
        """
        @summary Queries the shared storage that is attached to a cluster.
        
        @param request: ListSharedStoragesRequest
        @return: ListSharedStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_storages_with_options_async(request, runtime)

    def list_softwares_with_options(
        self,
        request: ehpc20240730_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListSoftwaresResponse:
        """
        @summary Queries the software that can be installed in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSoftwaresResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_softwares_with_options_async(
        self,
        request: ehpc20240730_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListSoftwaresResponse:
        """
        @summary Queries the software that can be installed in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSoftwaresResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_softwares(
        self,
        request: ehpc20240730_models.ListSoftwaresRequest,
    ) -> ehpc20240730_models.ListSoftwaresResponse:
        """
        @summary Queries the software that can be installed in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListSoftwaresRequest
        @return: ListSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    async def list_softwares_async(
        self,
        request: ehpc20240730_models.ListSoftwaresRequest,
    ) -> ehpc20240730_models.ListSoftwaresResponse:
        """
        @summary Queries the software that can be installed in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: ListSoftwaresRequest
        @return: ListSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_softwares_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ehpc20240730_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListUsersResponse:
        """
        @summary Queries the users of a cluster.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ehpc20240730_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.ListUsersResponse:
        """
        @summary Queries the users of a cluster.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: ehpc20240730_models.ListUsersRequest,
    ) -> ehpc20240730_models.ListUsersResponse:
        """
        @summary Queries the users of a cluster.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ehpc20240730_models.ListUsersRequest,
    ) -> ehpc20240730_models.ListUsersResponse:
        """
        @summary Queries the users of a cluster.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def stop_jobs_with_options(
        self,
        tmp_req: ehpc20240730_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.StopJobsResponse:
        """
        @summary Stops uncompleted jobs in a batch in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: StopJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.StopJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.StopJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_jobs_with_options_async(
        self,
        tmp_req: ehpc20240730_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.StopJobsResponse:
        """
        @summary Stops uncompleted jobs in a batch in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: StopJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.StopJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.StopJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_jobs(
        self,
        request: ehpc20240730_models.StopJobsRequest,
    ) -> ehpc20240730_models.StopJobsResponse:
        """
        @summary Stops uncompleted jobs in a batch in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: StopJobsRequest
        @return: StopJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    async def stop_jobs_async(
        self,
        request: ehpc20240730_models.StopJobsRequest,
    ) -> ehpc20240730_models.StopJobsResponse:
        """
        @summary Stops uncompleted jobs in a batch in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: StopJobsRequest
        @return: StopJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_jobs_with_options_async(request, runtime)

    def un_install_addon_with_options(
        self,
        request: ehpc20240730_models.UnInstallAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UnInstallAddonResponse:
        """
        @summary Uninstalls an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into the following types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: UnInstallAddonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnInstallAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_id):
            query['AddonId'] = request.addon_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnInstallAddon',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UnInstallAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_install_addon_with_options_async(
        self,
        request: ehpc20240730_models.UnInstallAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UnInstallAddonResponse:
        """
        @summary Uninstalls an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into the following types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: UnInstallAddonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnInstallAddonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_id):
            query['AddonId'] = request.addon_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnInstallAddon',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UnInstallAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_install_addon(
        self,
        request: ehpc20240730_models.UnInstallAddonRequest,
    ) -> ehpc20240730_models.UnInstallAddonResponse:
        """
        @summary Uninstalls an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into the following types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: UnInstallAddonRequest
        @return: UnInstallAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_install_addon_with_options(request, runtime)

    async def un_install_addon_async(
        self,
        request: ehpc20240730_models.UnInstallAddonRequest,
    ) -> ehpc20240730_models.UnInstallAddonResponse:
        """
        @summary Uninstalls an addon.
        
        @description ## [](#)Usage notes
        Take note of the following items when you call this operation:
        The cluster must be in the `Running` state.
        Clusters fall into the following types:
        Regular clusters on Alibaba Cloud Public Cloud
        Managed clusters on Alibaba Cloud Public Cloud
        
        @param request: UnInstallAddonRequest
        @return: UnInstallAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_install_addon_with_options_async(request, runtime)

    def uninstall_softwares_with_options(
        self,
        tmp_req: ehpc20240730_models.UninstallSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UninstallSoftwaresResponse:
        """
        @summary Uninstalls software systems from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## Interface Description
        When calling this interface, please note:
        The cluster status must be `Running`.
        
        @param tmp_req: UninstallSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallSoftwaresResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UninstallSoftwaresShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_packages):
            request.additional_packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UninstallSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_softwares_with_options_async(
        self,
        tmp_req: ehpc20240730_models.UninstallSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UninstallSoftwaresResponse:
        """
        @summary Uninstalls software systems from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## Interface Description
        When calling this interface, please note:
        The cluster status must be `Running`.
        
        @param tmp_req: UninstallSoftwaresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallSoftwaresResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UninstallSoftwaresShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_packages):
            request.additional_packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_packages, 'AdditionalPackages', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallSoftwares',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UninstallSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_softwares(
        self,
        request: ehpc20240730_models.UninstallSoftwaresRequest,
    ) -> ehpc20240730_models.UninstallSoftwaresResponse:
        """
        @summary Uninstalls software systems from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## Interface Description
        When calling this interface, please note:
        The cluster status must be `Running`.
        
        @param request: UninstallSoftwaresRequest
        @return: UninstallSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_softwares_with_options(request, runtime)

    async def uninstall_softwares_async(
        self,
        request: ehpc20240730_models.UninstallSoftwaresRequest,
    ) -> ehpc20240730_models.UninstallSoftwaresResponse:
        """
        @summary Uninstalls software systems from an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## Interface Description
        When calling this interface, please note:
        The cluster status must be `Running`.
        
        @param request: UninstallSoftwaresRequest
        @return: UninstallSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_softwares_with_options_async(request, runtime)

    def update_cluster_with_options(
        self,
        tmp_req: ehpc20240730_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateClusterResponse:
        """
        @summary Modify the basic information of a specified cluster.
        
        @param tmp_req: UpdateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UpdateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_spec):
            request.monitor_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_spec, 'MonitorSpec', 'json')
        if not UtilClient.is_unset(tmp_req.scheduler_spec):
            request.scheduler_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_spec, 'SchedulerSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not UtilClient.is_unset(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.enable_scale_in):
            query['EnableScaleIn'] = request.enable_scale_in
        if not UtilClient.is_unset(request.enable_scale_out):
            query['EnableScaleOut'] = request.enable_scale_out
        if not UtilClient.is_unset(request.grow_interval):
            query['GrowInterval'] = request.grow_interval
        if not UtilClient.is_unset(request.idle_interval):
            query['IdleInterval'] = request.idle_interval
        if not UtilClient.is_unset(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not UtilClient.is_unset(request.max_count):
            query['MaxCount'] = request.max_count
        if not UtilClient.is_unset(request.monitor_spec_shrink):
            query['MonitorSpec'] = request.monitor_spec_shrink
        if not UtilClient.is_unset(request.scheduler_spec_shrink):
            query['SchedulerSpec'] = request.scheduler_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        tmp_req: ehpc20240730_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateClusterResponse:
        """
        @summary Modify the basic information of a specified cluster.
        
        @param tmp_req: UpdateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UpdateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_custom_configuration):
            request.cluster_custom_configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_custom_configuration, 'ClusterCustomConfiguration', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_spec):
            request.monitor_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_spec, 'MonitorSpec', 'json')
        if not UtilClient.is_unset(tmp_req.scheduler_spec):
            request.scheduler_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_spec, 'SchedulerSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.cluster_custom_configuration_shrink):
            query['ClusterCustomConfiguration'] = request.cluster_custom_configuration_shrink
        if not UtilClient.is_unset(request.cluster_description):
            query['ClusterDescription'] = request.cluster_description
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.enable_scale_in):
            query['EnableScaleIn'] = request.enable_scale_in
        if not UtilClient.is_unset(request.enable_scale_out):
            query['EnableScaleOut'] = request.enable_scale_out
        if not UtilClient.is_unset(request.grow_interval):
            query['GrowInterval'] = request.grow_interval
        if not UtilClient.is_unset(request.idle_interval):
            query['IdleInterval'] = request.idle_interval
        if not UtilClient.is_unset(request.max_core_count):
            query['MaxCoreCount'] = request.max_core_count
        if not UtilClient.is_unset(request.max_count):
            query['MaxCount'] = request.max_count
        if not UtilClient.is_unset(request.monitor_spec_shrink):
            query['MonitorSpec'] = request.monitor_spec_shrink
        if not UtilClient.is_unset(request.scheduler_spec_shrink):
            query['SchedulerSpec'] = request.scheduler_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster(
        self,
        request: ehpc20240730_models.UpdateClusterRequest,
    ) -> ehpc20240730_models.UpdateClusterResponse:
        """
        @summary Modify the basic information of a specified cluster.
        
        @param request: UpdateClusterRequest
        @return: UpdateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    async def update_cluster_async(
        self,
        request: ehpc20240730_models.UpdateClusterRequest,
    ) -> ehpc20240730_models.UpdateClusterResponse:
        """
        @summary Modify the basic information of a specified cluster.
        
        @param request: UpdateClusterRequest
        @return: UpdateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_with_options_async(request, runtime)

    def update_nodes_with_options(
        self,
        tmp_req: ehpc20240730_models.UpdateNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateNodesResponse:
        """
        @summary Updates the configurations of compute nodes in an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param tmp_req: UpdateNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UpdateNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instances_shrink):
            query['Instances'] = request.instances_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nodes_with_options_async(
        self,
        tmp_req: ehpc20240730_models.UpdateNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateNodesResponse:
        """
        @summary Updates the configurations of compute nodes in an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param tmp_req: UpdateNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UpdateNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instances_shrink):
            query['Instances'] = request.instances_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNodes',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nodes(
        self,
        request: ehpc20240730_models.UpdateNodesRequest,
    ) -> ehpc20240730_models.UpdateNodesResponse:
        """
        @summary Updates the configurations of compute nodes in an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: UpdateNodesRequest
        @return: UpdateNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_nodes_with_options(request, runtime)

    async def update_nodes_async(
        self,
        request: ehpc20240730_models.UpdateNodesRequest,
    ) -> ehpc20240730_models.UpdateNodesResponse:
        """
        @summary Updates the configurations of compute nodes in an Enterprise High Performance Computing (E-HPC) cluster.
        
        @description ## [](#)Usage notes
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: UpdateNodesRequest
        @return: UpdateNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_nodes_with_options_async(request, runtime)

    def update_queue_with_options(
        self,
        tmp_req: ehpc20240730_models.UpdateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateQueueResponse:
        """
        @summary Modifies the configurations of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: UpdateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UpdateQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue):
            request.queue_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQueue',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_queue_with_options_async(
        self,
        tmp_req: ehpc20240730_models.UpdateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateQueueResponse:
        """
        @summary Modifies the configurations of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: UpdateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20240730_models.UpdateQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.queue):
            request.queue_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.queue, 'Queue', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.queue_shrink):
            query['Queue'] = request.queue_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQueue',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_queue(
        self,
        request: ehpc20240730_models.UpdateQueueRequest,
    ) -> ehpc20240730_models.UpdateQueueResponse:
        """
        @summary Modifies the configurations of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: UpdateQueueRequest
        @return: UpdateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_queue_with_options(request, runtime)

    async def update_queue_async(
        self,
        request: ehpc20240730_models.UpdateQueueRequest,
    ) -> ehpc20240730_models.UpdateQueueResponse:
        """
        @summary Modifies the configurations of a queue in an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: UpdateQueueRequest
        @return: UpdateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_queue_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: ehpc20240730_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateUserResponse:
        """
        @summary Updates the information of a user in an Elastic High Performance Computing (E-HPC) cluster, including the user group and password.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: ehpc20240730_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20240730_models.UpdateUserResponse:
        """
        @summary Updates the information of a user in an Elastic High Performance Computing (E-HPC) cluster, including the user group and password.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2024-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20240730_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: ehpc20240730_models.UpdateUserRequest,
    ) -> ehpc20240730_models.UpdateUserResponse:
        """
        @summary Updates the information of a user in an Elastic High Performance Computing (E-HPC) cluster, including the user group and password.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: ehpc20240730_models.UpdateUserRequest,
    ) -> ehpc20240730_models.UpdateUserResponse:
        """
        @summary Updates the information of a user in an Elastic High Performance Computing (E-HPC) cluster, including the user group and password.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
