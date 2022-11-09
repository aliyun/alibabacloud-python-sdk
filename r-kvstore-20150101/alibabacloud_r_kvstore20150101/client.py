# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_r_kvstore20150101 import models as r_kvstore_20150101_models
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
            'cn-qingdao': 'r-kvstore.aliyuncs.com',
            'cn-beijing': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou': 'r-kvstore.aliyuncs.com',
            'cn-shanghai': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen': 'r-kvstore.aliyuncs.com',
            'cn-heyuan': 'r-kvstore.aliyuncs.com',
            'ap-southeast-1': 'r-kvstore.aliyuncs.com',
            'us-west-1': 'r-kvstore.aliyuncs.com',
            'us-east-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-finance': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-north-2-gov-1': 'r-kvstore.aliyuncs.com',
            'ap-northeast-2-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-gov-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-nu16-b01': 'r-kvstore.aliyuncs.com',
            'cn-edge-1': 'r-kvstore.aliyuncs.com',
            'cn-fujian': 'r-kvstore.aliyuncs.com',
            'cn-haidian-cm12-c01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-test-306': 'r-kvstore.aliyuncs.com',
            'cn-hongkong-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'r-kvstore.aliyuncs.com',
            'cn-qingdao-nebula': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et15-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et2-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-inner': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-inner': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'r-kvstore.aliyuncs.com',
            'cn-wuhan': 'r-kvstore.aliyuncs.com',
            'cn-wulanchabu': 'r-kvstore.aliyuncs.com',
            'cn-yushanfang': 'r-kvstore.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'r-kvstore.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'r-kvstore.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'r-kvstore.aliyuncs.com',
            'eu-west-1-oxs': 'r-kvstore.aliyuncs.com',
            'rus-west-1-pop': 'r-kvstore.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('r-kvstore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_sharding_node_with_options(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AddShardingNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sharding_node_with_options_async(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AddShardingNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sharding_node(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sharding_node_with_options(request, runtime)

    async def add_sharding_node_async(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sharding_node_with_options_async(request, runtime)

    def allocate_direct_connection_with_options(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateDirectConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_direct_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateDirectConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_direct_connection(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_direct_connection_with_options(request, runtime)

    async def allocate_direct_connection_async(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_direct_connection_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def check_cloud_resource_authorized_with_options(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: r_kvstore_20150101_models.CheckCloudResourceAuthorizedRequest,
    ) -> r_kvstore_20150101_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_cache_analysis_task_with_options(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cache_analysis_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cache_analysis_task(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_task_with_options(request, runtime)

    async def create_cache_analysis_task_async(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cache_analysis_task_with_options_async(request, runtime)

    def create_global_distribute_cache_with_options(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.seed_sub_instance_id):
            query['SeedSubInstanceId'] = request.seed_sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_distribute_cache_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.seed_sub_instance_id):
            query['SeedSubInstanceId'] = request.seed_sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_distribute_cache(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_global_distribute_cache_with_options(request, runtime)

    async def create_global_distribute_cache_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_global_distribute_cache_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instances_with_options(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rebuild_instance):
            query['RebuildInstance'] = request.rebuild_instance
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instances_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rebuild_instance):
            query['RebuildInstance'] = request.rebuild_instance
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instances(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instances_with_options(request, runtime)

    async def create_instances_async(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instances_with_options_async(request, runtime)

    def create_tair_instance_with_options(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.shard_type):
            query['ShardType'] = request.shard_type
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTairInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateTairInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tair_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.shard_type):
            query['ShardType'] = request.shard_type
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTairInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateTairInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tair_instance(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tair_instance_with_options(request, runtime)

    async def create_tair_instance_async(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tair_instance_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_sharding_node_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteShardingNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sharding_node_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteShardingNode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteShardingNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sharding_node(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sharding_node_with_options(request, runtime)

    async def delete_sharding_node_async(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sharding_node_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_task_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_with_options(request, runtime)

    async def describe_active_operation_task_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_with_options_async(request, runtime)

    def describe_audit_log_config_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_config(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_config_with_options(request, runtime)

    async def describe_audit_log_config_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_config_with_options_async(request, runtime)

    def describe_audit_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_records(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    async def describe_audit_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_records_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_mode):
            query['JobMode'] = request.job_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_mode):
            query['JobMode'] = request.job_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_aof):
            query['NeedAof'] = request.need_aof
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_aof):
            query['NeedAof'] = request.need_aof
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cache_analysis_report_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_type):
            query['AnalysisType'] = request.analysis_type
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisReport',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_report_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_type):
            query['AnalysisType'] = request.analysis_type
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisReport',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cache_analysis_report(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_with_options(request, runtime)

    async def describe_cache_analysis_report_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_report_with_options_async(request, runtime)

    def describe_cache_analysis_report_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisReportList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_report_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisReportList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cache_analysis_report_list(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_list_with_options(request, runtime)

    async def describe_cache_analysis_report_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_report_list_with_options_async(request, runtime)

    def describe_cluster_member_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterMemberInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterMemberInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_member_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterMemberInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterMemberInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_member_info(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_member_info_with_options(request, runtime)

    async def describe_cluster_member_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_member_info_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dedicated_cluster_instance_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_net_type):
            query['InstanceNetType'] = request.instance_net_type
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedClusterInstanceList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_cluster_instance_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_net_type):
            query['InstanceNetType'] = request.instance_net_type
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedClusterInstanceList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_cluster_instance_list(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_instance_list_with_options(request, runtime)

    async def describe_dedicated_cluster_instance_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_cluster_instance_list_with_options_async(request, runtime)

    def describe_encryption_key_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEncryptionKey',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_encryption_key_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEncryptionKey',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_encryption_key(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_encryption_key_with_options(request, runtime)

    async def describe_encryption_key_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_encryption_key_with_options_async(request, runtime)

    def describe_encryption_key_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEncryptionKeyList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_encryption_key_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEncryptionKeyList',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_encryption_key_list(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_encryption_key_list_with_options(request, runtime)

    async def describe_encryption_key_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeEncryptionKeyListRequest,
    ) -> r_kvstore_20150101_models.DescribeEncryptionKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_encryption_key_list_with_options_async(request, runtime)

    def describe_engine_version_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEngineVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_engine_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEngineVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_engine_version(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_engine_version_with_options(request, runtime)

    async def describe_engine_version_async(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_engine_version_with_options_async(request, runtime)

    def describe_global_distribute_cache_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sub_instance_id):
            query['SubInstanceId'] = request.sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_distribute_cache_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_instance_id):
            query['GlobalInstanceId'] = request.global_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sub_instance_id):
            query['SubInstanceId'] = request.sub_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDistributeCache',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_distribute_cache(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_global_distribute_cache_with_options(request, runtime)

    async def describe_global_distribute_cache_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_distribute_cache_with_options_async(request, runtime)

    def describe_history_monitor_values_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval_for_history):
            query['IntervalForHistory'] = request.interval_for_history
        if not UtilClient.is_unset(request.monitor_keys):
            query['MonitorKeys'] = request.monitor_keys
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryMonitorValues',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_monitor_values_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval_for_history):
            query['IntervalForHistory'] = request.interval_for_history
        if not UtilClient.is_unset(request.monitor_keys):
            query['MonitorKeys'] = request.monitor_keys
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryMonitorValues',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_monitor_values(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_monitor_values_with_options(request, runtime)

    async def describe_history_monitor_values_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_monitor_values_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_instance_config_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_config(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_config_with_options(request, runtime)

    async def describe_instance_config_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_config_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sslwith_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ssl(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_instance_tdestatus_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTDEStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_tdestatus_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTDEStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_tdestatus(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tdestatus_with_options(request, runtime)

    async def describe_instance_tdestatus_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceTDEStatusRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceTDEStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_tdestatus_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.global_instance):
            query['GlobalInstance'] = request.global_instance
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instances_overview_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancesOverview',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_overview_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture_type):
            query['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.edition_type):
            query['EditionType'] = request.edition_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancesOverview',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances_overview(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_overview_with_options(request, runtime)

    async def describe_instances_overview_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesOverviewRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_overview_with_options_async(request, runtime)

    def describe_intranet_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeIntranetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intranet_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeIntranetAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intranet_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_intranet_attribute_with_options(request, runtime)

    async def describe_intranet_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_intranet_attribute_with_options_async(request, runtime)

    def describe_logic_instance_topology_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogicInstanceTopology',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_logic_instance_topology_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogicInstanceTopology',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_logic_instance_topology(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_logic_instance_topology_with_options(request, runtime)

    async def describe_logic_instance_topology_async(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_logic_instance_topology_with_options_async(request, runtime)

    def describe_monitor_items_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorItems',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeMonitorItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_items_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorItems',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeMonitorItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_items(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_items_with_options(request, runtime)

    async def describe_monitor_items_async(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_items_with_options_async(request, runtime)

    def describe_parameter_modification_history_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_name):
            query['ParameterName'] = request.parameter_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterModificationHistory',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_modification_history_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_name):
            query['ParameterName'] = request.parameter_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterModificationHistory',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_modification_history(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_modification_history_with_options(request, runtime)

    async def describe_parameter_modification_history_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterModificationHistoryRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterModificationHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_modification_history_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_role_zone_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoleZoneInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRoleZoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_role_zone_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoleZoneInfo',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRoleZoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_role_zone_info(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    async def describe_role_zone_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_role_zone_info_with_options_async(request, runtime)

    def describe_running_log_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRunningLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_running_log_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRunningLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_running_log_records(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    async def describe_running_log_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_running_log_records_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ips(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.slow_log_record_type):
            query['SlowLogRecordType'] = request.slow_log_record_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.slow_log_record_type):
            query['SlowLogRecordType'] = request.slow_log_record_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def enable_additional_bandwidth_with_options(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.EnableAdditionalBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_additional_bandwidth_with_options_async(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.EnableAdditionalBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_additional_bandwidth(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_additional_bandwidth_with_options(request, runtime)

    async def enable_additional_bandwidth_async(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_additional_bandwidth_with_options_async(request, runtime)

    def flush_expire_keys_with_options(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlushExpireKeys',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushExpireKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def flush_expire_keys_with_options_async(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlushExpireKeys',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushExpireKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flush_expire_keys(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.flush_expire_keys_with_options(request, runtime)

    async def flush_expire_keys_async(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.flush_expire_keys_with_options_async(request, runtime)

    def flush_instance_with_options(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlushInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def flush_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlushInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flush_instance(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.flush_instance_with_options(request, runtime)

    async def flush_instance_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.flush_instance_with_options_async(request, runtime)

    def grant_account_privilege_with_options(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.GrantAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_account_privilege_with_options_async(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.GrantAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_account_privilege(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    async def grant_account_privilege_async(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_account_privilege_with_options_async(request, runtime)

    def initialize_kvstore_permission_with_options(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeKvstorePermission',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.InitializeKvstorePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_kvstore_permission_with_options_async(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeKvstorePermission',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.InitializeKvstorePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_kvstore_permission(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_kvstore_permission_with_options(request, runtime)

    async def initialize_kvstore_permission_async(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_kvstore_permission_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.MigrateToOtherZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_password_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        if not UtilClient.is_unset(request.old_account_password):
            query['OldAccountPassword'] = request.old_account_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_password_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        if not UtilClient.is_unset(request.old_account_password):
            query['OldAccountPassword'] = request.old_account_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_password(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    async def modify_account_password_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_password_with_options_async(request, runtime)

    def modify_active_operation_task_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTask',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_task(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_task_with_options(request, runtime)

    async def modify_active_operation_task_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_task_with_options_async(request, runtime)

    def modify_audit_log_config_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_audit):
            query['DbAudit'] = request.db_audit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_audit):
            query['DbAudit'] = request.db_audit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_config(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    async def modify_audit_log_config_async(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_config_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.iptype):
            query['IPType'] = request.iptype
        if not UtilClient.is_unset(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_release_protection):
            query['InstanceReleaseProtection'] = request.instance_release_protection
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_release_protection):
            query['InstanceReleaseProtection'] = request.instance_release_protection
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_config_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_config_with_options(request, runtime)

    async def modify_instance_config_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_config_with_options_async(request, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMaintainTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMaintainTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    async def modify_instance_maintain_time_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintain_time_with_options_async(request, runtime)

    def modify_instance_major_version_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMajorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_major_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMajorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_major_version(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_major_version_with_options(request, runtime)

    async def modify_instance_major_version_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_major_version_with_options_async(request, runtime)

    def modify_instance_minor_version_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minorversion):
            query['Minorversion'] = request.minorversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMinorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_minor_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.minorversion):
            query['Minorversion'] = request.minorversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMinorVersion',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_minor_version(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_minor_version_with_options(request, runtime)

    async def modify_instance_minor_version_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_minor_version_with_options_async(request, runtime)

    def modify_instance_net_expire_time_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceNetExpireTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_net_expire_time_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceNetExpireTime',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_net_expire_time(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_net_expire_time_with_options(request, runtime)

    async def modify_instance_net_expire_time_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_net_expire_time_with_options_async(request, runtime)

    def modify_instance_sslwith_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_sslwith_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ssl(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    async def modify_instance_ssl_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_sslwith_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_only_count):
            query['ReadOnlyCount'] = request.read_only_count
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.shard_count):
            query['ShardCount'] = request.shard_count
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_spec(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_tdewith_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_name):
            query['EncryptionName'] = request.encryption_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTDE',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_tdewith_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_name):
            query['EncryptionName'] = request.encryption_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTDE',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_tde(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_tdewith_options(request, runtime)

    async def modify_instance_tde_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceTDERequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_tdewith_options_async(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAuthMode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vpc_auth_mode_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAuthMode',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vpc_auth_mode(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    async def modify_instance_vpc_auth_mode_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_auth_mode_with_options_async(request, runtime)

    def modify_intranet_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.band_width):
            query['BandWidth'] = request.band_width
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyIntranetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_intranet_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.band_width):
            query['BandWidth'] = request.band_width
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIntranetAttribute',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyIntranetAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_intranet_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_intranet_attribute_with_options(request, runtime)

    async def modify_intranet_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_intranet_attribute_with_options_async(request, runtime)

    def modify_resource_group_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyResourceGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_group_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyResourceGroup',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_group(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    async def modify_resource_group_async(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_group_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not UtilClient.is_unset(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not UtilClient.is_unset(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def release_direct_connection_with_options(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseDirectConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_direct_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseDirectConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseDirectConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_direct_connection(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_direct_connection_with_options(request, runtime)

    async def release_direct_connection_async(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_direct_connection_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def remove_sub_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSubInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RemoveSubInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_sub_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSubInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RemoveSubInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_sub_instance(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_sub_instance_with_options(request, runtime)

    async def remove_sub_instance_async(
        self,
        request: r_kvstore_20150101_models.RemoveSubInstanceRequest,
    ) -> r_kvstore_20150101_models.RemoveSubInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_sub_instance_with_options_async(request, runtime)

    def renew_additional_bandwidth_with_options(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewAdditionalBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_additional_bandwidth_with_options_async(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_time_length):
            query['OrderTimeLength'] = request.order_time_length
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAdditionalBandwidth',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewAdditionalBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_additional_bandwidth(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_additional_bandwidth_with_options(request, runtime)

    async def renew_additional_bandwidth_async(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_additional_bandwidth_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.upgrade_minor_version):
            query['UpgradeMinorVersion'] = request.upgrade_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.upgrade_minor_version):
            query['UpgradeMinorVersion'] = request.upgrade_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def restore_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestoreInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreInstance',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestoreInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_instance(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_instance_with_options(request, runtime)

    async def restore_instance_async(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_instance_with_options_async(request, runtime)

    def switch_instance_hawith_options(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchInstanceHA',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_instance_hawith_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchInstanceHA',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_instance_ha(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_instance_hawith_options(request, runtime)

    async def switch_instance_ha_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_instance_hawith_options_async(request, runtime)

    def switch_instance_proxy_with_options(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchInstanceProxy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_instance_proxy_with_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchInstanceProxy',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_instance_proxy(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_instance_proxy_with_options(request, runtime)

    async def switch_instance_proxy_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_instance_proxy_with_options_async(request, runtime)

    def switch_network_with_options(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_network_type):
            query['TargetNetworkType'] = request.target_network_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchNetwork',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_network_with_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_network_type):
            query['TargetNetworkType'] = request.target_network_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchNetwork',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_network(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_network_with_options(request, runtime)

    async def switch_network_async(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_network_with_options_async(request, runtime)

    def sync_dts_status_with_options(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncDtsStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SyncDtsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_dts_status_with_options_async(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncDtsStatus',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SyncDtsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_dts_status(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_dts_status_with_options(request, runtime)

    async def sync_dts_status_async(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_dts_status_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transform_instance_charge_type_with_options(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformInstanceChargeType',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_instance_charge_type_with_options_async(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformInstanceChargeType',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_instance_charge_type(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_instance_charge_type_with_options(request, runtime)

    async def transform_instance_charge_type_async(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_instance_charge_type_with_options_async(request, runtime)

    def transform_to_pre_paid_with_options(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformToPrePaid',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformToPrePaidResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_to_pre_paid_with_options_async(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformToPrePaid',
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformToPrePaidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_to_pre_paid(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    async def transform_to_pre_paid_async(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_to_pre_paid_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
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
            version='2015-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
