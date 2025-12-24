# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_slb20140515 import models as main_models
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

    def add_access_control_list_entry_with_options(
        self,
        request: main_models.AddAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
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
            action = 'AddAccessControlListEntry',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_access_control_list_entry_with_options_async(
        self,
        request: main_models.AddAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
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
            action = 'AddAccessControlListEntry',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAccessControlListEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_access_control_list_entry(
        self,
        request: main_models.AddAccessControlListEntryRequest,
    ) -> main_models.AddAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return self.add_access_control_list_entry_with_options(request, runtime)

    async def add_access_control_list_entry_async(
        self,
        request: main_models.AddAccessControlListEntryRequest,
    ) -> main_models.AddAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return await self.add_access_control_list_entry_with_options_async(request, runtime)

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
            action = 'AddBackendServers',
            version = '2014-05-15',
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
            action = 'AddBackendServers',
            version = '2014-05-15',
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

    def add_listener_white_list_item_with_options(
        self,
        request: main_models.AddListenerWhiteListItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddListenerWhiteListItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        if not DaraCore.is_null(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddListenerWhiteListItem',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddListenerWhiteListItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_listener_white_list_item_with_options_async(
        self,
        request: main_models.AddListenerWhiteListItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddListenerWhiteListItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        if not DaraCore.is_null(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddListenerWhiteListItem',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddListenerWhiteListItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_listener_white_list_item(
        self,
        request: main_models.AddListenerWhiteListItemRequest,
    ) -> main_models.AddListenerWhiteListItemResponse:
        runtime = RuntimeOptions()
        return self.add_listener_white_list_item_with_options(request, runtime)

    async def add_listener_white_list_item_async(
        self,
        request: main_models.AddListenerWhiteListItemRequest,
    ) -> main_models.AddListenerWhiteListItemResponse:
        runtime = RuntimeOptions()
        return await self.add_listener_white_list_item_with_options_async(request, runtime)

    def add_tags_with_options(
        self,
        request: main_models.AddTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTagsResponse:
        request.validate()
        query = {}
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTags',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: main_models.AddTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTagsResponse:
        request.validate()
        query = {}
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTags',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags(
        self,
        request: main_models.AddTagsRequest,
    ) -> main_models.AddTagsResponse:
        runtime = RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    async def add_tags_async(
        self,
        request: main_models.AddTagsRequest,
    ) -> main_models.AddTagsResponse:
        runtime = RuntimeOptions()
        return await self.add_tags_with_options_async(request, runtime)

    def add_vserver_group_backend_servers_with_options(
        self,
        request: main_models.AddVServerGroupBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVServerGroupBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVServerGroupBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vserver_group_backend_servers_with_options_async(
        self,
        request: main_models.AddVServerGroupBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVServerGroupBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVServerGroupBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVServerGroupBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vserver_group_backend_servers(
        self,
        request: main_models.AddVServerGroupBackendServersRequest,
    ) -> main_models.AddVServerGroupBackendServersResponse:
        runtime = RuntimeOptions()
        return self.add_vserver_group_backend_servers_with_options(request, runtime)

    async def add_vserver_group_backend_servers_async(
        self,
        request: main_models.AddVServerGroupBackendServersRequest,
    ) -> main_models.AddVServerGroupBackendServersResponse:
        runtime = RuntimeOptions()
        return await self.add_vserver_group_backend_servers_with_options_async(request, runtime)

    def create_access_control_list_with_options(
        self,
        request: main_models.CreateAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessControlList',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_control_list_with_options_async(
        self,
        request: main_models.CreateAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessControlList',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_control_list(
        self,
        request: main_models.CreateAccessControlListRequest,
    ) -> main_models.CreateAccessControlListResponse:
        runtime = RuntimeOptions()
        return self.create_access_control_list_with_options(request, runtime)

    async def create_access_control_list_async(
        self,
        request: main_models.CreateAccessControlListRequest,
    ) -> main_models.CreateAccessControlListResponse:
        runtime = RuntimeOptions()
        return await self.create_access_control_list_with_options_async(request, runtime)

    def create_domain_extension_with_options(
        self,
        request: main_models.CreateDomainExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomainExtension',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_extension_with_options_async(
        self,
        request: main_models.CreateDomainExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomainExtension',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain_extension(
        self,
        request: main_models.CreateDomainExtensionRequest,
    ) -> main_models.CreateDomainExtensionResponse:
        runtime = RuntimeOptions()
        return self.create_domain_extension_with_options(request, runtime)

    async def create_domain_extension_async(
        self,
        request: main_models.CreateDomainExtensionRequest,
    ) -> main_models.CreateDomainExtensionResponse:
        runtime = RuntimeOptions()
        return await self.create_domain_extension_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: main_models.CreateLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not DaraCore.is_null(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not DaraCore.is_null(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not DaraCore.is_null(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not DaraCore.is_null(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not DaraCore.is_null(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerHTTPListener',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerHTTPListener',
            version = '2014-05-15',
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

    def create_load_balancer_httpslistener_with_options(
        self,
        request: main_models.CreateLoadBalancerHTTPSListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerHTTPSListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerHTTPSListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerHTTPSListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_httpslistener_with_options_async(
        self,
        request: main_models.CreateLoadBalancerHTTPSListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerHTTPSListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerHTTPSListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerHTTPSListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_httpslistener(
        self,
        request: main_models.CreateLoadBalancerHTTPSListenerRequest,
    ) -> main_models.CreateLoadBalancerHTTPSListenerResponse:
        runtime = RuntimeOptions()
        return self.create_load_balancer_httpslistener_with_options(request, runtime)

    async def create_load_balancer_httpslistener_async(
        self,
        request: main_models.CreateLoadBalancerHTTPSListenerRequest,
    ) -> main_models.CreateLoadBalancerHTTPSListenerResponse:
        runtime = RuntimeOptions()
        return await self.create_load_balancer_httpslistener_with_options_async(request, runtime)

    def create_load_balancer_tcplistener_with_options(
        self,
        request: main_models.CreateLoadBalancerTCPListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerTCPListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not DaraCore.is_null(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerTCPListener',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not DaraCore.is_null(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerTCPListener',
            version = '2014-05-15',
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

    def create_load_balancer_udplistener_with_options(
        self,
        request: main_models.CreateLoadBalancerUDPListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerUDPListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not DaraCore.is_null(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerUDPListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerUDPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_udplistener_with_options_async(
        self,
        request: main_models.CreateLoadBalancerUDPListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerUDPListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not DaraCore.is_null(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancerUDPListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerUDPListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_udplistener(
        self,
        request: main_models.CreateLoadBalancerUDPListenerRequest,
    ) -> main_models.CreateLoadBalancerUDPListenerResponse:
        runtime = RuntimeOptions()
        return self.create_load_balancer_udplistener_with_options(request, runtime)

    async def create_load_balancer_udplistener_async(
        self,
        request: main_models.CreateLoadBalancerUDPListenerRequest,
    ) -> main_models.CreateLoadBalancerUDPListenerResponse:
        runtime = RuntimeOptions()
        return await self.create_load_balancer_udplistener_with_options_async(request, runtime)

    def create_master_slave_server_group_with_options(
        self,
        request: main_models.CreateMasterSlaveServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMasterSlaveServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_backend_servers):
            query['MasterSlaveBackendServers'] = request.master_slave_backend_servers
        if not DaraCore.is_null(request.master_slave_server_group_name):
            query['MasterSlaveServerGroupName'] = request.master_slave_server_group_name
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMasterSlaveServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMasterSlaveServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_master_slave_server_group_with_options_async(
        self,
        request: main_models.CreateMasterSlaveServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMasterSlaveServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_backend_servers):
            query['MasterSlaveBackendServers'] = request.master_slave_backend_servers
        if not DaraCore.is_null(request.master_slave_server_group_name):
            query['MasterSlaveServerGroupName'] = request.master_slave_server_group_name
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMasterSlaveServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMasterSlaveServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_master_slave_server_group(
        self,
        request: main_models.CreateMasterSlaveServerGroupRequest,
    ) -> main_models.CreateMasterSlaveServerGroupResponse:
        runtime = RuntimeOptions()
        return self.create_master_slave_server_group_with_options(request, runtime)

    async def create_master_slave_server_group_async(
        self,
        request: main_models.CreateMasterSlaveServerGroupRequest,
    ) -> main_models.CreateMasterSlaveServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_master_slave_server_group_with_options_async(request, runtime)

    def create_rules_with_options(
        self,
        request: main_models.CreateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        if not DaraCore.is_null(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRules',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        request: main_models.CreateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        if not DaraCore.is_null(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRules',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rules(
        self,
        request: main_models.CreateRulesRequest,
    ) -> main_models.CreateRulesResponse:
        runtime = RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    async def create_rules_async(
        self,
        request: main_models.CreateRulesRequest,
    ) -> main_models.CreateRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_rules_with_options_async(request, runtime)

    def create_tlscipher_policy_with_options(
        self,
        request: main_models.CreateTLSCipherPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTLSCipherPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
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
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTLSCipherPolicy',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTLSCipherPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tlscipher_policy_with_options_async(
        self,
        request: main_models.CreateTLSCipherPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTLSCipherPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
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
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTLSCipherPolicy',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTLSCipherPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tlscipher_policy(
        self,
        request: main_models.CreateTLSCipherPolicyRequest,
    ) -> main_models.CreateTLSCipherPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_tlscipher_policy_with_options(request, runtime)

    async def create_tlscipher_policy_async(
        self,
        request: main_models.CreateTLSCipherPolicyRequest,
    ) -> main_models.CreateTLSCipherPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_tlscipher_policy_with_options_async(request, runtime)

    def create_vserver_group_with_options(
        self,
        request: main_models.CreateVServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVServerGroupResponse:
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vserver_group_with_options_async(
        self,
        request: main_models.CreateVServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVServerGroupResponse:
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vserver_group(
        self,
        request: main_models.CreateVServerGroupRequest,
    ) -> main_models.CreateVServerGroupResponse:
        runtime = RuntimeOptions()
        return self.create_vserver_group_with_options(request, runtime)

    async def create_vserver_group_async(
        self,
        request: main_models.CreateVServerGroupRequest,
    ) -> main_models.CreateVServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_vserver_group_with_options_async(request, runtime)

    def delete_access_control_list_with_options(
        self,
        request: main_models.DeleteAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
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
            action = 'DeleteAccessControlList',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_control_list_with_options_async(
        self,
        request: main_models.DeleteAccessControlListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
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
            action = 'DeleteAccessControlList',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_control_list(
        self,
        request: main_models.DeleteAccessControlListRequest,
    ) -> main_models.DeleteAccessControlListResponse:
        runtime = RuntimeOptions()
        return self.delete_access_control_list_with_options(request, runtime)

    async def delete_access_control_list_async(
        self,
        request: main_models.DeleteAccessControlListRequest,
    ) -> main_models.DeleteAccessControlListResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_control_list_with_options_async(request, runtime)

    def delete_access_logs_download_attribute_with_options(
        self,
        request: main_models.DeleteAccessLogsDownloadAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessLogsDownloadAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.logs_download_attributes):
            query['LogsDownloadAttributes'] = request.logs_download_attributes
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessLogsDownloadAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessLogsDownloadAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_logs_download_attribute_with_options_async(
        self,
        request: main_models.DeleteAccessLogsDownloadAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessLogsDownloadAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.logs_download_attributes):
            query['LogsDownloadAttributes'] = request.logs_download_attributes
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessLogsDownloadAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessLogsDownloadAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_logs_download_attribute(
        self,
        request: main_models.DeleteAccessLogsDownloadAttributeRequest,
    ) -> main_models.DeleteAccessLogsDownloadAttributeResponse:
        runtime = RuntimeOptions()
        return self.delete_access_logs_download_attribute_with_options(request, runtime)

    async def delete_access_logs_download_attribute_async(
        self,
        request: main_models.DeleteAccessLogsDownloadAttributeRequest,
    ) -> main_models.DeleteAccessLogsDownloadAttributeResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_logs_download_attribute_with_options_async(request, runtime)

    def delete_cacertificate_with_options(
        self,
        request: main_models.DeleteCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
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
            action = 'DeleteCACertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cacertificate_with_options_async(
        self,
        request: main_models.DeleteCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
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
            action = 'DeleteCACertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cacertificate(
        self,
        request: main_models.DeleteCACertificateRequest,
    ) -> main_models.DeleteCACertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_cacertificate_with_options(request, runtime)

    async def delete_cacertificate_async(
        self,
        request: main_models.DeleteCACertificateRequest,
    ) -> main_models.DeleteCACertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_cacertificate_with_options_async(request, runtime)

    def delete_domain_extension_with_options(
        self,
        request: main_models.DeleteDomainExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
            action = 'DeleteDomainExtension',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_extension_with_options_async(
        self,
        request: main_models.DeleteDomainExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
            action = 'DeleteDomainExtension',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_extension(
        self,
        request: main_models.DeleteDomainExtensionRequest,
    ) -> main_models.DeleteDomainExtensionResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_extension_with_options(request, runtime)

    async def delete_domain_extension_async(
        self,
        request: main_models.DeleteDomainExtensionRequest,
    ) -> main_models.DeleteDomainExtensionResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_extension_with_options_async(request, runtime)

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
            action = 'DeleteLoadBalancer',
            version = '2014-05-15',
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
            action = 'DeleteLoadBalancer',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancerListener',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancerListener',
            version = '2014-05-15',
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

    def delete_master_slave_server_group_with_options(
        self,
        request: main_models.DeleteMasterSlaveServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMasterSlaveServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
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
            action = 'DeleteMasterSlaveServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMasterSlaveServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_master_slave_server_group_with_options_async(
        self,
        request: main_models.DeleteMasterSlaveServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMasterSlaveServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
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
            action = 'DeleteMasterSlaveServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMasterSlaveServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_master_slave_server_group(
        self,
        request: main_models.DeleteMasterSlaveServerGroupRequest,
    ) -> main_models.DeleteMasterSlaveServerGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_master_slave_server_group_with_options(request, runtime)

    async def delete_master_slave_server_group_async(
        self,
        request: main_models.DeleteMasterSlaveServerGroupRequest,
    ) -> main_models.DeleteMasterSlaveServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_master_slave_server_group_with_options_async(request, runtime)

    def delete_rules_with_options(
        self,
        request: main_models.DeleteRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRulesResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRules',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rules_with_options_async(
        self,
        request: main_models.DeleteRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRulesResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRules',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rules(
        self,
        request: main_models.DeleteRulesRequest,
    ) -> main_models.DeleteRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    async def delete_rules_async(
        self,
        request: main_models.DeleteRulesRequest,
    ) -> main_models.DeleteRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_rules_with_options_async(request, runtime)

    def delete_server_certificate_with_options(
        self,
        request: main_models.DeleteServerCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServerCertificateResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerCertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_server_certificate_with_options_async(
        self,
        request: main_models.DeleteServerCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServerCertificateResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerCertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_server_certificate(
        self,
        request: main_models.DeleteServerCertificateRequest,
    ) -> main_models.DeleteServerCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_server_certificate_with_options(request, runtime)

    async def delete_server_certificate_async(
        self,
        request: main_models.DeleteServerCertificateRequest,
    ) -> main_models.DeleteServerCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_server_certificate_with_options_async(request, runtime)

    def delete_tlscipher_policy_with_options(
        self,
        request: main_models.DeleteTLSCipherPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTLSCipherPolicyResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTLSCipherPolicy',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTLSCipherPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tlscipher_policy_with_options_async(
        self,
        request: main_models.DeleteTLSCipherPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTLSCipherPolicyResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTLSCipherPolicy',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTLSCipherPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tlscipher_policy(
        self,
        request: main_models.DeleteTLSCipherPolicyRequest,
    ) -> main_models.DeleteTLSCipherPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_tlscipher_policy_with_options(request, runtime)

    async def delete_tlscipher_policy_async(
        self,
        request: main_models.DeleteTLSCipherPolicyRequest,
    ) -> main_models.DeleteTLSCipherPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_tlscipher_policy_with_options_async(request, runtime)

    def delete_vserver_group_with_options(
        self,
        request: main_models.DeleteVServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVServerGroupResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vserver_group_with_options_async(
        self,
        request: main_models.DeleteVServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVServerGroupResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVServerGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vserver_group(
        self,
        request: main_models.DeleteVServerGroupRequest,
    ) -> main_models.DeleteVServerGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_vserver_group_with_options(request, runtime)

    async def delete_vserver_group_async(
        self,
        request: main_models.DeleteVServerGroupRequest,
    ) -> main_models.DeleteVServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_vserver_group_with_options_async(request, runtime)

    def describe_access_control_list_attribute_with_options(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entry_comment):
            query['AclEntryComment'] = request.acl_entry_comment
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
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
            action = 'DescribeAccessControlListAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_list_attribute_with_options_async(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entry_comment):
            query['AclEntryComment'] = request.acl_entry_comment
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
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
            action = 'DescribeAccessControlListAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_control_list_attribute(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_access_control_list_attribute_with_options(request, runtime)

    async def describe_access_control_list_attribute_async(
        self,
        request: main_models.DescribeAccessControlListAttributeRequest,
    ) -> main_models.DescribeAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_control_list_attribute_with_options_async(request, runtime)

    def describe_access_control_lists_with_options(
        self,
        request: main_models.DescribeAccessControlListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlLists',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_lists_with_options_async(
        self,
        request: main_models.DescribeAccessControlListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlLists',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_control_lists(
        self,
        request: main_models.DescribeAccessControlListsRequest,
    ) -> main_models.DescribeAccessControlListsResponse:
        runtime = RuntimeOptions()
        return self.describe_access_control_lists_with_options(request, runtime)

    async def describe_access_control_lists_async(
        self,
        request: main_models.DescribeAccessControlListsRequest,
    ) -> main_models.DescribeAccessControlListsResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_control_lists_with_options_async(request, runtime)

    def describe_access_logs_download_attribute_with_options(
        self,
        request: main_models.DescribeAccessLogsDownloadAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessLogsDownloadAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessLogsDownloadAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessLogsDownloadAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_logs_download_attribute_with_options_async(
        self,
        request: main_models.DescribeAccessLogsDownloadAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessLogsDownloadAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessLogsDownloadAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessLogsDownloadAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_logs_download_attribute(
        self,
        request: main_models.DescribeAccessLogsDownloadAttributeRequest,
    ) -> main_models.DescribeAccessLogsDownloadAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_access_logs_download_attribute_with_options(request, runtime)

    async def describe_access_logs_download_attribute_async(
        self,
        request: main_models.DescribeAccessLogsDownloadAttributeRequest,
    ) -> main_models.DescribeAccessLogsDownloadAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_logs_download_attribute_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: main_models.DescribeAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
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
            action = 'DescribeAvailableResource',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: main_models.DescribeAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
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
            action = 'DescribeAvailableResource',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: main_models.DescribeAvailableResourceRequest,
    ) -> main_models.DescribeAvailableResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: main_models.DescribeAvailableResourceRequest,
    ) -> main_models.DescribeAvailableResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_cacertificates_with_options(
        self,
        request: main_models.DescribeCACertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCACertificates',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificates_with_options_async(
        self,
        request: main_models.DescribeCACertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCACertificates',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificates(
        self,
        request: main_models.DescribeCACertificatesRequest,
    ) -> main_models.DescribeCACertificatesResponse:
        runtime = RuntimeOptions()
        return self.describe_cacertificates_with_options(request, runtime)

    async def describe_cacertificates_async(
        self,
        request: main_models.DescribeCACertificatesRequest,
    ) -> main_models.DescribeCACertificatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cacertificates_with_options_async(request, runtime)

    def describe_domain_extension_attribute_with_options(
        self,
        request: main_models.DescribeDomainExtensionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainExtensionAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
            action = 'DescribeDomainExtensionAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_extension_attribute_with_options_async(
        self,
        request: main_models.DescribeDomainExtensionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainExtensionAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
            action = 'DescribeDomainExtensionAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainExtensionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_extension_attribute(
        self,
        request: main_models.DescribeDomainExtensionAttributeRequest,
    ) -> main_models.DescribeDomainExtensionAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_extension_attribute_with_options(request, runtime)

    async def describe_domain_extension_attribute_async(
        self,
        request: main_models.DescribeDomainExtensionAttributeRequest,
    ) -> main_models.DescribeDomainExtensionAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_extension_attribute_with_options_async(request, runtime)

    def describe_domain_extensions_with_options(
        self,
        request: main_models.DescribeDomainExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainExtensions',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_extensions_with_options_async(
        self,
        request: main_models.DescribeDomainExtensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainExtensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainExtensions',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainExtensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_extensions(
        self,
        request: main_models.DescribeDomainExtensionsRequest,
    ) -> main_models.DescribeDomainExtensionsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_extensions_with_options(request, runtime)

    async def describe_domain_extensions_async(
        self,
        request: main_models.DescribeDomainExtensionsRequest,
    ) -> main_models.DescribeDomainExtensionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_extensions_with_options_async(request, runtime)

    def describe_health_status_with_options(
        self,
        request: main_models.DescribeHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthStatus',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_status_with_options_async(
        self,
        request: main_models.DescribeHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHealthStatus',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_status(
        self,
        request: main_models.DescribeHealthStatusRequest,
    ) -> main_models.DescribeHealthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    async def describe_health_status_async(
        self,
        request: main_models.DescribeHealthStatusRequest,
    ) -> main_models.DescribeHealthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_health_status_with_options_async(request, runtime)

    def describe_high_defination_monitor_with_options(
        self,
        request: main_models.DescribeHighDefinationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHighDefinationMonitorResponse:
        request.validate()
        query = {}
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHighDefinationMonitor',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHighDefinationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_high_defination_monitor_with_options_async(
        self,
        request: main_models.DescribeHighDefinationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHighDefinationMonitorResponse:
        request.validate()
        query = {}
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHighDefinationMonitor',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHighDefinationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_high_defination_monitor(
        self,
        request: main_models.DescribeHighDefinationMonitorRequest,
    ) -> main_models.DescribeHighDefinationMonitorResponse:
        runtime = RuntimeOptions()
        return self.describe_high_defination_monitor_with_options(request, runtime)

    async def describe_high_defination_monitor_async(
        self,
        request: main_models.DescribeHighDefinationMonitorRequest,
    ) -> main_models.DescribeHighDefinationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.describe_high_defination_monitor_with_options_async(request, runtime)

    def describe_listener_access_control_attribute_with_options(
        self,
        request: main_models.DescribeListenerAccessControlAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListenerAccessControlAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListenerAccessControlAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListenerAccessControlAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_listener_access_control_attribute_with_options_async(
        self,
        request: main_models.DescribeListenerAccessControlAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListenerAccessControlAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeListenerAccessControlAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListenerAccessControlAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_listener_access_control_attribute(
        self,
        request: main_models.DescribeListenerAccessControlAttributeRequest,
    ) -> main_models.DescribeListenerAccessControlAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_listener_access_control_attribute_with_options(request, runtime)

    async def describe_listener_access_control_attribute_async(
        self,
        request: main_models.DescribeListenerAccessControlAttributeRequest,
    ) -> main_models.DescribeListenerAccessControlAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_listener_access_control_attribute_with_options_async(request, runtime)

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
            action = 'DescribeLoadBalancerAttribute',
            version = '2014-05-15',
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
            action = 'DescribeLoadBalancerAttribute',
            version = '2014-05-15',
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
            action = 'DescribeLoadBalancerHTTPListenerAttribute',
            version = '2014-05-15',
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
            action = 'DescribeLoadBalancerHTTPListenerAttribute',
            version = '2014-05-15',
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

    def describe_load_balancer_httpslistener_attribute_with_options(
        self,
        request: main_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerHTTPSListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: main_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerHTTPSListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_httpslistener_attribute(
        self,
        request: main_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_load_balancer_httpslistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_httpslistener_attribute_async(
        self,
        request: main_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_balancer_httpslistener_attribute_with_options_async(request, runtime)

    def describe_load_balancer_listeners_with_options(
        self,
        request: main_models.DescribeLoadBalancerListenersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerListenersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerListeners',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_listeners_with_options_async(
        self,
        request: main_models.DescribeLoadBalancerListenersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerListenersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerListeners',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_listeners(
        self,
        request: main_models.DescribeLoadBalancerListenersRequest,
    ) -> main_models.DescribeLoadBalancerListenersResponse:
        runtime = RuntimeOptions()
        return self.describe_load_balancer_listeners_with_options(request, runtime)

    async def describe_load_balancer_listeners_async(
        self,
        request: main_models.DescribeLoadBalancerListenersRequest,
    ) -> main_models.DescribeLoadBalancerListenersResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_balancer_listeners_with_options_async(request, runtime)

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
            action = 'DescribeLoadBalancerTCPListenerAttribute',
            version = '2014-05-15',
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
            action = 'DescribeLoadBalancerTCPListenerAttribute',
            version = '2014-05-15',
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

    def describe_load_balancer_udplistener_attribute_with_options(
        self,
        request: main_models.DescribeLoadBalancerUDPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerUDPListenerAttributeResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerUDPListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: main_models.DescribeLoadBalancerUDPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancerUDPListenerAttributeResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancerUDPListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_udplistener_attribute(
        self,
        request: main_models.DescribeLoadBalancerUDPListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_load_balancer_udplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_udplistener_attribute_async(
        self,
        request: main_models.DescribeLoadBalancerUDPListenerAttributeRequest,
    ) -> main_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_balancer_udplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancers_with_options(
        self,
        request: main_models.DescribeLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancers',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadBalancers',
            version = '2014-05-15',
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

    def describe_master_slave_server_group_attribute_with_options(
        self,
        request: main_models.DescribeMasterSlaveServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMasterSlaveServerGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
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
            action = 'DescribeMasterSlaveServerGroupAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMasterSlaveServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_master_slave_server_group_attribute_with_options_async(
        self,
        request: main_models.DescribeMasterSlaveServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMasterSlaveServerGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
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
            action = 'DescribeMasterSlaveServerGroupAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMasterSlaveServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_master_slave_server_group_attribute(
        self,
        request: main_models.DescribeMasterSlaveServerGroupAttributeRequest,
    ) -> main_models.DescribeMasterSlaveServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_master_slave_server_group_attribute_with_options(request, runtime)

    async def describe_master_slave_server_group_attribute_async(
        self,
        request: main_models.DescribeMasterSlaveServerGroupAttributeRequest,
    ) -> main_models.DescribeMasterSlaveServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_master_slave_server_group_attribute_with_options_async(request, runtime)

    def describe_master_slave_server_groups_with_options(
        self,
        request: main_models.DescribeMasterSlaveServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMasterSlaveServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.include_listener):
            query['IncludeListener'] = request.include_listener
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMasterSlaveServerGroups',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMasterSlaveServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_master_slave_server_groups_with_options_async(
        self,
        request: main_models.DescribeMasterSlaveServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMasterSlaveServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.include_listener):
            query['IncludeListener'] = request.include_listener
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMasterSlaveServerGroups',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMasterSlaveServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_master_slave_server_groups(
        self,
        request: main_models.DescribeMasterSlaveServerGroupsRequest,
    ) -> main_models.DescribeMasterSlaveServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_master_slave_server_groups_with_options(request, runtime)

    async def describe_master_slave_server_groups_async(
        self,
        request: main_models.DescribeMasterSlaveServerGroupsRequest,
    ) -> main_models.DescribeMasterSlaveServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_master_slave_server_groups_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'DescribeRegions',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'DescribeRegions',
            version = '2014-05-15',
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

    def describe_rule_attribute_with_options(
        self,
        request: main_models.DescribeRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleAttributeResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_attribute_with_options_async(
        self,
        request: main_models.DescribeRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleAttributeResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_attribute(
        self,
        request: main_models.DescribeRuleAttributeRequest,
    ) -> main_models.DescribeRuleAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_attribute_with_options(request, runtime)

    async def describe_rule_attribute_async(
        self,
        request: main_models.DescribeRuleAttributeRequest,
    ) -> main_models.DescribeRuleAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_attribute_with_options_async(request, runtime)

    def describe_rules_with_options(
        self,
        request: main_models.DescribeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRules',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: main_models.DescribeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRules',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rules(
        self,
        request: main_models.DescribeRulesRequest,
    ) -> main_models.DescribeRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    async def describe_rules_async(
        self,
        request: main_models.DescribeRulesRequest,
    ) -> main_models.DescribeRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_rules_with_options_async(request, runtime)

    def describe_server_certificates_with_options(
        self,
        request: main_models.DescribeServerCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServerCertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServerCertificates',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_server_certificates_with_options_async(
        self,
        request: main_models.DescribeServerCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServerCertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServerCertificates',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServerCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_server_certificates(
        self,
        request: main_models.DescribeServerCertificatesRequest,
    ) -> main_models.DescribeServerCertificatesResponse:
        runtime = RuntimeOptions()
        return self.describe_server_certificates_with_options(request, runtime)

    async def describe_server_certificates_async(
        self,
        request: main_models.DescribeServerCertificatesRequest,
    ) -> main_models.DescribeServerCertificatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_server_certificates_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.distinct_key):
            query['DistinctKey'] = request.distinct_key
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.distinct_key):
            query['DistinctKey'] = request.distinct_key
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_vserver_group_attribute_with_options(
        self,
        request: main_models.DescribeVServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVServerGroupAttributeResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVServerGroupAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vserver_group_attribute_with_options_async(
        self,
        request: main_models.DescribeVServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVServerGroupAttributeResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVServerGroupAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vserver_group_attribute(
        self,
        request: main_models.DescribeVServerGroupAttributeRequest,
    ) -> main_models.DescribeVServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_vserver_group_attribute_with_options(request, runtime)

    async def describe_vserver_group_attribute_async(
        self,
        request: main_models.DescribeVServerGroupAttributeRequest,
    ) -> main_models.DescribeVServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_vserver_group_attribute_with_options_async(request, runtime)

    def describe_vserver_groups_with_options(
        self,
        request: main_models.DescribeVServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not DaraCore.is_null(request.include_rule):
            query['IncludeRule'] = request.include_rule
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVServerGroups',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vserver_groups_with_options_async(
        self,
        request: main_models.DescribeVServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not DaraCore.is_null(request.include_rule):
            query['IncludeRule'] = request.include_rule
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVServerGroups',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vserver_groups(
        self,
        request: main_models.DescribeVServerGroupsRequest,
    ) -> main_models.DescribeVServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_vserver_groups_with_options(request, runtime)

    async def describe_vserver_groups_async(
        self,
        request: main_models.DescribeVServerGroupsRequest,
    ) -> main_models.DescribeVServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vserver_groups_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'DescribeZones',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'DescribeZones',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def enable_high_defination_monitor_with_options(
        self,
        request: main_models.EnableHighDefinationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHighDefinationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHighDefinationMonitor',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHighDefinationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_high_defination_monitor_with_options_async(
        self,
        request: main_models.EnableHighDefinationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHighDefinationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHighDefinationMonitor',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHighDefinationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_high_defination_monitor(
        self,
        request: main_models.EnableHighDefinationMonitorRequest,
    ) -> main_models.EnableHighDefinationMonitorResponse:
        runtime = RuntimeOptions()
        return self.enable_high_defination_monitor_with_options(request, runtime)

    async def enable_high_defination_monitor_async(
        self,
        request: main_models.EnableHighDefinationMonitorRequest,
    ) -> main_models.EnableHighDefinationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.enable_high_defination_monitor_with_options_async(request, runtime)

    def list_tlscipher_policies_with_options(
        self,
        request: main_models.ListTLSCipherPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTLSCipherPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
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
        if not DaraCore.is_null(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTLSCipherPolicies',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTLSCipherPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tlscipher_policies_with_options_async(
        self,
        request: main_models.ListTLSCipherPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTLSCipherPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
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
        if not DaraCore.is_null(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTLSCipherPolicies',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTLSCipherPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tlscipher_policies(
        self,
        request: main_models.ListTLSCipherPoliciesRequest,
    ) -> main_models.ListTLSCipherPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_tlscipher_policies_with_options(request, runtime)

    async def list_tlscipher_policies_async(
        self,
        request: main_models.ListTLSCipherPoliciesRequest,
    ) -> main_models.ListTLSCipherPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_tlscipher_policies_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_high_defination_monitor_with_options(
        self,
        request: main_models.ModifyHighDefinationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHighDefinationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
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
            action = 'ModifyHighDefinationMonitor',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHighDefinationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_high_defination_monitor_with_options_async(
        self,
        request: main_models.ModifyHighDefinationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHighDefinationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
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
            action = 'ModifyHighDefinationMonitor',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHighDefinationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_high_defination_monitor(
        self,
        request: main_models.ModifyHighDefinationMonitorRequest,
    ) -> main_models.ModifyHighDefinationMonitorResponse:
        runtime = RuntimeOptions()
        return self.modify_high_defination_monitor_with_options(request, runtime)

    async def modify_high_defination_monitor_async(
        self,
        request: main_models.ModifyHighDefinationMonitorRequest,
    ) -> main_models.ModifyHighDefinationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.modify_high_defination_monitor_with_options_async(request, runtime)

    def modify_load_balancer_instance_charge_type_with_options(
        self,
        request: main_models.ModifyLoadBalancerInstanceChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
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
            action = 'ModifyLoadBalancerInstanceChargeType',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_instance_charge_type_with_options_async(
        self,
        request: main_models.ModifyLoadBalancerInstanceChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
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
            action = 'ModifyLoadBalancerInstanceChargeType',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_load_balancer_instance_charge_type(
        self,
        request: main_models.ModifyLoadBalancerInstanceChargeTypeRequest,
    ) -> main_models.ModifyLoadBalancerInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_load_balancer_instance_charge_type_with_options(request, runtime)

    async def modify_load_balancer_instance_charge_type_async(
        self,
        request: main_models.ModifyLoadBalancerInstanceChargeTypeRequest,
    ) -> main_models.ModifyLoadBalancerInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_load_balancer_instance_charge_type_with_options_async(request, runtime)

    def modify_load_balancer_instance_spec_with_options(
        self,
        request: main_models.ModifyLoadBalancerInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
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
            action = 'ModifyLoadBalancerInstanceSpec',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_instance_spec_with_options_async(
        self,
        request: main_models.ModifyLoadBalancerInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
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
            action = 'ModifyLoadBalancerInstanceSpec',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_load_balancer_instance_spec(
        self,
        request: main_models.ModifyLoadBalancerInstanceSpecRequest,
    ) -> main_models.ModifyLoadBalancerInstanceSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_load_balancer_instance_spec_with_options(request, runtime)

    async def modify_load_balancer_instance_spec_async(
        self,
        request: main_models.ModifyLoadBalancerInstanceSpecRequest,
    ) -> main_models.ModifyLoadBalancerInstanceSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_load_balancer_instance_spec_with_options_async(request, runtime)

    def modify_load_balancer_internet_spec_with_options(
        self,
        request: main_models.ModifyLoadBalancerInternetSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerInternetSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLoadBalancerInternetSpec',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerInternetSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_internet_spec_with_options_async(
        self,
        request: main_models.ModifyLoadBalancerInternetSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerInternetSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLoadBalancerInternetSpec',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerInternetSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_load_balancer_internet_spec(
        self,
        request: main_models.ModifyLoadBalancerInternetSpecRequest,
    ) -> main_models.ModifyLoadBalancerInternetSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_load_balancer_internet_spec_with_options(request, runtime)

    async def modify_load_balancer_internet_spec_async(
        self,
        request: main_models.ModifyLoadBalancerInternetSpecRequest,
    ) -> main_models.ModifyLoadBalancerInternetSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_load_balancer_internet_spec_with_options_async(request, runtime)

    def modify_load_balancer_pay_type_with_options(
        self,
        request: main_models.ModifyLoadBalancerPayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerPayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
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
            action = 'ModifyLoadBalancerPayType',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_pay_type_with_options_async(
        self,
        request: main_models.ModifyLoadBalancerPayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLoadBalancerPayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
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
            action = 'ModifyLoadBalancerPayType',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLoadBalancerPayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_load_balancer_pay_type(
        self,
        request: main_models.ModifyLoadBalancerPayTypeRequest,
    ) -> main_models.ModifyLoadBalancerPayTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_load_balancer_pay_type_with_options(request, runtime)

    async def modify_load_balancer_pay_type_async(
        self,
        request: main_models.ModifyLoadBalancerPayTypeRequest,
    ) -> main_models.ModifyLoadBalancerPayTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_load_balancer_pay_type_with_options_async(request, runtime)

    def modify_vserver_group_backend_servers_with_options(
        self,
        request: main_models.ModifyVServerGroupBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVServerGroupBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_backend_servers):
            query['NewBackendServers'] = request.new_backend_servers
        if not DaraCore.is_null(request.old_backend_servers):
            query['OldBackendServers'] = request.old_backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVServerGroupBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vserver_group_backend_servers_with_options_async(
        self,
        request: main_models.ModifyVServerGroupBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVServerGroupBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_backend_servers):
            query['NewBackendServers'] = request.new_backend_servers
        if not DaraCore.is_null(request.old_backend_servers):
            query['OldBackendServers'] = request.old_backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVServerGroupBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVServerGroupBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vserver_group_backend_servers(
        self,
        request: main_models.ModifyVServerGroupBackendServersRequest,
    ) -> main_models.ModifyVServerGroupBackendServersResponse:
        runtime = RuntimeOptions()
        return self.modify_vserver_group_backend_servers_with_options(request, runtime)

    async def modify_vserver_group_backend_servers_async(
        self,
        request: main_models.ModifyVServerGroupBackendServersRequest,
    ) -> main_models.ModifyVServerGroupBackendServersResponse:
        runtime = RuntimeOptions()
        return await self.modify_vserver_group_backend_servers_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def remove_access_control_list_entry_with_options(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
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
            action = 'RemoveAccessControlListEntry',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_control_list_entry_with_options_async(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
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
            action = 'RemoveAccessControlListEntry',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAccessControlListEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_access_control_list_entry(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return self.remove_access_control_list_entry_with_options(request, runtime)

    async def remove_access_control_list_entry_async(
        self,
        request: main_models.RemoveAccessControlListEntryRequest,
    ) -> main_models.RemoveAccessControlListEntryResponse:
        runtime = RuntimeOptions()
        return await self.remove_access_control_list_entry_with_options_async(request, runtime)

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
            action = 'RemoveBackendServers',
            version = '2014-05-15',
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
            action = 'RemoveBackendServers',
            version = '2014-05-15',
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

    def remove_listener_white_list_item_with_options(
        self,
        request: main_models.RemoveListenerWhiteListItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveListenerWhiteListItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        if not DaraCore.is_null(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveListenerWhiteListItem',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveListenerWhiteListItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_listener_white_list_item_with_options_async(
        self,
        request: main_models.RemoveListenerWhiteListItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveListenerWhiteListItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        if not DaraCore.is_null(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveListenerWhiteListItem',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveListenerWhiteListItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_listener_white_list_item(
        self,
        request: main_models.RemoveListenerWhiteListItemRequest,
    ) -> main_models.RemoveListenerWhiteListItemResponse:
        runtime = RuntimeOptions()
        return self.remove_listener_white_list_item_with_options(request, runtime)

    async def remove_listener_white_list_item_async(
        self,
        request: main_models.RemoveListenerWhiteListItemRequest,
    ) -> main_models.RemoveListenerWhiteListItemResponse:
        runtime = RuntimeOptions()
        return await self.remove_listener_white_list_item_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: main_models.RemoveTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTagsResponse:
        request.validate()
        query = {}
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTags',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: main_models.RemoveTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTagsResponse:
        request.validate()
        query = {}
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTags',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tags(
        self,
        request: main_models.RemoveTagsRequest,
    ) -> main_models.RemoveTagsResponse:
        runtime = RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    async def remove_tags_async(
        self,
        request: main_models.RemoveTagsRequest,
    ) -> main_models.RemoveTagsResponse:
        runtime = RuntimeOptions()
        return await self.remove_tags_with_options_async(request, runtime)

    def remove_vserver_group_backend_servers_with_options(
        self,
        request: main_models.RemoveVServerGroupBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveVServerGroupBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveVServerGroupBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vserver_group_backend_servers_with_options_async(
        self,
        request: main_models.RemoveVServerGroupBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveVServerGroupBackendServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveVServerGroupBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveVServerGroupBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vserver_group_backend_servers(
        self,
        request: main_models.RemoveVServerGroupBackendServersRequest,
    ) -> main_models.RemoveVServerGroupBackendServersResponse:
        runtime = RuntimeOptions()
        return self.remove_vserver_group_backend_servers_with_options(request, runtime)

    async def remove_vserver_group_backend_servers_async(
        self,
        request: main_models.RemoveVServerGroupBackendServersRequest,
    ) -> main_models.RemoveVServerGroupBackendServersResponse:
        runtime = RuntimeOptions()
        return await self.remove_vserver_group_backend_servers_with_options_async(request, runtime)

    def set_access_control_list_attribute_with_options(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
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
            action = 'SetAccessControlListAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_control_list_attribute_with_options_async(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccessControlListAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
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
            action = 'SetAccessControlListAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccessControlListAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_control_list_attribute(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
    ) -> main_models.SetAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_access_control_list_attribute_with_options(request, runtime)

    async def set_access_control_list_attribute_async(
        self,
        request: main_models.SetAccessControlListAttributeRequest,
    ) -> main_models.SetAccessControlListAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_access_control_list_attribute_with_options_async(request, runtime)

    def set_access_logs_download_attribute_with_options(
        self,
        request: main_models.SetAccessLogsDownloadAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccessLogsDownloadAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.logs_download_attributes):
            query['LogsDownloadAttributes'] = request.logs_download_attributes
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccessLogsDownloadAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccessLogsDownloadAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_logs_download_attribute_with_options_async(
        self,
        request: main_models.SetAccessLogsDownloadAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccessLogsDownloadAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.logs_download_attributes):
            query['LogsDownloadAttributes'] = request.logs_download_attributes
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccessLogsDownloadAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccessLogsDownloadAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_logs_download_attribute(
        self,
        request: main_models.SetAccessLogsDownloadAttributeRequest,
    ) -> main_models.SetAccessLogsDownloadAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_access_logs_download_attribute_with_options(request, runtime)

    async def set_access_logs_download_attribute_async(
        self,
        request: main_models.SetAccessLogsDownloadAttributeRequest,
    ) -> main_models.SetAccessLogsDownloadAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_access_logs_download_attribute_with_options_async(request, runtime)

    def set_backend_servers_with_options(
        self,
        request: main_models.SetBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetBackendServersResponse:
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
            action = 'SetBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_backend_servers_with_options_async(
        self,
        request: main_models.SetBackendServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetBackendServersResponse:
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
            action = 'SetBackendServers',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_backend_servers(
        self,
        request: main_models.SetBackendServersRequest,
    ) -> main_models.SetBackendServersResponse:
        runtime = RuntimeOptions()
        return self.set_backend_servers_with_options(request, runtime)

    async def set_backend_servers_async(
        self,
        request: main_models.SetBackendServersRequest,
    ) -> main_models.SetBackendServersResponse:
        runtime = RuntimeOptions()
        return await self.set_backend_servers_with_options_async(request, runtime)

    def set_cacertificate_name_with_options(
        self,
        request: main_models.SetCACertificateNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCACertificateNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
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
            action = 'SetCACertificateName',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCACertificateNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cacertificate_name_with_options_async(
        self,
        request: main_models.SetCACertificateNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCACertificateNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
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
            action = 'SetCACertificateName',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCACertificateNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cacertificate_name(
        self,
        request: main_models.SetCACertificateNameRequest,
    ) -> main_models.SetCACertificateNameResponse:
        runtime = RuntimeOptions()
        return self.set_cacertificate_name_with_options(request, runtime)

    async def set_cacertificate_name_async(
        self,
        request: main_models.SetCACertificateNameRequest,
    ) -> main_models.SetCACertificateNameResponse:
        runtime = RuntimeOptions()
        return await self.set_cacertificate_name_with_options_async(request, runtime)

    def set_domain_extension_attribute_with_options(
        self,
        request: main_models.SetDomainExtensionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainExtensionAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainExtensionAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_extension_attribute_with_options_async(
        self,
        request: main_models.SetDomainExtensionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDomainExtensionAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDomainExtensionAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDomainExtensionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_extension_attribute(
        self,
        request: main_models.SetDomainExtensionAttributeRequest,
    ) -> main_models.SetDomainExtensionAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_domain_extension_attribute_with_options(request, runtime)

    async def set_domain_extension_attribute_async(
        self,
        request: main_models.SetDomainExtensionAttributeRequest,
    ) -> main_models.SetDomainExtensionAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_domain_extension_attribute_with_options_async(request, runtime)

    def set_listener_access_control_status_with_options(
        self,
        request: main_models.SetListenerAccessControlStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetListenerAccessControlStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_control_status):
            query['AccessControlStatus'] = request.access_control_status
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetListenerAccessControlStatus',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetListenerAccessControlStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_listener_access_control_status_with_options_async(
        self,
        request: main_models.SetListenerAccessControlStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetListenerAccessControlStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_control_status):
            query['AccessControlStatus'] = request.access_control_status
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetListenerAccessControlStatus',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetListenerAccessControlStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_listener_access_control_status(
        self,
        request: main_models.SetListenerAccessControlStatusRequest,
    ) -> main_models.SetListenerAccessControlStatusResponse:
        runtime = RuntimeOptions()
        return self.set_listener_access_control_status_with_options(request, runtime)

    async def set_listener_access_control_status_async(
        self,
        request: main_models.SetListenerAccessControlStatusRequest,
    ) -> main_models.SetListenerAccessControlStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_listener_access_control_status_with_options_async(request, runtime)

    def set_load_balancer_delete_protection_with_options(
        self,
        request: main_models.SetLoadBalancerDeleteProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerDeleteProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerDeleteProtection',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerDeleteProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_delete_protection_with_options_async(
        self,
        request: main_models.SetLoadBalancerDeleteProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerDeleteProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerDeleteProtection',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerDeleteProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_delete_protection(
        self,
        request: main_models.SetLoadBalancerDeleteProtectionRequest,
    ) -> main_models.SetLoadBalancerDeleteProtectionResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_delete_protection_with_options(request, runtime)

    async def set_load_balancer_delete_protection_async(
        self,
        request: main_models.SetLoadBalancerDeleteProtectionRequest,
    ) -> main_models.SetLoadBalancerDeleteProtectionResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_delete_protection_with_options_async(request, runtime)

    def set_load_balancer_httplistener_attribute_with_options(
        self,
        request: main_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerHTTPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerHTTPListenerAttribute',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerHTTPListenerAttribute',
            version = '2014-05-15',
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

    def set_load_balancer_httpslistener_attribute_with_options(
        self,
        request: main_models.SetLoadBalancerHTTPSListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerHTTPSListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: main_models.SetLoadBalancerHTTPSListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not DaraCore.is_null(request.gzip):
            query['Gzip'] = request.gzip
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
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
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not DaraCore.is_null(request.xforwarded_for_client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for_client_src_port
        if not DaraCore.is_null(request.xforwarded_for_slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for_slbid
        if not DaraCore.is_null(request.xforwarded_for_slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for_slbip
        if not DaraCore.is_null(request.xforwarded_for_slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for_slbport
        if not DaraCore.is_null(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerHTTPSListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_httpslistener_attribute(
        self,
        request: main_models.SetLoadBalancerHTTPSListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_httpslistener_attribute_with_options(request, runtime)

    async def set_load_balancer_httpslistener_attribute_async(
        self,
        request: main_models.SetLoadBalancerHTTPSListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_httpslistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_modification_protection_with_options(
        self,
        request: main_models.SetLoadBalancerModificationProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerModificationProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not DaraCore.is_null(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
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
            action = 'SetLoadBalancerModificationProtection',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerModificationProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_modification_protection_with_options_async(
        self,
        request: main_models.SetLoadBalancerModificationProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerModificationProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not DaraCore.is_null(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
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
            action = 'SetLoadBalancerModificationProtection',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerModificationProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_modification_protection(
        self,
        request: main_models.SetLoadBalancerModificationProtectionRequest,
    ) -> main_models.SetLoadBalancerModificationProtectionResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_modification_protection_with_options(request, runtime)

    async def set_load_balancer_modification_protection_async(
        self,
        request: main_models.SetLoadBalancerModificationProtectionRequest,
    ) -> main_models.SetLoadBalancerModificationProtectionResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_modification_protection_with_options_async(request, runtime)

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
            action = 'SetLoadBalancerName',
            version = '2014-05-15',
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
            action = 'SetLoadBalancerName',
            version = '2014-05-15',
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
            action = 'SetLoadBalancerStatus',
            version = '2014-05-15',
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
            action = 'SetLoadBalancerStatus',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not DaraCore.is_null(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.syn_proxy):
            query['SynProxy'] = request.syn_proxy
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerTCPListenerAttribute',
            version = '2014-05-15',
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
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not DaraCore.is_null(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.syn_proxy):
            query['SynProxy'] = request.syn_proxy
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerTCPListenerAttribute',
            version = '2014-05-15',
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

    def set_load_balancer_udplistener_attribute_with_options(
        self,
        request: main_models.SetLoadBalancerUDPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerUDPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not DaraCore.is_null(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerUDPListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: main_models.SetLoadBalancerUDPListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoadBalancerUDPListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not DaraCore.is_null(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not DaraCore.is_null(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoadBalancerUDPListenerAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoadBalancerUDPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_udplistener_attribute(
        self,
        request: main_models.SetLoadBalancerUDPListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerUDPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_load_balancer_udplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_udplistener_attribute_async(
        self,
        request: main_models.SetLoadBalancerUDPListenerAttributeRequest,
    ) -> main_models.SetLoadBalancerUDPListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_load_balancer_udplistener_attribute_with_options_async(request, runtime)

    def set_rule_with_options(
        self,
        request: main_models.SetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_sync):
            query['ListenerSync'] = request.listener_sync
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
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRule',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_rule_with_options_async(
        self,
        request: main_models.SetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cookie):
            query['Cookie'] = request.cookie
        if not DaraCore.is_null(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not DaraCore.is_null(request.health_check):
            query['HealthCheck'] = request.health_check
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not DaraCore.is_null(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.listener_sync):
            query['ListenerSync'] = request.listener_sync
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
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not DaraCore.is_null(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRule',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_rule(
        self,
        request: main_models.SetRuleRequest,
    ) -> main_models.SetRuleResponse:
        runtime = RuntimeOptions()
        return self.set_rule_with_options(request, runtime)

    async def set_rule_async(
        self,
        request: main_models.SetRuleRequest,
    ) -> main_models.SetRuleResponse:
        runtime = RuntimeOptions()
        return await self.set_rule_with_options_async(request, runtime)

    def set_server_certificate_name_with_options(
        self,
        request: main_models.SetServerCertificateNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetServerCertificateNameResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetServerCertificateName',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetServerCertificateNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_server_certificate_name_with_options_async(
        self,
        request: main_models.SetServerCertificateNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetServerCertificateNameResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not DaraCore.is_null(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetServerCertificateName',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetServerCertificateNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_server_certificate_name(
        self,
        request: main_models.SetServerCertificateNameRequest,
    ) -> main_models.SetServerCertificateNameResponse:
        runtime = RuntimeOptions()
        return self.set_server_certificate_name_with_options(request, runtime)

    async def set_server_certificate_name_async(
        self,
        request: main_models.SetServerCertificateNameRequest,
    ) -> main_models.SetServerCertificateNameResponse:
        runtime = RuntimeOptions()
        return await self.set_server_certificate_name_with_options_async(request, runtime)

    def set_tlscipher_policy_attribute_with_options(
        self,
        request: main_models.SetTLSCipherPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTLSCipherPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
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
        if not DaraCore.is_null(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTLSCipherPolicyAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTLSCipherPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_tlscipher_policy_attribute_with_options_async(
        self,
        request: main_models.SetTLSCipherPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTLSCipherPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
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
        if not DaraCore.is_null(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTLSCipherPolicyAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTLSCipherPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_tlscipher_policy_attribute(
        self,
        request: main_models.SetTLSCipherPolicyAttributeRequest,
    ) -> main_models.SetTLSCipherPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_tlscipher_policy_attribute_with_options(request, runtime)

    async def set_tlscipher_policy_attribute_async(
        self,
        request: main_models.SetTLSCipherPolicyAttributeRequest,
    ) -> main_models.SetTLSCipherPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_tlscipher_policy_attribute_with_options_async(request, runtime)

    def set_vserver_group_attribute_with_options(
        self,
        request: main_models.SetVServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVServerGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVServerGroupAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vserver_group_attribute_with_options_async(
        self,
        request: main_models.SetVServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVServerGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_servers):
            query['BackendServers'] = request.backend_servers
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
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVServerGroupAttribute',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vserver_group_attribute(
        self,
        request: main_models.SetVServerGroupAttributeRequest,
    ) -> main_models.SetVServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.set_vserver_group_attribute_with_options(request, runtime)

    async def set_vserver_group_attribute_async(
        self,
        request: main_models.SetVServerGroupAttributeRequest,
    ) -> main_models.SetVServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.set_vserver_group_attribute_with_options_async(request, runtime)

    def start_load_balancer_listener_with_options(
        self,
        request: main_models.StartLoadBalancerListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartLoadBalancerListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartLoadBalancerListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_load_balancer_listener_with_options_async(
        self,
        request: main_models.StartLoadBalancerListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartLoadBalancerListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartLoadBalancerListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_load_balancer_listener(
        self,
        request: main_models.StartLoadBalancerListenerRequest,
    ) -> main_models.StartLoadBalancerListenerResponse:
        runtime = RuntimeOptions()
        return self.start_load_balancer_listener_with_options(request, runtime)

    async def start_load_balancer_listener_async(
        self,
        request: main_models.StartLoadBalancerListenerRequest,
    ) -> main_models.StartLoadBalancerListenerResponse:
        runtime = RuntimeOptions()
        return await self.start_load_balancer_listener_with_options_async(request, runtime)

    def stop_load_balancer_listener_with_options(
        self,
        request: main_models.StopLoadBalancerListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopLoadBalancerListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLoadBalancerListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_load_balancer_listener_with_options_async(
        self,
        request: main_models.StopLoadBalancerListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopLoadBalancerListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLoadBalancerListener',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_load_balancer_listener(
        self,
        request: main_models.StopLoadBalancerListenerRequest,
    ) -> main_models.StopLoadBalancerListenerResponse:
        runtime = RuntimeOptions()
        return self.stop_load_balancer_listener_with_options(request, runtime)

    async def stop_load_balancer_listener_async(
        self,
        request: main_models.StopLoadBalancerListenerRequest,
    ) -> main_models.StopLoadBalancerListenerResponse:
        runtime = RuntimeOptions()
        return await self.stop_load_balancer_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upload_cacertificate_with_options(
        self,
        request: main_models.UploadCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate):
            query['CACertificate'] = request.cacertificate
        if not DaraCore.is_null(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadCACertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_cacertificate_with_options_async(
        self,
        request: main_models.UploadCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cacertificate):
            query['CACertificate'] = request.cacertificate
        if not DaraCore.is_null(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadCACertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_cacertificate(
        self,
        request: main_models.UploadCACertificateRequest,
    ) -> main_models.UploadCACertificateResponse:
        runtime = RuntimeOptions()
        return self.upload_cacertificate_with_options(request, runtime)

    async def upload_cacertificate_async(
        self,
        request: main_models.UploadCACertificateRequest,
    ) -> main_models.UploadCACertificateResponse:
        runtime = RuntimeOptions()
        return await self.upload_cacertificate_with_options_async(request, runtime)

    def upload_server_certificate_with_options(
        self,
        request: main_models.UploadServerCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadServerCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_cloud_certificate_id):
            query['AliCloudCertificateId'] = request.ali_cloud_certificate_id
        if not DaraCore.is_null(request.ali_cloud_certificate_name):
            query['AliCloudCertificateName'] = request.ali_cloud_certificate_name
        if not DaraCore.is_null(request.ali_cloud_certificate_region_id):
            query['AliCloudCertificateRegionId'] = request.ali_cloud_certificate_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not DaraCore.is_null(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadServerCertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_server_certificate_with_options_async(
        self,
        request: main_models.UploadServerCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadServerCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_cloud_certificate_id):
            query['AliCloudCertificateId'] = request.ali_cloud_certificate_id
        if not DaraCore.is_null(request.ali_cloud_certificate_name):
            query['AliCloudCertificateName'] = request.ali_cloud_certificate_name
        if not DaraCore.is_null(request.ali_cloud_certificate_region_id):
            query['AliCloudCertificateRegionId'] = request.ali_cloud_certificate_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not DaraCore.is_null(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadServerCertificate',
            version = '2014-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_server_certificate(
        self,
        request: main_models.UploadServerCertificateRequest,
    ) -> main_models.UploadServerCertificateResponse:
        runtime = RuntimeOptions()
        return self.upload_server_certificate_with_options(request, runtime)

    async def upload_server_certificate_async(
        self,
        request: main_models.UploadServerCertificateRequest,
    ) -> main_models.UploadServerCertificateResponse:
        runtime = RuntimeOptions()
        return await self.upload_server_certificate_with_options_async(request, runtime)
