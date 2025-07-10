# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gwlb20240415 import models as gwlb_20240415_models
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
        self._endpoint = self.get_endpoint('gwlb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_servers_to_server_group_with_options(
        self,
        request: gwlb_20240415_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of the server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of the backend server.
        If the backend server is in the **Adding** state, the backend server is being added to the server group.
        If the backend server is in the **Available** state, the server is running.
        
        @param request: AddServersToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServersToServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.servers):
            body_flat['Servers'] = request.servers
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.AddServersToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_servers_to_server_group_with_options_async(
        self,
        request: gwlb_20240415_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of the server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of the backend server.
        If the backend server is in the **Adding** state, the backend server is being added to the server group.
        If the backend server is in the **Available** state, the server is running.
        
        @param request: AddServersToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServersToServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.servers):
            body_flat['Servers'] = request.servers
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.AddServersToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_servers_to_server_group(
        self,
        request: gwlb_20240415_models.AddServersToServerGroupRequest,
    ) -> gwlb_20240415_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of the server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of the backend server.
        If the backend server is in the **Adding** state, the backend server is being added to the server group.
        If the backend server is in the **Available** state, the server is running.
        
        @param request: AddServersToServerGroupRequest
        @return: AddServersToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_servers_to_server_group_with_options(request, runtime)

    async def add_servers_to_server_group_async(
        self,
        request: gwlb_20240415_models.AddServersToServerGroupRequest,
    ) -> gwlb_20240415_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of the server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of the backend server.
        If the backend server is in the **Adding** state, the backend server is being added to the server group.
        If the backend server is in the **Available** state, the server is running.
        
        @param request: AddServersToServerGroupRequest
        @return: AddServersToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_servers_to_server_group_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        request: gwlb_20240415_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.CreateListenerResponse:
        """
        @summary Creates a listener for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Provisioning** state, the listener is being created.
        If the listener is in the **Running** state, the listener is running.
        
        @param request: CreateListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.CreateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_listener_with_options_async(
        self,
        request: gwlb_20240415_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.CreateListenerResponse:
        """
        @summary Creates a listener for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Provisioning** state, the listener is being created.
        If the listener is in the **Running** state, the listener is running.
        
        @param request: CreateListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.CreateListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_listener(
        self,
        request: gwlb_20240415_models.CreateListenerRequest,
    ) -> gwlb_20240415_models.CreateListenerResponse:
        """
        @summary Creates a listener for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Provisioning** state, the listener is being created.
        If the listener is in the **Running** state, the listener is running.
        
        @param request: CreateListenerRequest
        @return: CreateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    async def create_listener_async(
        self,
        request: gwlb_20240415_models.CreateListenerRequest,
    ) -> gwlb_20240415_models.CreateListenerResponse:
        """
        @summary Creates a listener for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Provisioning** state, the listener is being created.
        If the listener is in the **Running** state, the listener is running.
        
        @param request: CreateListenerRequest
        @return: CreateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_listener_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: gwlb_20240415_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.CreateLoadBalancerResponse:
        """
        @summary Creates a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        When you create a GWLB instance, the service-linked role AliyunServiceRoleForGwlb is automatically created.
        **CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of a GWLB instance.
        If the GWLB instance is in the **Provisioning** state, the GWLB instance is being created.
        If the GWLB instance is in the **Active** state, the GWLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: gwlb_20240415_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.CreateLoadBalancerResponse:
        """
        @summary Creates a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        When you create a GWLB instance, the service-linked role AliyunServiceRoleForGwlb is automatically created.
        **CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of a GWLB instance.
        If the GWLB instance is in the **Provisioning** state, the GWLB instance is being created.
        If the GWLB instance is in the **Active** state, the GWLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer(
        self,
        request: gwlb_20240415_models.CreateLoadBalancerRequest,
    ) -> gwlb_20240415_models.CreateLoadBalancerResponse:
        """
        @summary Creates a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        When you create a GWLB instance, the service-linked role AliyunServiceRoleForGwlb is automatically created.
        **CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of a GWLB instance.
        If the GWLB instance is in the **Provisioning** state, the GWLB instance is being created.
        If the GWLB instance is in the **Active** state, the GWLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: gwlb_20240415_models.CreateLoadBalancerRequest,
    ) -> gwlb_20240415_models.CreateLoadBalancerResponse:
        """
        @summary Creates a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        When you create a GWLB instance, the service-linked role AliyunServiceRoleForGwlb is automatically created.
        **CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of a GWLB instance.
        If the GWLB instance is in the **Provisioning** state, the GWLB instance is being created.
        If the GWLB instance is in the **Active** state, the GWLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_server_group_with_options(
        self,
        request: gwlb_20240415_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.CreateServerGroupResponse:
        """
        @summary Creates a server group for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Creating** state, it indicates that the server group is being created.
        If the server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not UtilClient.is_unset(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.CreateServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_group_with_options_async(
        self,
        request: gwlb_20240415_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.CreateServerGroupResponse:
        """
        @summary Creates a server group for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Creating** state, it indicates that the server group is being created.
        If the server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not UtilClient.is_unset(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.CreateServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_group(
        self,
        request: gwlb_20240415_models.CreateServerGroupRequest,
    ) -> gwlb_20240415_models.CreateServerGroupResponse:
        """
        @summary Creates a server group for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Creating** state, it indicates that the server group is being created.
        If the server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @return: CreateServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_server_group_with_options(request, runtime)

    async def create_server_group_async(
        self,
        request: gwlb_20240415_models.CreateServerGroupRequest,
    ) -> gwlb_20240415_models.CreateServerGroupResponse:
        """
        @summary Creates a server group for a Gateway Load Balancer (GWLB) instance.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Creating** state, it indicates that the server group is being created.
        If the server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @return: CreateServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_server_group_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: gwlb_20240415_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DeleteListenerResponse:
        """
        @summary Deletes a listener from a Gateway Load Balancer (GWLB) instance.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DeleteListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_listener_with_options_async(
        self,
        request: gwlb_20240415_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DeleteListenerResponse:
        """
        @summary Deletes a listener from a Gateway Load Balancer (GWLB) instance.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DeleteListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_listener(
        self,
        request: gwlb_20240415_models.DeleteListenerRequest,
    ) -> gwlb_20240415_models.DeleteListenerResponse:
        """
        @summary Deletes a listener from a Gateway Load Balancer (GWLB) instance.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @return: DeleteListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    async def delete_listener_async(
        self,
        request: gwlb_20240415_models.DeleteListenerRequest,
    ) -> gwlb_20240415_models.DeleteListenerResponse:
        """
        @summary Deletes a listener from a Gateway Load Balancer (GWLB) instance.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @return: DeleteListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_listener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: gwlb_20240415_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes a Gateway Load Balancer (GWLB) instance.
        
        @param request: DeleteLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: gwlb_20240415_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes a Gateway Load Balancer (GWLB) instance.
        
        @param request: DeleteLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DeleteLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer(
        self,
        request: gwlb_20240415_models.DeleteLoadBalancerRequest,
    ) -> gwlb_20240415_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes a Gateway Load Balancer (GWLB) instance.
        
        @param request: DeleteLoadBalancerRequest
        @return: DeleteLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: gwlb_20240415_models.DeleteLoadBalancerRequest,
    ) -> gwlb_20240415_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes a Gateway Load Balancer (GWLB) instance.
        
        @param request: DeleteLoadBalancerRequest
        @return: DeleteLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_server_group_with_options(
        self,
        request: gwlb_20240415_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group from a Gateway Load Balancer (GWLB) instance.
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DeleteServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_server_group_with_options_async(
        self,
        request: gwlb_20240415_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group from a Gateway Load Balancer (GWLB) instance.
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DeleteServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_server_group(
        self,
        request: gwlb_20240415_models.DeleteServerGroupRequest,
    ) -> gwlb_20240415_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group from a Gateway Load Balancer (GWLB) instance.
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @return: DeleteServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_server_group_with_options(request, runtime)

    async def delete_server_group_async(
        self,
        request: gwlb_20240415_models.DeleteServerGroupRequest,
    ) -> gwlb_20240415_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group from a Gateway Load Balancer (GWLB) instance.
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @return: DeleteServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_server_group_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: gwlb_20240415_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: gwlb_20240415_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: gwlb_20240415_models.DescribeRegionsRequest,
    ) -> gwlb_20240415_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: gwlb_20240415_models.DescribeRegionsRequest,
    ) -> gwlb_20240415_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: gwlb_20240415_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DescribeZonesResponse:
        """
        @summary Queries the most recent zone list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: gwlb_20240415_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.DescribeZonesResponse:
        """
        @summary Queries the most recent zone list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: gwlb_20240415_models.DescribeZonesRequest,
    ) -> gwlb_20240415_models.DescribeZonesResponse:
        """
        @summary Queries the most recent zone list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: gwlb_20240415_models.DescribeZonesRequest,
    ) -> gwlb_20240415_models.DescribeZonesResponse:
        """
        @summary Queries the most recent zone list of Gateway Load Balancer (GWLB).
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: gwlb_20240415_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.GetListenerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.GetListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_attribute_with_options_async(
        self,
        request: gwlb_20240415_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.GetListenerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.GetListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_attribute(
        self,
        request: gwlb_20240415_models.GetListenerAttributeRequest,
    ) -> gwlb_20240415_models.GetListenerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerAttributeRequest
        @return: GetListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_listener_attribute_with_options(request, runtime)

    async def get_listener_attribute_async(
        self,
        request: gwlb_20240415_models.GetListenerAttributeRequest,
    ) -> gwlb_20240415_models.GetListenerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerAttributeRequest
        @return: GetListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_attribute_with_options_async(request, runtime)

    def get_listener_health_status_with_options(
        self,
        request: gwlb_20240415_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerHealthStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.filter):
            body_flat['Filter'] = request.filter
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.GetListenerHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_health_status_with_options_async(
        self,
        request: gwlb_20240415_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerHealthStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.filter):
            body_flat['Filter'] = request.filter
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.GetListenerHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_health_status(
        self,
        request: gwlb_20240415_models.GetListenerHealthStatusRequest,
    ) -> gwlb_20240415_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerHealthStatusRequest
        @return: GetListenerHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_listener_health_status_with_options(request, runtime)

    async def get_listener_health_status_async(
        self,
        request: gwlb_20240415_models.GetListenerHealthStatusRequest,
    ) -> gwlb_20240415_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a Gateway Load Balancer (GWLB) listener.
        
        @param request: GetListenerHealthStatusRequest
        @return: GetListenerHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_health_status_with_options_async(request, runtime)

    def get_load_balancer_attribute_with_options(
        self,
        request: gwlb_20240415_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.GetLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_load_balancer_attribute_with_options_async(
        self,
        request: gwlb_20240415_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.GetLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_load_balancer_attribute(
        self,
        request: gwlb_20240415_models.GetLoadBalancerAttributeRequest,
    ) -> gwlb_20240415_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @return: GetLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_load_balancer_attribute_with_options(request, runtime)

    async def get_load_balancer_attribute_async(
        self,
        request: gwlb_20240415_models.GetLoadBalancerAttributeRequest,
    ) -> gwlb_20240415_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of a Gateway Load Balancer (GWLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @return: GetLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_load_balancer_attribute_with_options_async(request, runtime)

    def list_listeners_with_options(
        self,
        request: gwlb_20240415_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListListenersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) listeners.
        
        @param request: ListListenersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.listener_ids):
            body_flat['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_with_options_async(
        self,
        request: gwlb_20240415_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListListenersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) listeners.
        
        @param request: ListListenersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.listener_ids):
            body_flat['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners(
        self,
        request: gwlb_20240415_models.ListListenersRequest,
    ) -> gwlb_20240415_models.ListListenersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) listeners.
        
        @param request: ListListenersRequest
        @return: ListListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    async def list_listeners_async(
        self,
        request: gwlb_20240415_models.ListListenersRequest,
    ) -> gwlb_20240415_models.ListListenersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) listeners.
        
        @param request: ListListenersRequest
        @return: ListListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_with_options_async(request, runtime)

    def list_load_balancers_with_options(
        self,
        request: gwlb_20240415_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListLoadBalancersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) instances.
        
        @param request: ListLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.load_balancer_business_status):
            body['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        body_flat = {}
        if not UtilClient.is_unset(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            body_flat['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            body['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        if not UtilClient.is_unset(request.vpc_ids):
            body_flat['VpcIds'] = request.vpc_ids
        if not UtilClient.is_unset(request.zone_ids):
            body_flat['ZoneIds'] = request.zone_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLoadBalancers',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_load_balancers_with_options_async(
        self,
        request: gwlb_20240415_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListLoadBalancersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) instances.
        
        @param request: ListLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.load_balancer_business_status):
            body['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        body_flat = {}
        if not UtilClient.is_unset(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            body_flat['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            body['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        if not UtilClient.is_unset(request.vpc_ids):
            body_flat['VpcIds'] = request.vpc_ids
        if not UtilClient.is_unset(request.zone_ids):
            body_flat['ZoneIds'] = request.zone_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLoadBalancers',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_load_balancers(
        self,
        request: gwlb_20240415_models.ListLoadBalancersRequest,
    ) -> gwlb_20240415_models.ListLoadBalancersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) instances.
        
        @param request: ListLoadBalancersRequest
        @return: ListLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_load_balancers_with_options(request, runtime)

    async def list_load_balancers_async(
        self,
        request: gwlb_20240415_models.ListLoadBalancersRequest,
    ) -> gwlb_20240415_models.ListLoadBalancersResponse:
        """
        @summary Queries Gateway Load Balancer (GWLB) instances.
        
        @param request: ListLoadBalancersRequest
        @return: ListLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_load_balancers_with_options_async(request, runtime)

    def list_server_group_servers_with_options(
        self,
        request: gwlb_20240415_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListServerGroupServersResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupServersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.server_ids):
            body_flat['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.server_ips):
            body_flat['ServerIps'] = request.server_ips
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListServerGroupServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_group_servers_with_options_async(
        self,
        request: gwlb_20240415_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListServerGroupServersResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupServersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.server_ids):
            body_flat['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.server_ips):
            body_flat['ServerIps'] = request.server_ips
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListServerGroupServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_group_servers(
        self,
        request: gwlb_20240415_models.ListServerGroupServersRequest,
    ) -> gwlb_20240415_models.ListServerGroupServersResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupServersRequest
        @return: ListServerGroupServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_server_group_servers_with_options(request, runtime)

    async def list_server_group_servers_async(
        self,
        request: gwlb_20240415_models.ListServerGroupServersRequest,
    ) -> gwlb_20240415_models.ListServerGroupServersResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupServersRequest
        @return: ListServerGroupServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_server_group_servers_with_options_async(request, runtime)

    def list_server_groups_with_options(
        self,
        request: gwlb_20240415_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListServerGroupsResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.server_group_ids):
            body_flat['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            body_flat['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_groups_with_options_async(
        self,
        request: gwlb_20240415_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListServerGroupsResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.server_group_ids):
            body_flat['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            body_flat['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.skip):
            body['Skip'] = request.skip
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_groups(
        self,
        request: gwlb_20240415_models.ListServerGroupsRequest,
    ) -> gwlb_20240415_models.ListServerGroupsResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupsRequest
        @return: ListServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_server_groups_with_options(request, runtime)

    async def list_server_groups_async(
        self,
        request: gwlb_20240415_models.ListServerGroupsRequest,
    ) -> gwlb_20240415_models.ListServerGroupsResponse:
        """
        @summary Queries the server groups of a Gateway Load Balancer (GWLB) instance.
        
        @param request: ListServerGroupsRequest
        @return: ListServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_server_groups_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: gwlb_20240415_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: gwlb_20240415_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: gwlb_20240415_models.ListTagResourcesRequest,
    ) -> gwlb_20240415_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: gwlb_20240415_models.ListTagResourcesRequest,
    ) -> gwlb_20240415_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: gwlb_20240415_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.MoveResourceGroupResponse:
        """
        @summary Changes the resource group to which a specified cloud resource belongs.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: gwlb_20240415_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.MoveResourceGroupResponse:
        """
        @summary Changes the resource group to which a specified cloud resource belongs.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: gwlb_20240415_models.MoveResourceGroupRequest,
    ) -> gwlb_20240415_models.MoveResourceGroupResponse:
        """
        @summary Changes the resource group to which a specified cloud resource belongs.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: gwlb_20240415_models.MoveResourceGroupRequest,
    ) -> gwlb_20240415_models.MoveResourceGroupResponse:
        """
        @summary Changes the resource group to which a specified cloud resource belongs.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def remove_servers_from_server_group_with_options(
        self,
        request: gwlb_20240415_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of a server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of a backend server.
        If the backend server is in the **Removing** state, the backend server is being removed from the server group.
        If the backend server cannot be found, the backend server is no longer in the server group.
        >
        If connection draining id enabled (**ConnectionDrainEnabled** set to true) for the server group of the backend server, the backend server that you remove enters the **Removing** state before entering the **Draining** state. When the connection draining timeout period (**ConnectionDrainTimeout**) ends, the backend server is removed from the server group.
        You can add the backend server to the server group again before the connection draining timeout period ends. In this case, the status of the backend server changes from **Draining** to **Adding**. After the backend server is added to the server group, the backend server enters the **Available** state.
        
        @param request: RemoveServersFromServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServersFromServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.servers):
            body_flat['Servers'] = request.servers
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.RemoveServersFromServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_servers_from_server_group_with_options_async(
        self,
        request: gwlb_20240415_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of a server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of a backend server.
        If the backend server is in the **Removing** state, the backend server is being removed from the server group.
        If the backend server cannot be found, the backend server is no longer in the server group.
        >
        If connection draining id enabled (**ConnectionDrainEnabled** set to true) for the server group of the backend server, the backend server that you remove enters the **Removing** state before entering the **Draining** state. When the connection draining timeout period (**ConnectionDrainTimeout**) ends, the backend server is removed from the server group.
        You can add the backend server to the server group again before the connection draining timeout period ends. In this case, the status of the backend server changes from **Draining** to **Adding**. After the backend server is added to the server group, the backend server enters the **Available** state.
        
        @param request: RemoveServersFromServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServersFromServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not UtilClient.is_unset(request.servers):
            body_flat['Servers'] = request.servers
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.RemoveServersFromServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_servers_from_server_group(
        self,
        request: gwlb_20240415_models.RemoveServersFromServerGroupRequest,
    ) -> gwlb_20240415_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of a server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of a backend server.
        If the backend server is in the **Removing** state, the backend server is being removed from the server group.
        If the backend server cannot be found, the backend server is no longer in the server group.
        >
        If connection draining id enabled (**ConnectionDrainEnabled** set to true) for the server group of the backend server, the backend server that you remove enters the **Removing** state before entering the **Draining** state. When the connection draining timeout period (**ConnectionDrainTimeout**) ends, the backend server is removed from the server group.
        You can add the backend server to the server group again before the connection draining timeout period ends. In this case, the status of the backend server changes from **Draining** to **Adding**. After the backend server is added to the server group, the backend server enters the **Available** state.
        
        @param request: RemoveServersFromServerGroupRequest
        @return: RemoveServersFromServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_servers_from_server_group_with_options(request, runtime)

    async def remove_servers_from_server_group_async(
        self,
        request: gwlb_20240415_models.RemoveServersFromServerGroupRequest,
    ) -> gwlb_20240415_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from the server group of a Gateway Load Balancer (GWLB) instance.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the ListServerGroups operation to query the status of a server group.
        If the server group is in the **Configuring** state, the server group is being modified.
        If the server group is in the **Available** state, the server group is running.
        2.  You can call the ListServerGroupServers operation to query the status of a backend server.
        If the backend server is in the **Removing** state, the backend server is being removed from the server group.
        If the backend server cannot be found, the backend server is no longer in the server group.
        >
        If connection draining id enabled (**ConnectionDrainEnabled** set to true) for the server group of the backend server, the backend server that you remove enters the **Removing** state before entering the **Draining** state. When the connection draining timeout period (**ConnectionDrainTimeout**) ends, the backend server is removed from the server group.
        You can add the backend server to the server group again before the connection draining timeout period ends. In this case, the status of the backend server changes from **Draining** to **Adding**. After the backend server is added to the server group, the backend server enters the **Available** state.
        
        @param request: RemoveServersFromServerGroupRequest
        @return: RemoveServersFromServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_servers_from_server_group_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: gwlb_20240415_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: gwlb_20240415_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: gwlb_20240415_models.TagResourcesRequest,
    ) -> gwlb_20240415_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: gwlb_20240415_models.TagResourcesRequest,
    ) -> gwlb_20240415_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: gwlb_20240415_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: gwlb_20240415_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: gwlb_20240415_models.UntagResourcesRequest,
    ) -> gwlb_20240415_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: gwlb_20240415_models.UntagResourcesRequest,
    ) -> gwlb_20240415_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_listener_attribute_with_options(
        self,
        request: gwlb_20240415_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the configurations of a Gateway Load Balancer (GWLB) listener.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of a listener.
        If the listener is in the **Configuring** state, the listener is being modified.
        If the listener is in the **Running** state, the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_attribute_with_options_async(
        self,
        request: gwlb_20240415_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the configurations of a Gateway Load Balancer (GWLB) listener.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of a listener.
        If the listener is in the **Configuring** state, the listener is being modified.
        If the listener is in the **Running** state, the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_attribute(
        self,
        request: gwlb_20240415_models.UpdateListenerAttributeRequest,
    ) -> gwlb_20240415_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the configurations of a Gateway Load Balancer (GWLB) listener.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of a listener.
        If the listener is in the **Configuring** state, the listener is being modified.
        If the listener is in the **Running** state, the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @return: UpdateListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_listener_attribute_with_options(request, runtime)

    async def update_listener_attribute_async(
        self,
        request: gwlb_20240415_models.UpdateListenerAttributeRequest,
    ) -> gwlb_20240415_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the configurations of a Gateway Load Balancer (GWLB) listener.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the **GetListenerAttribute** operation to query the status of a listener.
        If the listener is in the **Configuring** state, the listener is being modified.
        If the listener is in the **Running** state, the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @return: UpdateListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_attribute_with_options_async(request, runtime)

    def update_load_balancer_attribute_with_options(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Updates the attributes of a Gateway Load Balancer (GWLB) instance.
        
        @description    UpdateLoadBalancerAttribute is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the GetLoadBalancerAttribute operation to query the status of the GWLB instance.
        If the GWLB instance is in the Configuring state, the GWLB instance is being modified.
        If the GWLB instance is in the Active state, the GWLB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_attribute_with_options_async(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Updates the attributes of a Gateway Load Balancer (GWLB) instance.
        
        @description    UpdateLoadBalancerAttribute is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the GetLoadBalancerAttribute operation to query the status of the GWLB instance.
        If the GWLB instance is in the Configuring state, the GWLB instance is being modified.
        If the GWLB instance is in the Active state, the GWLB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_attribute(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerAttributeRequest,
    ) -> gwlb_20240415_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Updates the attributes of a Gateway Load Balancer (GWLB) instance.
        
        @description    UpdateLoadBalancerAttribute is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the GetLoadBalancerAttribute operation to query the status of the GWLB instance.
        If the GWLB instance is in the Configuring state, the GWLB instance is being modified.
        If the GWLB instance is in the Active state, the GWLB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @return: UpdateLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_attribute_with_options(request, runtime)

    async def update_load_balancer_attribute_async(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerAttributeRequest,
    ) -> gwlb_20240415_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Updates the attributes of a Gateway Load Balancer (GWLB) instance.
        
        @description    UpdateLoadBalancerAttribute is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the GetLoadBalancerAttribute operation to query the status of the GWLB instance.
        If the GWLB instance is in the Configuring state, the GWLB instance is being modified.
        If the GWLB instance is in the Active state, the GWLB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @return: UpdateLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_attribute_with_options_async(request, runtime)

    def update_load_balancer_zones_with_options(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Updates the zones of a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of the GWLB instance.
        If the GWLB instance is in the **Configuring** state, the GWLB instance is being modified.
        If the GWLB instance is in the **Active** state, the GWLB instance is modified.
        >  Before you initiate a call, ensure that all zones, including the current zones and the zones that you want to add, are specified. The zones that you do not specify are deleted. You can call the GetLoadBalancerAttribute operation to query the current zones of your GWLB instance.
        
        @param request: UpdateLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        body_flat = {}
        if not UtilClient.is_unset(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_zones_with_options_async(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Updates the zones of a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of the GWLB instance.
        If the GWLB instance is in the **Configuring** state, the GWLB instance is being modified.
        If the GWLB instance is in the **Active** state, the GWLB instance is modified.
        >  Before you initiate a call, ensure that all zones, including the current zones and the zones that you want to add, are specified. The zones that you do not specify are deleted. You can call the GetLoadBalancerAttribute operation to query the current zones of your GWLB instance.
        
        @param request: UpdateLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        body_flat = {}
        if not UtilClient.is_unset(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_zones(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerZonesRequest,
    ) -> gwlb_20240415_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Updates the zones of a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of the GWLB instance.
        If the GWLB instance is in the **Configuring** state, the GWLB instance is being modified.
        If the GWLB instance is in the **Active** state, the GWLB instance is modified.
        >  Before you initiate a call, ensure that all zones, including the current zones and the zones that you want to add, are specified. The zones that you do not specify are deleted. You can call the GetLoadBalancerAttribute operation to query the current zones of your GWLB instance.
        
        @param request: UpdateLoadBalancerZonesRequest
        @return: UpdateLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_zones_with_options(request, runtime)

    async def update_load_balancer_zones_async(
        self,
        request: gwlb_20240415_models.UpdateLoadBalancerZonesRequest,
    ) -> gwlb_20240415_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Updates the zones of a Gateway Load Balancer (GWLB) instance.
        
        @description *Ensure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/2806160.html) of GWLB before calling this operation.**\
        *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/2853555.html) operation to query the status of the GWLB instance.
        If the GWLB instance is in the **Configuring** state, the GWLB instance is being modified.
        If the GWLB instance is in the **Active** state, the GWLB instance is modified.
        >  Before you initiate a call, ensure that all zones, including the current zones and the zones that you want to add, are specified. The zones that you do not specify are deleted. You can call the GetLoadBalancerAttribute operation to query the current zones of your GWLB instance.
        
        @param request: UpdateLoadBalancerZonesRequest
        @return: UpdateLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_zones_with_options_async(request, runtime)

    def update_server_group_attribute_with_options(
        self,
        request: gwlb_20240415_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateServerGroupAttributeResponse:
        """
        @summary Updates the attributes of a server group.
        
        @description *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Configuring** state, the configuration of the server group is being modified.
        If the server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not UtilClient.is_unset(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_attribute_with_options_async(
        self,
        request: gwlb_20240415_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gwlb_20240415_models.UpdateServerGroupAttributeResponse:
        """
        @summary Updates the attributes of a server group.
        
        @description *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Configuring** state, the configuration of the server group is being modified.
        If the server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not UtilClient.is_unset(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2024-04-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gwlb_20240415_models.UpdateServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_attribute(
        self,
        request: gwlb_20240415_models.UpdateServerGroupAttributeRequest,
    ) -> gwlb_20240415_models.UpdateServerGroupAttributeResponse:
        """
        @summary Updates the attributes of a server group.
        
        @description *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Configuring** state, the configuration of the server group is being modified.
        If the server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @return: UpdateServerGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_attribute_with_options(request, runtime)

    async def update_server_group_attribute_async(
        self,
        request: gwlb_20240415_models.UpdateServerGroupAttributeRequest,
    ) -> gwlb_20240415_models.UpdateServerGroupAttributeResponse:
        """
        @summary Updates the attributes of a server group.
        
        @description *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the ListServerGroups operation to query the status of the task.
        If the server group is in the **Configuring** state, the configuration of the server group is being modified.
        If the server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @return: UpdateServerGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_attribute_with_options_async(request, runtime)
