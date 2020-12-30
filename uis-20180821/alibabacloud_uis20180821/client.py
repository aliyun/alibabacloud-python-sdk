# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_uis20180821 import models as uis_20180821_models
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
            'cn-north-2-gov-1': 'uis.cn-hangzhou.aliyuncs.com',
            'ap-northeast-1': 'uis.aliyuncs.com',
            'ap-northeast-2-pop': 'uis.aliyuncs.com',
            'ap-south-1': 'uis.aliyuncs.com',
            'ap-southeast-1': 'uis.aliyuncs.com',
            'ap-southeast-2': 'uis.aliyuncs.com',
            'ap-southeast-3': 'uis.aliyuncs.com',
            'ap-southeast-5': 'uis.aliyuncs.com',
            'cn-beijing': 'uis.aliyuncs.com',
            'cn-beijing-finance-1': 'uis.aliyuncs.com',
            'cn-beijing-finance-pop': 'uis.aliyuncs.com',
            'cn-beijing-gov-1': 'uis.aliyuncs.com',
            'cn-beijing-nu16-b01': 'uis.aliyuncs.com',
            'cn-chengdu': 'uis.aliyuncs.com',
            'cn-edge-1': 'uis.aliyuncs.com',
            'cn-fujian': 'uis.aliyuncs.com',
            'cn-haidian-cm12-c01': 'uis.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'uis.aliyuncs.com',
            'cn-hangzhou-finance': 'uis.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'uis.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'uis.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'uis.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'uis.aliyuncs.com',
            'cn-hangzhou-test-306': 'uis.aliyuncs.com',
            'cn-hongkong': 'uis.aliyuncs.com',
            'cn-hongkong-finance-pop': 'uis.aliyuncs.com',
            'cn-huhehaote': 'uis.aliyuncs.com',
            'cn-qingdao': 'uis.aliyuncs.com',
            'cn-qingdao-nebula': 'uis.aliyuncs.com',
            'cn-shanghai': 'uis.aliyuncs.com',
            'cn-shanghai-et15-b01': 'uis.aliyuncs.com',
            'cn-shanghai-et2-b01': 'uis.aliyuncs.com',
            'cn-shanghai-finance-1': 'uis.aliyuncs.com',
            'cn-shanghai-inner': 'uis.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'uis.aliyuncs.com',
            'cn-shenzhen': 'uis.aliyuncs.com',
            'cn-shenzhen-finance-1': 'uis.aliyuncs.com',
            'cn-shenzhen-inner': 'uis.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'uis.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'uis.aliyuncs.com',
            'cn-wuhan': 'uis.aliyuncs.com',
            'cn-yushanfang': 'uis.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'uis.aliyuncs.com',
            'cn-zhangjiakou': 'uis.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'uis.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'uis.aliyuncs.com',
            'eu-central-1': 'uis.aliyuncs.com',
            'eu-west-1': 'uis.aliyuncs.com',
            'eu-west-1-oxs': 'uis.aliyuncs.com',
            'me-east-1': 'uis.aliyuncs.com',
            'rus-west-1-pop': 'uis.aliyuncs.com',
            'us-east-1': 'uis.aliyuncs.com',
            'us-west-1': 'uis.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('uis', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_high_priority_ip_with_options(
        self,
        request: uis_20180821_models.AddHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.AddHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.AddHighPriorityIpResponse().from_map(
            self.do_rpcrequest('AddHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_high_priority_ip_with_options_async(
        self,
        request: uis_20180821_models.AddHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.AddHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.AddHighPriorityIpResponse().from_map(
            await self.do_rpcrequest_async('AddHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_high_priority_ip(
        self,
        request: uis_20180821_models.AddHighPriorityIpRequest,
    ) -> uis_20180821_models.AddHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_high_priority_ip_with_options(request, runtime)

    async def add_high_priority_ip_async(
        self,
        request: uis_20180821_models.AddHighPriorityIpRequest,
    ) -> uis_20180821_models.AddHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_high_priority_ip_with_options_async(request, runtime)

    def add_uis_node_ip_with_options(
        self,
        request: uis_20180821_models.AddUisNodeIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.AddUisNodeIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.AddUisNodeIpResponse().from_map(
            self.do_rpcrequest('AddUisNodeIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_uis_node_ip_with_options_async(
        self,
        request: uis_20180821_models.AddUisNodeIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.AddUisNodeIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.AddUisNodeIpResponse().from_map(
            await self.do_rpcrequest_async('AddUisNodeIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_uis_node_ip(
        self,
        request: uis_20180821_models.AddUisNodeIpRequest,
    ) -> uis_20180821_models.AddUisNodeIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_uis_node_ip_with_options(request, runtime)

    async def add_uis_node_ip_async(
        self,
        request: uis_20180821_models.AddUisNodeIpRequest,
    ) -> uis_20180821_models.AddUisNodeIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_uis_node_ip_with_options_async(request, runtime)

    def create_dnat_entry_with_options(
        self,
        request: uis_20180821_models.CreateDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateDnatEntryResponse().from_map(
            self.do_rpcrequest('CreateDnatEntry', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dnat_entry_with_options_async(
        self,
        request: uis_20180821_models.CreateDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateDnatEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateDnatEntry', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dnat_entry(
        self,
        request: uis_20180821_models.CreateDnatEntryRequest,
    ) -> uis_20180821_models.CreateDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dnat_entry_with_options(request, runtime)

    async def create_dnat_entry_async(
        self,
        request: uis_20180821_models.CreateDnatEntryRequest,
    ) -> uis_20180821_models.CreateDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dnat_entry_with_options_async(request, runtime)

    def create_sub_connection_with_options(
        self,
        request: uis_20180821_models.CreateSubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateSubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateSubConnectionResponse().from_map(
            self.do_rpcrequest('CreateSubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sub_connection_with_options_async(
        self,
        request: uis_20180821_models.CreateSubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateSubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateSubConnectionResponse().from_map(
            await self.do_rpcrequest_async('CreateSubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sub_connection(
        self,
        request: uis_20180821_models.CreateSubConnectionRequest,
    ) -> uis_20180821_models.CreateSubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sub_connection_with_options(request, runtime)

    async def create_sub_connection_async(
        self,
        request: uis_20180821_models.CreateSubConnectionRequest,
    ) -> uis_20180821_models.CreateSubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sub_connection_with_options_async(request, runtime)

    def create_uis_with_options(
        self,
        request: uis_20180821_models.CreateUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisResponse().from_map(
            self.do_rpcrequest('CreateUis', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_uis_with_options_async(
        self,
        request: uis_20180821_models.CreateUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisResponse().from_map(
            await self.do_rpcrequest_async('CreateUis', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_uis(
        self,
        request: uis_20180821_models.CreateUisRequest,
    ) -> uis_20180821_models.CreateUisResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_uis_with_options(request, runtime)

    async def create_uis_async(
        self,
        request: uis_20180821_models.CreateUisRequest,
    ) -> uis_20180821_models.CreateUisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_uis_with_options_async(request, runtime)

    def create_uis_connection_with_options(
        self,
        request: uis_20180821_models.CreateUisConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisConnectionResponse().from_map(
            self.do_rpcrequest('CreateUisConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_uis_connection_with_options_async(
        self,
        request: uis_20180821_models.CreateUisConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisConnectionResponse().from_map(
            await self.do_rpcrequest_async('CreateUisConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_uis_connection(
        self,
        request: uis_20180821_models.CreateUisConnectionRequest,
    ) -> uis_20180821_models.CreateUisConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_uis_connection_with_options(request, runtime)

    async def create_uis_connection_async(
        self,
        request: uis_20180821_models.CreateUisConnectionRequest,
    ) -> uis_20180821_models.CreateUisConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_uis_connection_with_options_async(request, runtime)

    def create_uis_network_interface_with_options(
        self,
        request: uis_20180821_models.CreateUisNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisNetworkInterfaceResponse().from_map(
            self.do_rpcrequest('CreateUisNetworkInterface', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_uis_network_interface_with_options_async(
        self,
        request: uis_20180821_models.CreateUisNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisNetworkInterfaceResponse().from_map(
            await self.do_rpcrequest_async('CreateUisNetworkInterface', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_uis_network_interface(
        self,
        request: uis_20180821_models.CreateUisNetworkInterfaceRequest,
    ) -> uis_20180821_models.CreateUisNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_uis_network_interface_with_options(request, runtime)

    async def create_uis_network_interface_async(
        self,
        request: uis_20180821_models.CreateUisNetworkInterfaceRequest,
    ) -> uis_20180821_models.CreateUisNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_uis_network_interface_with_options_async(request, runtime)

    def create_uis_node_with_options(
        self,
        request: uis_20180821_models.CreateUisNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisNodeResponse().from_map(
            self.do_rpcrequest('CreateUisNode', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_uis_node_with_options_async(
        self,
        request: uis_20180821_models.CreateUisNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.CreateUisNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.CreateUisNodeResponse().from_map(
            await self.do_rpcrequest_async('CreateUisNode', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_uis_node(
        self,
        request: uis_20180821_models.CreateUisNodeRequest,
    ) -> uis_20180821_models.CreateUisNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_uis_node_with_options(request, runtime)

    async def create_uis_node_async(
        self,
        request: uis_20180821_models.CreateUisNodeRequest,
    ) -> uis_20180821_models.CreateUisNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_uis_node_with_options_async(request, runtime)

    def delete_dnat_entry_with_options(
        self,
        request: uis_20180821_models.DeleteDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteDnatEntryResponse().from_map(
            self.do_rpcrequest('DeleteDnatEntry', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dnat_entry_with_options_async(
        self,
        request: uis_20180821_models.DeleteDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteDnatEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteDnatEntry', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dnat_entry(
        self,
        request: uis_20180821_models.DeleteDnatEntryRequest,
    ) -> uis_20180821_models.DeleteDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dnat_entry_with_options(request, runtime)

    async def delete_dnat_entry_async(
        self,
        request: uis_20180821_models.DeleteDnatEntryRequest,
    ) -> uis_20180821_models.DeleteDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dnat_entry_with_options_async(request, runtime)

    def delete_high_priority_ip_with_options(
        self,
        request: uis_20180821_models.DeleteHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteHighPriorityIpResponse().from_map(
            self.do_rpcrequest('DeleteHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_high_priority_ip_with_options_async(
        self,
        request: uis_20180821_models.DeleteHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteHighPriorityIpResponse().from_map(
            await self.do_rpcrequest_async('DeleteHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_high_priority_ip(
        self,
        request: uis_20180821_models.DeleteHighPriorityIpRequest,
    ) -> uis_20180821_models.DeleteHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_high_priority_ip_with_options(request, runtime)

    async def delete_high_priority_ip_async(
        self,
        request: uis_20180821_models.DeleteHighPriorityIpRequest,
    ) -> uis_20180821_models.DeleteHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_high_priority_ip_with_options_async(request, runtime)

    def delete_sub_connection_with_options(
        self,
        request: uis_20180821_models.DeleteSubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteSubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteSubConnectionResponse().from_map(
            self.do_rpcrequest('DeleteSubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sub_connection_with_options_async(
        self,
        request: uis_20180821_models.DeleteSubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteSubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteSubConnectionResponse().from_map(
            await self.do_rpcrequest_async('DeleteSubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sub_connection(
        self,
        request: uis_20180821_models.DeleteSubConnectionRequest,
    ) -> uis_20180821_models.DeleteSubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sub_connection_with_options(request, runtime)

    async def delete_sub_connection_async(
        self,
        request: uis_20180821_models.DeleteSubConnectionRequest,
    ) -> uis_20180821_models.DeleteSubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sub_connection_with_options_async(request, runtime)

    def delete_uis_with_options(
        self,
        request: uis_20180821_models.DeleteUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisResponse().from_map(
            self.do_rpcrequest('DeleteUis', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_uis_with_options_async(
        self,
        request: uis_20180821_models.DeleteUisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisResponse().from_map(
            await self.do_rpcrequest_async('DeleteUis', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_uis(
        self,
        request: uis_20180821_models.DeleteUisRequest,
    ) -> uis_20180821_models.DeleteUisResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uis_with_options(request, runtime)

    async def delete_uis_async(
        self,
        request: uis_20180821_models.DeleteUisRequest,
    ) -> uis_20180821_models.DeleteUisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uis_with_options_async(request, runtime)

    def delete_uis_connection_with_options(
        self,
        request: uis_20180821_models.DeleteUisConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisConnectionResponse().from_map(
            self.do_rpcrequest('DeleteUisConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_uis_connection_with_options_async(
        self,
        request: uis_20180821_models.DeleteUisConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisConnectionResponse().from_map(
            await self.do_rpcrequest_async('DeleteUisConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_uis_connection(
        self,
        request: uis_20180821_models.DeleteUisConnectionRequest,
    ) -> uis_20180821_models.DeleteUisConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uis_connection_with_options(request, runtime)

    async def delete_uis_connection_async(
        self,
        request: uis_20180821_models.DeleteUisConnectionRequest,
    ) -> uis_20180821_models.DeleteUisConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uis_connection_with_options_async(request, runtime)

    def delete_uis_network_interface_with_options(
        self,
        request: uis_20180821_models.DeleteUisNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisNetworkInterfaceResponse().from_map(
            self.do_rpcrequest('DeleteUisNetworkInterface', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_uis_network_interface_with_options_async(
        self,
        request: uis_20180821_models.DeleteUisNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisNetworkInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteUisNetworkInterface', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_uis_network_interface(
        self,
        request: uis_20180821_models.DeleteUisNetworkInterfaceRequest,
    ) -> uis_20180821_models.DeleteUisNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uis_network_interface_with_options(request, runtime)

    async def delete_uis_network_interface_async(
        self,
        request: uis_20180821_models.DeleteUisNetworkInterfaceRequest,
    ) -> uis_20180821_models.DeleteUisNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uis_network_interface_with_options_async(request, runtime)

    def delete_uis_node_with_options(
        self,
        request: uis_20180821_models.DeleteUisNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisNodeResponse().from_map(
            self.do_rpcrequest('DeleteUisNode', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_uis_node_with_options_async(
        self,
        request: uis_20180821_models.DeleteUisNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisNodeResponse().from_map(
            await self.do_rpcrequest_async('DeleteUisNode', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_uis_node(
        self,
        request: uis_20180821_models.DeleteUisNodeRequest,
    ) -> uis_20180821_models.DeleteUisNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uis_node_with_options(request, runtime)

    async def delete_uis_node_async(
        self,
        request: uis_20180821_models.DeleteUisNodeRequest,
    ) -> uis_20180821_models.DeleteUisNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uis_node_with_options_async(request, runtime)

    def delete_uis_node_ip_with_options(
        self,
        request: uis_20180821_models.DeleteUisNodeIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisNodeIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisNodeIpResponse().from_map(
            self.do_rpcrequest('DeleteUisNodeIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_uis_node_ip_with_options_async(
        self,
        request: uis_20180821_models.DeleteUisNodeIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DeleteUisNodeIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DeleteUisNodeIpResponse().from_map(
            await self.do_rpcrequest_async('DeleteUisNodeIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_uis_node_ip(
        self,
        request: uis_20180821_models.DeleteUisNodeIpRequest,
    ) -> uis_20180821_models.DeleteUisNodeIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uis_node_ip_with_options(request, runtime)

    async def delete_uis_node_ip_async(
        self,
        request: uis_20180821_models.DeleteUisNodeIpRequest,
    ) -> uis_20180821_models.DeleteUisNodeIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uis_node_ip_with_options_async(request, runtime)

    def describe_areas_with_options(
        self,
        request: uis_20180821_models.DescribeAreasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeAreasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeAreasResponse().from_map(
            self.do_rpcrequest('DescribeAreas', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_areas_with_options_async(
        self,
        request: uis_20180821_models.DescribeAreasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeAreasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeAreasResponse().from_map(
            await self.do_rpcrequest_async('DescribeAreas', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_areas(
        self,
        request: uis_20180821_models.DescribeAreasRequest,
    ) -> uis_20180821_models.DescribeAreasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_areas_with_options(request, runtime)

    async def describe_areas_async(
        self,
        request: uis_20180821_models.DescribeAreasRequest,
    ) -> uis_20180821_models.DescribeAreasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_areas_with_options_async(request, runtime)

    def describe_dnat_entries_with_options(
        self,
        request: uis_20180821_models.DescribeDnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeDnatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeDnatEntriesResponse().from_map(
            self.do_rpcrequest('DescribeDnatEntries', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dnat_entries_with_options_async(
        self,
        request: uis_20180821_models.DescribeDnatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeDnatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeDnatEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDnatEntries', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dnat_entries(
        self,
        request: uis_20180821_models.DescribeDnatEntriesRequest,
    ) -> uis_20180821_models.DescribeDnatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dnat_entries_with_options(request, runtime)

    async def describe_dnat_entries_async(
        self,
        request: uis_20180821_models.DescribeDnatEntriesRequest,
    ) -> uis_20180821_models.DescribeDnatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dnat_entries_with_options_async(request, runtime)

    def describe_high_priority_ip_with_options(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeHighPriorityIpResponse().from_map(
            self.do_rpcrequest('DescribeHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_high_priority_ip_with_options_async(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeHighPriorityIpResponse().from_map(
            await self.do_rpcrequest_async('DescribeHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_high_priority_ip(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpRequest,
    ) -> uis_20180821_models.DescribeHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_high_priority_ip_with_options(request, runtime)

    async def describe_high_priority_ip_async(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpRequest,
    ) -> uis_20180821_models.DescribeHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_high_priority_ip_with_options_async(request, runtime)

    def describe_high_priority_ips_with_options(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeHighPriorityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeHighPriorityIpsResponse().from_map(
            self.do_rpcrequest('DescribeHighPriorityIps', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_high_priority_ips_with_options_async(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeHighPriorityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeHighPriorityIpsResponse().from_map(
            await self.do_rpcrequest_async('DescribeHighPriorityIps', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_high_priority_ips(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpsRequest,
    ) -> uis_20180821_models.DescribeHighPriorityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_high_priority_ips_with_options(request, runtime)

    async def describe_high_priority_ips_async(
        self,
        request: uis_20180821_models.DescribeHighPriorityIpsRequest,
    ) -> uis_20180821_models.DescribeHighPriorityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_high_priority_ips_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: uis_20180821_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: uis_20180821_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: uis_20180821_models.DescribeRegionsRequest,
    ) -> uis_20180821_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: uis_20180821_models.DescribeRegionsRequest,
    ) -> uis_20180821_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_sub_connection_with_options(
        self,
        request: uis_20180821_models.DescribeSubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeSubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeSubConnectionResponse().from_map(
            self.do_rpcrequest('DescribeSubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sub_connection_with_options_async(
        self,
        request: uis_20180821_models.DescribeSubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeSubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeSubConnectionResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sub_connection(
        self,
        request: uis_20180821_models.DescribeSubConnectionRequest,
    ) -> uis_20180821_models.DescribeSubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sub_connection_with_options(request, runtime)

    async def describe_sub_connection_async(
        self,
        request: uis_20180821_models.DescribeSubConnectionRequest,
    ) -> uis_20180821_models.DescribeSubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sub_connection_with_options_async(request, runtime)

    def describe_sub_connections_with_options(
        self,
        request: uis_20180821_models.DescribeSubConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeSubConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeSubConnectionsResponse().from_map(
            self.do_rpcrequest('DescribeSubConnections', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sub_connections_with_options_async(
        self,
        request: uis_20180821_models.DescribeSubConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeSubConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeSubConnectionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubConnections', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sub_connections(
        self,
        request: uis_20180821_models.DescribeSubConnectionsRequest,
    ) -> uis_20180821_models.DescribeSubConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sub_connections_with_options(request, runtime)

    async def describe_sub_connections_async(
        self,
        request: uis_20180821_models.DescribeSubConnectionsRequest,
    ) -> uis_20180821_models.DescribeSubConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sub_connections_with_options_async(request, runtime)

    def describe_uis_connections_with_options(
        self,
        request: uis_20180821_models.DescribeUisConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisConnectionsResponse().from_map(
            self.do_rpcrequest('DescribeUisConnections', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_uis_connections_with_options_async(
        self,
        request: uis_20180821_models.DescribeUisConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisConnectionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUisConnections', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_uis_connections(
        self,
        request: uis_20180821_models.DescribeUisConnectionsRequest,
    ) -> uis_20180821_models.DescribeUisConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uis_connections_with_options(request, runtime)

    async def describe_uis_connections_async(
        self,
        request: uis_20180821_models.DescribeUisConnectionsRequest,
    ) -> uis_20180821_models.DescribeUisConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uis_connections_with_options_async(request, runtime)

    def describe_uise_node_status_with_options(
        self,
        request: uis_20180821_models.DescribeUiseNodeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUiseNodeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUiseNodeStatusResponse().from_map(
            self.do_rpcrequest('DescribeUiseNodeStatus', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_uise_node_status_with_options_async(
        self,
        request: uis_20180821_models.DescribeUiseNodeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUiseNodeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUiseNodeStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeUiseNodeStatus', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_uise_node_status(
        self,
        request: uis_20180821_models.DescribeUiseNodeStatusRequest,
    ) -> uis_20180821_models.DescribeUiseNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uise_node_status_with_options(request, runtime)

    async def describe_uise_node_status_async(
        self,
        request: uis_20180821_models.DescribeUiseNodeStatusRequest,
    ) -> uis_20180821_models.DescribeUiseNodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uise_node_status_with_options_async(request, runtime)

    def describe_uises_with_options(
        self,
        request: uis_20180821_models.DescribeUisesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisesResponse().from_map(
            self.do_rpcrequest('DescribeUises', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_uises_with_options_async(
        self,
        request: uis_20180821_models.DescribeUisesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisesResponse().from_map(
            await self.do_rpcrequest_async('DescribeUises', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_uises(
        self,
        request: uis_20180821_models.DescribeUisesRequest,
    ) -> uis_20180821_models.DescribeUisesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uises_with_options(request, runtime)

    async def describe_uises_async(
        self,
        request: uis_20180821_models.DescribeUisesRequest,
    ) -> uis_20180821_models.DescribeUisesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uises_with_options_async(request, runtime)

    def describe_uis_network_interfaces_with_options(
        self,
        request: uis_20180821_models.DescribeUisNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisNetworkInterfacesResponse().from_map(
            self.do_rpcrequest('DescribeUisNetworkInterfaces', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_uis_network_interfaces_with_options_async(
        self,
        request: uis_20180821_models.DescribeUisNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisNetworkInterfacesResponse().from_map(
            await self.do_rpcrequest_async('DescribeUisNetworkInterfaces', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_uis_network_interfaces(
        self,
        request: uis_20180821_models.DescribeUisNetworkInterfacesRequest,
    ) -> uis_20180821_models.DescribeUisNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uis_network_interfaces_with_options(request, runtime)

    async def describe_uis_network_interfaces_async(
        self,
        request: uis_20180821_models.DescribeUisNetworkInterfacesRequest,
    ) -> uis_20180821_models.DescribeUisNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uis_network_interfaces_with_options_async(request, runtime)

    def describe_uis_nodes_with_options(
        self,
        request: uis_20180821_models.DescribeUisNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisNodesResponse().from_map(
            self.do_rpcrequest('DescribeUisNodes', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_uis_nodes_with_options_async(
        self,
        request: uis_20180821_models.DescribeUisNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeUisNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeUisNodesResponse().from_map(
            await self.do_rpcrequest_async('DescribeUisNodes', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_uis_nodes(
        self,
        request: uis_20180821_models.DescribeUisNodesRequest,
    ) -> uis_20180821_models.DescribeUisNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uis_nodes_with_options(request, runtime)

    async def describe_uis_nodes_async(
        self,
        request: uis_20180821_models.DescribeUisNodesRequest,
    ) -> uis_20180821_models.DescribeUisNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uis_nodes_with_options_async(request, runtime)

    def describe_white_list_with_options(
        self,
        request: uis_20180821_models.DescribeWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeWhiteListResponse().from_map(
            self.do_rpcrequest('DescribeWhiteList', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_white_list_with_options_async(
        self,
        request: uis_20180821_models.DescribeWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.DescribeWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.DescribeWhiteListResponse().from_map(
            await self.do_rpcrequest_async('DescribeWhiteList', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_white_list(
        self,
        request: uis_20180821_models.DescribeWhiteListRequest,
    ) -> uis_20180821_models.DescribeWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_white_list_with_options(request, runtime)

    async def describe_white_list_async(
        self,
        request: uis_20180821_models.DescribeWhiteListRequest,
    ) -> uis_20180821_models.DescribeWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_white_list_with_options_async(request, runtime)

    def get_dropped_ip_list_with_options(
        self,
        request: uis_20180821_models.GetDroppedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.GetDroppedIpListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.GetDroppedIpListResponse().from_map(
            self.do_rpcrequest('GetDroppedIpList', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dropped_ip_list_with_options_async(
        self,
        request: uis_20180821_models.GetDroppedIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.GetDroppedIpListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.GetDroppedIpListResponse().from_map(
            await self.do_rpcrequest_async('GetDroppedIpList', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dropped_ip_list(
        self,
        request: uis_20180821_models.GetDroppedIpListRequest,
    ) -> uis_20180821_models.GetDroppedIpListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dropped_ip_list_with_options(request, runtime)

    async def get_dropped_ip_list_async(
        self,
        request: uis_20180821_models.GetDroppedIpListRequest,
    ) -> uis_20180821_models.GetDroppedIpListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dropped_ip_list_with_options_async(request, runtime)

    def modify_dnat_entry_with_options(
        self,
        request: uis_20180821_models.ModifyDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyDnatEntryResponse().from_map(
            self.do_rpcrequest('ModifyDnatEntry', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dnat_entry_with_options_async(
        self,
        request: uis_20180821_models.ModifyDnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyDnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyDnatEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifyDnatEntry', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dnat_entry(
        self,
        request: uis_20180821_models.ModifyDnatEntryRequest,
    ) -> uis_20180821_models.ModifyDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dnat_entry_with_options(request, runtime)

    async def modify_dnat_entry_async(
        self,
        request: uis_20180821_models.ModifyDnatEntryRequest,
    ) -> uis_20180821_models.ModifyDnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dnat_entry_with_options_async(request, runtime)

    def modify_high_priority_ip_with_options(
        self,
        request: uis_20180821_models.ModifyHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyHighPriorityIpResponse().from_map(
            self.do_rpcrequest('ModifyHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_high_priority_ip_with_options_async(
        self,
        request: uis_20180821_models.ModifyHighPriorityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyHighPriorityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyHighPriorityIpResponse().from_map(
            await self.do_rpcrequest_async('ModifyHighPriorityIp', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_high_priority_ip(
        self,
        request: uis_20180821_models.ModifyHighPriorityIpRequest,
    ) -> uis_20180821_models.ModifyHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_high_priority_ip_with_options(request, runtime)

    async def modify_high_priority_ip_async(
        self,
        request: uis_20180821_models.ModifyHighPriorityIpRequest,
    ) -> uis_20180821_models.ModifyHighPriorityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_high_priority_ip_with_options_async(request, runtime)

    def modify_sub_connection_with_options(
        self,
        request: uis_20180821_models.ModifySubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifySubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifySubConnectionResponse().from_map(
            self.do_rpcrequest('ModifySubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sub_connection_with_options_async(
        self,
        request: uis_20180821_models.ModifySubConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifySubConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifySubConnectionResponse().from_map(
            await self.do_rpcrequest_async('ModifySubConnection', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sub_connection(
        self,
        request: uis_20180821_models.ModifySubConnectionRequest,
    ) -> uis_20180821_models.ModifySubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sub_connection_with_options(request, runtime)

    async def modify_sub_connection_async(
        self,
        request: uis_20180821_models.ModifySubConnectionRequest,
    ) -> uis_20180821_models.ModifySubConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sub_connection_with_options_async(request, runtime)

    def modify_uis_attribute_with_options(
        self,
        request: uis_20180821_models.ModifyUisAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyUisAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyUisAttributeResponse().from_map(
            self.do_rpcrequest('ModifyUisAttribute', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_uis_attribute_with_options_async(
        self,
        request: uis_20180821_models.ModifyUisAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyUisAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyUisAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyUisAttribute', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_uis_attribute(
        self,
        request: uis_20180821_models.ModifyUisAttributeRequest,
    ) -> uis_20180821_models.ModifyUisAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_uis_attribute_with_options(request, runtime)

    async def modify_uis_attribute_async(
        self,
        request: uis_20180821_models.ModifyUisAttributeRequest,
    ) -> uis_20180821_models.ModifyUisAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_uis_attribute_with_options_async(request, runtime)

    def modify_uis_connection_attribute_with_options(
        self,
        request: uis_20180821_models.ModifyUisConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyUisConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyUisConnectionAttributeResponse().from_map(
            self.do_rpcrequest('ModifyUisConnectionAttribute', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_uis_connection_attribute_with_options_async(
        self,
        request: uis_20180821_models.ModifyUisConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyUisConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyUisConnectionAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyUisConnectionAttribute', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_uis_connection_attribute(
        self,
        request: uis_20180821_models.ModifyUisConnectionAttributeRequest,
    ) -> uis_20180821_models.ModifyUisConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_uis_connection_attribute_with_options(request, runtime)

    async def modify_uis_connection_attribute_async(
        self,
        request: uis_20180821_models.ModifyUisConnectionAttributeRequest,
    ) -> uis_20180821_models.ModifyUisConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_uis_connection_attribute_with_options_async(request, runtime)

    def modify_uis_node_attribute_with_options(
        self,
        request: uis_20180821_models.ModifyUisNodeAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyUisNodeAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyUisNodeAttributeResponse().from_map(
            self.do_rpcrequest('ModifyUisNodeAttribute', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_uis_node_attribute_with_options_async(
        self,
        request: uis_20180821_models.ModifyUisNodeAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyUisNodeAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyUisNodeAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyUisNodeAttribute', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_uis_node_attribute(
        self,
        request: uis_20180821_models.ModifyUisNodeAttributeRequest,
    ) -> uis_20180821_models.ModifyUisNodeAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_uis_node_attribute_with_options(request, runtime)

    async def modify_uis_node_attribute_async(
        self,
        request: uis_20180821_models.ModifyUisNodeAttributeRequest,
    ) -> uis_20180821_models.ModifyUisNodeAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_uis_node_attribute_with_options_async(request, runtime)

    def modify_white_list_with_options(
        self,
        request: uis_20180821_models.ModifyWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyWhiteListResponse().from_map(
            self.do_rpcrequest('ModifyWhiteList', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_white_list_with_options_async(
        self,
        request: uis_20180821_models.ModifyWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> uis_20180821_models.ModifyWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return uis_20180821_models.ModifyWhiteListResponse().from_map(
            await self.do_rpcrequest_async('ModifyWhiteList', '2018-08-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_white_list(
        self,
        request: uis_20180821_models.ModifyWhiteListRequest,
    ) -> uis_20180821_models.ModifyWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_white_list_with_options(request, runtime)

    async def modify_white_list_async(
        self,
        request: uis_20180821_models.ModifyWhiteListRequest,
    ) -> uis_20180821_models.ModifyWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_white_list_with_options_async(request, runtime)
