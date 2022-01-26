# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_slb20140515 import models as slb_20140515_models
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
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAccessControlListEntry',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_access_control_list_entry_with_options_async(
        self,
        request: slb_20140515_models.AddAccessControlListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddAccessControlListEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAccessControlListEntry',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddAccessControlListEntryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.AddBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddBackendServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddListenerWhiteListItem',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddListenerWhiteListItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_listener_white_list_item_with_options_async(
        self,
        request: slb_20140515_models.AddListenerWhiteListItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddListenerWhiteListItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddListenerWhiteListItem',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddListenerWhiteListItemResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: slb_20140515_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vserver_group_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.AddVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.AddVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddVServerGroupBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessControlList',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_control_list_with_options_async(
        self,
        request: slb_20140515_models.CreateAccessControlListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateAccessControlListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessControlList',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainExtension',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateDomainExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_extension_with_options_async(
        self,
        request: slb_20140515_models.CreateDomainExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateDomainExtensionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainExtension',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateDomainExtensionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_httplistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPListenerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPSListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_httpslistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerHTTPSListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPSListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not UtilClient.is_unset(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerTCPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerTCPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_tcplistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerTCPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerTCPListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not UtilClient.is_unset(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerTCPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerTCPListenerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerUDPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerUDPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_udplistener_with_options_async(
        self,
        request: slb_20140515_models.CreateLoadBalancerUDPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateLoadBalancerUDPListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerUDPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerUDPListenerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_backend_servers):
            query['MasterSlaveBackendServers'] = request.master_slave_backend_servers
        if not UtilClient.is_unset(request.master_slave_server_group_name):
            query['MasterSlaveServerGroupName'] = request.master_slave_server_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMasterSlaveServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateMasterSlaveServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_master_slave_server_group_with_options_async(
        self,
        request: slb_20140515_models.CreateMasterSlaveServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateMasterSlaveServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_backend_servers):
            query['MasterSlaveBackendServers'] = request.master_slave_backend_servers
        if not UtilClient.is_unset(request.master_slave_server_group_name):
            query['MasterSlaveServerGroupName'] = request.master_slave_server_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMasterSlaveServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateMasterSlaveServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        request: slb_20140515_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTLSCipherPolicy',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateTLSCipherPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tlscipher_policy_with_options_async(
        self,
        request: slb_20140515_models.CreateTLSCipherPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateTLSCipherPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTLSCipherPolicy',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateTLSCipherPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateVServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vserver_group_with_options_async(
        self,
        request: slb_20140515_models.CreateVServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.CreateVServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateVServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessControlList',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_control_list_with_options_async(
        self,
        request: slb_20140515_models.DeleteAccessControlListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteAccessControlListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessControlList',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCACertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cacertificate_with_options_async(
        self,
        request: slb_20140515_models.DeleteCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCACertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainExtension',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteDomainExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_extension_with_options_async(
        self,
        request: slb_20140515_models.DeleteDomainExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteDomainExtensionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainExtension',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteDomainExtensionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: slb_20140515_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_listener_with_options_async(
        self,
        request: slb_20140515_models.DeleteLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMasterSlaveServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteMasterSlaveServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_master_slave_server_group_with_options_async(
        self,
        request: slb_20140515_models.DeleteMasterSlaveServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteMasterSlaveServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMasterSlaveServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteMasterSlaveServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rules_with_options_async(
        self,
        request: slb_20140515_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServerCertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_server_certificate_with_options_async(
        self,
        request: slb_20140515_models.DeleteServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteServerCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServerCertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTLSCipherPolicy',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteTLSCipherPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tlscipher_policy_with_options_async(
        self,
        request: slb_20140515_models.DeleteTLSCipherPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteTLSCipherPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTLSCipherPolicy',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteTLSCipherPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteVServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vserver_group_with_options_async(
        self,
        request: slb_20140515_models.DeleteVServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DeleteVServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteVServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_entry_comment):
            query['AclEntryComment'] = request.acl_entry_comment
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlListAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_list_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeAccessControlListAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAccessControlListAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entry_comment):
            query['AclEntryComment'] = request.acl_entry_comment
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlListAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlLists',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_lists_with_options_async(
        self,
        request: slb_20140515_models.DescribeAccessControlListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAccessControlListsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlLists',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: slb_20140515_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificates',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeCACertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificates_with_options_async(
        self,
        request: slb_20140515_models.DescribeCACertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeCACertificatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificates',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeCACertificatesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainExtensionAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_extension_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeDomainExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeDomainExtensionAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainExtensionAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainExtensions',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_extensions_with_options_async(
        self,
        request: slb_20140515_models.DescribeDomainExtensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeDomainExtensionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainExtensions',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_status_with_options_async(
        self,
        request: slb_20140515_models.DescribeHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeListenerAccessControlAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeListenerAccessControlAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_listener_access_control_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeListenerAccessControlAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeListenerAccessControlAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeListenerAccessControlAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeListenerAccessControlAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPSListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPSListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_load_balancer_listeners_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancerListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerListenersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerListeners',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_listeners_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerListenersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerListeners',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_listeners(
        self,
        request: slb_20140515_models.DescribeLoadBalancerListenersRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerListenersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_listeners_with_options(request, runtime)

    async def describe_load_balancer_listeners_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerListenersRequest,
    ) -> slb_20140515_models.DescribeLoadBalancerListenersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_listeners_with_options_async(request, runtime)

    def describe_load_balancer_tcplistener_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerTCPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerTCPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerUDPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerUDPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_load_balancers_with_options(
        self,
        request: slb_20140515_models.DescribeLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        if not UtilClient.is_unset(request.server_intranet_address):
            query['ServerIntranetAddress'] = request.server_intranet_address
        if not UtilClient.is_unset(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancers_with_options_async(
        self,
        request: slb_20140515_models.DescribeLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        if not UtilClient.is_unset(request.server_intranet_address):
            query['ServerIntranetAddress'] = request.server_intranet_address
        if not UtilClient.is_unset(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_master_slave_server_group_attribute_with_options(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMasterSlaveServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_master_slave_server_group_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMasterSlaveServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMasterSlaveServerGroups',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_master_slave_server_groups_with_options_async(
        self,
        request: slb_20140515_models.DescribeMasterSlaveServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeMasterSlaveServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMasterSlaveServerGroups',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: slb_20140515_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRuleAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: slb_20140515_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerCertificates',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeServerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_server_certificates_with_options_async(
        self,
        request: slb_20140515_models.DescribeServerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeServerCertificatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerCertificates',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeServerCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.distinct_key):
            query['DistinctKey'] = request.distinct_key
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: slb_20140515_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.distinct_key):
            query['DistinctKey'] = request.distinct_key
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vserver_group_attribute_with_options_async(
        self,
        request: slb_20140515_models.DescribeVServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeVServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVServerGroups',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vserver_groups_with_options_async(
        self,
        request: slb_20140515_models.DescribeVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeVServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVServerGroups',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: slb_20140515_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_tlscipher_policies_with_options(
        self,
        request: slb_20140515_models.ListTLSCipherPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTLSCipherPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTLSCipherPolicies',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTLSCipherPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tlscipher_policies_with_options_async(
        self,
        request: slb_20140515_models.ListTLSCipherPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTLSCipherPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTLSCipherPolicies',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTLSCipherPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_tag_resources_with_options(
        self,
        request: slb_20140515_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: slb_20140515_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_load_balancer_instance_spec_with_options(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerInstanceSpec',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_instance_spec_with_options_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerInstanceSpec',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerInternetSpec',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInternetSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_internet_spec_with_options_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerInternetSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerInternetSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerInternetSpec',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInternetSpecResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerPayType',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_pay_type_with_options_async(
        self,
        request: slb_20140515_models.ModifyLoadBalancerPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyLoadBalancerPayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerPayType',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerPayTypeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.new_backend_servers):
            query['NewBackendServers'] = request.new_backend_servers
        if not UtilClient.is_unset(request.old_backend_servers):
            query['OldBackendServers'] = request.old_backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vserver_group_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.ModifyVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.ModifyVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_backend_servers):
            query['NewBackendServers'] = request.new_backend_servers
        if not UtilClient.is_unset(request.old_backend_servers):
            query['OldBackendServers'] = request.old_backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyVServerGroupBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessControlListEntry',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_control_list_entry_with_options_async(
        self,
        request: slb_20140515_models.RemoveAccessControlListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveAccessControlListEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessControlListEntry',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveAccessControlListEntryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.RemoveBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveBackendServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveListenerWhiteListItem',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveListenerWhiteListItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_listener_white_list_item_with_options_async(
        self,
        request: slb_20140515_models.RemoveListenerWhiteListItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveListenerWhiteListItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveListenerWhiteListItem',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveListenerWhiteListItemResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: slb_20140515_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vserver_group_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.RemoveVServerGroupBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.RemoveVServerGroupBackendServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveVServerGroupBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessControlListAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_control_list_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetAccessControlListAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetAccessControlListAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessControlListAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetAccessControlListAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_backend_servers_with_options_async(
        self,
        request: slb_20140515_models.SetBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetBackendServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCACertificateName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetCACertificateNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cacertificate_name_with_options_async(
        self,
        request: slb_20140515_models.SetCACertificateNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetCACertificateNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCACertificateName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetCACertificateNameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainExtensionAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetDomainExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_extension_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetDomainExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetDomainExtensionAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainExtensionAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetDomainExtensionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.access_control_status):
            query['AccessControlStatus'] = request.access_control_status
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetListenerAccessControlStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetListenerAccessControlStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_listener_access_control_status_with_options_async(
        self,
        request: slb_20140515_models.SetListenerAccessControlStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetListenerAccessControlStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_control_status):
            query['AccessControlStatus'] = request.access_control_status
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetListenerAccessControlStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetListenerAccessControlStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerDeleteProtection',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerDeleteProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_delete_protection_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerDeleteProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerDeleteProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerDeleteProtection',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerDeleteProtectionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPSListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPSListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerModificationProtection',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerModificationProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_modification_protection_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerModificationProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerModificationProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerModificationProtection',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerModificationProtectionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_name_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerNameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_status_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not UtilClient.is_unset(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.syn_proxy):
            query['SynProxy'] = request.syn_proxy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerTCPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not UtilClient.is_unset(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.syn_proxy):
            query['SynProxy'] = request.syn_proxy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerTCPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerUDPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerUDPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_sync):
            query['ListenerSync'] = request.listener_sync
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRule',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_rule_with_options_async(
        self,
        request: slb_20140515_models.SetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_sync):
            query['ListenerSync'] = request.listener_sync
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRule',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetServerCertificateName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetServerCertificateNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_server_certificate_name_with_options_async(
        self,
        request: slb_20140515_models.SetServerCertificateNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetServerCertificateNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetServerCertificateName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetServerCertificateNameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTLSCipherPolicyAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetTLSCipherPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_tlscipher_policy_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetTLSCipherPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetTLSCipherPolicyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTLSCipherPolicyAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetTLSCipherPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetVServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vserver_group_attribute_with_options_async(
        self,
        request: slb_20140515_models.SetVServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.SetVServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetVServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.StartLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_load_balancer_listener_with_options_async(
        self,
        request: slb_20140515_models.StartLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.StartLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.StartLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.StopLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_load_balancer_listener_with_options_async(
        self,
        request: slb_20140515_models.StopLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.StopLoadBalancerListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.StopLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: slb_20140515_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: slb_20140515_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cacertificate):
            query['CACertificate'] = request.cacertificate
        if not UtilClient.is_unset(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCACertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_cacertificate_with_options_async(
        self,
        request: slb_20140515_models.UploadCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UploadCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate):
            query['CACertificate'] = request.cacertificate
        if not UtilClient.is_unset(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCACertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ali_cloud_certificate_id):
            query['AliCloudCertificateId'] = request.ali_cloud_certificate_id
        if not UtilClient.is_unset(request.ali_cloud_certificate_name):
            query['AliCloudCertificateName'] = request.ali_cloud_certificate_name
        if not UtilClient.is_unset(request.ali_cloud_certificate_region_id):
            query['AliCloudCertificateRegionId'] = request.ali_cloud_certificate_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not UtilClient.is_unset(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadServerCertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_server_certificate_with_options_async(
        self,
        request: slb_20140515_models.UploadServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> slb_20140515_models.UploadServerCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_cloud_certificate_id):
            query['AliCloudCertificateId'] = request.ali_cloud_certificate_id
        if not UtilClient.is_unset(request.ali_cloud_certificate_name):
            query['AliCloudCertificateName'] = request.ali_cloud_certificate_name
        if not UtilClient.is_unset(request.ali_cloud_certificate_region_id):
            query['AliCloudCertificateRegionId'] = request.ali_cloud_certificate_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not UtilClient.is_unset(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadServerCertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
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
