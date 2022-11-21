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

    def add_container_app_with_options(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddContainerApp',
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
            ehpc20180412_models.AddContainerAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_container_app_with_options_async(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddContainerApp',
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
            ehpc20180412_models.AddContainerAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_container_app(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_container_app_with_options(request, runtime)

    async def add_container_app_async(
        self,
        request: ehpc20180412_models.AddContainerAppRequest,
    ) -> ehpc20180412_models.AddContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_container_app_with_options_async(request, runtime)

    def add_existed_nodes_with_options(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_existed_nodes_with_options(request, runtime)

    async def add_existed_nodes_async(
        self,
        request: ehpc20180412_models.AddExistedNodesRequest,
    ) -> ehpc20180412_models.AddExistedNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_existed_nodes_with_options_async(request, runtime)

    def add_local_nodes_with_options(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_local_nodes_with_options(request, runtime)

    async def add_local_nodes_async(
        self,
        request: ehpc20180412_models.AddLocalNodesRequest,
    ) -> ehpc20180412_models.AddLocalNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_local_nodes_with_options_async(request, runtime)

    def add_nodes_with_options(
        self,
        request: ehpc20180412_models.AddNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_nodes_with_options(request, runtime)

    async def add_nodes_async(
        self,
        request: ehpc20180412_models.AddNodesRequest,
    ) -> ehpc20180412_models.AddNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_nodes_with_options_async(request, runtime)

    def add_queue_with_options(
        self,
        request: ehpc20180412_models.AddQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddQueueResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_queue_with_options(request, runtime)

    async def add_queue_async(
        self,
        request: ehpc20180412_models.AddQueueRequest,
    ) -> ehpc20180412_models.AddQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_queue_with_options_async(request, runtime)

    def add_security_group_with_options(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_security_group_with_options(request, runtime)

    async def add_security_group_async(
        self,
        request: ehpc20180412_models.AddSecurityGroupRequest,
    ) -> ehpc20180412_models.AddSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_security_group_with_options_async(request, runtime)

    def add_users_with_options(
        self,
        request: ehpc20180412_models.AddUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.AddUsersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_users_with_options(request, runtime)

    async def add_users_async(
        self,
        request: ehpc20180412_models.AddUsersRequest,
    ) -> ehpc20180412_models.AddUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_users_with_options_async(request, runtime)

    def apply_nodes_with_options(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ApplyNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.apply_nodes_with_options(request, runtime)

    async def apply_nodes_async(
        self,
        request: ehpc20180412_models.ApplyNodesRequest,
    ) -> ehpc20180412_models.ApplyNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_nodes_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: ehpc20180412_models.CreateClusterRequest,
    ) -> ehpc20180412_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_gwscluster_with_options(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSCluster',
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
            ehpc20180412_models.CreateGWSClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gwscluster_with_options_async(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSCluster',
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
            ehpc20180412_models.CreateGWSClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gwscluster(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gwscluster_with_options(request, runtime)

    async def create_gwscluster_async(
        self,
        request: ehpc20180412_models.CreateGWSClusterRequest,
    ) -> ehpc20180412_models.CreateGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gwscluster_with_options_async(request, runtime)

    def create_gwsimage_with_options(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSImage',
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
            ehpc20180412_models.CreateGWSImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gwsimage_with_options_async(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSImage',
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
            ehpc20180412_models.CreateGWSImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gwsimage(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gwsimage_with_options(request, runtime)

    async def create_gwsimage_async(
        self,
        request: ehpc20180412_models.CreateGWSImageRequest,
    ) -> ehpc20180412_models.CreateGWSImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gwsimage_with_options_async(request, runtime)

    def create_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSInstance',
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
            ehpc20180412_models.CreateGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSInstance',
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
            ehpc20180412_models.CreateGWSInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gwsinstance(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gwsinstance_with_options(request, runtime)

    async def create_gwsinstance_async(
        self,
        request: ehpc20180412_models.CreateGWSInstanceRequest,
    ) -> ehpc20180412_models.CreateGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gwsinstance_with_options_async(request, runtime)

    def create_hybrid_cluster_with_options(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_cluster_with_options(request, runtime)

    async def create_hybrid_cluster_async(
        self,
        request: ehpc20180412_models.CreateHybridClusterRequest,
    ) -> ehpc20180412_models.CreateHybridClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_hybrid_cluster_with_options_async(request, runtime)

    def create_job_file_with_options(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobFileResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_job_file_with_options(request, runtime)

    async def create_job_file_async(
        self,
        request: ehpc20180412_models.CreateJobFileRequest,
    ) -> ehpc20180412_models.CreateJobFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_file_with_options_async(request, runtime)

    def create_job_template_with_options(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_job_template_with_options(request, runtime)

    async def create_job_template_async(
        self,
        request: ehpc20180412_models.CreateJobTemplateRequest,
    ) -> ehpc20180412_models.CreateJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_template_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: ehpc20180412_models.DeleteClusterRequest,
    ) -> ehpc20180412_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_container_apps_with_options(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContainerApps',
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
            ehpc20180412_models.DeleteContainerAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_container_apps_with_options_async(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContainerApps',
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
            ehpc20180412_models.DeleteContainerAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_container_apps(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_container_apps_with_options(request, runtime)

    async def delete_container_apps_async(
        self,
        request: ehpc20180412_models.DeleteContainerAppsRequest,
    ) -> ehpc20180412_models.DeleteContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_container_apps_with_options_async(request, runtime)

    def delete_gwscluster_with_options(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGWSCluster',
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
            ehpc20180412_models.DeleteGWSClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gwscluster_with_options_async(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGWSCluster',
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
            ehpc20180412_models.DeleteGWSClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gwscluster(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gwscluster_with_options(request, runtime)

    async def delete_gwscluster_async(
        self,
        request: ehpc20180412_models.DeleteGWSClusterRequest,
    ) -> ehpc20180412_models.DeleteGWSClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gwscluster_with_options_async(request, runtime)

    def delete_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGWSInstance',
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
            ehpc20180412_models.DeleteGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGWSInstance',
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
            ehpc20180412_models.DeleteGWSInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gwsinstance(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gwsinstance_with_options(request, runtime)

    async def delete_gwsinstance_async(
        self,
        request: ehpc20180412_models.DeleteGWSInstanceRequest,
    ) -> ehpc20180412_models.DeleteGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gwsinstance_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
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
            ehpc20180412_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
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
            ehpc20180412_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
    ) -> ehpc20180412_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: ehpc20180412_models.DeleteImageRequest,
    ) -> ehpc20180412_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_job_templates_with_options(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_job_templates_with_options(request, runtime)

    async def delete_job_templates_async(
        self,
        request: ehpc20180412_models.DeleteJobTemplatesRequest,
    ) -> ehpc20180412_models.DeleteJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_templates_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteJobsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: ehpc20180412_models.DeleteJobsRequest,
    ) -> ehpc20180412_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def delete_local_image_with_options(
        self,
        request: ehpc20180412_models.DeleteLocalImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteLocalImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLocalImage',
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
            ehpc20180412_models.DeleteLocalImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_local_image_with_options_async(
        self,
        request: ehpc20180412_models.DeleteLocalImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteLocalImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLocalImage',
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
            ehpc20180412_models.DeleteLocalImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_local_image(
        self,
        request: ehpc20180412_models.DeleteLocalImageRequest,
    ) -> ehpc20180412_models.DeleteLocalImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_local_image_with_options(request, runtime)

    async def delete_local_image_async(
        self,
        request: ehpc20180412_models.DeleteLocalImageRequest,
    ) -> ehpc20180412_models.DeleteLocalImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_local_image_with_options_async(request, runtime)

    def delete_nodes_with_options(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    async def delete_nodes_async(
        self,
        request: ehpc20180412_models.DeleteNodesRequest,
    ) -> ehpc20180412_models.DeleteNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nodes_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteQueueResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: ehpc20180412_models.DeleteQueueRequest,
    ) -> ehpc20180412_models.DeleteQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_security_group_with_options(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    async def delete_security_group_async(
        self,
        request: ehpc20180412_models.DeleteSecurityGroupRequest,
    ) -> ehpc20180412_models.DeleteSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_group_with_options_async(request, runtime)

    def delete_users_with_options(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DeleteUsersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: ehpc20180412_models.DeleteUsersRequest,
    ) -> ehpc20180412_models.DeleteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def describe_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scale_config_with_options(request, runtime)

    async def describe_auto_scale_config_async(
        self,
        request: ehpc20180412_models.DescribeAutoScaleConfigRequest,
    ) -> ehpc20180412_models.DescribeAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_scale_config_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: ehpc20180412_models.DescribeClusterRequest,
    ) -> ehpc20180412_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def describe_container_app_with_options(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerApp',
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
            ehpc20180412_models.DescribeContainerAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_app_with_options_async(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerApp',
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
            ehpc20180412_models.DescribeContainerAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_app(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_app_with_options(request, runtime)

    async def describe_container_app_async(
        self,
        request: ehpc20180412_models.DescribeContainerAppRequest,
    ) -> ehpc20180412_models.DescribeContainerAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_app_with_options_async(request, runtime)

    def describe_estack_image_with_options(
        self,
        request: ehpc20180412_models.DescribeEstackImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeEstackImageResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_estack_image_with_options(request, runtime)

    async def describe_estack_image_async(
        self,
        request: ehpc20180412_models.DescribeEstackImageRequest,
    ) -> ehpc20180412_models.DescribeEstackImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_estack_image_with_options_async(request, runtime)

    def describe_gwscluster_policy_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_mode):
            query['AsyncMode'] = request.async_mode
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSClusterPolicy',
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
            ehpc20180412_models.DescribeGWSClusterPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gwscluster_policy_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_mode):
            query['AsyncMode'] = request.async_mode
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSClusterPolicy',
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
            ehpc20180412_models.DescribeGWSClusterPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gwscluster_policy(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwscluster_policy_with_options(request, runtime)

    async def describe_gwscluster_policy_async(
        self,
        request: ehpc20180412_models.DescribeGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.DescribeGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwscluster_policy_with_options_async(request, runtime)

    def describe_gwsclusters_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSClusters',
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
            ehpc20180412_models.DescribeGWSClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gwsclusters_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSClusters',
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
            ehpc20180412_models.DescribeGWSClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gwsclusters(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsclusters_with_options(request, runtime)

    async def describe_gwsclusters_async(
        self,
        request: ehpc20180412_models.DescribeGWSClustersRequest,
    ) -> ehpc20180412_models.DescribeGWSClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwsclusters_with_options_async(request, runtime)

    def describe_gwsimages_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSImages',
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
            ehpc20180412_models.DescribeGWSImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gwsimages_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSImages',
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
            ehpc20180412_models.DescribeGWSImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gwsimages(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsimages_with_options(request, runtime)

    async def describe_gwsimages_async(
        self,
        request: ehpc20180412_models.DescribeGWSImagesRequest,
    ) -> ehpc20180412_models.DescribeGWSImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwsimages_with_options_async(request, runtime)

    def describe_gwsinstances_with_options(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSInstances',
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
            ehpc20180412_models.DescribeGWSInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gwsinstances_with_options_async(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSInstances',
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
            ehpc20180412_models.DescribeGWSInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gwsinstances(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsinstances_with_options(request, runtime)

    async def describe_gwsinstances_async(
        self,
        request: ehpc20180412_models.DescribeGWSInstancesRequest,
    ) -> ehpc20180412_models.DescribeGWSInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gwsinstances_with_options_async(request, runtime)

    def describe_image_with_options(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImage',
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
            ehpc20180412_models.DescribeImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_with_options_async(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImage',
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
            ehpc20180412_models.DescribeImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
    ) -> ehpc20180412_models.DescribeImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_with_options(request, runtime)

    async def describe_image_async(
        self,
        request: ehpc20180412_models.DescribeImageRequest,
    ) -> ehpc20180412_models.DescribeImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_with_options_async(request, runtime)

    def describe_image_gateway_config_with_options(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageGatewayConfig',
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
            ehpc20180412_models.DescribeImageGatewayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_gateway_config_with_options_async(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageGatewayConfig',
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
            ehpc20180412_models.DescribeImageGatewayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_gateway_config(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_gateway_config_with_options(request, runtime)

    async def describe_image_gateway_config_async(
        self,
        request: ehpc20180412_models.DescribeImageGatewayConfigRequest,
    ) -> ehpc20180412_models.DescribeImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_gateway_config_with_options_async(request, runtime)

    def describe_image_price_with_options(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_image_price_with_options(request, runtime)

    async def describe_image_price_async(
        self,
        request: ehpc20180412_models.DescribeImagePriceRequest,
    ) -> ehpc20180412_models.DescribeImagePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_price_with_options_async(request, runtime)

    def describe_job_with_options(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeJobResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    async def describe_job_async(
        self,
        request: ehpc20180412_models.DescribeJobRequest,
    ) -> ehpc20180412_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_with_options_async(request, runtime)

    def describe_nfsclient_status_with_options(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNFSClientStatus',
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
            ehpc20180412_models.DescribeNFSClientStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nfsclient_status_with_options_async(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNFSClientStatus',
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
            ehpc20180412_models.DescribeNFSClientStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nfsclient_status(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nfsclient_status_with_options(request, runtime)

    async def describe_nfsclient_status_async(
        self,
        request: ehpc20180412_models.DescribeNFSClientStatusRequest,
    ) -> ehpc20180412_models.DescribeNFSClientStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nfsclient_status_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.DescribePriceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: ehpc20180412_models.DescribePriceRequest,
    ) -> ehpc20180412_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def edit_job_template_with_options(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.edit_job_template_with_options(request, runtime)

    async def edit_job_template_async(
        self,
        request: ehpc20180412_models.EditJobTemplateRequest,
    ) -> ehpc20180412_models.EditJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_job_template_with_options_async(request, runtime)

    def get_accounting_report_with_options(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_accounting_report_with_options(request, runtime)

    async def get_accounting_report_async(
        self,
        request: ehpc20180412_models.GetAccountingReportRequest,
    ) -> ehpc20180412_models.GetAccountingReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_accounting_report_with_options_async(request, runtime)

    def get_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scale_config_with_options(request, runtime)

    async def get_auto_scale_config_async(
        self,
        request: ehpc20180412_models.GetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.GetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scale_config_with_options_async(request, runtime)

    def get_cloud_metric_logs_with_options(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_logs_with_options(request, runtime)

    async def get_cloud_metric_logs_async(
        self,
        request: ehpc20180412_models.GetCloudMetricLogsRequest,
    ) -> ehpc20180412_models.GetCloudMetricLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_metric_logs_with_options_async(request, runtime)

    def get_cloud_metric_profiling_with_options(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_profiling_with_options(request, runtime)

    async def get_cloud_metric_profiling_async(
        self,
        request: ehpc20180412_models.GetCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.GetCloudMetricProfilingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_metric_profiling_with_options_async(request, runtime)

    def get_cluster_volumes_with_options(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_volumes_with_options(request, runtime)

    async def get_cluster_volumes_async(
        self,
        request: ehpc20180412_models.GetClusterVolumesRequest,
    ) -> ehpc20180412_models.GetClusterVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_volumes_with_options_async(request, runtime)

    def get_common_image_with_options(
        self,
        request: ehpc20180412_models.GetCommonImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCommonImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommonImage',
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
            ehpc20180412_models.GetCommonImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_common_image_with_options_async(
        self,
        request: ehpc20180412_models.GetCommonImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetCommonImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommonImage',
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
            ehpc20180412_models.GetCommonImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_common_image(
        self,
        request: ehpc20180412_models.GetCommonImageRequest,
    ) -> ehpc20180412_models.GetCommonImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_common_image_with_options(request, runtime)

    async def get_common_image_async(
        self,
        request: ehpc20180412_models.GetCommonImageRequest,
    ) -> ehpc20180412_models.GetCommonImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_common_image_with_options_async(request, runtime)

    def get_gwsconnect_ticket_with_options(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGWSConnectTicket',
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
            ehpc20180412_models.GetGWSConnectTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwsconnect_ticket_with_options_async(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGWSConnectTicket',
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
            ehpc20180412_models.GetGWSConnectTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwsconnect_ticket(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_gwsconnect_ticket_with_options(request, runtime)

    async def get_gwsconnect_ticket_async(
        self,
        request: ehpc20180412_models.GetGWSConnectTicketRequest,
    ) -> ehpc20180412_models.GetGWSConnectTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_gwsconnect_ticket_with_options_async(request, runtime)

    def get_hybrid_cluster_config_with_options(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_hybrid_cluster_config_with_options(request, runtime)

    async def get_hybrid_cluster_config_async(
        self,
        request: ehpc20180412_models.GetHybridClusterConfigRequest,
    ) -> ehpc20180412_models.GetHybridClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hybrid_cluster_config_with_options_async(request, runtime)

    def get_if_ecs_type_support_ht_config_with_options(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_if_ecs_type_support_ht_config_with_options(request, runtime)

    async def get_if_ecs_type_support_ht_config_async(
        self,
        request: ehpc20180412_models.GetIfEcsTypeSupportHtConfigRequest,
    ) -> ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_if_ecs_type_support_ht_config_with_options_async(request, runtime)

    def get_job_log_with_options(
        self,
        request: ehpc20180412_models.GetJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetJobLogResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_job_log_with_options(request, runtime)

    async def get_job_log_async(
        self,
        request: ehpc20180412_models.GetJobLogRequest,
    ) -> ehpc20180412_models.GetJobLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_log_with_options_async(request, runtime)

    def get_post_scripts_with_options(
        self,
        request: ehpc20180412_models.GetPostScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetPostScriptsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_post_scripts_with_options(request, runtime)

    async def get_post_scripts_async(
        self,
        request: ehpc20180412_models.GetPostScriptsRequest,
    ) -> ehpc20180412_models.GetPostScriptsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_post_scripts_with_options_async(request, runtime)

    def get_scheduler_info_with_options(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_scheduler_info_with_options(request, runtime)

    async def get_scheduler_info_async(
        self,
        request: ehpc20180412_models.GetSchedulerInfoRequest,
    ) -> ehpc20180412_models.GetSchedulerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scheduler_info_with_options_async(request, runtime)

    def get_user_image_with_options(
        self,
        request: ehpc20180412_models.GetUserImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetUserImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserImage',
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
            ehpc20180412_models.GetUserImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_image_with_options_async(
        self,
        request: ehpc20180412_models.GetUserImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetUserImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserImage',
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
            ehpc20180412_models.GetUserImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_image(
        self,
        request: ehpc20180412_models.GetUserImageRequest,
    ) -> ehpc20180412_models.GetUserImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_image_with_options(request, runtime)

    async def get_user_image_async(
        self,
        request: ehpc20180412_models.GetUserImageRequest,
    ) -> ehpc20180412_models.GetUserImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_image_with_options_async(request, runtime)

    def get_visual_service_status_with_options(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_visual_service_status_with_options(request, runtime)

    async def get_visual_service_status_async(
        self,
        request: ehpc20180412_models.GetVisualServiceStatusRequest,
    ) -> ehpc20180412_models.GetVisualServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_visual_service_status_with_options_async(request, runtime)

    def initialize_ehpcwith_options(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.initialize_ehpcwith_options(request, runtime)

    async def initialize_ehpc_async(
        self,
        request: ehpc20180412_models.InitializeEHPCRequest,
    ) -> ehpc20180412_models.InitializeEHPCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_ehpcwith_options_async(request, runtime)

    def inspect_image_with_options(
        self,
        request: ehpc20180412_models.InspectImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InspectImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InspectImage',
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
            ehpc20180412_models.InspectImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def inspect_image_with_options_async(
        self,
        request: ehpc20180412_models.InspectImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InspectImageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InspectImage',
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
            ehpc20180412_models.InspectImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inspect_image(
        self,
        request: ehpc20180412_models.InspectImageRequest,
    ) -> ehpc20180412_models.InspectImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.inspect_image_with_options(request, runtime)

    async def inspect_image_async(
        self,
        request: ehpc20180412_models.InspectImageRequest,
    ) -> ehpc20180412_models.InspectImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inspect_image_with_options_async(request, runtime)

    def install_software_with_options(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.install_software_with_options(request, runtime)

    async def install_software_async(
        self,
        request: ehpc20180412_models.InstallSoftwareRequest,
    ) -> ehpc20180412_models.InstallSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_software_with_options_async(request, runtime)

    def invoke_shell_command_with_options(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.invoke_shell_command_with_options(request, runtime)

    async def invoke_shell_command_async(
        self,
        request: ehpc20180412_models.InvokeShellCommandRequest,
    ) -> ehpc20180412_models.InvokeShellCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_shell_command_with_options_async(request, runtime)

    def list_available_ecs_types_with_options(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_available_ecs_types_with_options(request, runtime)

    async def list_available_ecs_types_async(
        self,
        request: ehpc20180412_models.ListAvailableEcsTypesRequest,
    ) -> ehpc20180412_models.ListAvailableEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_available_ecs_types_with_options_async(request, runtime)

    def list_cloud_metric_profilings_with_options(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_metric_profilings_with_options(request, runtime)

    async def list_cloud_metric_profilings_async(
        self,
        request: ehpc20180412_models.ListCloudMetricProfilingsRequest,
    ) -> ehpc20180412_models.ListCloudMetricProfilingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_metric_profilings_with_options_async(request, runtime)

    def list_cluster_logs_with_options(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_logs_with_options(request, runtime)

    async def list_cluster_logs_async(
        self,
        request: ehpc20180412_models.ListClusterLogsRequest,
    ) -> ehpc20180412_models.ListClusterLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_logs_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: ehpc20180412_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: ehpc20180412_models.ListClustersRequest,
    ) -> ehpc20180412_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_clusters_meta_with_options(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_meta_with_options(request, runtime)

    async def list_clusters_meta_async(
        self,
        request: ehpc20180412_models.ListClustersMetaRequest,
    ) -> ehpc20180412_models.ListClustersMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_meta_with_options_async(request, runtime)

    def list_commands_with_options(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommandsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_commands_with_options(request, runtime)

    async def list_commands_async(
        self,
        request: ehpc20180412_models.ListCommandsRequest,
    ) -> ehpc20180412_models.ListCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_commands_with_options_async(request, runtime)

    def list_community_images_with_options(
        self,
        request: ehpc20180412_models.ListCommunityImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCommunityImagesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_community_images_with_options(request, runtime)

    async def list_community_images_async(
        self,
        request: ehpc20180412_models.ListCommunityImagesRequest,
    ) -> ehpc20180412_models.ListCommunityImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_community_images_with_options_async(request, runtime)

    def list_container_apps_with_options(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerApps',
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
            ehpc20180412_models.ListContainerAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_container_apps_with_options_async(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerApps',
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
            ehpc20180412_models.ListContainerAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_container_apps(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_container_apps_with_options(request, runtime)

    async def list_container_apps_async(
        self,
        request: ehpc20180412_models.ListContainerAppsRequest,
    ) -> ehpc20180412_models.ListContainerAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_container_apps_with_options_async(request, runtime)

    def list_container_images_with_options(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerImages',
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
            ehpc20180412_models.ListContainerImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_container_images_with_options_async(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerImages',
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
            ehpc20180412_models.ListContainerImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_container_images(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_container_images_with_options(request, runtime)

    async def list_container_images_async(
        self,
        request: ehpc20180412_models.ListContainerImagesRequest,
    ) -> ehpc20180412_models.ListContainerImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_container_images_with_options_async(request, runtime)

    def list_cpfs_file_systems_with_options(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_cpfs_file_systems_with_options(request, runtime)

    async def list_cpfs_file_systems_async(
        self,
        request: ehpc20180412_models.ListCpfsFileSystemsRequest,
    ) -> ehpc20180412_models.ListCpfsFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cpfs_file_systems_with_options_async(request, runtime)

    def list_current_client_version_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCurrentClientVersionResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_current_client_version_with_options(runtime)

    async def list_current_client_version_async(self) -> ehpc20180412_models.ListCurrentClientVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_current_client_version_with_options_async(runtime)

    def list_custom_images_with_options(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    async def list_custom_images_async(
        self,
        request: ehpc20180412_models.ListCustomImagesRequest,
    ) -> ehpc20180412_models.ListCustomImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_images_with_options_async(request, runtime)

    def list_file_system_with_mount_targets_with_options(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_file_system_with_mount_targets_with_options(request, runtime)

    async def list_file_system_with_mount_targets_async(
        self,
        request: ehpc20180412_models.ListFileSystemWithMountTargetsRequest,
    ) -> ehpc20180412_models.ListFileSystemWithMountTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_file_system_with_mount_targets_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: ehpc20180412_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListImagesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: ehpc20180412_models.ListImagesRequest,
    ) -> ehpc20180412_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_installed_software_with_options(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_installed_software_with_options(request, runtime)

    async def list_installed_software_async(
        self,
        request: ehpc20180412_models.ListInstalledSoftwareRequest,
    ) -> ehpc20180412_models.ListInstalledSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_installed_software_with_options_async(request, runtime)

    def list_invocation_results_with_options(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_results_with_options(request, runtime)

    async def list_invocation_results_async(
        self,
        request: ehpc20180412_models.ListInvocationResultsRequest,
    ) -> ehpc20180412_models.ListInvocationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_invocation_results_with_options_async(request, runtime)

    def list_invocation_status_with_options(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_status_with_options(request, runtime)

    async def list_invocation_status_async(
        self,
        request: ehpc20180412_models.ListInvocationStatusRequest,
    ) -> ehpc20180412_models.ListInvocationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_invocation_status_with_options_async(request, runtime)

    def list_job_templates_with_options(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_job_templates_with_options(request, runtime)

    async def list_job_templates_async(
        self,
        request: ehpc20180412_models.ListJobTemplatesRequest,
    ) -> ehpc20180412_models.ListJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_templates_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: ehpc20180412_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: ehpc20180412_models.ListJobsRequest,
    ) -> ehpc20180412_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_jobs_with_filters_with_options(
        self,
        request: ehpc20180412_models.ListJobsWithFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListJobsWithFiltersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_filters_with_options(request, runtime)

    async def list_jobs_with_filters_async(
        self,
        request: ehpc20180412_models.ListJobsWithFiltersRequest,
    ) -> ehpc20180412_models.ListJobsWithFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_filters_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: ehpc20180412_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: ehpc20180412_models.ListNodesRequest,
    ) -> ehpc20180412_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_nodes_by_queue_with_options(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_queue_with_options(request, runtime)

    async def list_nodes_by_queue_async(
        self,
        request: ehpc20180412_models.ListNodesByQueueRequest,
    ) -> ehpc20180412_models.ListNodesByQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_by_queue_with_options_async(request, runtime)

    def list_nodes_no_paging_with_options(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_no_paging_with_options(request, runtime)

    async def list_nodes_no_paging_async(
        self,
        request: ehpc20180412_models.ListNodesNoPagingRequest,
    ) -> ehpc20180412_models.ListNodesNoPagingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_no_paging_with_options_async(request, runtime)

    def list_preferred_ecs_types_with_options(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_preferred_ecs_types_with_options(request, runtime)

    async def list_preferred_ecs_types_async(
        self,
        request: ehpc20180412_models.ListPreferredEcsTypesRequest,
    ) -> ehpc20180412_models.ListPreferredEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_preferred_ecs_types_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListQueuesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: ehpc20180412_models.ListQueuesRequest,
    ) -> ehpc20180412_models.ListQueuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> ehpc20180412_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_security_groups_with_options(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_security_groups_with_options(request, runtime)

    async def list_security_groups_async(
        self,
        request: ehpc20180412_models.ListSecurityGroupsRequest,
    ) -> ehpc20180412_models.ListSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_groups_with_options_async(request, runtime)

    def list_softwares_with_options(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    async def list_softwares_async(
        self,
        request: ehpc20180412_models.ListSoftwaresRequest,
    ) -> ehpc20180412_models.ListSoftwaresResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_softwares_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ehpc20180412_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ehpc20180412_models.ListTagResourcesRequest,
    ) -> ehpc20180412_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: ehpc20180412_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListTasksResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: ehpc20180412_models.ListTasksRequest,
    ) -> ehpc20180412_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_upgrade_clients_with_options(
        self,
        request: ehpc20180412_models.ListUpgradeClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUpgradeClientsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_upgrade_clients_with_options(request, runtime)

    async def list_upgrade_clients_async(
        self,
        request: ehpc20180412_models.ListUpgradeClientsRequest,
    ) -> ehpc20180412_models.ListUpgradeClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_upgrade_clients_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ehpc20180412_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ehpc20180412_models.ListUsersRequest,
    ) -> ehpc20180412_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_async_with_options(
        self,
        request: ehpc20180412_models.ListUsersAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListUsersAsyncResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_users_async_with_options(request, runtime)

    async def list_users_async_async(
        self,
        request: ehpc20180412_models.ListUsersAsyncRequest,
    ) -> ehpc20180412_models.ListUsersAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_async_with_options_async(request, runtime)

    def list_volumes_with_options(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ListVolumesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_volumes_with_options(request, runtime)

    async def list_volumes_async(
        self,
        request: ehpc20180412_models.ListVolumesRequest,
    ) -> ehpc20180412_models.ListVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_volumes_with_options_async(request, runtime)

    def modify_cluster_attributes_with_options(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_attributes_with_options(request, runtime)

    async def modify_cluster_attributes_async(
        self,
        request: ehpc20180412_models.ModifyClusterAttributesRequest,
    ) -> ehpc20180412_models.ModifyClusterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_attributes_with_options_async(request, runtime)

    def modify_container_app_attributes_with_options(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyContainerAppAttributes',
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
            ehpc20180412_models.ModifyContainerAppAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_container_app_attributes_with_options_async(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyContainerAppAttributes',
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
            ehpc20180412_models.ModifyContainerAppAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_container_app_attributes(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_container_app_attributes_with_options(request, runtime)

    async def modify_container_app_attributes_async(
        self,
        request: ehpc20180412_models.ModifyContainerAppAttributesRequest,
    ) -> ehpc20180412_models.ModifyContainerAppAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_container_app_attributes_with_options_async(request, runtime)

    def modify_image_gateway_config_with_options(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageGatewayConfig',
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
            ehpc20180412_models.ModifyImageGatewayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_gateway_config_with_options_async(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageGatewayConfig',
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
            ehpc20180412_models.ModifyImageGatewayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_gateway_config(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_gateway_config_with_options(request, runtime)

    async def modify_image_gateway_config_async(
        self,
        request: ehpc20180412_models.ModifyImageGatewayConfigRequest,
    ) -> ehpc20180412_models.ModifyImageGatewayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_gateway_config_with_options_async(request, runtime)

    def modify_user_groups_with_options(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_user_groups_with_options(request, runtime)

    async def modify_user_groups_async(
        self,
        request: ehpc20180412_models.ModifyUserGroupsRequest,
    ) -> ehpc20180412_models.ModifyUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_groups_with_options_async(request, runtime)

    def modify_user_passwords_with_options(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_user_passwords_with_options(request, runtime)

    async def modify_user_passwords_async(
        self,
        request: ehpc20180412_models.ModifyUserPasswordsRequest,
    ) -> ehpc20180412_models.ModifyUserPasswordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_passwords_with_options_async(request, runtime)

    def modify_visual_service_passwd_with_options(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_visual_service_passwd_with_options(request, runtime)

    async def modify_visual_service_passwd_async(
        self,
        request: ehpc20180412_models.ModifyVisualServicePasswdRequest,
    ) -> ehpc20180412_models.ModifyVisualServicePasswdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_visual_service_passwd_with_options_async(request, runtime)

    def mount_nfswith_options(
        self,
        request: ehpc20180412_models.MountNFSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.MountNFSResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MountNFS',
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
            ehpc20180412_models.MountNFSResponse(),
            self.call_api(params, req, runtime)
        )

    async def mount_nfswith_options_async(
        self,
        request: ehpc20180412_models.MountNFSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.MountNFSResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MountNFS',
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
            ehpc20180412_models.MountNFSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mount_nfs(
        self,
        request: ehpc20180412_models.MountNFSRequest,
    ) -> ehpc20180412_models.MountNFSResponse:
        runtime = util_models.RuntimeOptions()
        return self.mount_nfswith_options(request, runtime)

    async def mount_nfs_async(
        self,
        request: ehpc20180412_models.MountNFSRequest,
    ) -> ehpc20180412_models.MountNFSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mount_nfswith_options_async(request, runtime)

    def pull_image_with_options(
        self,
        request: ehpc20180412_models.PullImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.PullImageResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.pull_image_with_options(request, runtime)

    async def pull_image_async(
        self,
        request: ehpc20180412_models.PullImageRequest,
    ) -> ehpc20180412_models.PullImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pull_image_with_options_async(request, runtime)

    def query_service_pack_and_price_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_service_pack_and_price_with_options(runtime)

    async def query_service_pack_and_price_async(self) -> ehpc20180412_models.QueryServicePackAndPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_service_pack_and_price_with_options_async(runtime)

    def recover_cluster_with_options(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RecoverClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.recover_cluster_with_options(request, runtime)

    async def recover_cluster_async(
        self,
        request: ehpc20180412_models.RecoverClusterRequest,
    ) -> ehpc20180412_models.RecoverClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_cluster_with_options_async(request, runtime)

    def rerun_jobs_with_options(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RerunJobsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.rerun_jobs_with_options(request, runtime)

    async def rerun_jobs_async(
        self,
        request: ehpc20180412_models.RerunJobsRequest,
    ) -> ehpc20180412_models.RerunJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rerun_jobs_with_options_async(request, runtime)

    def reset_nodes_with_options(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.ResetNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.reset_nodes_with_options(request, runtime)

    async def reset_nodes_async(
        self,
        request: ehpc20180412_models.ResetNodesRequest,
    ) -> ehpc20180412_models.ResetNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_nodes_with_options_async(request, runtime)

    def run_cloud_metric_profiling_with_options(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_metric_profiling_with_options(request, runtime)

    async def run_cloud_metric_profiling_async(
        self,
        request: ehpc20180412_models.RunCloudMetricProfilingRequest,
    ) -> ehpc20180412_models.RunCloudMetricProfilingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_cloud_metric_profiling_with_options_async(request, runtime)

    def set_auto_scale_config_with_options(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_auto_scale_config_with_options(request, runtime)

    async def set_auto_scale_config_async(
        self,
        request: ehpc20180412_models.SetAutoScaleConfigRequest,
    ) -> ehpc20180412_models.SetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_auto_scale_config_with_options_async(request, runtime)

    def set_gwscluster_policy_with_options(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_mode):
            query['AsyncMode'] = request.async_mode
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.udp_port):
            query['UdpPort'] = request.udp_port
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSClusterPolicy',
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
            ehpc20180412_models.SetGWSClusterPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gwscluster_policy_with_options_async(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_mode):
            query['AsyncMode'] = request.async_mode
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.udp_port):
            query['UdpPort'] = request.udp_port
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSClusterPolicy',
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
            ehpc20180412_models.SetGWSClusterPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gwscluster_policy(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gwscluster_policy_with_options(request, runtime)

    async def set_gwscluster_policy_async(
        self,
        request: ehpc20180412_models.SetGWSClusterPolicyRequest,
    ) -> ehpc20180412_models.SetGWSClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gwscluster_policy_with_options_async(request, runtime)

    def set_gwsinstance_name_with_options(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSInstanceName',
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
            ehpc20180412_models.SetGWSInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gwsinstance_name_with_options_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSInstanceName',
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
            ehpc20180412_models.SetGWSInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gwsinstance_name(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_name_with_options(request, runtime)

    async def set_gwsinstance_name_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceNameRequest,
    ) -> ehpc20180412_models.SetGWSInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gwsinstance_name_with_options_async(request, runtime)

    def set_gwsinstance_user_with_options(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSInstanceUser',
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
            ehpc20180412_models.SetGWSInstanceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_gwsinstance_user_with_options_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSInstanceUser',
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
            ehpc20180412_models.SetGWSInstanceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_gwsinstance_user(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_user_with_options(request, runtime)

    async def set_gwsinstance_user_async(
        self,
        request: ehpc20180412_models.SetGWSInstanceUserRequest,
    ) -> ehpc20180412_models.SetGWSInstanceUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_gwsinstance_user_with_options_async(request, runtime)

    def set_post_scripts_with_options(
        self,
        request: ehpc20180412_models.SetPostScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetPostScriptsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_post_scripts_with_options(request, runtime)

    async def set_post_scripts_async(
        self,
        request: ehpc20180412_models.SetPostScriptsRequest,
    ) -> ehpc20180412_models.SetPostScriptsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_post_scripts_with_options_async(request, runtime)

    def set_queue_with_options(
        self,
        request: ehpc20180412_models.SetQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetQueueResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_queue_with_options(request, runtime)

    async def set_queue_async(
        self,
        request: ehpc20180412_models.SetQueueRequest,
    ) -> ehpc20180412_models.SetQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_queue_with_options_async(request, runtime)

    def set_scheduler_info_with_options(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_scheduler_info_with_options(request, runtime)

    async def set_scheduler_info_async(
        self,
        request: ehpc20180412_models.SetSchedulerInfoRequest,
    ) -> ehpc20180412_models.SetSchedulerInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scheduler_info_with_options_async(request, runtime)

    def start_cluster_with_options(
        self,
        request: ehpc20180412_models.StartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.start_cluster_with_options(request, runtime)

    async def start_cluster_async(
        self,
        request: ehpc20180412_models.StartClusterRequest,
    ) -> ehpc20180412_models.StartClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_cluster_with_options_async(request, runtime)

    def start_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartGWSInstance',
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
            ehpc20180412_models.StartGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartGWSInstance',
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
            ehpc20180412_models.StartGWSInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_gwsinstance(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_gwsinstance_with_options(request, runtime)

    async def start_gwsinstance_async(
        self,
        request: ehpc20180412_models.StartGWSInstanceRequest,
    ) -> ehpc20180412_models.StartGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_gwsinstance_with_options_async(request, runtime)

    def start_nodes_with_options(
        self,
        request: ehpc20180412_models.StartNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.start_nodes_with_options(request, runtime)

    async def start_nodes_async(
        self,
        request: ehpc20180412_models.StartNodesRequest,
    ) -> ehpc20180412_models.StartNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_nodes_with_options_async(request, runtime)

    def start_visual_service_with_options(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.start_visual_service_with_options(request, runtime)

    async def start_visual_service_async(
        self,
        request: ehpc20180412_models.StartVisualServiceRequest,
    ) -> ehpc20180412_models.StartVisualServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_visual_service_with_options_async(request, runtime)

    def stop_cluster_with_options(
        self,
        request: ehpc20180412_models.StopClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.stop_cluster_with_options(request, runtime)

    async def stop_cluster_async(
        self,
        request: ehpc20180412_models.StopClusterRequest,
    ) -> ehpc20180412_models.StopClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_cluster_with_options_async(request, runtime)

    def stop_gwsinstance_with_options(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopGWSInstance',
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
            ehpc20180412_models.StopGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_gwsinstance_with_options_async(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopGWSInstance',
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
            ehpc20180412_models.StopGWSInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_gwsinstance(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_gwsinstance_with_options(request, runtime)

    async def stop_gwsinstance_async(
        self,
        request: ehpc20180412_models.StopGWSInstanceRequest,
    ) -> ehpc20180412_models.StopGWSInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_gwsinstance_with_options_async(request, runtime)

    def stop_jobs_with_options(
        self,
        request: ehpc20180412_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopJobsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    async def stop_jobs_async(
        self,
        request: ehpc20180412_models.StopJobsRequest,
    ) -> ehpc20180412_models.StopJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_jobs_with_options_async(request, runtime)

    def stop_nodes_with_options(
        self,
        request: ehpc20180412_models.StopNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.stop_nodes_with_options(request, runtime)

    async def stop_nodes_async(
        self,
        request: ehpc20180412_models.StopNodesRequest,
    ) -> ehpc20180412_models.StopNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_nodes_with_options_async(request, runtime)

    def stop_visual_service_with_options(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.stop_visual_service_with_options(request, runtime)

    async def stop_visual_service_async(
        self,
        request: ehpc20180412_models.StopVisualServiceRequest,
    ) -> ehpc20180412_models.StopVisualServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_visual_service_with_options_async(request, runtime)

    def submit_job_with_options(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SubmitJobResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.submit_job_with_options(request, runtime)

    async def submit_job_async(
        self,
        request: ehpc20180412_models.SubmitJobRequest,
    ) -> ehpc20180412_models.SubmitJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_job_with_options_async(request, runtime)

    def summary_images_with_options(
        self,
        request: ehpc20180412_models.SummaryImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SummaryImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryImages',
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
            ehpc20180412_models.SummaryImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def summary_images_with_options_async(
        self,
        request: ehpc20180412_models.SummaryImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SummaryImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryImages',
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
            ehpc20180412_models.SummaryImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def summary_images(
        self,
        request: ehpc20180412_models.SummaryImagesRequest,
    ) -> ehpc20180412_models.SummaryImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.summary_images_with_options(request, runtime)

    async def summary_images_async(
        self,
        request: ehpc20180412_models.SummaryImagesRequest,
    ) -> ehpc20180412_models.SummaryImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.summary_images_with_options_async(request, runtime)

    def summary_images_info_with_options(
        self,
        request: ehpc20180412_models.SummaryImagesInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SummaryImagesInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryImagesInfo',
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
            ehpc20180412_models.SummaryImagesInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def summary_images_info_with_options_async(
        self,
        request: ehpc20180412_models.SummaryImagesInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SummaryImagesInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryImagesInfo',
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
            ehpc20180412_models.SummaryImagesInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def summary_images_info(
        self,
        request: ehpc20180412_models.SummaryImagesInfoRequest,
    ) -> ehpc20180412_models.SummaryImagesInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.summary_images_info_with_options(request, runtime)

    async def summary_images_info_async(
        self,
        request: ehpc20180412_models.SummaryImagesInfoRequest,
    ) -> ehpc20180412_models.SummaryImagesInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.summary_images_info_with_options_async(request, runtime)

    def sync_users_with_options(
        self,
        request: ehpc20180412_models.SyncUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.SyncUsersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.sync_users_with_options(request, runtime)

    async def sync_users_async(
        self,
        request: ehpc20180412_models.SyncUsersRequest,
    ) -> ehpc20180412_models.SyncUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_users_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ehpc20180412_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.TagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ehpc20180412_models.TagResourcesRequest,
    ) -> ehpc20180412_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: ehpc20180412_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UnTagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: ehpc20180412_models.UnTagResourcesRequest,
    ) -> ehpc20180412_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def uninstall_software_with_options(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.uninstall_software_with_options(request, runtime)

    async def uninstall_software_async(
        self,
        request: ehpc20180412_models.UninstallSoftwareRequest,
    ) -> ehpc20180412_models.UninstallSoftwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_software_with_options_async(request, runtime)

    def update_cluster_volumes_with_options(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_volumes_with_options(request, runtime)

    async def update_cluster_volumes_async(
        self,
        request: ehpc20180412_models.UpdateClusterVolumesRequest,
    ) -> ehpc20180412_models.UpdateClusterVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_volumes_with_options_async(request, runtime)

    def update_queue_config_with_options(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_queue_config_with_options(request, runtime)

    async def update_queue_config_async(
        self,
        request: ehpc20180412_models.UpdateQueueConfigRequest,
    ) -> ehpc20180412_models.UpdateQueueConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_queue_config_with_options_async(request, runtime)

    def upgrade_client_with_options(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20180412_models.UpgradeClientResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)

    async def upgrade_client_async(
        self,
        request: ehpc20180412_models.UpgradeClientRequest,
    ) -> ehpc20180412_models.UpgradeClientResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_client_with_options_async(request, runtime)
