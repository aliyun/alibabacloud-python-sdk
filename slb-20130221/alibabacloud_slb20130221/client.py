# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_slb20130221 import models as main_models
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
            'cn-qingdao': 'slb.aliyuncs.com',
            'cn-beijing': 'slb.aliyuncs.com',
            'cn-hangzhou': 'slb.aliyuncs.com',
            'cn-shanghai': 'slb.aliyuncs.com',
            'cn-shenzhen': 'slb.aliyuncs.com',
            'cn-hongkong': 'slb.aliyuncs.com',
            'ap-southeast-1': 'slb.aliyuncs.com',
            'us-east-1': 'slb.aliyuncs.com',
            'us-west-1': 'slb.aliyuncs.com',
            'cn-shanghai-finance-1': 'slb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'slb.aliyuncs.com',
            'cn-north-2-gov-1': 'slb.aliyuncs.com',
            'ap-northeast-2-pop': 'slb.aliyuncs.com',
            'cn-beijing-finance-pop': 'slb.aliyuncs.com',
            'cn-beijing-gov-1': 'slb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'slb.aliyuncs.com',
            'cn-edge-1': 'slb.aliyuncs.com',
            'cn-fujian': 'slb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'slb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'slb.aliyuncs.com',
            'cn-hangzhou-finance': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'slb.aliyuncs.com',
            'cn-hangzhou-test-306': 'slb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'slb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'slb-api.cn-qingdao-nebula.aliyuncs.com',
            'cn-shanghai-et15-b01': 'slb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'slb.aliyuncs.com',
            'cn-shanghai-inner': 'slb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'slb.aliyuncs.com',
            'cn-shenzhen-inner': 'slb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'slb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'slb.aliyuncs.com',
            'cn-wuhan': 'slb.aliyuncs.com',
            'cn-yushanfang': 'slb.aliyuncs.com',
            'cn-zhangbei': 'slb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'slb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'slb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'slb.aliyuncs.com',
            'eu-west-1-oxs': 'slb.aliyuncs.com',
            'rus-west-1-pop': 'slb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('slb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_backend_servers_with_options(
        self,
        request: main_models.AddBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBackendServers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_backend_servers_with_options_async(
        self,
        request: main_models.AddBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBackendServers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_backend_servers(
        self,
        request: main_models.AddBackendServersRequest,
    ) -> main_models.AddBackendServersResponse:
        runtime = RuntimeOptions()
        return self.add_backend_servers_with_options(request, runtime)

    async def add_backend_servers_async(
        self,
        request: main_models.AddBackendServersRequest,
    ) -> main_models.AddBackendServersResponse:
        runtime = RuntimeOptions()
        return await self.add_backend_servers_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: main_models.CreateLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.is_public_address):
            query['IsPublicAddress'] = request.is_public_address
        if not DaraCore.is_null(request.load_balancer_mode):
            query['LoadBalancerMode'] = request.load_balancer_mode
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: main_models.CreateLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.is_public_address):
            query['IsPublicAddress'] = request.is_public_address
        if not DaraCore.is_null(request.load_balancer_mode):
            query['LoadBalancerMode'] = request.load_balancer_mode
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer(
        self,
        request: main_models.CreateLoadBalancerRequest,
    ) -> main_models.CreateLoadBalancerResponse:
        runtime = RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: main_models.CreateLoadBalancerRequest,
    ) -> main_models.CreateLoadBalancerResponse:
        runtime = RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_load_balancer_httplistener_with_options(
        self,
        request: main_models.CreateLoadBalancerHTTPListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerHTTPListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_status):
            query['ListenerStatus'] = request.listener_status
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerHTTPListener',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerHTTPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_httplistener_with_options_async(
        self,
        request: main_models.CreateLoadBalancerHTTPListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerHTTPListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_status):
            query['ListenerStatus'] = request.listener_status
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerHTTPListener',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerHTTPListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_httplistener(
        self,
        request: main_models.CreateLoadBalancerHTTPListenerRequest,
    ) -> main_models.CreateLoadBalancerHTTPListenerResponse:
        runtime = RuntimeOptions()
        return self.create_load_balancer_httplistener_with_options(request, runtime)

    async def create_load_balancer_httplistener_async(
        self,
        request: main_models.CreateLoadBalancerHTTPListenerRequest,
    ) -> main_models.CreateLoadBalancerHTTPListenerResponse:
        runtime = RuntimeOptions()
        return await self.create_load_balancer_httplistener_with_options_async(request, runtime)

    def create_load_balancer_tcplistener_with_options(
        self,
        request: main_models.CreateLoadBalancerTCPListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerTCPListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.connect_port):
            query['ConnectPort'] = request.connect_port
        if not DaraCore.is_null(request.connect_timeout):
            query['ConnectTimeout'] = request.connect_timeout
        if not DaraCore.is_null(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_status):
            query['ListenerStatus'] = request.listener_status
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.max_connection):
            query['MaxConnection'] = request.max_connection
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerTCPListener',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerTCPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_tcplistener_with_options_async(
        self,
        request: main_models.CreateLoadBalancerTCPListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerTCPListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.connect_port):
            query['ConnectPort'] = request.connect_port
        if not DaraCore.is_null(request.connect_timeout):
            query['ConnectTimeout'] = request.connect_timeout
        if not DaraCore.is_null(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_status):
            query['ListenerStatus'] = request.listener_status
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.max_connection):
            query['MaxConnection'] = request.max_connection
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerTCPListener',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerTCPListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_tcplistener(
        self,
        request: main_models.CreateLoadBalancerTCPListenerRequest,
    ) -> main_models.CreateLoadBalancerTCPListenerResponse:
        runtime = RuntimeOptions()
        return self.create_load_balancer_tcplistener_with_options(request, runtime)

    async def create_load_balancer_tcplistener_async(
        self,
        request: main_models.CreateLoadBalancerTCPListenerRequest,
    ) -> main_models.CreateLoadBalancerTCPListenerResponse:
        runtime = RuntimeOptions()
        return await self.create_load_balancer_tcplistener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: main_models.DeleteLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: main_models.DeleteLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer(
        self,
        request: main_models.DeleteLoadBalancerRequest,
    ) -> main_models.DeleteLoadBalancerResponse:
        runtime = RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: main_models.DeleteLoadBalancerRequest,
    ) -> main_models.DeleteLoadBalancerResponse:
        runtime = RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_load_balancer_listener_with_options(
        self,
        request: main_models.DeleteLoadBalancerListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoadBalancerListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancerListener',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_listener_with_options_async(
        self,
        request: main_models.DeleteLoadBalancerListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoadBalancerListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancerListener',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer_listener(
        self,
        request: main_models.DeleteLoadBalancerListenerRequest,
    ) -> main_models.DeleteLoadBalancerListenerResponse:
        runtime = RuntimeOptions()
        return self.delete_load_balancer_listener_with_options(request, runtime)

    async def delete_load_balancer_listener_async(
        self,
        request: main_models.DeleteLoadBalancerListenerRequest,
    ) -> main_models.DeleteLoadBalancerListenerResponse:
        runtime = RuntimeOptions()
        return await self.delete_load_balancer_listener_with_options_async(request, runtime)

    def describe_backend_servers_with_options(
        self,
        request: main_models.DescribeBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackendServers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backend_servers_with_options_async(
        self,
        request: main_models.DescribeBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackendServers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backend_servers(
        self,
        request: main_models.DescribeBackendServersRequest,
    ) -> main_models.DescribeBackendServersResponse:
        runtime = RuntimeOptions()
        return self.describe_backend_servers_with_options(request, runtime)

    async def describe_backend_servers_async(
        self,
        request: main_models.DescribeBackendServersRequest,
    ) -> main_models.DescribeBackendServersResponse:
        runtime = RuntimeOptions()
        return await self.describe_backend_servers_with_options_async(request, runtime)

    def describe_load_balancer_attribute_with_options(
        self,
        request: main_models.DescribeLoadBalancerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_attribute_with_options_async(
        self,
        request: main_models.DescribeLoadBalancerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_attribute(
        self,
        request: main_models.DescribeLoadBalancerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_load_balancer_attribute_with_options(request, runtime)

    async def describe_load_balancer_attribute_async(
        self,
        request: main_models.DescribeLoadBalancerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_balancer_attribute_with_options_async(request, runtime)

    def describe_load_balancer_httplistener_attribute_with_options(
        self,
        request: main_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerHTTPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: main_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerHTTPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_httplistener_attribute(
        self,
        request: main_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_load_balancer_httplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_httplistener_attribute_async(
        self,
        request: main_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_balancer_httplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancer_tcplistener_attribute_with_options(
        self,
        request: main_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerTCPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: main_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerTCPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_tcplistener_attribute(
        self,
        request: main_models.DescribeLoadBalancerTCPListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_load_balancer_tcplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_tcplistener_attribute_async(
        self,
        request: main_models.DescribeLoadBalancerTCPListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_balancer_tcplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancers_with_options(
        self,
        request: main_models.DescribeLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.server_id):
            query['ServerId'] = request.server_id
        if not DaraCore.is_null(request.server_intranet_address):
            query['ServerIntranetAddress'] = request.server_intranet_address
        if not DaraCore.is_null(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancers_with_options_async(
        self,
        request: main_models.DescribeLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.server_id):
            query['ServerId'] = request.server_id
        if not DaraCore.is_null(request.server_intranet_address):
            query['ServerIntranetAddress'] = request.server_intranet_address
        if not DaraCore.is_null(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancers(
        self,
        request: main_models.DescribeLoadBalancersRequest,
    ) -> main_models.DescribeLoadBalancersResponse:
        runtime = RuntimeOptions()
        return self.describe_load_balancers_with_options(request, runtime)

    async def describe_load_balancers_async(
        self,
        request: main_models.DescribeLoadBalancersRequest,
    ) -> main_models.DescribeLoadBalancersResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_balancers_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def remove_backend_servers_with_options(
        self,
        request: main_models.RemoveBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveBackendServers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_backend_servers_with_options_async(
        self,
        request: main_models.RemoveBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveBackendServers',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_backend_servers(
        self,
        request: main_models.RemoveBackendServersRequest,
    ) -> main_models.RemoveBackendServersResponse:
        runtime = RuntimeOptions()
        return self.remove_backend_servers_with_options(request, runtime)

    async def remove_backend_servers_async(
        self,
        request: main_models.RemoveBackendServersRequest,
    ) -> main_models.RemoveBackendServersResponse:
        runtime = RuntimeOptions()
        return await self.remove_backend_servers_with_options_async(request, runtime)

    def set_load_balancer_httplistener_attribute_with_options(
        self,
        request: main_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerHTTPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerHTTPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: main_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerHTTPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerHTTPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_httplistener_attribute(
        self,
        request: main_models.SetLoadBalancerHTTPListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerHTTPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_httplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_httplistener_attribute_async(
        self,
        request: main_models.SetLoadBalancerHTTPListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerHTTPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_httplistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_listener_status_with_options(
        self,
        request: main_models.SetLoadBalancerListenerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerListenerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_status):
            query['ListenerStatus'] = request.listener_status
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerListenerStatus',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerListenerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_listener_status_with_options_async(
        self,
        request: main_models.SetLoadBalancerListenerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerListenerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_status):
            query['ListenerStatus'] = request.listener_status
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerListenerStatus',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerListenerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_listener_status(
        self,
        request: main_models.SetLoadBalancerListenerStatusRequest,
    ) -> main_models.SetLoadBalancerListenerStatusResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_listener_status_with_options(request, runtime)

    async def set_load_balancer_listener_status_async(
        self,
        request: main_models.SetLoadBalancerListenerStatusRequest,
    ) -> main_models.SetLoadBalancerListenerStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_listener_status_with_options_async(request, runtime)

    def set_load_balancer_name_with_options(
        self,
        request: main_models.SetLoadBalancerNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerName',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_name_with_options_async(
        self,
        request: main_models.SetLoadBalancerNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerName',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_name(
        self,
        request: main_models.SetLoadBalancerNameRequest,
    ) -> main_models.SetLoadBalancerNameResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_name_with_options(request, runtime)

    async def set_load_balancer_name_async(
        self,
        request: main_models.SetLoadBalancerNameRequest,
    ) -> main_models.SetLoadBalancerNameResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_name_with_options_async(request, runtime)

    def set_load_balancer_status_with_options(
        self,
        request: main_models.SetLoadBalancerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerStatus',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_status_with_options_async(
        self,
        request: main_models.SetLoadBalancerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerStatus',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_status(
        self,
        request: main_models.SetLoadBalancerStatusRequest,
    ) -> main_models.SetLoadBalancerStatusResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_status_with_options(request, runtime)

    async def set_load_balancer_status_async(
        self,
        request: main_models.SetLoadBalancerStatusRequest,
    ) -> main_models.SetLoadBalancerStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_status_with_options_async(request, runtime)

    def set_load_balancer_tcplistener_attribute_with_options(
        self,
        request: main_models.SetLoadBalancerTCPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerTCPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_port):
            query['ConnectPort'] = request.connect_port
        if not DaraCore.is_null(request.connect_timeout):
            query['ConnectTimeout'] = request.connect_timeout
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerTCPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: main_models.SetLoadBalancerTCPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerTCPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_port):
            query['ConnectPort'] = request.connect_port
        if not DaraCore.is_null(request.connect_timeout):
            query['ConnectTimeout'] = request.connect_timeout
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerTCPListenerAttribute',
            version = '2013-02-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerTCPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_tcplistener_attribute(
        self,
        request: main_models.SetLoadBalancerTCPListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerTCPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_tcplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_tcplistener_attribute_async(
        self,
        request: main_models.SetLoadBalancerTCPListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerTCPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_tcplistener_attribute_with_options_async(request, runtime)
