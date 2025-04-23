# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ehpc20180412 import models as ehpc20180412_models
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

    def add_existed_nodes_with_options(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        """
        @summary Adds one or more existing ECS instances as compute nodes to a specified cluster.
        
        @description    The compute nodes to be added are in the Stopped state.
        After the compute nodes are added to the cluster, the operating systems of the nodes are replaced with the operating system specified by the ImageId parameter.
        The hosts of the compute nodes must be different from those of the existing compute nodes in the cluster. Otherwise, the add operation fails.
        
        @param request: AddExistedNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddExistedNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExistedNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddExistedNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_existed_nodes_with_options_async(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        """
        @summary Adds one or more existing ECS instances as compute nodes to a specified cluster.
        
        @description    The compute nodes to be added are in the Stopped state.
        After the compute nodes are added to the cluster, the operating systems of the nodes are replaced with the operating system specified by the ImageId parameter.
        The hosts of the compute nodes must be different from those of the existing compute nodes in the cluster. Otherwise, the add operation fails.
        
        @param request: AddExistedNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddExistedNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExistedNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddExistedNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_existed_nodes(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        """
        @summary Adds one or more existing ECS instances as compute nodes to a specified cluster.
        
        @description    The compute nodes to be added are in the Stopped state.
        After the compute nodes are added to the cluster, the operating systems of the nodes are replaced with the operating system specified by the ImageId parameter.
        The hosts of the compute nodes must be different from those of the existing compute nodes in the cluster. Otherwise, the add operation fails.
        
        @param request: AddExistedNodesRequest
        @return: AddExistedNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_existed_nodes_with_options(request, runtime)

    async def add_existed_nodes_async(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        """
        @summary Adds one or more existing ECS instances as compute nodes to a specified cluster.
        
        @description    The compute nodes to be added are in the Stopped state.
        After the compute nodes are added to the cluster, the operating systems of the nodes are replaced with the operating system specified by the ImageId parameter.
        The hosts of the compute nodes must be different from those of the existing compute nodes in the cluster. Otherwise, the add operation fails.
        
        @param request: AddExistedNodesRequest
        @return: AddExistedNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_existed_nodes_with_options_async(request, runtime)

    def add_local_nodes_with_options(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        """
        @param request: AddLocalNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLocalNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLocalNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddLocalNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_local_nodes_with_options_async(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        """
        @param request: AddLocalNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLocalNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLocalNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddLocalNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_local_nodes(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        """
        @param request: AddLocalNodesRequest
        @return: AddLocalNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_local_nodes_with_options(request, runtime)

    async def add_local_nodes_async(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        """
        @param request: AddLocalNodesRequest
        @return: AddLocalNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_local_nodes_with_options_async(request, runtime)

    def add_nodes_with_options(
        self,
        request: ehpc20180412_models.AddNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddNodesResponse:
        """
        @summary Adds one or more compute nodes to an E-HPC cluster.
        
        @param request: AddNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_nodes_with_options_async(
        self,
        request: ehpc20180412_models.AddNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddNodesResponse:
        """
        @summary Adds one or more compute nodes to an E-HPC cluster.
        
        @param request: AddNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_nodes(
        self,
        request: ehpc20180412_models.AddNodesRequest,
    ) -> ehpc20180412_models.AddNodesResponse:
        """
        @summary Adds one or more compute nodes to an E-HPC cluster.
        
        @param request: AddNodesRequest
        @return: AddNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_nodes_with_options(request, runtime)

    async def add_nodes_async(
        self,
        request: ehpc20180412_models.AddNodesRequest,
    ) -> ehpc20180412_models.AddNodesResponse:
        """
        @summary Adds one or more compute nodes to an E-HPC cluster.
        
        @param request: AddNodesRequest
        @return: AddNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_nodes_with_options_async(request, runtime)

    def add_queue_with_options(
        self,
        request: ehpc20180412_models.AddQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddQueueResponse:
        """
        @summary Creates a queue for a cluster.
        
        @param request: AddQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_queue_with_options_async(
        self,
        request: ehpc20180412_models.AddQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddQueueResponse:
        """
        @summary Creates a queue for a cluster.
        
        @param request: AddQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_queue(
        self,
        request: ehpc20180412_models.AddQueueRequest,
    ) -> ehpc20180412_models.AddQueueResponse:
        """
        @summary Creates a queue for a cluster.
        
        @param request: AddQueueRequest
        @return: AddQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_queue_with_options(request, runtime)

    async def add_queue_async(
        self,
        request: ehpc20180412_models.AddQueueRequest,
    ) -> ehpc20180412_models.AddQueueResponse:
        """
        @summary Creates a queue for a cluster.
        
        @param request: AddQueueRequest
        @return: AddQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_queue_with_options_async(request, runtime)

    def add_security_group_with_options(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        """
        @summary Adds a cluster to a security group.
        
        @param request: AddSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSecurityGroup',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_security_group_with_options_async(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        """
        @summary Adds a cluster to a security group.
        
        @param request: AddSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSecurityGroup',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_security_group(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        """
        @summary Adds a cluster to a security group.
        
        @param request: AddSecurityGroupRequest
        @return: AddSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_security_group_with_options(request, runtime)

    async def add_security_group_async(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        """
        @summary Adds a cluster to a security group.
        
        @param request: AddSecurityGroupRequest
        @return: AddSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_security_group_with_options_async(request, runtime)

    def add_users_with_options(
        self,
        request: ehpc20180412_models.AddUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddUsersResponse:
        """
        @summary Adds users to a cluster.
        
        @param request: AddUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_with_options_async(
        self,
        request: ehpc20180412_models.AddUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddUsersResponse:
        """
        @summary Adds users to a cluster.
        
        @param request: AddUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users(
        self,
        request: ehpc20180412_models.AddUsersRequest,
    ) -> ehpc20180412_models.AddUsersResponse:
        """
        @summary Adds users to a cluster.
        
        @param request: AddUsersRequest
        @return: AddUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_users_with_options(request, runtime)

    async def add_users_async(
        self,
        request: ehpc20180412_models.AddUsersRequest,
    ) -> ehpc20180412_models.AddUsersResponse:
        """
        @summary Adds users to a cluster.
        
        @param request: AddUsersRequest
        @return: AddUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_users_with_options_async(request, runtime)

    def apply_nodes_with_options(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        """
        @summary Adds pay-as-you-go or preemptible compute nodes to a cluster.
        
        @description ## [](#)Description
        You can call the ApplyNodes operation to specify the number of compute nodes, the number of vCPUs, and the memory size when you add nodes to a cluster.
        
        @param request: ApplyNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ApplyNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_nodes_with_options_async(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        """
        @summary Adds pay-as-you-go or preemptible compute nodes to a cluster.
        
        @description ## [](#)Description
        You can call the ApplyNodes operation to specify the number of compute nodes, the number of vCPUs, and the memory size when you add nodes to a cluster.
        
        @param request: ApplyNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ApplyNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_nodes(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        """
        @summary Adds pay-as-you-go or preemptible compute nodes to a cluster.
        
        @description ## [](#)Description
        You can call the ApplyNodes operation to specify the number of compute nodes, the number of vCPUs, and the memory size when you add nodes to a cluster.
        
        @param request: ApplyNodesRequest
        @return: ApplyNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_nodes_with_options(request, runtime)

    async def apply_nodes_async(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        """
        @summary Adds pay-as-you-go or preemptible compute nodes to a cluster.
        
        @description ## [](#)Description
        You can call the ApplyNodes operation to specify the number of compute nodes, the number of vCPUs, and the memory size when you add nodes to a cluster.
        
        @param request: ApplyNodesRequest
        @return: ApplyNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_nodes_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription E-HPC cluster.
        
        @description After you create an Elastic High Performance Computing (E-HPC) cluster, you are charged for the cluster resources that you use. We recommend that you learn about the billing methods of E-HPC in advance. For more information, see [Billing overview](https://help.aliyun.com/document_detail/57844.html).
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription E-HPC cluster.
        
        @description After you create an Elastic High Performance Computing (E-HPC) cluster, you are charged for the cluster resources that you use. We recommend that you learn about the billing methods of E-HPC in advance. For more information, see [Billing overview](https://help.aliyun.com/document_detail/57844.html).
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
    ) -> ehpc20180412_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription E-HPC cluster.
        
        @description After you create an Elastic High Performance Computing (E-HPC) cluster, you are charged for the cluster resources that you use. We recommend that you learn about the billing methods of E-HPC in advance. For more information, see [Billing overview](https://help.aliyun.com/document_detail/57844.html).
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
    ) -> ehpc20180412_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription E-HPC cluster.
        
        @description After you create an Elastic High Performance Computing (E-HPC) cluster, you are charged for the cluster resources that you use. We recommend that you learn about the billing methods of E-HPC in advance. For more information, see [Billing overview](https://help.aliyun.com/document_detail/57844.html).
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_hybrid_cluster_with_options(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        """
        @summary Creates a hybrid cloud cluster.
        
        @param request: CreateHybridClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateHybridClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_cluster_with_options_async(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        """
        @summary Creates a hybrid cloud cluster.
        
        @param request: CreateHybridClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHybridClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateHybridClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_cluster(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        """
        @summary Creates a hybrid cloud cluster.
        
        @param request: CreateHybridClusterRequest
        @return: CreateHybridClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_cluster_with_options(request, runtime)

    async def create_hybrid_cluster_async(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        """
        @summary Creates a hybrid cloud cluster.
        
        @param request: CreateHybridClusterRequest
        @return: CreateHybridClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hybrid_cluster_with_options_async(request, runtime)

    def create_job_file_with_options(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        """
        @summary Creates a job file.
        
        @param request: CreateJobFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobFileResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobFile',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_file_with_options_async(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        """
        @summary Creates a job file.
        
        @param request: CreateJobFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobFileResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobFile',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_file(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        """
        @summary Creates a job file.
        
        @param request: CreateJobFileRequest
        @return: CreateJobFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_file_with_options(request, runtime)

    async def create_job_file_async(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        """
        @summary Creates a job file.
        
        @param request: CreateJobFileRequest
        @return: CreateJobFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_file_with_options_async(request, runtime)

    def create_job_template_with_options(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        """
        @summary Creates a job template.
        
        @param request: CreateJobTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobTemplateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobTemplate',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_template_with_options_async(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        """
        @summary Creates a job template.
        
        @param request: CreateJobTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobTemplateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobTemplate',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_template(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        """
        @summary Creates a job template.
        
        @param request: CreateJobTemplateRequest
        @return: CreateJobTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_template_with_options(request, runtime)

    async def create_job_template_async(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        """
        @summary Creates a job template.
        
        @param request: CreateJobTemplateRequest
        @return: CreateJobTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_template_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        """
        @summary Releases a cluster.
        
        @description After a cluster is released, the pay-as-you-go nodes and the subscription nodes that are expired are automatically released. The subscription nodes that are expired are retained. If you need to release subscription nodes that are not expired, change the billing method to pay-as-you-go. Before you release a cluster, make sure that you no longer use the cluster.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        """
        @summary Releases a cluster.
        
        @description After a cluster is released, the pay-as-you-go nodes and the subscription nodes that are expired are automatically released. The subscription nodes that are expired are retained. If you need to release subscription nodes that are not expired, change the billing method to pay-as-you-go. Before you release a cluster, make sure that you no longer use the cluster.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        """
        @summary Releases a cluster.
        
        @description After a cluster is released, the pay-as-you-go nodes and the subscription nodes that are expired are automatically released. The subscription nodes that are expired are retained. If you need to release subscription nodes that are not expired, change the billing method to pay-as-you-go. Before you release a cluster, make sure that you no longer use the cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        """
        @summary Releases a cluster.
        
        @description After a cluster is released, the pay-as-you-go nodes and the subscription nodes that are expired are automatically released. The subscription nodes that are expired are retained. If you need to release subscription nodes that are not expired, change the billing method to pay-as-you-go. Before you release a cluster, make sure that you no longer use the cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_job_templates_with_options(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        """
        @summary Deletes job templates.
        
        @param request: DeleteJobTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobTemplates',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_templates_with_options_async(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        """
        @summary Deletes job templates.
        
        @param request: DeleteJobTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobTemplates',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job_templates(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        """
        @summary Deletes job templates.
        
        @param request: DeleteJobTemplatesRequest
        @return: DeleteJobTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_job_templates_with_options(request, runtime)

    async def delete_job_templates_async(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        """
        @summary Deletes job templates.
        
        @param request: DeleteJobTemplatesRequest
        @return: DeleteJobTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_templates_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        """
        @summary Deletes jobs from a cluster.
        
        @param request: DeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        """
        @summary Deletes jobs from a cluster.
        
        @param request: DeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jobs(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        """
        @summary Deletes jobs from a cluster.
        
        @param request: DeleteJobsRequest
        @return: DeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        """
        @summary Deletes jobs from a cluster.
        
        @param request: DeleteJobsRequest
        @return: DeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def delete_nodes_with_options(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        """
        @description Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: DeleteNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nodes_with_options_async(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        """
        @description Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: DeleteNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nodes(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        """
        @description Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: DeleteNodesRequest
        @return: DeleteNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    async def delete_nodes_async(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        """
        @description Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        
        @param request: DeleteNodesRequest
        @return: DeleteNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_nodes_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        """
        @param request: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        """
        @param request: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_queue(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        """
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        """
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_security_group_with_options(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        """
        @summary Removes a cluster from a specified security group.
        
        @param request: DeleteSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityGroup',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_group_with_options_async(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        """
        @summary Removes a cluster from a specified security group.
        
        @param request: DeleteSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityGroup',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_group(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        """
        @summary Removes a cluster from a specified security group.
        
        @param request: DeleteSecurityGroupRequest
        @return: DeleteSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    async def delete_security_group_async(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        """
        @summary Removes a cluster from a specified security group.
        
        @param request: DeleteSecurityGroupRequest
        @return: DeleteSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_group_with_options_async(request, runtime)

    def delete_users_with_options(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @description If you delete a user, only its information is deleted. The files stored in the /home directory for the user are retained. For example, if you delete a user named user1, the files in the `/home/user1/` directory of the cluster are not deleted. However, a deleted user cannot be recovered. Even if you create another user that has the same name, the data retained for the deleted user is not reused.
        
        @param request: DeleteUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_users_with_options_async(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @description If you delete a user, only its information is deleted. The files stored in the /home directory for the user are retained. For example, if you delete a user named user1, the files in the `/home/user1/` directory of the cluster are not deleted. However, a deleted user cannot be recovered. Even if you create another user that has the same name, the data retained for the deleted user is not reused.
        
        @param request: DeleteUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_users(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @description If you delete a user, only its information is deleted. The files stored in the /home directory for the user are retained. For example, if you delete a user named user1, the files in the `/home/user1/` directory of the cluster are not deleted. However, a deleted user cannot be recovered. Even if you create another user that has the same name, the data retained for the deleted user is not reused.
        
        @param request: DeleteUsersRequest
        @return: DeleteUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        """
        @summary Deletes users from a cluster.
        
        @description If you delete a user, only its information is deleted. The files stored in the /home directory for the user are retained. For example, if you delete a user named user1, the files in the `/home/user1/` directory of the cluster are not deleted. However, a deleted user cannot be recovered. Even if you create another user that has the same name, the data retained for the deleted user is not reused.
        
        @param request: DeleteUsersRequest
        @return: DeleteUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def describe_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        """
        @summary Queries the auto scaling settings of a cluster.
        
        @param request: DescribeAutoScaleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_scale_config_with_options_async(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        """
        @summary Queries the auto scaling settings of a cluster.
        
        @param request: DescribeAutoScaleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeAutoScaleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_scale_config(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        """
        @summary Queries the auto scaling settings of a cluster.
        
        @param request: DescribeAutoScaleConfigRequest
        @return: DescribeAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scale_config_with_options(request, runtime)

    async def describe_auto_scale_config_async(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        """
        @summary Queries the auto scaling settings of a cluster.
        
        @param request: DescribeAutoScaleConfigRequest
        @return: DescribeAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_scale_config_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @param request: DescribeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_with_options_async(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @param request: DescribeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @param request: DescribeClusterRequest
        @return: DescribeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @param request: DescribeClusterRequest
        @return: DescribeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def describe_estack_image_with_options(
        self,
        request: ehpc20180412_models.DescribeEstackImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeEstackImageResponse:
        """
        @summary Queries the base images of Elastic High Performance Computing (E-HPC).
        
        @param request: DescribeEstackImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEstackImageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEstackImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeEstackImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_estack_image_with_options_async(
        self,
        request: ehpc20180412_models.DescribeEstackImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeEstackImageResponse:
        """
        @summary Queries the base images of Elastic High Performance Computing (E-HPC).
        
        @param request: DescribeEstackImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEstackImageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEstackImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeEstackImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_estack_image(
        self,
        request: ehpc20180412_models.DescribeEstackImageRequest,
    ) -> ehpc20180412_models.DescribeEstackImageResponse:
        """
        @summary Queries the base images of Elastic High Performance Computing (E-HPC).
        
        @param request: DescribeEstackImageRequest
        @return: DescribeEstackImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_estack_image_with_options(request, runtime)

    async def describe_estack_image_async(
        self,
        request: ehpc20180412_models.DescribeEstackImageRequest,
    ) -> ehpc20180412_models.DescribeEstackImageResponse:
        """
        @summary Queries the base images of Elastic High Performance Computing (E-HPC).
        
        @param request: DescribeEstackImageRequest
        @return: DescribeEstackImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_estack_image_with_options_async(request, runtime)

    def describe_image_price_with_options(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        """
        @summary Queries the price of an Alibaba Cloud Marketplace image.
        
        @param request: DescribeImagePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImagePriceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImagePrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImagePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_price_with_options_async(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        """
        @summary Queries the price of an Alibaba Cloud Marketplace image.
        
        @param request: DescribeImagePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImagePriceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImagePrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImagePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_price(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        """
        @summary Queries the price of an Alibaba Cloud Marketplace image.
        
        @param request: DescribeImagePriceRequest
        @return: DescribeImagePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_price_with_options(request, runtime)

    async def describe_image_price_async(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        """
        @summary Queries the price of an Alibaba Cloud Marketplace image.
        
        @param request: DescribeImagePriceRequest
        @return: DescribeImagePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_price_with_options_async(request, runtime)

    def describe_job_with_options(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeJobResponse:
        """
        @summary Queries the information about a job in an E-HPC cluster.
        
        @param request: DescribeJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeJobResponse:
        """
        @summary Queries the information about a job in an E-HPC cluster.
        
        @param request: DescribeJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
    ) -> ehpc20180412_models.DescribeJobResponse:
        """
        @summary Queries the information about a job in an E-HPC cluster.
        
        @param request: DescribeJobRequest
        @return: DescribeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    async def describe_job_async(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
    ) -> ehpc20180412_models.DescribeJobResponse:
        """
        @summary Queries the information about a job in an E-HPC cluster.
        
        @param request: DescribeJobRequest
        @return: DescribeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribePriceResponse:
        """
        @summary Queries the pricing information of a cluster.
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribePriceResponse:
        """
        @summary Queries the pricing information of a cluster.
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
    ) -> ehpc20180412_models.DescribePriceResponse:
        """
        @summary Queries the pricing information of a cluster.
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
    ) -> ehpc20180412_models.DescribePriceResponse:
        """
        @summary Queries the pricing information of a cluster.
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_serverless_jobs_with_options(
        self,
        request: ehpc20180412_models.DescribeServerlessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeServerlessJobsResponse:
        """
        @summary Queries the details of a serverless job by job ID or subtask ID (array job). You can specify only a single job ID or a single subtask ID at a time.
        
        @param request: DescribeServerlessJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServerlessJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeServerlessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_serverless_jobs_with_options_async(
        self,
        request: ehpc20180412_models.DescribeServerlessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeServerlessJobsResponse:
        """
        @summary Queries the details of a serverless job by job ID or subtask ID (array job). You can specify only a single job ID or a single subtask ID at a time.
        
        @param request: DescribeServerlessJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServerlessJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeServerlessJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_serverless_jobs(
        self,
        request: ehpc20180412_models.DescribeServerlessJobsRequest,
    ) -> ehpc20180412_models.DescribeServerlessJobsResponse:
        """
        @summary Queries the details of a serverless job by job ID or subtask ID (array job). You can specify only a single job ID or a single subtask ID at a time.
        
        @param request: DescribeServerlessJobsRequest
        @return: DescribeServerlessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_serverless_jobs_with_options(request, runtime)

    async def describe_serverless_jobs_async(
        self,
        request: ehpc20180412_models.DescribeServerlessJobsRequest,
    ) -> ehpc20180412_models.DescribeServerlessJobsResponse:
        """
        @summary Queries the details of a serverless job by job ID or subtask ID (array job). You can specify only a single job ID or a single subtask ID at a time.
        
        @param request: DescribeServerlessJobsRequest
        @return: DescribeServerlessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_serverless_jobs_with_options_async(request, runtime)

    def edit_job_template_with_options(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        """
        @param request: EditJobTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditJobTemplateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditJobTemplate',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.EditJobTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_job_template_with_options_async(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        """
        @param request: EditJobTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditJobTemplateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditJobTemplate',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.EditJobTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_job_template(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        """
        @param request: EditJobTemplateRequest
        @return: EditJobTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_job_template_with_options(request, runtime)

    async def edit_job_template_async(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        """
        @param request: EditJobTemplateRequest
        @return: EditJobTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.edit_job_template_with_options_async(request, runtime)

    def get_accounting_report_with_options(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        """
        @param request: GetAccountingReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountingReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountingReport',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAccountingReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_accounting_report_with_options_async(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        """
        @param request: GetAccountingReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountingReportResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountingReport',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAccountingReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_accounting_report(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        """
        @param request: GetAccountingReportRequest
        @return: GetAccountingReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_accounting_report_with_options(request, runtime)

    async def get_accounting_report_async(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        """
        @param request: GetAccountingReportRequest
        @return: GetAccountingReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_accounting_report_with_options_async(request, runtime)

    def get_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        """
        @summary Obtains the auto scaling settings of a cluster.
        
        @param request: GetAutoScaleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scale_config_with_options_async(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        """
        @summary Obtains the auto scaling settings of a cluster.
        
        @param request: GetAutoScaleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAutoScaleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scale_config(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        """
        @summary Obtains the auto scaling settings of a cluster.
        
        @param request: GetAutoScaleConfigRequest
        @return: GetAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scale_config_with_options(request, runtime)

    async def get_auto_scale_config_async(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        """
        @summary Obtains the auto scaling settings of a cluster.
        
        @param request: GetAutoScaleConfigRequest
        @return: GetAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scale_config_with_options_async(request, runtime)

    def get_cloud_metric_logs_with_options(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        """
        @summary Reads performance metrics (CloudMetrics) logs of E-HPC.
        
        @param request: GetCloudMetricLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudMetricLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudMetricLogs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_metric_logs_with_options_async(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        """
        @summary Reads performance metrics (CloudMetrics) logs of E-HPC.
        
        @param request: GetCloudMetricLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudMetricLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudMetricLogs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_metric_logs(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        """
        @summary Reads performance metrics (CloudMetrics) logs of E-HPC.
        
        @param request: GetCloudMetricLogsRequest
        @return: GetCloudMetricLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_logs_with_options(request, runtime)

    async def get_cloud_metric_logs_async(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        """
        @summary Reads performance metrics (CloudMetrics) logs of E-HPC.
        
        @param request: GetCloudMetricLogsRequest
        @return: GetCloudMetricLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_metric_logs_with_options_async(request, runtime)

    def get_cloud_metric_profiling_with_options(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        """
        @param request: GetCloudMetricProfilingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudMetricProfilingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudMetricProfiling',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricProfilingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_metric_profiling_with_options_async(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        """
        @param request: GetCloudMetricProfilingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudMetricProfilingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudMetricProfiling',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricProfilingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_metric_profiling(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        """
        @param request: GetCloudMetricProfilingRequest
        @return: GetCloudMetricProfilingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_profiling_with_options(request, runtime)

    async def get_cloud_metric_profiling_async(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        """
        @param request: GetCloudMetricProfilingRequest
        @return: GetCloudMetricProfilingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_metric_profiling_with_options_async(request, runtime)

    def get_cluster_volumes_with_options(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        """
        @summary Queries the information of the NAS file system mounted to a specified cluster.
        
        @param request: GetClusterVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterVolumesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetClusterVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_volumes_with_options_async(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        """
        @summary Queries the information of the NAS file system mounted to a specified cluster.
        
        @param request: GetClusterVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterVolumesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetClusterVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_volumes(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        """
        @summary Queries the information of the NAS file system mounted to a specified cluster.
        
        @param request: GetClusterVolumesRequest
        @return: GetClusterVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_volumes_with_options(request, runtime)

    async def get_cluster_volumes_async(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        """
        @summary Queries the information of the NAS file system mounted to a specified cluster.
        
        @param request: GetClusterVolumesRequest
        @return: GetClusterVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_volumes_with_options_async(request, runtime)

    def get_hybrid_cluster_config_with_options(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        """
        @param request: GetHybridClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHybridClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHybridClusterConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHybridClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hybrid_cluster_config_with_options_async(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        """
        @param request: GetHybridClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHybridClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHybridClusterConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHybridClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hybrid_cluster_config(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        """
        @param request: GetHybridClusterConfigRequest
        @return: GetHybridClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hybrid_cluster_config_with_options(request, runtime)

    async def get_hybrid_cluster_config_async(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        """
        @param request: GetHybridClusterConfigRequest
        @return: GetHybridClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hybrid_cluster_config_with_options_async(request, runtime)

    def get_if_ecs_type_support_ht_config_with_options(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        """
        @summary Queries whether hyper-threading can be enabled or disabled for an instance type.
        
        @param request: GetIfEcsTypeSupportHtConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIfEcsTypeSupportHtConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIfEcsTypeSupportHtConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_if_ecs_type_support_ht_config_with_options_async(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        """
        @summary Queries whether hyper-threading can be enabled or disabled for an instance type.
        
        @param request: GetIfEcsTypeSupportHtConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIfEcsTypeSupportHtConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIfEcsTypeSupportHtConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_if_ecs_type_support_ht_config(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        """
        @summary Queries whether hyper-threading can be enabled or disabled for an instance type.
        
        @param request: GetIfEcsTypeSupportHtConfigRequest
        @return: GetIfEcsTypeSupportHtConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_if_ecs_type_support_ht_config_with_options(request, runtime)

    async def get_if_ecs_type_support_ht_config_async(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        """
        @summary Queries whether hyper-threading can be enabled or disabled for an instance type.
        
        @param request: GetIfEcsTypeSupportHtConfigRequest
        @return: GetIfEcsTypeSupportHtConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_if_ecs_type_support_ht_config_with_options_async(request, runtime)

    def get_job_log_with_options(
        self,
        request: ehpc20180412_models.GetJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetJobLogResponse:
        """
        @summary 实时查询任务的输出日志
        
        @param request: GetJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobLog',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_log_with_options_async(
        self,
        request: ehpc20180412_models.GetJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetJobLogResponse:
        """
        @summary 实时查询任务的输出日志
        
        @param request: GetJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobLog',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_log(
        self,
        request: ehpc20180412_models.GetJobLogRequest,
    ) -> ehpc20180412_models.GetJobLogResponse:
        """
        @summary 实时查询任务的输出日志
        
        @param request: GetJobLogRequest
        @return: GetJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_log_with_options(request, runtime)

    async def get_job_log_async(
        self,
        request: ehpc20180412_models.GetJobLogRequest,
    ) -> ehpc20180412_models.GetJobLogResponse:
        """
        @summary 实时查询任务的输出日志
        
        @param request: GetJobLogRequest
        @return: GetJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_log_with_options_async(request, runtime)

    def get_post_scripts_with_options(
        self,
        request: ehpc20180412_models.GetPostScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetPostScriptsResponse:
        """
        @summary Queries the post-processing scripts of a cluster.
        
        @param request: GetPostScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPostScriptsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPostScripts',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetPostScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_post_scripts_with_options_async(
        self,
        request: ehpc20180412_models.GetPostScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetPostScriptsResponse:
        """
        @summary Queries the post-processing scripts of a cluster.
        
        @param request: GetPostScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPostScriptsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPostScripts',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetPostScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_post_scripts(
        self,
        request: ehpc20180412_models.GetPostScriptsRequest,
    ) -> ehpc20180412_models.GetPostScriptsResponse:
        """
        @summary Queries the post-processing scripts of a cluster.
        
        @param request: GetPostScriptsRequest
        @return: GetPostScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_post_scripts_with_options(request, runtime)

    async def get_post_scripts_async(
        self,
        request: ehpc20180412_models.GetPostScriptsRequest,
    ) -> ehpc20180412_models.GetPostScriptsResponse:
        """
        @summary Queries the post-processing scripts of a cluster.
        
        @param request: GetPostScriptsRequest
        @return: GetPostScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_post_scripts_with_options_async(request, runtime)

    def get_scheduler_info_with_options(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        """
        @summary Queries the scheduler settings of a cluster.
        
        @param request: GetSchedulerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSchedulerInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchedulerInfo',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetSchedulerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheduler_info_with_options_async(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        """
        @summary Queries the scheduler settings of a cluster.
        
        @param request: GetSchedulerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSchedulerInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchedulerInfo',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetSchedulerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheduler_info(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        """
        @summary Queries the scheduler settings of a cluster.
        
        @param request: GetSchedulerInfoRequest
        @return: GetSchedulerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_scheduler_info_with_options(request, runtime)

    async def get_scheduler_info_async(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        """
        @summary Queries the scheduler settings of a cluster.
        
        @param request: GetSchedulerInfoRequest
        @return: GetSchedulerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_scheduler_info_with_options_async(request, runtime)

    def get_visual_service_status_with_options(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        """
        @summary Queries the status of the VNC service in a cluster.
        
        @param request: GetVisualServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVisualServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVisualServiceStatus',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetVisualServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_visual_service_status_with_options_async(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        """
        @summary Queries the status of the VNC service in a cluster.
        
        @param request: GetVisualServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVisualServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVisualServiceStatus',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetVisualServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_visual_service_status(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        """
        @summary Queries the status of the VNC service in a cluster.
        
        @param request: GetVisualServiceStatusRequest
        @return: GetVisualServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_visual_service_status_with_options(request, runtime)

    async def get_visual_service_status_async(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        """
        @summary Queries the status of the VNC service in a cluster.
        
        @param request: GetVisualServiceStatusRequest
        @return: GetVisualServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_visual_service_status_with_options_async(request, runtime)

    def initialize_ehpcwith_options(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        """
        @summary Creates a service-linked role for Elastic High Performance Computing (E-HPC). A service-linked role is required for you to use E-HPC.
        
        @param request: InitializeEHPCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeEHPCResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeEHPC',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InitializeEHPCResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_ehpcwith_options_async(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        """
        @summary Creates a service-linked role for Elastic High Performance Computing (E-HPC). A service-linked role is required for you to use E-HPC.
        
        @param request: InitializeEHPCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeEHPCResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeEHPC',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InitializeEHPCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_ehpc(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        """
        @summary Creates a service-linked role for Elastic High Performance Computing (E-HPC). A service-linked role is required for you to use E-HPC.
        
        @param request: InitializeEHPCRequest
        @return: InitializeEHPCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initialize_ehpcwith_options(request, runtime)

    async def initialize_ehpc_async(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        """
        @summary Creates a service-linked role for Elastic High Performance Computing (E-HPC). A service-linked role is required for you to use E-HPC.
        
        @param request: InitializeEHPCRequest
        @return: InitializeEHPCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initialize_ehpcwith_options_async(request, runtime)

    def install_software_with_options(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        """
        @summary Installs software in a cluster.
        
        @param request: InstallSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InstallSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_software_with_options_async(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        """
        @summary Installs software in a cluster.
        
        @param request: InstallSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InstallSoftwareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_software(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        """
        @summary Installs software in a cluster.
        
        @param request: InstallSoftwareRequest
        @return: InstallSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_software_with_options(request, runtime)

    async def install_software_async(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        """
        @summary Installs software in a cluster.
        
        @param request: InstallSoftwareRequest
        @return: InstallSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_software_with_options_async(request, runtime)

    def invoke_shell_command_with_options(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        """
        @summary Runs interactive commands in a cluster node.
        
        @param request: InvokeShellCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeShellCommandResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeShellCommand',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InvokeShellCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_shell_command_with_options_async(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        """
        @summary Runs interactive commands in a cluster node.
        
        @param request: InvokeShellCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeShellCommandResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeShellCommand',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InvokeShellCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_shell_command(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        """
        @summary Runs interactive commands in a cluster node.
        
        @param request: InvokeShellCommandRequest
        @return: InvokeShellCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.invoke_shell_command_with_options(request, runtime)

    async def invoke_shell_command_async(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        """
        @summary Runs interactive commands in a cluster node.
        
        @param request: InvokeShellCommandRequest
        @return: InvokeShellCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.invoke_shell_command_with_options_async(request, runtime)

    def list_available_ecs_types_with_options(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        """
        @summary Queries available Elastic Compute Service (ECS) instance types.
        
        @param request: ListAvailableEcsTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableEcsTypesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableEcsTypes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListAvailableEcsTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_ecs_types_with_options_async(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        """
        @summary Queries available Elastic Compute Service (ECS) instance types.
        
        @param request: ListAvailableEcsTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAvailableEcsTypesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableEcsTypes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListAvailableEcsTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_ecs_types(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        """
        @summary Queries available Elastic Compute Service (ECS) instance types.
        
        @param request: ListAvailableEcsTypesRequest
        @return: ListAvailableEcsTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_available_ecs_types_with_options(request, runtime)

    async def list_available_ecs_types_async(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        """
        @summary Queries available Elastic Compute Service (ECS) instance types.
        
        @param request: ListAvailableEcsTypesRequest
        @return: ListAvailableEcsTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_available_ecs_types_with_options_async(request, runtime)

    def list_cloud_metric_profilings_with_options(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        """
        @summary Queries the profiling history of a cluster.
        
        @param request: ListCloudMetricProfilingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudMetricProfilingsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudMetricProfilings',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCloudMetricProfilingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_metric_profilings_with_options_async(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        """
        @summary Queries the profiling history of a cluster.
        
        @param request: ListCloudMetricProfilingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudMetricProfilingsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudMetricProfilings',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCloudMetricProfilingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_metric_profilings(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        """
        @summary Queries the profiling history of a cluster.
        
        @param request: ListCloudMetricProfilingsRequest
        @return: ListCloudMetricProfilingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_metric_profilings_with_options(request, runtime)

    async def list_cloud_metric_profilings_async(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        """
        @summary Queries the profiling history of a cluster.
        
        @param request: ListCloudMetricProfilingsRequest
        @return: ListCloudMetricProfilingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_metric_profilings_with_options_async(request, runtime)

    def list_cluster_logs_with_options(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        """
        @summary Queries the operation logs of a cluster within the last three days.
        
        @param request: ListClusterLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterLogs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_logs_with_options_async(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        """
        @summary Queries the operation logs of a cluster within the last three days.
        
        @param request: ListClusterLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterLogs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClusterLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_logs(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        """
        @summary Queries the operation logs of a cluster within the last three days.
        
        @param request: ListClusterLogsRequest
        @return: ListClusterLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_logs_with_options(request, runtime)

    async def list_cluster_logs_async(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        """
        @summary Queries the operation logs of a cluster within the last three days.
        
        @param request: ListClusterLogsRequest
        @return: ListClusterLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_logs_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: ehpc20180412_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersResponse:
        """
        @summary Queries the list of clusters in all regions within an account.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: ehpc20180412_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersResponse:
        """
        @summary Queries the list of clusters in all regions within an account.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: ehpc20180412_models.ListClustersRequest,
    ) -> ehpc20180412_models.ListClustersResponse:
        """
        @summary Queries the list of clusters in all regions within an account.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: ehpc20180412_models.ListClustersRequest,
    ) -> ehpc20180412_models.ListClustersResponse:
        """
        @summary Queries the list of clusters in all regions within an account.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_clusters_meta_with_options(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        """
        @summary Queries the list of cluster metadata.
        
        @param request: ListClustersMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersMetaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClustersMeta',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_meta_with_options_async(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        """
        @summary Queries the list of cluster metadata.
        
        @param request: ListClustersMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersMetaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClustersMeta',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters_meta(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        """
        @summary Queries the list of cluster metadata.
        
        @param request: ListClustersMetaRequest
        @return: ListClustersMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_meta_with_options(request, runtime)

    async def list_clusters_meta_async(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        """
        @summary Queries the list of cluster metadata.
        
        @param request: ListClustersMetaRequest
        @return: ListClustersMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_meta_with_options_async(request, runtime)

    def list_commands_with_options(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommandsResponse:
        """
        @summary Queries the interactive commands in a specified cluster.
        
        @param request: ListCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommandsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommands',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_commands_with_options_async(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommandsResponse:
        """
        @summary Queries the interactive commands in a specified cluster.
        
        @param request: ListCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommandsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommands',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_commands(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
    ) -> ehpc20180412_models.ListCommandsResponse:
        """
        @summary Queries the interactive commands in a specified cluster.
        
        @param request: ListCommandsRequest
        @return: ListCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_commands_with_options(request, runtime)

    async def list_commands_async(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
    ) -> ehpc20180412_models.ListCommandsResponse:
        """
        @summary Queries the interactive commands in a specified cluster.
        
        @param request: ListCommandsRequest
        @return: ListCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_commands_with_options_async(request, runtime)

    def list_community_images_with_options(
        self,
        request: ehpc20180412_models.ListCommunityImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommunityImagesResponse:
        """
        @summary Queries a list of community images.
        
        @param request: ListCommunityImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommunityImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommunityImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommunityImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_community_images_with_options_async(
        self,
        request: ehpc20180412_models.ListCommunityImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommunityImagesResponse:
        """
        @summary Queries a list of community images.
        
        @param request: ListCommunityImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCommunityImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommunityImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommunityImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_community_images(
        self,
        request: ehpc20180412_models.ListCommunityImagesRequest,
    ) -> ehpc20180412_models.ListCommunityImagesResponse:
        """
        @summary Queries a list of community images.
        
        @param request: ListCommunityImagesRequest
        @return: ListCommunityImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_community_images_with_options(request, runtime)

    async def list_community_images_async(
        self,
        request: ehpc20180412_models.ListCommunityImagesRequest,
    ) -> ehpc20180412_models.ListCommunityImagesResponse:
        """
        @summary Queries a list of community images.
        
        @param request: ListCommunityImagesRequest
        @return: ListCommunityImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_community_images_with_options_async(request, runtime)

    def list_cpfs_file_systems_with_options(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        """
        @summary Queries the information about Cloud Paralleled File System (CPFS) and its mount targets.
        
        @param request: ListCpfsFileSystemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCpfsFileSystemsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCpfsFileSystems',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCpfsFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cpfs_file_systems_with_options_async(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        """
        @summary Queries the information about Cloud Paralleled File System (CPFS) and its mount targets.
        
        @param request: ListCpfsFileSystemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCpfsFileSystemsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCpfsFileSystems',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCpfsFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cpfs_file_systems(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        """
        @summary Queries the information about Cloud Paralleled File System (CPFS) and its mount targets.
        
        @param request: ListCpfsFileSystemsRequest
        @return: ListCpfsFileSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cpfs_file_systems_with_options(request, runtime)

    async def list_cpfs_file_systems_async(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        """
        @summary Queries the information about Cloud Paralleled File System (CPFS) and its mount targets.
        
        @param request: ListCpfsFileSystemsRequest
        @return: ListCpfsFileSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cpfs_file_systems_with_options_async(request, runtime)

    def list_current_client_version_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        """
        @summary Query the latest version number of the cluster client (ehpcutil).
        
        @param request: ListCurrentClientVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCurrentClientVersionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCurrentClientVersion',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCurrentClientVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_current_client_version_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        """
        @summary Query the latest version number of the cluster client (ehpcutil).
        
        @param request: ListCurrentClientVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCurrentClientVersionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCurrentClientVersion',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCurrentClientVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_current_client_version(self) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        """
        @summary Query the latest version number of the cluster client (ehpcutil).
        
        @return: ListCurrentClientVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_current_client_version_with_options(runtime)

    async def list_current_client_version_async(self) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        """
        @summary Query the latest version number of the cluster client (ehpcutil).
        
        @return: ListCurrentClientVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_current_client_version_with_options_async(runtime)

    def list_custom_images_with_options(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        """
        @summary Queries custom images and shared images supported by Elastic High Performance Computing (E-HPC).
        
        @param request: ListCustomImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCustomImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_images_with_options_async(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        """
        @summary Queries custom images and shared images supported by Elastic High Performance Computing (E-HPC).
        
        @param request: ListCustomImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCustomImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_images(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        """
        @summary Queries custom images and shared images supported by Elastic High Performance Computing (E-HPC).
        
        @param request: ListCustomImagesRequest
        @return: ListCustomImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    async def list_custom_images_async(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        """
        @summary Queries custom images and shared images supported by Elastic High Performance Computing (E-HPC).
        
        @param request: ListCustomImagesRequest
        @return: ListCustomImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_images_with_options_async(request, runtime)

    def list_file_system_with_mount_targets_with_options(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        """
        @summary Queries file systems and mount targets.
        
        @param request: ListFileSystemWithMountTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFileSystemWithMountTargetsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFileSystemWithMountTargets',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListFileSystemWithMountTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_system_with_mount_targets_with_options_async(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        """
        @summary Queries file systems and mount targets.
        
        @param request: ListFileSystemWithMountTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFileSystemWithMountTargetsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFileSystemWithMountTargets',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListFileSystemWithMountTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file_system_with_mount_targets(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        """
        @summary Queries file systems and mount targets.
        
        @param request: ListFileSystemWithMountTargetsRequest
        @return: ListFileSystemWithMountTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_file_system_with_mount_targets_with_options(request, runtime)

    async def list_file_system_with_mount_targets_async(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        """
        @summary Queries file systems and mount targets.
        
        @param request: ListFileSystemWithMountTargetsRequest
        @return: ListFileSystemWithMountTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_file_system_with_mount_targets_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: ehpc20180412_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListImagesResponse:
        """
        @summary Queries the list of images that can be installed in a cluster.
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: ehpc20180412_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListImagesResponse:
        """
        @summary Queries the list of images that can be installed in a cluster.
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: ehpc20180412_models.ListImagesRequest,
    ) -> ehpc20180412_models.ListImagesResponse:
        """
        @summary Queries the list of images that can be installed in a cluster.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: ehpc20180412_models.ListImagesRequest,
    ) -> ehpc20180412_models.ListImagesResponse:
        """
        @summary Queries the list of images that can be installed in a cluster.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_installed_software_with_options(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        """
        @summary Queries the software that is installed in a cluster.
        
        @param request: ListInstalledSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstalledSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstalledSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInstalledSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_installed_software_with_options_async(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        """
        @summary Queries the software that is installed in a cluster.
        
        @param request: ListInstalledSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstalledSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstalledSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInstalledSoftwareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_installed_software(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        """
        @summary Queries the software that is installed in a cluster.
        
        @param request: ListInstalledSoftwareRequest
        @return: ListInstalledSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_installed_software_with_options(request, runtime)

    async def list_installed_software_async(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        """
        @summary Queries the software that is installed in a cluster.
        
        @param request: ListInstalledSoftwareRequest
        @return: ListInstalledSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_installed_software_with_options_async(request, runtime)

    def list_invocation_results_with_options(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        """
        @summary Queries the result of an interactive command in a cluster.
        
        @param request: ListInvocationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvocationResultsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvocationResults',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_invocation_results_with_options_async(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        """
        @summary Queries the result of an interactive command in a cluster.
        
        @param request: ListInvocationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvocationResultsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvocationResults',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_invocation_results(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        """
        @summary Queries the result of an interactive command in a cluster.
        
        @param request: ListInvocationResultsRequest
        @return: ListInvocationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_results_with_options(request, runtime)

    async def list_invocation_results_async(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        """
        @summary Queries the result of an interactive command in a cluster.
        
        @param request: ListInvocationResultsRequest
        @return: ListInvocationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_invocation_results_with_options_async(request, runtime)

    def list_invocation_status_with_options(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        """
        @summary Queries the status of an interactive command.
        
        @param request: ListInvocationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvocationStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvocationStatus',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_invocation_status_with_options_async(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        """
        @summary Queries the status of an interactive command.
        
        @param request: ListInvocationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvocationStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvocationStatus',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_invocation_status(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        """
        @summary Queries the status of an interactive command.
        
        @param request: ListInvocationStatusRequest
        @return: ListInvocationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_status_with_options(request, runtime)

    async def list_invocation_status_async(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        """
        @summary Queries the status of an interactive command.
        
        @param request: ListInvocationStatusRequest
        @return: ListInvocationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_invocation_status_with_options_async(request, runtime)

    def list_job_templates_with_options(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        """
        @summary Queries the list of job templates.
        
        @param request: ListJobTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobTemplates',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_templates_with_options_async(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        """
        @summary Queries the list of job templates.
        
        @param request: ListJobTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobTemplates',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_templates(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        """
        @summary Queries the list of job templates.
        
        @param request: ListJobTemplatesRequest
        @return: ListJobTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_job_templates_with_options(request, runtime)

    async def list_job_templates_async(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        """
        @summary Queries the list of job templates.
        
        @param request: ListJobTemplatesRequest
        @return: ListJobTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_job_templates_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: ehpc20180412_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsResponse:
        """
        @summary Queries the list of jobs in a cluster.
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: ehpc20180412_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsResponse:
        """
        @summary Queries the list of jobs in a cluster.
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: ehpc20180412_models.ListJobsRequest,
    ) -> ehpc20180412_models.ListJobsResponse:
        """
        @summary Queries the list of jobs in a cluster.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: ehpc20180412_models.ListJobsRequest,
    ) -> ehpc20180412_models.ListJobsResponse:
        """
        @summary Queries the list of jobs in a cluster.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_jobs_with_filters_with_options(
        self,
        request: ehpc20180412_models.ListJobsWithFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsWithFiltersResponse:
        """
        @summary Queries the details of a specified job.
        
        @param request: ListJobsWithFiltersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsWithFiltersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobsWithFilters',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsWithFiltersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_filters_with_options_async(
        self,
        request: ehpc20180412_models.ListJobsWithFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsWithFiltersResponse:
        """
        @summary Queries the details of a specified job.
        
        @param request: ListJobsWithFiltersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsWithFiltersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobsWithFilters',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsWithFiltersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs_with_filters(
        self,
        request: ehpc20180412_models.ListJobsWithFiltersRequest,
    ) -> ehpc20180412_models.ListJobsWithFiltersResponse:
        """
        @summary Queries the details of a specified job.
        
        @param request: ListJobsWithFiltersRequest
        @return: ListJobsWithFiltersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_filters_with_options(request, runtime)

    async def list_jobs_with_filters_async(
        self,
        request: ehpc20180412_models.ListJobsWithFiltersRequest,
    ) -> ehpc20180412_models.ListJobsWithFiltersResponse:
        """
        @summary Queries the details of a specified job.
        
        @param request: ListJobsWithFiltersRequest
        @return: ListJobsWithFiltersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_filters_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: ehpc20180412_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesResponse:
        """
        @summary Queries the list of nodes in a cluster.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: ehpc20180412_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesResponse:
        """
        @summary Queries the list of nodes in a cluster.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: ehpc20180412_models.ListNodesRequest,
    ) -> ehpc20180412_models.ListNodesResponse:
        """
        @summary Queries the list of nodes in a cluster.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: ehpc20180412_models.ListNodesRequest,
    ) -> ehpc20180412_models.ListNodesResponse:
        """
        @summary Queries the list of nodes in a cluster.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_nodes_by_queue_with_options(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        """
        @summary Queries the node information of a single cluster within an Alibaba Cloud account by queue.
        
        @param request: ListNodesByQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesByQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesByQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesByQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_by_queue_with_options_async(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        """
        @summary Queries the node information of a single cluster within an Alibaba Cloud account by queue.
        
        @param request: ListNodesByQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesByQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesByQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesByQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes_by_queue(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        """
        @summary Queries the node information of a single cluster within an Alibaba Cloud account by queue.
        
        @param request: ListNodesByQueueRequest
        @return: ListNodesByQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_queue_with_options(request, runtime)

    async def list_nodes_by_queue_async(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        """
        @summary Queries the node information of a single cluster within an Alibaba Cloud account by queue.
        
        @param request: ListNodesByQueueRequest
        @return: ListNodesByQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_by_queue_with_options_async(request, runtime)

    def list_nodes_no_paging_with_options(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        """
        @summary Queries the information of all nodes in a specified cluster on one page.
        
        @param request: ListNodesNoPagingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesNoPagingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesNoPaging',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesNoPagingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_no_paging_with_options_async(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        """
        @summary Queries the information of all nodes in a specified cluster on one page.
        
        @param request: ListNodesNoPagingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesNoPagingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesNoPaging',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesNoPagingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes_no_paging(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        """
        @summary Queries the information of all nodes in a specified cluster on one page.
        
        @param request: ListNodesNoPagingRequest
        @return: ListNodesNoPagingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_no_paging_with_options(request, runtime)

    async def list_nodes_no_paging_async(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        """
        @summary Queries the information of all nodes in a specified cluster on one page.
        
        @param request: ListNodesNoPagingRequest
        @return: ListNodesNoPagingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_no_paging_with_options_async(request, runtime)

    def list_preferred_ecs_types_with_options(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instance types recommended by Elastic High Performance Computing (E-HPC).
        
        @param request: ListPreferredEcsTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPreferredEcsTypesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPreferredEcsTypes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListPreferredEcsTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_preferred_ecs_types_with_options_async(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instance types recommended by Elastic High Performance Computing (E-HPC).
        
        @param request: ListPreferredEcsTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPreferredEcsTypesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPreferredEcsTypes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListPreferredEcsTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_preferred_ecs_types(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instance types recommended by Elastic High Performance Computing (E-HPC).
        
        @param request: ListPreferredEcsTypesRequest
        @return: ListPreferredEcsTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_preferred_ecs_types_with_options(request, runtime)

    async def list_preferred_ecs_types_async(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instance types recommended by Elastic High Performance Computing (E-HPC).
        
        @param request: ListPreferredEcsTypesRequest
        @return: ListPreferredEcsTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_preferred_ecs_types_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListQueuesResponse:
        """
        @summary Queries the queues of a specified cluster.
        
        @param request: ListQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueuesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queues_with_options_async(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListQueuesResponse:
        """
        @summary Queries the queues of a specified cluster.
        
        @param request: ListQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueuesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queues(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
    ) -> ehpc20180412_models.ListQueuesResponse:
        """
        @summary Queries the queues of a specified cluster.
        
        @param request: ListQueuesRequest
        @return: ListQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
    ) -> ehpc20180412_models.ListQueuesResponse:
        """
        @summary Queries the queues of a specified cluster.
        
        @param request: ListQueuesRequest
        @return: ListQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListRegionsResponse:
        """
        @summary Queries a list of regions where Elastic High Performance Computing (E-HPC) is supported.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListRegionsResponse:
        """
        @summary Queries a list of regions where Elastic High Performance Computing (E-HPC) is supported.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> ehpc20180412_models.ListRegionsResponse:
        """
        @summary Queries a list of regions where Elastic High Performance Computing (E-HPC) is supported.
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> ehpc20180412_models.ListRegionsResponse:
        """
        @summary Queries a list of regions where Elastic High Performance Computing (E-HPC) is supported.
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_security_groups_with_options(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        """
        @summary Queries the security groups that are assigned to an E-HPC cluster.
        
        @param request: ListSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityGroups',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_groups_with_options_async(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        """
        @summary Queries the security groups that are assigned to an E-HPC cluster.
        
        @param request: ListSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityGroups',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_groups(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        """
        @summary Queries the security groups that are assigned to an E-HPC cluster.
        
        @param request: ListSecurityGroupsRequest
        @return: ListSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_security_groups_with_options(request, runtime)

    async def list_security_groups_async(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        """
        @summary Queries the security groups that are assigned to an E-HPC cluster.
        
        @param request: ListSecurityGroupsRequest
        @return: ListSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_security_groups_with_options_async(request, runtime)

    def list_serverless_jobs_with_options(
        self,
        request: ehpc20180412_models.ListServerlessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListServerlessJobsResponse:
        """
        @summary Queries the list of serverless jobs based on filter conditions.
        
        @param request: ListServerlessJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerlessJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.job_names):
            query['JobNames'] = request.job_names
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_order):
            query['StartOrder'] = request.start_order
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.submit_order):
            query['SubmitOrder'] = request.submit_order
        if not UtilClient.is_unset(request.submit_time_end):
            query['SubmitTimeEnd'] = request.submit_time_end
        if not UtilClient.is_unset(request.submit_time_start):
            query['SubmitTimeStart'] = request.submit_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListServerlessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_serverless_jobs_with_options_async(
        self,
        request: ehpc20180412_models.ListServerlessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListServerlessJobsResponse:
        """
        @summary Queries the list of serverless jobs based on filter conditions.
        
        @param request: ListServerlessJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerlessJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.job_names):
            query['JobNames'] = request.job_names
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_order):
            query['StartOrder'] = request.start_order
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.submit_order):
            query['SubmitOrder'] = request.submit_order
        if not UtilClient.is_unset(request.submit_time_end):
            query['SubmitTimeEnd'] = request.submit_time_end
        if not UtilClient.is_unset(request.submit_time_start):
            query['SubmitTimeStart'] = request.submit_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListServerlessJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_serverless_jobs(
        self,
        request: ehpc20180412_models.ListServerlessJobsRequest,
    ) -> ehpc20180412_models.ListServerlessJobsResponse:
        """
        @summary Queries the list of serverless jobs based on filter conditions.
        
        @param request: ListServerlessJobsRequest
        @return: ListServerlessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_serverless_jobs_with_options(request, runtime)

    async def list_serverless_jobs_async(
        self,
        request: ehpc20180412_models.ListServerlessJobsRequest,
    ) -> ehpc20180412_models.ListServerlessJobsResponse:
        """
        @summary Queries the list of serverless jobs based on filter conditions.
        
        @param request: ListServerlessJobsRequest
        @return: ListServerlessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_serverless_jobs_with_options_async(request, runtime)

    def list_softwares_with_options(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        """
        @summary Queries the list of software that can be installed in a cluster.
        
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
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_softwares_with_options_async(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        """
        @summary Queries the list of software that can be installed in a cluster.
        
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
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_softwares(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        """
        @summary Queries the list of software that can be installed in a cluster.
        
        @param request: ListSoftwaresRequest
        @return: ListSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    async def list_softwares_async(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        """
        @summary Queries the list of software that can be installed in a cluster.
        
        @param request: ListSoftwaresRequest
        @return: ListSoftwaresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_softwares_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ehpc20180412_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a specified resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ehpc20180412_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a specified resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ehpc20180412_models.ListTagResourcesRequest,
    ) -> ehpc20180412_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a specified resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ehpc20180412_models.ListTagResourcesRequest,
    ) -> ehpc20180412_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are attached to a specified resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: ehpc20180412_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTasksResponse:
        """
        @summary Queries the response of an asynchronous API operation for a cluster.
        
        @description For some asynchronous API operations such as AddNodes, the system immediately returns a result without waiting for the node to be created if the request succeeds. In this case, you can use the TaskId returned by the asynchronous API operation to query the result of the task.
        
        @param request: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: ehpc20180412_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTasksResponse:
        """
        @summary Queries the response of an asynchronous API operation for a cluster.
        
        @description For some asynchronous API operations such as AddNodes, the system immediately returns a result without waiting for the node to be created if the request succeeds. In this case, you can use the TaskId returned by the asynchronous API operation to query the result of the task.
        
        @param request: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: ehpc20180412_models.ListTasksRequest,
    ) -> ehpc20180412_models.ListTasksResponse:
        """
        @summary Queries the response of an asynchronous API operation for a cluster.
        
        @description For some asynchronous API operations such as AddNodes, the system immediately returns a result without waiting for the node to be created if the request succeeds. In this case, you can use the TaskId returned by the asynchronous API operation to query the result of the task.
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: ehpc20180412_models.ListTasksRequest,
    ) -> ehpc20180412_models.ListTasksResponse:
        """
        @summary Queries the response of an asynchronous API operation for a cluster.
        
        @description For some asynchronous API operations such as AddNodes, the system immediately returns a result without waiting for the node to be created if the request succeeds. In this case, you can use the TaskId returned by the asynchronous API operation to query the result of the task.
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_upgrade_clients_with_options(
        self,
        request: ehpc20180412_models.ListUpgradeClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUpgradeClientsResponse:
        """
        @summary Queries the latest version to which the client (ehpcutil) in a cluster can be updated and historical update records of the client.
        
        @param request: ListUpgradeClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpgradeClientsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUpgradeClients',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUpgradeClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upgrade_clients_with_options_async(
        self,
        request: ehpc20180412_models.ListUpgradeClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUpgradeClientsResponse:
        """
        @summary Queries the latest version to which the client (ehpcutil) in a cluster can be updated and historical update records of the client.
        
        @param request: ListUpgradeClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUpgradeClientsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUpgradeClients',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUpgradeClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upgrade_clients(
        self,
        request: ehpc20180412_models.ListUpgradeClientsRequest,
    ) -> ehpc20180412_models.ListUpgradeClientsResponse:
        """
        @summary Queries the latest version to which the client (ehpcutil) in a cluster can be updated and historical update records of the client.
        
        @param request: ListUpgradeClientsRequest
        @return: ListUpgradeClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_upgrade_clients_with_options(request, runtime)

    async def list_upgrade_clients_async(
        self,
        request: ehpc20180412_models.ListUpgradeClientsRequest,
    ) -> ehpc20180412_models.ListUpgradeClientsResponse:
        """
        @summary Queries the latest version to which the client (ehpcutil) in a cluster can be updated and historical update records of the client.
        
        @param request: ListUpgradeClientsRequest
        @return: ListUpgradeClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_upgrade_clients_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ehpc20180412_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersResponse:
        """
        @summary Queries all users of a cluster.
        
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
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ehpc20180412_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersResponse:
        """
        @summary Queries all users of a cluster.
        
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
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: ehpc20180412_models.ListUsersRequest,
    ) -> ehpc20180412_models.ListUsersResponse:
        """
        @summary Queries all users of a cluster.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ehpc20180412_models.ListUsersRequest,
    ) -> ehpc20180412_models.ListUsersResponse:
        """
        @summary Queries all users of a cluster.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_async_with_options(
        self,
        request: ehpc20180412_models.ListUsersAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersAsyncResponse:
        """
        @summary Queries the users in a cluster.
        
        @param request: ListUsersAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersAsyncResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersAsync',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_async_with_options_async(
        self,
        request: ehpc20180412_models.ListUsersAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersAsyncResponse:
        """
        @summary Queries the users in a cluster.
        
        @param request: ListUsersAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersAsyncResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersAsync',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_async(
        self,
        request: ehpc20180412_models.ListUsersAsyncRequest,
    ) -> ehpc20180412_models.ListUsersAsyncResponse:
        """
        @summary Queries the users in a cluster.
        
        @param request: ListUsersAsyncRequest
        @return: ListUsersAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_async_with_options(request, runtime)

    async def list_users_async_async(
        self,
        request: ehpc20180412_models.ListUsersAsyncRequest,
    ) -> ehpc20180412_models.ListUsersAsyncResponse:
        """
        @summary Queries the users in a cluster.
        
        @param request: ListUsersAsyncRequest
        @return: ListUsersAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_async_with_options_async(request, runtime)

    def list_volumes_with_options(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListVolumesResponse:
        """
        @summary Queries the file systems mounted on Elastic High Performance Computing (E-HPC) clusters.
        
        @param request: ListVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVolumesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_volumes_with_options_async(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListVolumesResponse:
        """
        @summary Queries the file systems mounted on Elastic High Performance Computing (E-HPC) clusters.
        
        @param request: ListVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVolumesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_volumes(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
    ) -> ehpc20180412_models.ListVolumesResponse:
        """
        @summary Queries the file systems mounted on Elastic High Performance Computing (E-HPC) clusters.
        
        @param request: ListVolumesRequest
        @return: ListVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_volumes_with_options(request, runtime)

    async def list_volumes_async(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
    ) -> ehpc20180412_models.ListVolumesResponse:
        """
        @summary Queries the file systems mounted on Elastic High Performance Computing (E-HPC) clusters.
        
        @param request: ListVolumesRequest
        @return: ListVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_volumes_with_options_async(request, runtime)

    def modify_cluster_attributes_with_options(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        """
        @summary Modifies the basic information of a cluster, including the name, description, and image.
        
        @description ## Usage notes
        Before you call this operation, you can call the [DescribeCluster](https://help.aliyun.com/document_detail/87126.html) operation to query details of the selected cluster.
        
        @param request: ModifyClusterAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterAttributesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAttributes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyClusterAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_attributes_with_options_async(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        """
        @summary Modifies the basic information of a cluster, including the name, description, and image.
        
        @description ## Usage notes
        Before you call this operation, you can call the [DescribeCluster](https://help.aliyun.com/document_detail/87126.html) operation to query details of the selected cluster.
        
        @param request: ModifyClusterAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterAttributesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAttributes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyClusterAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_attributes(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        """
        @summary Modifies the basic information of a cluster, including the name, description, and image.
        
        @description ## Usage notes
        Before you call this operation, you can call the [DescribeCluster](https://help.aliyun.com/document_detail/87126.html) operation to query details of the selected cluster.
        
        @param request: ModifyClusterAttributesRequest
        @return: ModifyClusterAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_attributes_with_options(request, runtime)

    async def modify_cluster_attributes_async(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        """
        @summary Modifies the basic information of a cluster, including the name, description, and image.
        
        @description ## Usage notes
        Before you call this operation, you can call the [DescribeCluster](https://help.aliyun.com/document_detail/87126.html) operation to query details of the selected cluster.
        
        @param request: ModifyClusterAttributesRequest
        @return: ModifyClusterAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_attributes_with_options_async(request, runtime)

    def modify_user_groups_with_options(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        """
        @summary Changes the user group to which users belong.
        
        @param request: ModifyUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroups',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_groups_with_options_async(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        """
        @summary Changes the user group to which users belong.
        
        @param request: ModifyUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroups',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_groups(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        """
        @summary Changes the user group to which users belong.
        
        @param request: ModifyUserGroupsRequest
        @return: ModifyUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_groups_with_options(request, runtime)

    async def modify_user_groups_async(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        """
        @summary Changes the user group to which users belong.
        
        @param request: ModifyUserGroupsRequest
        @return: ModifyUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_groups_with_options_async(request, runtime)

    def modify_user_passwords_with_options(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        """
        @summary Changes the passwords of users.
        
        @param request: ModifyUserPasswordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserPasswordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPasswords',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserPasswordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_passwords_with_options_async(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        """
        @summary Changes the passwords of users.
        
        @param request: ModifyUserPasswordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserPasswordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPasswords',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserPasswordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_passwords(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        """
        @summary Changes the passwords of users.
        
        @param request: ModifyUserPasswordsRequest
        @return: ModifyUserPasswordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_passwords_with_options(request, runtime)

    async def modify_user_passwords_async(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        """
        @summary Changes the passwords of users.
        
        @param request: ModifyUserPasswordsRequest
        @return: ModifyUserPasswordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_passwords_with_options_async(request, runtime)

    def modify_visual_service_passwd_with_options(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        """
        @summary Sets a password that you can use to remotely connect to a visualization service in a cluster over the virtual network console (VNC).
        
        @param request: ModifyVisualServicePasswdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVisualServicePasswdResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVisualServicePasswd',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyVisualServicePasswdResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_visual_service_passwd_with_options_async(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        """
        @summary Sets a password that you can use to remotely connect to a visualization service in a cluster over the virtual network console (VNC).
        
        @param request: ModifyVisualServicePasswdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVisualServicePasswdResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVisualServicePasswd',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyVisualServicePasswdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_visual_service_passwd(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        """
        @summary Sets a password that you can use to remotely connect to a visualization service in a cluster over the virtual network console (VNC).
        
        @param request: ModifyVisualServicePasswdRequest
        @return: ModifyVisualServicePasswdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_visual_service_passwd_with_options(request, runtime)

    async def modify_visual_service_passwd_async(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        """
        @summary Sets a password that you can use to remotely connect to a visualization service in a cluster over the virtual network console (VNC).
        
        @param request: ModifyVisualServicePasswdRequest
        @return: ModifyVisualServicePasswdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_visual_service_passwd_with_options_async(request, runtime)

    def pull_image_with_options(
        self,
        request: ehpc20180412_models.PullImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.PullImageResponse:
        """
        @param request: PullImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullImageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.PullImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def pull_image_with_options_async(
        self,
        request: ehpc20180412_models.PullImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.PullImageResponse:
        """
        @param request: PullImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullImageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.PullImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pull_image(
        self,
        request: ehpc20180412_models.PullImageRequest,
    ) -> ehpc20180412_models.PullImageResponse:
        """
        @param request: PullImageRequest
        @return: PullImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pull_image_with_options(request, runtime)

    async def pull_image_async(
        self,
        request: ehpc20180412_models.PullImageRequest,
    ) -> ehpc20180412_models.PullImageResponse:
        """
        @param request: PullImageRequest
        @return: PullImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pull_image_with_options_async(request, runtime)

    def query_service_pack_and_price_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        """
        @param request: QueryServicePackAndPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryServicePackAndPriceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryServicePackAndPrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.QueryServicePackAndPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_service_pack_and_price_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        """
        @param request: QueryServicePackAndPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryServicePackAndPriceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryServicePackAndPrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.QueryServicePackAndPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_service_pack_and_price(self) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        """
        @return: QueryServicePackAndPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_service_pack_and_price_with_options(runtime)

    async def query_service_pack_and_price_async(self) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        """
        @return: QueryServicePackAndPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_service_pack_and_price_with_options_async(runtime)

    def recover_cluster_with_options(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        """
        @summary Resets and restores a cluster.
        
        @description You can call the operation to reset and restore a cluster only when the cluster is in the Exception state. You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the ID and status of a cluster. We recommend that you export all job data before you restore a cluster. When you reset and restore a cluster, take note of the following impacts:
        The system disks of all nodes are changed. By default, new system disks are configured based on the settings that you specified when the cluster was created.
        The data on the system disks and data disks of all cluster nodes is lost. The data includes user information, job information, scheduler queue information, and configuration data of auto-scaling queues. However, the data on File Storage NAS file systems is retained.
        The self-managed queues in the cluster are deleted. All nodes are retained and migrated to the default queue of the cluster.
        
        @param request: RecoverClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RecoverClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_cluster_with_options_async(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        """
        @summary Resets and restores a cluster.
        
        @description You can call the operation to reset and restore a cluster only when the cluster is in the Exception state. You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the ID and status of a cluster. We recommend that you export all job data before you restore a cluster. When you reset and restore a cluster, take note of the following impacts:
        The system disks of all nodes are changed. By default, new system disks are configured based on the settings that you specified when the cluster was created.
        The data on the system disks and data disks of all cluster nodes is lost. The data includes user information, job information, scheduler queue information, and configuration data of auto-scaling queues. However, the data on File Storage NAS file systems is retained.
        The self-managed queues in the cluster are deleted. All nodes are retained and migrated to the default queue of the cluster.
        
        @param request: RecoverClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RecoverClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_cluster(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        """
        @summary Resets and restores a cluster.
        
        @description You can call the operation to reset and restore a cluster only when the cluster is in the Exception state. You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the ID and status of a cluster. We recommend that you export all job data before you restore a cluster. When you reset and restore a cluster, take note of the following impacts:
        The system disks of all nodes are changed. By default, new system disks are configured based on the settings that you specified when the cluster was created.
        The data on the system disks and data disks of all cluster nodes is lost. The data includes user information, job information, scheduler queue information, and configuration data of auto-scaling queues. However, the data on File Storage NAS file systems is retained.
        The self-managed queues in the cluster are deleted. All nodes are retained and migrated to the default queue of the cluster.
        
        @param request: RecoverClusterRequest
        @return: RecoverClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recover_cluster_with_options(request, runtime)

    async def recover_cluster_async(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        """
        @summary Resets and restores a cluster.
        
        @description You can call the operation to reset and restore a cluster only when the cluster is in the Exception state. You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the ID and status of a cluster. We recommend that you export all job data before you restore a cluster. When you reset and restore a cluster, take note of the following impacts:
        The system disks of all nodes are changed. By default, new system disks are configured based on the settings that you specified when the cluster was created.
        The data on the system disks and data disks of all cluster nodes is lost. The data includes user information, job information, scheduler queue information, and configuration data of auto-scaling queues. However, the data on File Storage NAS file systems is retained.
        The self-managed queues in the cluster are deleted. All nodes are retained and migrated to the default queue of the cluster.
        
        @param request: RecoverClusterRequest
        @return: RecoverClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recover_cluster_with_options_async(request, runtime)

    def rerun_jobs_with_options(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RerunJobsResponse:
        """
        @param request: RerunJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RerunJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RerunJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_jobs_with_options_async(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RerunJobsResponse:
        """
        @param request: RerunJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RerunJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RerunJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_jobs(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
    ) -> ehpc20180412_models.RerunJobsResponse:
        """
        @param request: RerunJobsRequest
        @return: RerunJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rerun_jobs_with_options(request, runtime)

    async def rerun_jobs_async(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
    ) -> ehpc20180412_models.RerunJobsResponse:
        """
        @param request: RerunJobsRequest
        @return: RerunJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rerun_jobs_with_options_async(request, runtime)

    def reset_nodes_with_options(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ResetNodesResponse:
        """
        @description After a node is reset, the operating system and software return to their initial states. To ensure that jobs run as expected, we recommend that you do not reset running nodes unless you need to perform crash recovery.
        
        @param request: ResetNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ResetNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_nodes_with_options_async(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ResetNodesResponse:
        """
        @description After a node is reset, the operating system and software return to their initial states. To ensure that jobs run as expected, we recommend that you do not reset running nodes unless you need to perform crash recovery.
        
        @param request: ResetNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ResetNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_nodes(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
    ) -> ehpc20180412_models.ResetNodesResponse:
        """
        @description After a node is reset, the operating system and software return to their initial states. To ensure that jobs run as expected, we recommend that you do not reset running nodes unless you need to perform crash recovery.
        
        @param request: ResetNodesRequest
        @return: ResetNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_nodes_with_options(request, runtime)

    async def reset_nodes_async(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
    ) -> ehpc20180412_models.ResetNodesResponse:
        """
        @description After a node is reset, the operating system and software return to their initial states. To ensure that jobs run as expected, we recommend that you do not reset running nodes unless you need to perform crash recovery.
        
        @param request: ResetNodesRequest
        @return: ResetNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_nodes_with_options_async(request, runtime)

    def run_cloud_metric_profiling_with_options(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        """
        @summary Starts the profiling process of a cluster.
        
        @param request: RunCloudMetricProfilingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCloudMetricProfilingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCloudMetricProfiling',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RunCloudMetricProfilingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cloud_metric_profiling_with_options_async(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        """
        @summary Starts the profiling process of a cluster.
        
        @param request: RunCloudMetricProfilingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCloudMetricProfilingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCloudMetricProfiling',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RunCloudMetricProfilingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_cloud_metric_profiling(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        """
        @summary Starts the profiling process of a cluster.
        
        @param request: RunCloudMetricProfilingRequest
        @return: RunCloudMetricProfilingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_metric_profiling_with_options(request, runtime)

    async def run_cloud_metric_profiling_async(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        """
        @summary Starts the profiling process of a cluster.
        
        @param request: RunCloudMetricProfilingRequest
        @return: RunCloudMetricProfilingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_cloud_metric_profiling_with_options_async(request, runtime)

    def set_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        """
        @summary Configures the auto scaling settings of a cluster.
        
        @description ## Usage notes
        If the settings in the Queue Configuration section are different from the settings in the Global Configurations section, the former prevails.
        
        @param request: SetAutoScaleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_auto_scale_config_with_options_async(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        """
        @summary Configures the auto scaling settings of a cluster.
        
        @description ## Usage notes
        If the settings in the Queue Configuration section are different from the settings in the Global Configurations section, the former prevails.
        
        @param request: SetAutoScaleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetAutoScaleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_auto_scale_config(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        """
        @summary Configures the auto scaling settings of a cluster.
        
        @description ## Usage notes
        If the settings in the Queue Configuration section are different from the settings in the Global Configurations section, the former prevails.
        
        @param request: SetAutoScaleConfigRequest
        @return: SetAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_auto_scale_config_with_options(request, runtime)

    async def set_auto_scale_config_async(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        """
        @summary Configures the auto scaling settings of a cluster.
        
        @description ## Usage notes
        If the settings in the Queue Configuration section are different from the settings in the Global Configurations section, the former prevails.
        
        @param request: SetAutoScaleConfigRequest
        @return: SetAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_auto_scale_config_with_options_async(request, runtime)

    def set_post_scripts_with_options(
        self,
        request: ehpc20180412_models.SetPostScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetPostScriptsResponse:
        """
        @summary Configures the post-processing scripts of a cluster.
        
        @param request: SetPostScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPostScriptsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPostScripts',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetPostScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_post_scripts_with_options_async(
        self,
        request: ehpc20180412_models.SetPostScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetPostScriptsResponse:
        """
        @summary Configures the post-processing scripts of a cluster.
        
        @param request: SetPostScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPostScriptsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPostScripts',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetPostScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_post_scripts(
        self,
        request: ehpc20180412_models.SetPostScriptsRequest,
    ) -> ehpc20180412_models.SetPostScriptsResponse:
        """
        @summary Configures the post-processing scripts of a cluster.
        
        @param request: SetPostScriptsRequest
        @return: SetPostScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_post_scripts_with_options(request, runtime)

    async def set_post_scripts_async(
        self,
        request: ehpc20180412_models.SetPostScriptsRequest,
    ) -> ehpc20180412_models.SetPostScriptsResponse:
        """
        @summary Configures the post-processing scripts of a cluster.
        
        @param request: SetPostScriptsRequest
        @return: SetPostScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_post_scripts_with_options_async(request, runtime)

    def set_queue_with_options(
        self,
        request: ehpc20180412_models.SetQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetQueueResponse:
        """
        @param request: SetQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_queue_with_options_async(
        self,
        request: ehpc20180412_models.SetQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetQueueResponse:
        """
        @param request: SetQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetQueueResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_queue(
        self,
        request: ehpc20180412_models.SetQueueRequest,
    ) -> ehpc20180412_models.SetQueueResponse:
        """
        @param request: SetQueueRequest
        @return: SetQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_queue_with_options(request, runtime)

    async def set_queue_async(
        self,
        request: ehpc20180412_models.SetQueueRequest,
    ) -> ehpc20180412_models.SetQueueResponse:
        """
        @param request: SetQueueRequest
        @return: SetQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_queue_with_options_async(request, runtime)

    def set_scheduler_info_with_options(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        """
        @summary Configures the scheduler settings of a cluster.
        
        @param request: SetSchedulerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSchedulerInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSchedulerInfo',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetSchedulerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scheduler_info_with_options_async(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        """
        @summary Configures the scheduler settings of a cluster.
        
        @param request: SetSchedulerInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSchedulerInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSchedulerInfo',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetSchedulerInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scheduler_info(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        """
        @summary Configures the scheduler settings of a cluster.
        
        @param request: SetSchedulerInfoRequest
        @return: SetSchedulerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_scheduler_info_with_options(request, runtime)

    async def set_scheduler_info_async(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        """
        @summary Configures the scheduler settings of a cluster.
        
        @param request: SetSchedulerInfoRequest
        @return: SetSchedulerInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_scheduler_info_with_options_async(request, runtime)

    def start_cluster_with_options(
        self,
        request: ehpc20180412_models.StartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartClusterResponse:
        """
        @param request: StartClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cluster_with_options_async(
        self,
        request: ehpc20180412_models.StartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartClusterResponse:
        """
        @param request: StartClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cluster(
        self,
        request: ehpc20180412_models.StartClusterRequest,
    ) -> ehpc20180412_models.StartClusterResponse:
        """
        @param request: StartClusterRequest
        @return: StartClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_cluster_with_options(request, runtime)

    async def start_cluster_async(
        self,
        request: ehpc20180412_models.StartClusterRequest,
    ) -> ehpc20180412_models.StartClusterResponse:
        """
        @param request: StartClusterRequest
        @return: StartClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_cluster_with_options_async(request, runtime)

    def start_nodes_with_options(
        self,
        request: ehpc20180412_models.StartNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartNodesResponse:
        """
        @param request: StartNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_nodes_with_options_async(
        self,
        request: ehpc20180412_models.StartNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartNodesResponse:
        """
        @param request: StartNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_nodes(
        self,
        request: ehpc20180412_models.StartNodesRequest,
    ) -> ehpc20180412_models.StartNodesResponse:
        """
        @param request: StartNodesRequest
        @return: StartNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_nodes_with_options(request, runtime)

    async def start_nodes_async(
        self,
        request: ehpc20180412_models.StartNodesRequest,
    ) -> ehpc20180412_models.StartNodesResponse:
        """
        @param request: StartNodesRequest
        @return: StartNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_nodes_with_options_async(request, runtime)

    def start_visual_service_with_options(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        """
        @summary Starts the Virtual Network Console (VNC) Remote visualization service in a specified cluster.
        
        @param request: StartVisualServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartVisualServiceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVisualService',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartVisualServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_visual_service_with_options_async(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        """
        @summary Starts the Virtual Network Console (VNC) Remote visualization service in a specified cluster.
        
        @param request: StartVisualServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartVisualServiceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVisualService',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartVisualServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_visual_service(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        """
        @summary Starts the Virtual Network Console (VNC) Remote visualization service in a specified cluster.
        
        @param request: StartVisualServiceRequest
        @return: StartVisualServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_visual_service_with_options(request, runtime)

    async def start_visual_service_async(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        """
        @summary Starts the Virtual Network Console (VNC) Remote visualization service in a specified cluster.
        
        @param request: StartVisualServiceRequest
        @return: StartVisualServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_visual_service_with_options_async(request, runtime)

    def stop_cluster_with_options(
        self,
        request: ehpc20180412_models.StopClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopClusterResponse:
        """
        @summary Stops a cluster.
        
        @description If you stop a subscription compute node, its billing is not affected. If you stop a pay-as-you-go compute node for which you have enabled the economical mode*, you are no longer charged for its computing resources. For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        
        @param request: StopClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cluster_with_options_async(
        self,
        request: ehpc20180412_models.StopClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopClusterResponse:
        """
        @summary Stops a cluster.
        
        @description If you stop a subscription compute node, its billing is not affected. If you stop a pay-as-you-go compute node for which you have enabled the economical mode*, you are no longer charged for its computing resources. For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        
        @param request: StopClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cluster(
        self,
        request: ehpc20180412_models.StopClusterRequest,
    ) -> ehpc20180412_models.StopClusterResponse:
        """
        @summary Stops a cluster.
        
        @description If you stop a subscription compute node, its billing is not affected. If you stop a pay-as-you-go compute node for which you have enabled the economical mode*, you are no longer charged for its computing resources. For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        
        @param request: StopClusterRequest
        @return: StopClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_cluster_with_options(request, runtime)

    async def stop_cluster_async(
        self,
        request: ehpc20180412_models.StopClusterRequest,
    ) -> ehpc20180412_models.StopClusterResponse:
        """
        @summary Stops a cluster.
        
        @description If you stop a subscription compute node, its billing is not affected. If you stop a pay-as-you-go compute node for which you have enabled the economical mode*, you are no longer charged for its computing resources. For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        
        @param request: StopClusterRequest
        @return: StopClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_cluster_with_options_async(request, runtime)

    def stop_jobs_with_options(
        self,
        request: ehpc20180412_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopJobsResponse:
        """
        @param request: StopJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_jobs_with_options_async(
        self,
        request: ehpc20180412_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopJobsResponse:
        """
        @param request: StopJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_jobs(
        self,
        request: ehpc20180412_models.StopJobsRequest,
    ) -> ehpc20180412_models.StopJobsResponse:
        """
        @param request: StopJobsRequest
        @return: StopJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    async def stop_jobs_async(
        self,
        request: ehpc20180412_models.StopJobsRequest,
    ) -> ehpc20180412_models.StopJobsResponse:
        """
        @param request: StopJobsRequest
        @return: StopJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_jobs_with_options_async(request, runtime)

    def stop_nodes_with_options(
        self,
        request: ehpc20180412_models.StopNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopNodesResponse:
        """
        @param request: StopNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_nodes_with_options_async(
        self,
        request: ehpc20180412_models.StopNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopNodesResponse:
        """
        @param request: StopNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_nodes(
        self,
        request: ehpc20180412_models.StopNodesRequest,
    ) -> ehpc20180412_models.StopNodesResponse:
        """
        @param request: StopNodesRequest
        @return: StopNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_nodes_with_options(request, runtime)

    async def stop_nodes_async(
        self,
        request: ehpc20180412_models.StopNodesRequest,
    ) -> ehpc20180412_models.StopNodesResponse:
        """
        @param request: StopNodesRequest
        @return: StopNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_nodes_with_options_async(request, runtime)

    def stop_serverless_jobs_with_options(
        self,
        request: ehpc20180412_models.StopServerlessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopServerlessJobsResponse:
        """
        @summary Stops Serverless jobs in a cluster based on job IDs or subtask IDs (array jobs). If you specify the job ID of an array job, all subtasks in the job are stopped.
        
        @param request: StopServerlessJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopServerlessJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopServerlessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_serverless_jobs_with_options_async(
        self,
        request: ehpc20180412_models.StopServerlessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopServerlessJobsResponse:
        """
        @summary Stops Serverless jobs in a cluster based on job IDs or subtask IDs (array jobs). If you specify the job ID of an array job, all subtasks in the job are stopped.
        
        @param request: StopServerlessJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopServerlessJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopServerlessJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_serverless_jobs(
        self,
        request: ehpc20180412_models.StopServerlessJobsRequest,
    ) -> ehpc20180412_models.StopServerlessJobsResponse:
        """
        @summary Stops Serverless jobs in a cluster based on job IDs or subtask IDs (array jobs). If you specify the job ID of an array job, all subtasks in the job are stopped.
        
        @param request: StopServerlessJobsRequest
        @return: StopServerlessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_serverless_jobs_with_options(request, runtime)

    async def stop_serverless_jobs_async(
        self,
        request: ehpc20180412_models.StopServerlessJobsRequest,
    ) -> ehpc20180412_models.StopServerlessJobsResponse:
        """
        @summary Stops Serverless jobs in a cluster based on job IDs or subtask IDs (array jobs). If you specify the job ID of an array job, all subtasks in the job are stopped.
        
        @param request: StopServerlessJobsRequest
        @return: StopServerlessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_serverless_jobs_with_options_async(request, runtime)

    def stop_visual_service_with_options(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        """
        @summary Stops the remote visualization service of Virtual Network Console (VNC) in a cluster.
        
        @param request: StopVisualServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopVisualServiceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopVisualService',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopVisualServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_visual_service_with_options_async(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        """
        @summary Stops the remote visualization service of Virtual Network Console (VNC) in a cluster.
        
        @param request: StopVisualServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopVisualServiceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopVisualService',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopVisualServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_visual_service(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        """
        @summary Stops the remote visualization service of Virtual Network Console (VNC) in a cluster.
        
        @param request: StopVisualServiceRequest
        @return: StopVisualServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_visual_service_with_options(request, runtime)

    async def stop_visual_service_async(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        """
        @summary Stops the remote visualization service of Virtual Network Console (VNC) in a cluster.
        
        @param request: StopVisualServiceRequest
        @return: StopVisualServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_visual_service_with_options_async(request, runtime)

    def submit_job_with_options(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SubmitJobResponse:
        """
        @summary Submits a job in a cluster.
        
        @description The ID of the request.
        
        @param request: SubmitJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_job_with_options_async(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SubmitJobResponse:
        """
        @summary Submits a job in a cluster.
        
        @description The ID of the request.
        
        @param request: SubmitJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_job(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
    ) -> ehpc20180412_models.SubmitJobResponse:
        """
        @summary Submits a job in a cluster.
        
        @description The ID of the request.
        
        @param request: SubmitJobRequest
        @return: SubmitJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_job_with_options(request, runtime)

    async def submit_job_async(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
    ) -> ehpc20180412_models.SubmitJobResponse:
        """
        @summary Submits a job in a cluster.
        
        @description The ID of the request.
        
        @param request: SubmitJobRequest
        @return: SubmitJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_job_with_options_async(request, runtime)

    def submit_serverless_job_with_options(
        self,
        tmp_req: ehpc20180412_models.SubmitServerlessJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SubmitServerlessJobResponse:
        """
        @summary Submits a serverless job to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: SubmitServerlessJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitServerlessJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20180412_models.SubmitServerlessJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.array_properties):
            request.array_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.array_properties, 'ArrayProperties', 'json')
        if not UtilClient.is_unset(tmp_req.container):
            request.container_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container, 'Container', 'json')
        if not UtilClient.is_unset(tmp_req.depends_on):
            request.depends_on_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.depends_on, 'DependsOn', 'json')
        if not UtilClient.is_unset(tmp_req.instance_type):
            request.instance_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_type, 'InstanceType', 'json')
        if not UtilClient.is_unset(tmp_req.retry_strategy):
            request.retry_strategy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_strategy, 'RetryStrategy', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_id):
            request.v_switch_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_id, 'VSwitchId', 'json')
        query = {}
        if not UtilClient.is_unset(request.array_properties_shrink):
            query['ArrayProperties'] = request.array_properties_shrink
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_shrink):
            query['Container'] = request.container_shrink
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.depends_on_shrink):
            query['DependsOn'] = request.depends_on_shrink
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.instance_type_shrink):
            query['InstanceType'] = request.instance_type_shrink
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_priority):
            query['JobPriority'] = request.job_priority
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.retry_strategy_shrink):
            query['RetryStrategy'] = request.retry_strategy_shrink
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.v_switch_id_shrink):
            query['VSwitchId'] = request.v_switch_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitServerlessJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitServerlessJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_serverless_job_with_options_async(
        self,
        tmp_req: ehpc20180412_models.SubmitServerlessJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SubmitServerlessJobResponse:
        """
        @summary Submits a serverless job to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param tmp_req: SubmitServerlessJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitServerlessJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc20180412_models.SubmitServerlessJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.array_properties):
            request.array_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.array_properties, 'ArrayProperties', 'json')
        if not UtilClient.is_unset(tmp_req.container):
            request.container_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container, 'Container', 'json')
        if not UtilClient.is_unset(tmp_req.depends_on):
            request.depends_on_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.depends_on, 'DependsOn', 'json')
        if not UtilClient.is_unset(tmp_req.instance_type):
            request.instance_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_type, 'InstanceType', 'json')
        if not UtilClient.is_unset(tmp_req.retry_strategy):
            request.retry_strategy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_strategy, 'RetryStrategy', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_id):
            request.v_switch_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_id, 'VSwitchId', 'json')
        query = {}
        if not UtilClient.is_unset(request.array_properties_shrink):
            query['ArrayProperties'] = request.array_properties_shrink
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_shrink):
            query['Container'] = request.container_shrink
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.depends_on_shrink):
            query['DependsOn'] = request.depends_on_shrink
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.instance_type_shrink):
            query['InstanceType'] = request.instance_type_shrink
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_priority):
            query['JobPriority'] = request.job_priority
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.retry_strategy_shrink):
            query['RetryStrategy'] = request.retry_strategy_shrink
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.v_switch_id_shrink):
            query['VSwitchId'] = request.v_switch_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitServerlessJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitServerlessJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_serverless_job(
        self,
        request: ehpc20180412_models.SubmitServerlessJobRequest,
    ) -> ehpc20180412_models.SubmitServerlessJobResponse:
        """
        @summary Submits a serverless job to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: SubmitServerlessJobRequest
        @return: SubmitServerlessJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_serverless_job_with_options(request, runtime)

    async def submit_serverless_job_async(
        self,
        request: ehpc20180412_models.SubmitServerlessJobRequest,
    ) -> ehpc20180412_models.SubmitServerlessJobResponse:
        """
        @summary Submits a serverless job to an Elastic High Performance Computing (E-HPC) cluster.
        
        @param request: SubmitServerlessJobRequest
        @return: SubmitServerlessJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_serverless_job_with_options_async(request, runtime)

    def sync_users_with_options(
        self,
        request: ehpc20180412_models.SyncUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SyncUsersResponse:
        """
        @summary Synchronizes local cluster users to a hybrid cloud cluster in hybrid-cloud proxy mode.
        
        @param request: SyncUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SyncUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_users_with_options_async(
        self,
        request: ehpc20180412_models.SyncUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SyncUsersResponse:
        """
        @summary Synchronizes local cluster users to a hybrid cloud cluster in hybrid-cloud proxy mode.
        
        @param request: SyncUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SyncUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_users(
        self,
        request: ehpc20180412_models.SyncUsersRequest,
    ) -> ehpc20180412_models.SyncUsersResponse:
        """
        @summary Synchronizes local cluster users to a hybrid cloud cluster in hybrid-cloud proxy mode.
        
        @param request: SyncUsersRequest
        @return: SyncUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_users_with_options(request, runtime)

    async def sync_users_async(
        self,
        request: ehpc20180412_models.SyncUsersRequest,
    ) -> ehpc20180412_models.SyncUsersResponse:
        """
        @summary Synchronizes local cluster users to a hybrid cloud cluster in hybrid-cloud proxy mode.
        
        @param request: SyncUsersRequest
        @return: SyncUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_users_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ehpc20180412_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.TagResourcesResponse:
        """
        @summary Creates tags and attach the tags to a specified resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ehpc20180412_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.TagResourcesResponse:
        """
        @summary Creates tags and attach the tags to a specified resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ehpc20180412_models.TagResourcesRequest,
    ) -> ehpc20180412_models.TagResourcesResponse:
        """
        @summary Creates tags and attach the tags to a specified resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ehpc20180412_models.TagResourcesRequest,
    ) -> ehpc20180412_models.TagResourcesResponse:
        """
        @summary Creates tags and attach the tags to a specified resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: ehpc20180412_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UnTagResourcesResponse:
        """
        @summary Removes tags from a specified resource.
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: ehpc20180412_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UnTagResourcesResponse:
        """
        @summary Removes tags from a specified resource.
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: ehpc20180412_models.UnTagResourcesRequest,
    ) -> ehpc20180412_models.UnTagResourcesResponse:
        """
        @summary Removes tags from a specified resource.
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: ehpc20180412_models.UnTagResourcesRequest,
    ) -> ehpc20180412_models.UnTagResourcesResponse:
        """
        @summary Removes tags from a specified resource.
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def uninstall_software_with_options(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        """
        @summary Uninstalls software from a cluster.
        
        @param request: UninstallSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UninstallSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_software_with_options_async(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        """
        @summary Uninstalls software from a cluster.
        
        @param request: UninstallSoftwareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallSoftwareResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UninstallSoftwareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_software(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        """
        @summary Uninstalls software from a cluster.
        
        @param request: UninstallSoftwareRequest
        @return: UninstallSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_software_with_options(request, runtime)

    async def uninstall_software_async(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        """
        @summary Uninstalls software from a cluster.
        
        @param request: UninstallSoftwareRequest
        @return: UninstallSoftwareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_software_with_options_async(request, runtime)

    def update_cluster_volumes_with_options(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        """
        @summary Mount new storage resources to a cluster.
        
        @param request: UpdateClusterVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterVolumesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateClusterVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_volumes_with_options_async(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        """
        @summary Mount new storage resources to a cluster.
        
        @param request: UpdateClusterVolumesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClusterVolumesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateClusterVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_volumes(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        """
        @summary Mount new storage resources to a cluster.
        
        @param request: UpdateClusterVolumesRequest
        @return: UpdateClusterVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_volumes_with_options(request, runtime)

    async def update_cluster_volumes_async(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        """
        @summary Mount new storage resources to a cluster.
        
        @param request: UpdateClusterVolumesRequest
        @return: UpdateClusterVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_volumes_with_options_async(request, runtime)

    def update_queue_config_with_options(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        """
        @summary Updates the resource group information and the instance types of compute nodes for a queue of a cluster.
        
        @description After you update the resource group, the nodes that you add by scaling out the cluster are automatically included in the resource group.
        
        @param request: UpdateQueueConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQueueConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQueueConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateQueueConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_queue_config_with_options_async(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        """
        @summary Updates the resource group information and the instance types of compute nodes for a queue of a cluster.
        
        @description After you update the resource group, the nodes that you add by scaling out the cluster are automatically included in the resource group.
        
        @param request: UpdateQueueConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQueueConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQueueConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateQueueConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_queue_config(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        """
        @summary Updates the resource group information and the instance types of compute nodes for a queue of a cluster.
        
        @description After you update the resource group, the nodes that you add by scaling out the cluster are automatically included in the resource group.
        
        @param request: UpdateQueueConfigRequest
        @return: UpdateQueueConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_queue_config_with_options(request, runtime)

    async def update_queue_config_async(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        """
        @summary Updates the resource group information and the instance types of compute nodes for a queue of a cluster.
        
        @description After you update the resource group, the nodes that you add by scaling out the cluster are automatically included in the resource group.
        
        @param request: UpdateQueueConfigRequest
        @return: UpdateQueueConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_queue_config_with_options_async(request, runtime)

    def upgrade_client_with_options(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        """
        @summary Updates the client (ehpcutil) in a cluster to a new version.
        
        @param request: UpgradeClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClientResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpgradeClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_client_with_options_async(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        """
        @summary Updates the client (ehpcutil) in a cluster to a new version.
        
        @param request: UpgradeClientRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClientResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpgradeClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_client(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        """
        @summary Updates the client (ehpcutil) in a cluster to a new version.
        
        @param request: UpgradeClientRequest
        @return: UpgradeClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)

    async def upgrade_client_async(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        """
        @summary Updates the client (ehpcutil) in a cluster to a new version.
        
        @param request: UpgradeClientRequest
        @return: UpgradeClientResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_client_with_options_async(request, runtime)
