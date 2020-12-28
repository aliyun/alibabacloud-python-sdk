# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_slb20140515 import models as slb_20140515_models
from alibabacloud_tea_util import models as util_models


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
            'cn-qingdao': 'slb.aliyuncs.com',
            'cn-beijing': 'slb.aliyuncs.com',
            'cn-hangzhou': 'slb.aliyuncs.com',
            'cn-shanghai': 'slb.aliyuncs.com',
            'cn-shenzhen': 'slb.aliyuncs.com',
            'cn-hongkong': 'slb.aliyuncs.com',
            'ap-southeast-1': 'slb.aliyuncs.com',
            'us-west-1': 'slb.aliyuncs.com',
            'us-east-1': 'slb.aliyuncs.com',
            'cn-shanghai-finance-1': 'slb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'slb.aliyuncs.com',
            'cn-north-2-gov-1': 'slb.aliyuncs.com',
            'ap-northeast-2-pop': 'slb.aliyuncs.com',
            'cn-beijing-finance-1': 'slb.aliyuncs.com',
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_access_control_list_entry_with_options(
        self,
        request: slb_20140515_models.AddAccessControlListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddAccessControlListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddAccessControlListEntryResponse().from_map(
            self.do_rpcrequest('AddAccessControlListEntry', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_access_control_list_entry_with_options_async(
        self,
        request: slb_20140515_models.AddAccessControlListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddAccessControlListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddAccessControlListEntryResponse().from_map(
            await self.do_rpcrequest_async('AddAccessControlListEntry', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_access_control_list_entry(
        self,
        request: slb_20140515_models.AddAccessControlListEntryRequest,
    ) -> slb_20140515_models.AddAccessControlListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_access_control_list_entry_with_options(request, runtime)

    async def add_access_control_list_entry_async(
        self,
        request: slb_20140515_models.AddAccessControlListEntryRequest,
    ) -> slb_20140515_models.AddAccessControlListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_access_control_list_entry_with_options_async(request, runtime)

    def add_backend_servers_with_options(
        self,
        request: slb_20140515_models.AddBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddBackendServersResponse().from_map(
            self.do_rpcrequest('AddBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.AddBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddBackendServersResponse().from_map(
            await self.do_rpcrequest_async('AddBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_backend_servers(
        self,
        request: slb_20140515_models.AddBackendServersRequest,
    ) -> slb_20140515_models.AddBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_backend_servers_with_options(request, runtime)

    async def add_backend_servers_async(
        self,
        request: slb_20140515_models.AddBackendServersRequest,
    ) -> slb_20140515_models.AddBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_backend_servers_with_options_async(request, runtime)

    def add_listener_white_list_item_with_options(
        self,
        request: slb_20140515_models.AddListenerWhiteListItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddListenerWhiteListItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddListenerWhiteListItemResponse().from_map(
            self.do_rpcrequest('AddListenerWhiteListItem', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_listener_white_list_item_with_options_async(
        self,
        request: slb_20140515_models.AddListenerWhiteListItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddListenerWhiteListItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddListenerWhiteListItemResponse().from_map(
            await self.do_rpcrequest_async('AddListenerWhiteListItem', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_listener_white_list_item(
        self,
        request: slb_20140515_models.AddListenerWhiteListItemRequest,
    ) -> slb_20140515_models.AddListenerWhiteListItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_listener_white_list_item_with_options(request, runtime)

    async def add_listener_white_list_item_async(
        self,
        request: slb_20140515_models.AddListenerWhiteListItemRequest,
    ) -> slb_20140515_models.AddListenerWhiteListItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_listener_white_list_item_with_options_async(request, runtime)

    def add_tags_with_options(
        self,
        request: slb_20140515_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddTagsResponse().from_map(
            self.do_rpcrequest('AddTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: slb_20140515_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddTagsResponse().from_map(
            await self.do_rpcrequest_async('AddTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags(
        self,
        request: slb_20140515_models.AddTagsRequest,
    ) -> slb_20140515_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    async def add_tags_async(
        self,
        request: slb_20140515_models.AddTagsRequest,
    ) -> slb_20140515_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_with_options_async(request, runtime)

    def add_vserver_group_backend_servers_with_options(
        self,
        request: slb_20140515_models.AddVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddVServerGroupBackendServersResponse().from_map(
            self.do_rpcrequest('AddVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_vserver_group_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.AddVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.AddVServerGroupBackendServersResponse().from_map(
            await self.do_rpcrequest_async('AddVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vserver_group_backend_servers(
        self,
        request: slb_20140515_models.AddVServerGroupBackendServersRequest,
    ) -> slb_20140515_models.AddVServerGroupBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vserver_group_backend_servers_with_options(request, runtime)

    async def add_vserver_group_backend_servers_async(
        self,
        request: slb_20140515_models.AddVServerGroupBackendServersRequest,
    ) -> slb_20140515_models.AddVServerGroupBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vserver_group_backend_servers_with_options_async(request, runtime)

    def create_access_control_list_with_options(
        self,
        request: slb_20140515_models.CreateAccessControlListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateAccessControlListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateAccessControlListResponse().from_map(
            self.do_rpcrequest('CreateAccessControlList', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_access_control_list_with_options_async(
        self,
        request: slb_20140515_models.CreateAccessControlListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateAccessControlListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateAccessControlListResponse().from_map(
            await self.do_rpcrequest_async('CreateAccessControlList', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_access_control_list(
        self,
        request: slb_20140515_models.CreateAccessControlListRequest,
    ) -> slb_20140515_models.CreateAccessControlListResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_control_list_with_options(request, runtime)

    async def create_access_control_list_async(
        self,
        request: slb_20140515_models.CreateAccessControlListRequest,
    ) -> slb_20140515_models.CreateAccessControlListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_control_list_with_options_async(request, runtime)

    def create_domain_extension_with_options(
        self,
        request: slb_20140515_models.CreateDomainExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateDomainExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateDomainExtensionResponse().from_map(
            self.do_rpcrequest('CreateDomainExtension', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_domain_extension_with_options_async(
        self,
        request: slb_20140515_models.CreateDomainExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateDomainExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateDomainExtensionResponse().from_map(
            await self.do_rpcrequest_async('CreateDomainExtension', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain_extension(
        self,
        request: slb_20140515_models.CreateDomainExtensionRequest,
    ) -> slb_20140515_models.CreateDomainExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_extension_with_options(request, runtime)

    async def create_domain_extension_async(
        self,
        request: slb_20140515_models.CreateDomainExtensionRequest,
    ) -> slb_20140515_models.CreateDomainExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_extension_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: slb_20140515_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerResponse().from_map(
            self.do_rpcrequest('CreateLoadBalancer', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerResponse().from_map(
            await self.do_rpcrequest_async('CreateLoadBalancer', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer(
        self,
        request: slb_20140515_models.CreateLoadBalancerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_load_balancer_httplistener_with_options(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerHTTPListenerResponse().from_map(
            self.do_rpcrequest('CreateLoadBalancerHTTPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_load_balancer_httplistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerHTTPListenerResponse().from_map(
            await self.do_rpcrequest_async('CreateLoadBalancerHTTPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_httplistener(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httplistener_with_options(request, runtime)

    async def create_load_balancer_httplistener_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_httplistener_with_options_async(request, runtime)

    def create_load_balancer_httpslistener_with_options(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPSListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse().from_map(
            self.do_rpcrequest('CreateLoadBalancerHTTPSListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_load_balancer_httpslistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPSListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse().from_map(
            await self.do_rpcrequest_async('CreateLoadBalancerHTTPSListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_httpslistener(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPSListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httpslistener_with_options(request, runtime)

    async def create_load_balancer_httpslistener_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPSListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_httpslistener_with_options_async(request, runtime)

    def create_load_balancer_tcplistener_with_options(
        self,
        request: slb_20140515_models.CreateLoadBalancerTCPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerTCPListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerTCPListenerResponse().from_map(
            self.do_rpcrequest('CreateLoadBalancerTCPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_load_balancer_tcplistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerTCPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerTCPListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerTCPListenerResponse().from_map(
            await self.do_rpcrequest_async('CreateLoadBalancerTCPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_tcplistener(
        self,
        request: slb_20140515_models.CreateLoadBalancerTCPListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerTCPListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_tcplistener_with_options(request, runtime)

    async def create_load_balancer_tcplistener_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerTCPListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerTCPListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_tcplistener_with_options_async(request, runtime)

    def create_load_balancer_udplistener_with_options(
        self,
        request: slb_20140515_models.CreateLoadBalancerUDPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerUDPListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerUDPListenerResponse().from_map(
            self.do_rpcrequest('CreateLoadBalancerUDPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_load_balancer_udplistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerUDPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerUDPListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateLoadBalancerUDPListenerResponse().from_map(
            await self.do_rpcrequest_async('CreateLoadBalancerUDPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_udplistener(
        self,
        request: slb_20140515_models.CreateLoadBalancerUDPListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerUDPListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_udplistener_with_options(request, runtime)

    async def create_load_balancer_udplistener_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerUDPListenerRequest,
    ) -> slb_20140515_models.CreateLoadBalancerUDPListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_udplistener_with_options_async(request, runtime)

    def create_master_slave_server_group_with_options(
        self,
        request: slb_20140515_models.CreateMasterSlaveServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateMasterSlaveServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateMasterSlaveServerGroupResponse().from_map(
            self.do_rpcrequest('CreateMasterSlaveServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_master_slave_server_group_with_options_async(
        self,
        request: slb_20140515_models.CreateMasterSlaveServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateMasterSlaveServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateMasterSlaveServerGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateMasterSlaveServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_master_slave_server_group(
        self,
        request: slb_20140515_models.CreateMasterSlaveServerGroupRequest,
    ) -> slb_20140515_models.CreateMasterSlaveServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_master_slave_server_group_with_options(request, runtime)

    async def create_master_slave_server_group_async(
        self,
        request: slb_20140515_models.CreateMasterSlaveServerGroupRequest,
    ) -> slb_20140515_models.CreateMasterSlaveServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_master_slave_server_group_with_options_async(request, runtime)

    def create_rules_with_options(
        self,
        request: slb_20140515_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateRulesResponse().from_map(
            self.do_rpcrequest('CreateRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        request: slb_20140515_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateRulesResponse().from_map(
            await self.do_rpcrequest_async('CreateRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rules(
        self,
        request: slb_20140515_models.CreateRulesRequest,
    ) -> slb_20140515_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    async def create_rules_async(
        self,
        request: slb_20140515_models.CreateRulesRequest,
    ) -> slb_20140515_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rules_with_options_async(request, runtime)

    def create_tlscipher_policy_with_options(
        self,
        request: slb_20140515_models.CreateTLSCipherPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateTLSCipherPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateTLSCipherPolicyResponse().from_map(
            self.do_rpcrequest('CreateTLSCipherPolicy', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_tlscipher_policy_with_options_async(
        self,
        request: slb_20140515_models.CreateTLSCipherPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateTLSCipherPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateTLSCipherPolicyResponse().from_map(
            await self.do_rpcrequest_async('CreateTLSCipherPolicy', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tlscipher_policy(
        self,
        request: slb_20140515_models.CreateTLSCipherPolicyRequest,
    ) -> slb_20140515_models.CreateTLSCipherPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tlscipher_policy_with_options(request, runtime)

    async def create_tlscipher_policy_async(
        self,
        request: slb_20140515_models.CreateTLSCipherPolicyRequest,
    ) -> slb_20140515_models.CreateTLSCipherPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tlscipher_policy_with_options_async(request, runtime)

    def create_vserver_group_with_options(
        self,
        request: slb_20140515_models.CreateVServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateVServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateVServerGroupResponse().from_map(
            self.do_rpcrequest('CreateVServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vserver_group_with_options_async(
        self,
        request: slb_20140515_models.CreateVServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateVServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.CreateVServerGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateVServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vserver_group(
        self,
        request: slb_20140515_models.CreateVServerGroupRequest,
    ) -> slb_20140515_models.CreateVServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vserver_group_with_options(request, runtime)

    async def create_vserver_group_async(
        self,
        request: slb_20140515_models.CreateVServerGroupRequest,
    ) -> slb_20140515_models.CreateVServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vserver_group_with_options_async(request, runtime)

    def delete_access_control_list_with_options(
        self,
        request: slb_20140515_models.DeleteAccessControlListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteAccessControlListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteAccessControlListResponse().from_map(
            self.do_rpcrequest('DeleteAccessControlList', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_access_control_list_with_options_async(
        self,
        request: slb_20140515_models.DeleteAccessControlListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteAccessControlListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteAccessControlListResponse().from_map(
            await self.do_rpcrequest_async('DeleteAccessControlList', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_access_control_list(
        self,
        request: slb_20140515_models.DeleteAccessControlListRequest,
    ) -> slb_20140515_models.DeleteAccessControlListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_control_list_with_options(request, runtime)

    async def delete_access_control_list_async(
        self,
        request: slb_20140515_models.DeleteAccessControlListRequest,
    ) -> slb_20140515_models.DeleteAccessControlListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_control_list_with_options_async(request, runtime)

    def delete_cacertificate_with_options(
        self,
        request: slb_20140515_models.DeleteCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteCACertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteCACertificateResponse().from_map(
            self.do_rpcrequest('DeleteCACertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cacertificate_with_options_async(
        self,
        request: slb_20140515_models.DeleteCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteCACertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteCACertificateResponse().from_map(
            await self.do_rpcrequest_async('DeleteCACertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cacertificate(
        self,
        request: slb_20140515_models.DeleteCACertificateRequest,
    ) -> slb_20140515_models.DeleteCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cacertificate_with_options(request, runtime)

    async def delete_cacertificate_async(
        self,
        request: slb_20140515_models.DeleteCACertificateRequest,
    ) -> slb_20140515_models.DeleteCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cacertificate_with_options_async(request, runtime)

    def delete_domain_extension_with_options(
        self,
        request: slb_20140515_models.DeleteDomainExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteDomainExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteDomainExtensionResponse().from_map(
            self.do_rpcrequest('DeleteDomainExtension', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_extension_with_options_async(
        self,
        request: slb_20140515_models.DeleteDomainExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteDomainExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteDomainExtensionResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomainExtension', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain_extension(
        self,
        request: slb_20140515_models.DeleteDomainExtensionRequest,
    ) -> slb_20140515_models.DeleteDomainExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_extension_with_options(request, runtime)

    async def delete_domain_extension_async(
        self,
        request: slb_20140515_models.DeleteDomainExtensionRequest,
    ) -> slb_20140515_models.DeleteDomainExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_extension_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: slb_20140515_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteLoadBalancerResponse().from_map(
            self.do_rpcrequest('DeleteLoadBalancer', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: slb_20140515_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteLoadBalancerResponse().from_map(
            await self.do_rpcrequest_async('DeleteLoadBalancer', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_load_balancer(
        self,
        request: slb_20140515_models.DeleteLoadBalancerRequest,
    ) -> slb_20140515_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: slb_20140515_models.DeleteLoadBalancerRequest,
    ) -> slb_20140515_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_load_balancer_listener_with_options(
        self,
        request: slb_20140515_models.DeleteLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteLoadBalancerListenerResponse().from_map(
            self.do_rpcrequest('DeleteLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_load_balancer_listener_with_options_async(
        self,
        request: slb_20140515_models.DeleteLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteLoadBalancerListenerResponse().from_map(
            await self.do_rpcrequest_async('DeleteLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_load_balancer_listener(
        self,
        request: slb_20140515_models.DeleteLoadBalancerListenerRequest,
    ) -> slb_20140515_models.DeleteLoadBalancerListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_listener_with_options(request, runtime)

    async def delete_load_balancer_listener_async(
        self,
        request: slb_20140515_models.DeleteLoadBalancerListenerRequest,
    ) -> slb_20140515_models.DeleteLoadBalancerListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_listener_with_options_async(request, runtime)

    def delete_master_slave_server_group_with_options(
        self,
        request: slb_20140515_models.DeleteMasterSlaveServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteMasterSlaveServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteMasterSlaveServerGroupResponse().from_map(
            self.do_rpcrequest('DeleteMasterSlaveServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_master_slave_server_group_with_options_async(
        self,
        request: slb_20140515_models.DeleteMasterSlaveServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteMasterSlaveServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteMasterSlaveServerGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteMasterSlaveServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_master_slave_server_group(
        self,
        request: slb_20140515_models.DeleteMasterSlaveServerGroupRequest,
    ) -> slb_20140515_models.DeleteMasterSlaveServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_master_slave_server_group_with_options(request, runtime)

    async def delete_master_slave_server_group_async(
        self,
        request: slb_20140515_models.DeleteMasterSlaveServerGroupRequest,
    ) -> slb_20140515_models.DeleteMasterSlaveServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_master_slave_server_group_with_options_async(request, runtime)

    def delete_rules_with_options(
        self,
        request: slb_20140515_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteRulesResponse().from_map(
            self.do_rpcrequest('DeleteRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rules_with_options_async(
        self,
        request: slb_20140515_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteRulesResponse().from_map(
            await self.do_rpcrequest_async('DeleteRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rules(
        self,
        request: slb_20140515_models.DeleteRulesRequest,
    ) -> slb_20140515_models.DeleteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    async def delete_rules_async(
        self,
        request: slb_20140515_models.DeleteRulesRequest,
    ) -> slb_20140515_models.DeleteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rules_with_options_async(request, runtime)

    def delete_server_certificate_with_options(
        self,
        request: slb_20140515_models.DeleteServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteServerCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteServerCertificateResponse().from_map(
            self.do_rpcrequest('DeleteServerCertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_server_certificate_with_options_async(
        self,
        request: slb_20140515_models.DeleteServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteServerCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteServerCertificateResponse().from_map(
            await self.do_rpcrequest_async('DeleteServerCertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_server_certificate(
        self,
        request: slb_20140515_models.DeleteServerCertificateRequest,
    ) -> slb_20140515_models.DeleteServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_server_certificate_with_options(request, runtime)

    async def delete_server_certificate_async(
        self,
        request: slb_20140515_models.DeleteServerCertificateRequest,
    ) -> slb_20140515_models.DeleteServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_server_certificate_with_options_async(request, runtime)

    def delete_tlscipher_policy_with_options(
        self,
        request: slb_20140515_models.DeleteTLSCipherPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteTLSCipherPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteTLSCipherPolicyResponse().from_map(
            self.do_rpcrequest('DeleteTLSCipherPolicy', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_tlscipher_policy_with_options_async(
        self,
        request: slb_20140515_models.DeleteTLSCipherPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteTLSCipherPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteTLSCipherPolicyResponse().from_map(
            await self.do_rpcrequest_async('DeleteTLSCipherPolicy', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tlscipher_policy(
        self,
        request: slb_20140515_models.DeleteTLSCipherPolicyRequest,
    ) -> slb_20140515_models.DeleteTLSCipherPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tlscipher_policy_with_options(request, runtime)

    async def delete_tlscipher_policy_async(
        self,
        request: slb_20140515_models.DeleteTLSCipherPolicyRequest,
    ) -> slb_20140515_models.DeleteTLSCipherPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tlscipher_policy_with_options_async(request, runtime)

    def delete_vserver_group_with_options(
        self,
        request: slb_20140515_models.DeleteVServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteVServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteVServerGroupResponse().from_map(
            self.do_rpcrequest('DeleteVServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vserver_group_with_options_async(
        self,
        request: slb_20140515_models.DeleteVServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteVServerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DeleteVServerGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteVServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vserver_group(
        self,
        request: slb_20140515_models.DeleteVServerGroupRequest,
    ) -> slb_20140515_models.DeleteVServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vserver_group_with_options(request, runtime)

    async def delete_vserver_group_async(
        self,
        request: slb_20140515_models.DeleteVServerGroupRequest,
    ) -> slb_20140515_models.DeleteVServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vserver_group_with_options_async(request, runtime)

    def describe_access_control_list_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeAccessControlListAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAccessControlListAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeAccessControlListAttributeResponse().from_map(
            self.do_rpcrequest('DescribeAccessControlListAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_access_control_list_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeAccessControlListAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAccessControlListAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeAccessControlListAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccessControlListAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_control_list_attribute(
        self,
        request: slb_20140515_models.DescribeAccessControlListAttributeRequest,
    ) -> slb_20140515_models.DescribeAccessControlListAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_list_attribute_with_options(request, runtime)

    async def describe_access_control_list_attribute_async(
        self,
        request: slb_20140515_models.DescribeAccessControlListAttributeRequest,
    ) -> slb_20140515_models.DescribeAccessControlListAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_control_list_attribute_with_options_async(request, runtime)

    def describe_access_control_lists_with_options(
        self,
        request: slb_20140515_models.DescribeAccessControlListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAccessControlListsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeAccessControlListsResponse().from_map(
            self.do_rpcrequest('DescribeAccessControlLists', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_access_control_lists_with_options_async(
        self,
        request: slb_20140515_models.DescribeAccessControlListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAccessControlListsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeAccessControlListsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccessControlLists', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_control_lists(
        self,
        request: slb_20140515_models.DescribeAccessControlListsRequest,
    ) -> slb_20140515_models.DescribeAccessControlListsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_lists_with_options(request, runtime)

    async def describe_access_control_lists_async(
        self,
        request: slb_20140515_models.DescribeAccessControlListsRequest,
    ) -> slb_20140515_models.DescribeAccessControlListsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_control_lists_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: slb_20140515_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeAvailableResourceResponse().from_map(
            self.do_rpcrequest('DescribeAvailableResource', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: slb_20140515_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeAvailableResourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableResource', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(
        self,
        request: slb_20140515_models.DescribeAvailableResourceRequest,
    ) -> slb_20140515_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: slb_20140515_models.DescribeAvailableResourceRequest,
    ) -> slb_20140515_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_cacertificates_with_options(
        self,
        request: slb_20140515_models.DescribeCACertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeCACertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeCACertificatesResponse().from_map(
            self.do_rpcrequest('DescribeCACertificates', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cacertificates_with_options_async(
        self,
        request: slb_20140515_models.DescribeCACertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeCACertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeCACertificatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCACertificates', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cacertificates(
        self,
        request: slb_20140515_models.DescribeCACertificatesRequest,
    ) -> slb_20140515_models.DescribeCACertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificates_with_options(request, runtime)

    async def describe_cacertificates_async(
        self,
        request: slb_20140515_models.DescribeCACertificatesRequest,
    ) -> slb_20140515_models.DescribeCACertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cacertificates_with_options_async(request, runtime)

    def describe_domain_extension_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeDomainExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeDomainExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeDomainExtensionAttributeResponse().from_map(
            self.do_rpcrequest('DescribeDomainExtensionAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_extension_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeDomainExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeDomainExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeDomainExtensionAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainExtensionAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_extension_attribute(
        self,
        request: slb_20140515_models.DescribeDomainExtensionAttributeRequest,
    ) -> slb_20140515_models.DescribeDomainExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_extension_attribute_with_options(request, runtime)

    async def describe_domain_extension_attribute_async(
        self,
        request: slb_20140515_models.DescribeDomainExtensionAttributeRequest,
    ) -> slb_20140515_models.DescribeDomainExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_extension_attribute_with_options_async(request, runtime)

    def describe_domain_extensions_with_options(
        self,
        request: slb_20140515_models.DescribeDomainExtensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeDomainExtensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeDomainExtensionsResponse().from_map(
            self.do_rpcrequest('DescribeDomainExtensions', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_extensions_with_options_async(
        self,
        request: slb_20140515_models.DescribeDomainExtensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeDomainExtensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeDomainExtensionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainExtensions', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_extensions(
        self,
        request: slb_20140515_models.DescribeDomainExtensionsRequest,
    ) -> slb_20140515_models.DescribeDomainExtensionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_extensions_with_options(request, runtime)

    async def describe_domain_extensions_async(
        self,
        request: slb_20140515_models.DescribeDomainExtensionsRequest,
    ) -> slb_20140515_models.DescribeDomainExtensionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_extensions_with_options_async(request, runtime)

    def describe_health_status_with_options(
        self,
        request: slb_20140515_models.DescribeHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeHealthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeHealthStatusResponse().from_map(
            self.do_rpcrequest('DescribeHealthStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_health_status_with_options_async(
        self,
        request: slb_20140515_models.DescribeHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeHealthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeHealthStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeHealthStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_status(
        self,
        request: slb_20140515_models.DescribeHealthStatusRequest,
    ) -> slb_20140515_models.DescribeHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    async def describe_health_status_async(
        self,
        request: slb_20140515_models.DescribeHealthStatusRequest,
    ) -> slb_20140515_models.DescribeHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_status_with_options_async(request, runtime)

    def describe_listener_access_control_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeListenerAccessControlAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeListenerAccessControlAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeListenerAccessControlAttributeResponse().from_map(
            self.do_rpcrequest('DescribeListenerAccessControlAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_listener_access_control_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeListenerAccessControlAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeListenerAccessControlAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeListenerAccessControlAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeListenerAccessControlAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_listener_access_control_attribute(
        self,
        request: slb_20140515_models.DescribeListenerAccessControlAttributeRequest,
    ) -> slb_20140515_models.DescribeListenerAccessControlAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_listener_access_control_attribute_with_options(request, runtime)

    async def describe_listener_access_control_attribute_async(
        self,
        request: slb_20140515_models.DescribeListenerAccessControlAttributeRequest,
    ) -> slb_20140515_models.DescribeListenerAccessControlAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_listener_access_control_attribute_with_options_async(request, runtime)

    def describe_load_balancer_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerAttributeResponse().from_map(
            self.do_rpcrequest('DescribeLoadBalancerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_load_balancer_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeLoadBalancerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_attribute(
        self,
        request: slb_20140515_models.DescribeLoadBalancerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_attribute_with_options(request, runtime)

    async def describe_load_balancer_attribute_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_attribute_with_options_async(request, runtime)

    def describe_load_balancer_httplistener_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse().from_map(
            self.do_rpcrequest('DescribeLoadBalancerHTTPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeLoadBalancerHTTPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_httplistener_attribute(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_httplistener_attribute_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_httplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancer_httpslistener_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse().from_map(
            self.do_rpcrequest('DescribeLoadBalancerHTTPSListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeLoadBalancerHTTPSListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_httpslistener_attribute(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httpslistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_httpslistener_attribute_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_httpslistener_attribute_with_options_async(request, runtime)

    def describe_load_balancers_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancersResponse().from_map(
            self.do_rpcrequest('DescribeLoadBalancers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_load_balancers_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancersResponse().from_map(
            await self.do_rpcrequest_async('DescribeLoadBalancers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancers(
        self,
        request: slb_20140515_models.DescribeLoadBalancersRequest,
    ) -> slb_20140515_models.DescribeLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancers_with_options(request, runtime)

    async def describe_load_balancers_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancersRequest,
    ) -> slb_20140515_models.DescribeLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancers_with_options_async(request, runtime)

    def describe_load_balancer_tcplistener_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse().from_map(
            self.do_rpcrequest('DescribeLoadBalancerTCPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeLoadBalancerTCPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_tcplistener_attribute(
        self,
        request: slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_tcplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_tcplistener_attribute_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_tcplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancer_udplistener_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse().from_map(
            self.do_rpcrequest('DescribeLoadBalancerUDPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeLoadBalancerUDPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_udplistener_attribute(
        self,
        request: slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_udplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_udplistener_attribute_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_udplistener_attribute_with_options_async(request, runtime)

    def describe_master_slave_server_group_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse().from_map(
            self.do_rpcrequest('DescribeMasterSlaveServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_master_slave_server_group_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeMasterSlaveServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_master_slave_server_group_attribute(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupAttributeRequest,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_master_slave_server_group_attribute_with_options(request, runtime)

    async def describe_master_slave_server_group_attribute_async(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupAttributeRequest,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_master_slave_server_group_attribute_with_options_async(request, runtime)

    def describe_master_slave_server_groups_with_options(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeMasterSlaveServerGroupsResponse().from_map(
            self.do_rpcrequest('DescribeMasterSlaveServerGroups', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_master_slave_server_groups_with_options_async(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeMasterSlaveServerGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeMasterSlaveServerGroups', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_master_slave_server_groups(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupsRequest,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_master_slave_server_groups_with_options(request, runtime)

    async def describe_master_slave_server_groups_async(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupsRequest,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_master_slave_server_groups_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: slb_20140515_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: slb_20140515_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: slb_20140515_models.DescribeRegionsRequest,
    ) -> slb_20140515_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: slb_20140515_models.DescribeRegionsRequest,
    ) -> slb_20140515_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_rule_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeRuleAttributeResponse().from_map(
            self.do_rpcrequest('DescribeRuleAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rule_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeRuleAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeRuleAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rule_attribute(
        self,
        request: slb_20140515_models.DescribeRuleAttributeRequest,
    ) -> slb_20140515_models.DescribeRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_attribute_with_options(request, runtime)

    async def describe_rule_attribute_async(
        self,
        request: slb_20140515_models.DescribeRuleAttributeRequest,
    ) -> slb_20140515_models.DescribeRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_attribute_with_options_async(request, runtime)

    def describe_rules_with_options(
        self,
        request: slb_20140515_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeRulesResponse().from_map(
            self.do_rpcrequest('DescribeRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: slb_20140515_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rules(
        self,
        request: slb_20140515_models.DescribeRulesRequest,
    ) -> slb_20140515_models.DescribeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    async def describe_rules_async(
        self,
        request: slb_20140515_models.DescribeRulesRequest,
    ) -> slb_20140515_models.DescribeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rules_with_options_async(request, runtime)

    def describe_server_certificates_with_options(
        self,
        request: slb_20140515_models.DescribeServerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeServerCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeServerCertificatesResponse().from_map(
            self.do_rpcrequest('DescribeServerCertificates', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_server_certificates_with_options_async(
        self,
        request: slb_20140515_models.DescribeServerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeServerCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeServerCertificatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeServerCertificates', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_server_certificates(
        self,
        request: slb_20140515_models.DescribeServerCertificatesRequest,
    ) -> slb_20140515_models.DescribeServerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_server_certificates_with_options(request, runtime)

    async def describe_server_certificates_async(
        self,
        request: slb_20140515_models.DescribeServerCertificatesRequest,
    ) -> slb_20140515_models.DescribeServerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_server_certificates_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: slb_20140515_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeTagsResponse().from_map(
            self.do_rpcrequest('DescribeTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: slb_20140515_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(
        self,
        request: slb_20140515_models.DescribeTagsRequest,
    ) -> slb_20140515_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: slb_20140515_models.DescribeTagsRequest,
    ) -> slb_20140515_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_vserver_group_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeVServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeVServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeVServerGroupAttributeResponse().from_map(
            self.do_rpcrequest('DescribeVServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vserver_group_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeVServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeVServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeVServerGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeVServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vserver_group_attribute(
        self,
        request: slb_20140515_models.DescribeVServerGroupAttributeRequest,
    ) -> slb_20140515_models.DescribeVServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vserver_group_attribute_with_options(request, runtime)

    async def describe_vserver_group_attribute_async(
        self,
        request: slb_20140515_models.DescribeVServerGroupAttributeRequest,
    ) -> slb_20140515_models.DescribeVServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vserver_group_attribute_with_options_async(request, runtime)

    def describe_vserver_groups_with_options(
        self,
        request: slb_20140515_models.DescribeVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeVServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeVServerGroupsResponse().from_map(
            self.do_rpcrequest('DescribeVServerGroups', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vserver_groups_with_options_async(
        self,
        request: slb_20140515_models.DescribeVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeVServerGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeVServerGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVServerGroups', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vserver_groups(
        self,
        request: slb_20140515_models.DescribeVServerGroupsRequest,
    ) -> slb_20140515_models.DescribeVServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vserver_groups_with_options(request, runtime)

    async def describe_vserver_groups_async(
        self,
        request: slb_20140515_models.DescribeVServerGroupsRequest,
    ) -> slb_20140515_models.DescribeVServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vserver_groups_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: slb_20140515_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: slb_20140515_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.DescribeZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeZones', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: slb_20140515_models.DescribeZonesRequest,
    ) -> slb_20140515_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: slb_20140515_models.DescribeZonesRequest,
    ) -> slb_20140515_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: slb_20140515_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: slb_20140515_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: slb_20140515_models.ListTagResourcesRequest,
    ) -> slb_20140515_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: slb_20140515_models.ListTagResourcesRequest,
    ) -> slb_20140515_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tlscipher_policies_with_options(
        self,
        request: slb_20140515_models.ListTLSCipherPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTLSCipherPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ListTLSCipherPoliciesResponse().from_map(
            self.do_rpcrequest('ListTLSCipherPolicies', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tlscipher_policies_with_options_async(
        self,
        request: slb_20140515_models.ListTLSCipherPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTLSCipherPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ListTLSCipherPoliciesResponse().from_map(
            await self.do_rpcrequest_async('ListTLSCipherPolicies', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tlscipher_policies(
        self,
        request: slb_20140515_models.ListTLSCipherPoliciesRequest,
    ) -> slb_20140515_models.ListTLSCipherPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tlscipher_policies_with_options(request, runtime)

    async def list_tlscipher_policies_async(
        self,
        request: slb_20140515_models.ListTLSCipherPoliciesRequest,
    ) -> slb_20140515_models.ListTLSCipherPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tlscipher_policies_with_options_async(request, runtime)

    def modify_load_balancer_instance_spec_with_options(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyLoadBalancerInstanceSpec', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_load_balancer_instance_spec_with_options_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyLoadBalancerInstanceSpec', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_load_balancer_instance_spec(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInstanceSpecRequest,
    ) -> slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_instance_spec_with_options(request, runtime)

    async def modify_load_balancer_instance_spec_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInstanceSpecRequest,
    ) -> slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_load_balancer_instance_spec_with_options_async(request, runtime)

    def modify_load_balancer_internet_spec_with_options(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInternetSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerInternetSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyLoadBalancerInternetSpecResponse().from_map(
            self.do_rpcrequest('ModifyLoadBalancerInternetSpec', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_load_balancer_internet_spec_with_options_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInternetSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerInternetSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyLoadBalancerInternetSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyLoadBalancerInternetSpec', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_load_balancer_internet_spec(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInternetSpecRequest,
    ) -> slb_20140515_models.ModifyLoadBalancerInternetSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_internet_spec_with_options(request, runtime)

    async def modify_load_balancer_internet_spec_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInternetSpecRequest,
    ) -> slb_20140515_models.ModifyLoadBalancerInternetSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_load_balancer_internet_spec_with_options_async(request, runtime)

    def modify_load_balancer_pay_type_with_options(
        self,
        request: slb_20140515_models.ModifyLoadBalancerPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerPayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyLoadBalancerPayTypeResponse().from_map(
            self.do_rpcrequest('ModifyLoadBalancerPayType', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_load_balancer_pay_type_with_options_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerPayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyLoadBalancerPayTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyLoadBalancerPayType', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_load_balancer_pay_type(
        self,
        request: slb_20140515_models.ModifyLoadBalancerPayTypeRequest,
    ) -> slb_20140515_models.ModifyLoadBalancerPayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_pay_type_with_options(request, runtime)

    async def modify_load_balancer_pay_type_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerPayTypeRequest,
    ) -> slb_20140515_models.ModifyLoadBalancerPayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_load_balancer_pay_type_with_options_async(request, runtime)

    def modify_vserver_group_backend_servers_with_options(
        self,
        request: slb_20140515_models.ModifyVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyVServerGroupBackendServersResponse().from_map(
            self.do_rpcrequest('ModifyVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vserver_group_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.ModifyVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.ModifyVServerGroupBackendServersResponse().from_map(
            await self.do_rpcrequest_async('ModifyVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vserver_group_backend_servers(
        self,
        request: slb_20140515_models.ModifyVServerGroupBackendServersRequest,
    ) -> slb_20140515_models.ModifyVServerGroupBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vserver_group_backend_servers_with_options(request, runtime)

    async def modify_vserver_group_backend_servers_async(
        self,
        request: slb_20140515_models.ModifyVServerGroupBackendServersRequest,
    ) -> slb_20140515_models.ModifyVServerGroupBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vserver_group_backend_servers_with_options_async(request, runtime)

    def remove_access_control_list_entry_with_options(
        self,
        request: slb_20140515_models.RemoveAccessControlListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveAccessControlListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveAccessControlListEntryResponse().from_map(
            self.do_rpcrequest('RemoveAccessControlListEntry', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_access_control_list_entry_with_options_async(
        self,
        request: slb_20140515_models.RemoveAccessControlListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveAccessControlListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveAccessControlListEntryResponse().from_map(
            await self.do_rpcrequest_async('RemoveAccessControlListEntry', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_access_control_list_entry(
        self,
        request: slb_20140515_models.RemoveAccessControlListEntryRequest,
    ) -> slb_20140515_models.RemoveAccessControlListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_access_control_list_entry_with_options(request, runtime)

    async def remove_access_control_list_entry_async(
        self,
        request: slb_20140515_models.RemoveAccessControlListEntryRequest,
    ) -> slb_20140515_models.RemoveAccessControlListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_access_control_list_entry_with_options_async(request, runtime)

    def remove_backend_servers_with_options(
        self,
        request: slb_20140515_models.RemoveBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveBackendServersResponse().from_map(
            self.do_rpcrequest('RemoveBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.RemoveBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveBackendServersResponse().from_map(
            await self.do_rpcrequest_async('RemoveBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_backend_servers(
        self,
        request: slb_20140515_models.RemoveBackendServersRequest,
    ) -> slb_20140515_models.RemoveBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_backend_servers_with_options(request, runtime)

    async def remove_backend_servers_async(
        self,
        request: slb_20140515_models.RemoveBackendServersRequest,
    ) -> slb_20140515_models.RemoveBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_backend_servers_with_options_async(request, runtime)

    def remove_listener_white_list_item_with_options(
        self,
        request: slb_20140515_models.RemoveListenerWhiteListItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveListenerWhiteListItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveListenerWhiteListItemResponse().from_map(
            self.do_rpcrequest('RemoveListenerWhiteListItem', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_listener_white_list_item_with_options_async(
        self,
        request: slb_20140515_models.RemoveListenerWhiteListItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveListenerWhiteListItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveListenerWhiteListItemResponse().from_map(
            await self.do_rpcrequest_async('RemoveListenerWhiteListItem', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_listener_white_list_item(
        self,
        request: slb_20140515_models.RemoveListenerWhiteListItemRequest,
    ) -> slb_20140515_models.RemoveListenerWhiteListItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_listener_white_list_item_with_options(request, runtime)

    async def remove_listener_white_list_item_async(
        self,
        request: slb_20140515_models.RemoveListenerWhiteListItemRequest,
    ) -> slb_20140515_models.RemoveListenerWhiteListItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_listener_white_list_item_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: slb_20140515_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveTagsResponse().from_map(
            self.do_rpcrequest('RemoveTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: slb_20140515_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveTagsResponse().from_map(
            await self.do_rpcrequest_async('RemoveTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags(
        self,
        request: slb_20140515_models.RemoveTagsRequest,
    ) -> slb_20140515_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    async def remove_tags_async(
        self,
        request: slb_20140515_models.RemoveTagsRequest,
    ) -> slb_20140515_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_with_options_async(request, runtime)

    def remove_vserver_group_backend_servers_with_options(
        self,
        request: slb_20140515_models.RemoveVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveVServerGroupBackendServersResponse().from_map(
            self.do_rpcrequest('RemoveVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_vserver_group_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.RemoveVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.RemoveVServerGroupBackendServersResponse().from_map(
            await self.do_rpcrequest_async('RemoveVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_vserver_group_backend_servers(
        self,
        request: slb_20140515_models.RemoveVServerGroupBackendServersRequest,
    ) -> slb_20140515_models.RemoveVServerGroupBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_vserver_group_backend_servers_with_options(request, runtime)

    async def remove_vserver_group_backend_servers_async(
        self,
        request: slb_20140515_models.RemoveVServerGroupBackendServersRequest,
    ) -> slb_20140515_models.RemoveVServerGroupBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_vserver_group_backend_servers_with_options_async(request, runtime)

    def set_access_control_list_attribute_with_options(
        self,
        request: slb_20140515_models.SetAccessControlListAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetAccessControlListAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetAccessControlListAttributeResponse().from_map(
            self.do_rpcrequest('SetAccessControlListAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_access_control_list_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetAccessControlListAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetAccessControlListAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetAccessControlListAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetAccessControlListAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_access_control_list_attribute(
        self,
        request: slb_20140515_models.SetAccessControlListAttributeRequest,
    ) -> slb_20140515_models.SetAccessControlListAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_access_control_list_attribute_with_options(request, runtime)

    async def set_access_control_list_attribute_async(
        self,
        request: slb_20140515_models.SetAccessControlListAttributeRequest,
    ) -> slb_20140515_models.SetAccessControlListAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_access_control_list_attribute_with_options_async(request, runtime)

    def set_backend_servers_with_options(
        self,
        request: slb_20140515_models.SetBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetBackendServersResponse().from_map(
            self.do_rpcrequest('SetBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.SetBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetBackendServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetBackendServersResponse().from_map(
            await self.do_rpcrequest_async('SetBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_backend_servers(
        self,
        request: slb_20140515_models.SetBackendServersRequest,
    ) -> slb_20140515_models.SetBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_backend_servers_with_options(request, runtime)

    async def set_backend_servers_async(
        self,
        request: slb_20140515_models.SetBackendServersRequest,
    ) -> slb_20140515_models.SetBackendServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_backend_servers_with_options_async(request, runtime)

    def set_cacertificate_name_with_options(
        self,
        request: slb_20140515_models.SetCACertificateNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetCACertificateNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetCACertificateNameResponse().from_map(
            self.do_rpcrequest('SetCACertificateName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_cacertificate_name_with_options_async(
        self,
        request: slb_20140515_models.SetCACertificateNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetCACertificateNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetCACertificateNameResponse().from_map(
            await self.do_rpcrequest_async('SetCACertificateName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_cacertificate_name(
        self,
        request: slb_20140515_models.SetCACertificateNameRequest,
    ) -> slb_20140515_models.SetCACertificateNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cacertificate_name_with_options(request, runtime)

    async def set_cacertificate_name_async(
        self,
        request: slb_20140515_models.SetCACertificateNameRequest,
    ) -> slb_20140515_models.SetCACertificateNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cacertificate_name_with_options_async(request, runtime)

    def set_domain_extension_attribute_with_options(
        self,
        request: slb_20140515_models.SetDomainExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetDomainExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetDomainExtensionAttributeResponse().from_map(
            self.do_rpcrequest('SetDomainExtensionAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_domain_extension_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetDomainExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetDomainExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetDomainExtensionAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetDomainExtensionAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_domain_extension_attribute(
        self,
        request: slb_20140515_models.SetDomainExtensionAttributeRequest,
    ) -> slb_20140515_models.SetDomainExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_extension_attribute_with_options(request, runtime)

    async def set_domain_extension_attribute_async(
        self,
        request: slb_20140515_models.SetDomainExtensionAttributeRequest,
    ) -> slb_20140515_models.SetDomainExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_extension_attribute_with_options_async(request, runtime)

    def set_listener_access_control_status_with_options(
        self,
        request: slb_20140515_models.SetListenerAccessControlStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetListenerAccessControlStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetListenerAccessControlStatusResponse().from_map(
            self.do_rpcrequest('SetListenerAccessControlStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_listener_access_control_status_with_options_async(
        self,
        request: slb_20140515_models.SetListenerAccessControlStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetListenerAccessControlStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetListenerAccessControlStatusResponse().from_map(
            await self.do_rpcrequest_async('SetListenerAccessControlStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_listener_access_control_status(
        self,
        request: slb_20140515_models.SetListenerAccessControlStatusRequest,
    ) -> slb_20140515_models.SetListenerAccessControlStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_listener_access_control_status_with_options(request, runtime)

    async def set_listener_access_control_status_async(
        self,
        request: slb_20140515_models.SetListenerAccessControlStatusRequest,
    ) -> slb_20140515_models.SetListenerAccessControlStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_listener_access_control_status_with_options_async(request, runtime)

    def set_load_balancer_delete_protection_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerDeleteProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerDeleteProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerDeleteProtectionResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerDeleteProtection', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_delete_protection_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerDeleteProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerDeleteProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerDeleteProtectionResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerDeleteProtection', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_delete_protection(
        self,
        request: slb_20140515_models.SetLoadBalancerDeleteProtectionRequest,
    ) -> slb_20140515_models.SetLoadBalancerDeleteProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_delete_protection_with_options(request, runtime)

    async def set_load_balancer_delete_protection_async(
        self,
        request: slb_20140515_models.SetLoadBalancerDeleteProtectionRequest,
    ) -> slb_20140515_models.SetLoadBalancerDeleteProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_delete_protection_with_options_async(request, runtime)

    def set_load_balancer_httplistener_attribute_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerHTTPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerHTTPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_httplistener_attribute(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_httplistener_attribute_async(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_httplistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_httpslistener_attribute_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerHTTPSListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerHTTPSListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_httpslistener_attribute(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httpslistener_attribute_with_options(request, runtime)

    async def set_load_balancer_httpslistener_attribute_async(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_httpslistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_modification_protection_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerModificationProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerModificationProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerModificationProtectionResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerModificationProtection', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_modification_protection_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerModificationProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerModificationProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerModificationProtectionResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerModificationProtection', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_modification_protection(
        self,
        request: slb_20140515_models.SetLoadBalancerModificationProtectionRequest,
    ) -> slb_20140515_models.SetLoadBalancerModificationProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_modification_protection_with_options(request, runtime)

    async def set_load_balancer_modification_protection_async(
        self,
        request: slb_20140515_models.SetLoadBalancerModificationProtectionRequest,
    ) -> slb_20140515_models.SetLoadBalancerModificationProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_modification_protection_with_options_async(request, runtime)

    def set_load_balancer_name_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerNameResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_name_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerNameResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_name(
        self,
        request: slb_20140515_models.SetLoadBalancerNameRequest,
    ) -> slb_20140515_models.SetLoadBalancerNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_name_with_options(request, runtime)

    async def set_load_balancer_name_async(
        self,
        request: slb_20140515_models.SetLoadBalancerNameRequest,
    ) -> slb_20140515_models.SetLoadBalancerNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_name_with_options_async(request, runtime)

    def set_load_balancer_status_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerStatusResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_status_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerStatusResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_status(
        self,
        request: slb_20140515_models.SetLoadBalancerStatusRequest,
    ) -> slb_20140515_models.SetLoadBalancerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_status_with_options(request, runtime)

    async def set_load_balancer_status_async(
        self,
        request: slb_20140515_models.SetLoadBalancerStatusRequest,
    ) -> slb_20140515_models.SetLoadBalancerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_status_with_options_async(request, runtime)

    def set_load_balancer_tcplistener_attribute_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerTCPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerTCPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_tcplistener_attribute(
        self,
        request: slb_20140515_models.SetLoadBalancerTCPListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_tcplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_tcplistener_attribute_async(
        self,
        request: slb_20140515_models.SetLoadBalancerTCPListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_tcplistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_udplistener_attribute_with_options(
        self,
        request: slb_20140515_models.SetLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse().from_map(
            self.do_rpcrequest('SetLoadBalancerUDPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetLoadBalancerUDPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_udplistener_attribute(
        self,
        request: slb_20140515_models.SetLoadBalancerUDPListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_udplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_udplistener_attribute_async(
        self,
        request: slb_20140515_models.SetLoadBalancerUDPListenerAttributeRequest,
    ) -> slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_udplistener_attribute_with_options_async(request, runtime)

    def set_rule_with_options(
        self,
        request: slb_20140515_models.SetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetRuleResponse().from_map(
            self.do_rpcrequest('SetRule', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_rule_with_options_async(
        self,
        request: slb_20140515_models.SetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetRuleResponse().from_map(
            await self.do_rpcrequest_async('SetRule', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_rule(
        self,
        request: slb_20140515_models.SetRuleRequest,
    ) -> slb_20140515_models.SetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_rule_with_options(request, runtime)

    async def set_rule_async(
        self,
        request: slb_20140515_models.SetRuleRequest,
    ) -> slb_20140515_models.SetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_rule_with_options_async(request, runtime)

    def set_server_certificate_name_with_options(
        self,
        request: slb_20140515_models.SetServerCertificateNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetServerCertificateNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetServerCertificateNameResponse().from_map(
            self.do_rpcrequest('SetServerCertificateName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_server_certificate_name_with_options_async(
        self,
        request: slb_20140515_models.SetServerCertificateNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetServerCertificateNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetServerCertificateNameResponse().from_map(
            await self.do_rpcrequest_async('SetServerCertificateName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_server_certificate_name(
        self,
        request: slb_20140515_models.SetServerCertificateNameRequest,
    ) -> slb_20140515_models.SetServerCertificateNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_server_certificate_name_with_options(request, runtime)

    async def set_server_certificate_name_async(
        self,
        request: slb_20140515_models.SetServerCertificateNameRequest,
    ) -> slb_20140515_models.SetServerCertificateNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_server_certificate_name_with_options_async(request, runtime)

    def set_tlscipher_policy_attribute_with_options(
        self,
        request: slb_20140515_models.SetTLSCipherPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetTLSCipherPolicyAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetTLSCipherPolicyAttributeResponse().from_map(
            self.do_rpcrequest('SetTLSCipherPolicyAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_tlscipher_policy_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetTLSCipherPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetTLSCipherPolicyAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetTLSCipherPolicyAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetTLSCipherPolicyAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_tlscipher_policy_attribute(
        self,
        request: slb_20140515_models.SetTLSCipherPolicyAttributeRequest,
    ) -> slb_20140515_models.SetTLSCipherPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_tlscipher_policy_attribute_with_options(request, runtime)

    async def set_tlscipher_policy_attribute_async(
        self,
        request: slb_20140515_models.SetTLSCipherPolicyAttributeRequest,
    ) -> slb_20140515_models.SetTLSCipherPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_tlscipher_policy_attribute_with_options_async(request, runtime)

    def set_vserver_group_attribute_with_options(
        self,
        request: slb_20140515_models.SetVServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetVServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetVServerGroupAttributeResponse().from_map(
            self.do_rpcrequest('SetVServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_vserver_group_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetVServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetVServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.SetVServerGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('SetVServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_vserver_group_attribute(
        self,
        request: slb_20140515_models.SetVServerGroupAttributeRequest,
    ) -> slb_20140515_models.SetVServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_vserver_group_attribute_with_options(request, runtime)

    async def set_vserver_group_attribute_async(
        self,
        request: slb_20140515_models.SetVServerGroupAttributeRequest,
    ) -> slb_20140515_models.SetVServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_vserver_group_attribute_with_options_async(request, runtime)

    def start_load_balancer_listener_with_options(
        self,
        request: slb_20140515_models.StartLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.StartLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.StartLoadBalancerListenerResponse().from_map(
            self.do_rpcrequest('StartLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_load_balancer_listener_with_options_async(
        self,
        request: slb_20140515_models.StartLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.StartLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.StartLoadBalancerListenerResponse().from_map(
            await self.do_rpcrequest_async('StartLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_load_balancer_listener(
        self,
        request: slb_20140515_models.StartLoadBalancerListenerRequest,
    ) -> slb_20140515_models.StartLoadBalancerListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_load_balancer_listener_with_options(request, runtime)

    async def start_load_balancer_listener_async(
        self,
        request: slb_20140515_models.StartLoadBalancerListenerRequest,
    ) -> slb_20140515_models.StartLoadBalancerListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_load_balancer_listener_with_options_async(request, runtime)

    def stop_load_balancer_listener_with_options(
        self,
        request: slb_20140515_models.StopLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.StopLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.StopLoadBalancerListenerResponse().from_map(
            self.do_rpcrequest('StopLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_load_balancer_listener_with_options_async(
        self,
        request: slb_20140515_models.StopLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.StopLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.StopLoadBalancerListenerResponse().from_map(
            await self.do_rpcrequest_async('StopLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_load_balancer_listener(
        self,
        request: slb_20140515_models.StopLoadBalancerListenerRequest,
    ) -> slb_20140515_models.StopLoadBalancerListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_load_balancer_listener_with_options(request, runtime)

    async def stop_load_balancer_listener_async(
        self,
        request: slb_20140515_models.StopLoadBalancerListenerRequest,
    ) -> slb_20140515_models.StopLoadBalancerListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_load_balancer_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: slb_20140515_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: slb_20140515_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: slb_20140515_models.TagResourcesRequest,
    ) -> slb_20140515_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: slb_20140515_models.TagResourcesRequest,
    ) -> slb_20140515_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: slb_20140515_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: slb_20140515_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: slb_20140515_models.UntagResourcesRequest,
    ) -> slb_20140515_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: slb_20140515_models.UntagResourcesRequest,
    ) -> slb_20140515_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upload_cacertificate_with_options(
        self,
        request: slb_20140515_models.UploadCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UploadCACertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.UploadCACertificateResponse().from_map(
            self.do_rpcrequest('UploadCACertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_cacertificate_with_options_async(
        self,
        request: slb_20140515_models.UploadCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UploadCACertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.UploadCACertificateResponse().from_map(
            await self.do_rpcrequest_async('UploadCACertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_cacertificate(
        self,
        request: slb_20140515_models.UploadCACertificateRequest,
    ) -> slb_20140515_models.UploadCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_cacertificate_with_options(request, runtime)

    async def upload_cacertificate_async(
        self,
        request: slb_20140515_models.UploadCACertificateRequest,
    ) -> slb_20140515_models.UploadCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_cacertificate_with_options_async(request, runtime)

    def upload_server_certificate_with_options(
        self,
        request: slb_20140515_models.UploadServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UploadServerCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.UploadServerCertificateResponse().from_map(
            self.do_rpcrequest('UploadServerCertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_server_certificate_with_options_async(
        self,
        request: slb_20140515_models.UploadServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UploadServerCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return slb_20140515_models.UploadServerCertificateResponse().from_map(
            await self.do_rpcrequest_async('UploadServerCertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_server_certificate(
        self,
        request: slb_20140515_models.UploadServerCertificateRequest,
    ) -> slb_20140515_models.UploadServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_server_certificate_with_options(request, runtime)

    async def upload_server_certificate_async(
        self,
        request: slb_20140515_models.UploadServerCertificateRequest,
    ) -> slb_20140515_models.UploadServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_server_certificate_with_options_async(request, runtime)
