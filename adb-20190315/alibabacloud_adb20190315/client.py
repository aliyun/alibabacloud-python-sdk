# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_adb20190315 import models as main_models
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
            'cn-qingdao': 'adb.aliyuncs.com',
            'cn-beijing': 'adb.aliyuncs.com',
            'cn-hangzhou': 'adb.aliyuncs.com',
            'cn-shanghai': 'adb.aliyuncs.com',
            'cn-shenzhen': 'adb.aliyuncs.com',
            'cn-hongkong': 'adb.aliyuncs.com',
            'ap-southeast-1': 'adb.aliyuncs.com',
            'us-west-1': 'adb.aliyuncs.com',
            'us-east-1': 'adb.aliyuncs.com',
            'cn-hangzhou-finance': 'adb.aliyuncs.com',
            'cn-north-2-gov-1': 'adb.aliyuncs.com',
            'ap-northeast-2-pop': 'adb.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'adb.aliyuncs.com',
            'cn-beijing-finance-pop': 'adb.aliyuncs.com',
            'cn-beijing-gov-1': 'adb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'adb.aliyuncs.com',
            'cn-edge-1': 'adb.aliyuncs.com',
            'cn-fujian': 'adb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'adb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'adb.aliyuncs.com',
            'cn-hangzhou-test-306': 'adb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'adb.aliyuncs.com',
            'cn-qingdao-nebula': 'adb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'adb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'adb.aliyuncs.com',
            'cn-shanghai-finance-1': 'adb.aliyuncs.com',
            'cn-shanghai-inner': 'adb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'adb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'adb.aliyuncs.com',
            'cn-shenzhen-inner': 'adb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'adb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'adb.aliyuncs.com',
            'cn-wuhan': 'adb.aliyuncs.com',
            'cn-yushanfang': 'adb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'adb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'adb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'adb.aliyuncs.com',
            'eu-west-1-oxs': 'adb.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'adb.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'adb.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('adb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_cluster_public_connection_with_options(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateClusterPublicConnection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateClusterPublicConnection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def apply_advice_by_id_with_options(
        self,
        request: main_models.ApplyAdviceByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAdviceByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not DaraCore.is_null(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAdviceById',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAdviceByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_advice_by_id_with_options_async(
        self,
        request: main_models.ApplyAdviceByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAdviceByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not DaraCore.is_null(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not DaraCore.is_null(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not DaraCore.is_null(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAdviceById',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAdviceByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_advice_by_id(
        self,
        request: main_models.ApplyAdviceByIdRequest,
    ) -> main_models.ApplyAdviceByIdResponse:
        runtime = RuntimeOptions()
        return self.apply_advice_by_id_with_options(request, runtime)

    async def apply_advice_by_id_async(
        self,
        request: main_models.ApplyAdviceByIdRequest,
    ) -> main_models.ApplyAdviceByIdResponse:
        runtime = RuntimeOptions()
        return await self.apply_advice_by_id_with_options_async(request, runtime)

    def attach_user_eniwith_options(
        self,
        request: main_models.AttachUserENIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachUserENIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachUserENI',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachUserENIResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_user_eniwith_options_async(
        self,
        request: main_models.AttachUserENIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachUserENIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachUserENI',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachUserENIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_user_eni(
        self,
        request: main_models.AttachUserENIRequest,
    ) -> main_models.AttachUserENIResponse:
        runtime = RuntimeOptions()
        return self.attach_user_eniwith_options(request, runtime)

    async def attach_user_eni_async(
        self,
        request: main_models.AttachUserENIRequest,
    ) -> main_models.AttachUserENIResponse:
        runtime = RuntimeOptions()
        return await self.attach_user_eniwith_options_async(request, runtime)

    def batch_apply_advice_by_id_list_with_options(
        self,
        request: main_models.BatchApplyAdviceByIdListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchApplyAdviceByIdListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not DaraCore.is_null(request.advice_id_list):
            query['AdviceIdList'] = request.advice_id_list
        if not DaraCore.is_null(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not DaraCore.is_null(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchApplyAdviceByIdList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchApplyAdviceByIdListResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_apply_advice_by_id_list_with_options_async(
        self,
        request: main_models.BatchApplyAdviceByIdListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchApplyAdviceByIdListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not DaraCore.is_null(request.advice_id_list):
            query['AdviceIdList'] = request.advice_id_list
        if not DaraCore.is_null(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not DaraCore.is_null(request.build_immediately):
            query['BuildImmediately'] = request.build_immediately
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchApplyAdviceByIdList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchApplyAdviceByIdListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_apply_advice_by_id_list(
        self,
        request: main_models.BatchApplyAdviceByIdListRequest,
    ) -> main_models.BatchApplyAdviceByIdListResponse:
        runtime = RuntimeOptions()
        return self.batch_apply_advice_by_id_list_with_options(request, runtime)

    async def batch_apply_advice_by_id_list_async(
        self,
        request: main_models.BatchApplyAdviceByIdListRequest,
    ) -> main_models.BatchApplyAdviceByIdListResponse:
        runtime = RuntimeOptions()
        return await self.batch_apply_advice_by_id_list_with_options_async(request, runtime)

    def bind_dbresource_group_with_user_with_options(
        self,
        request: main_models.BindDBResourceGroupWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDBResourceGroupWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourceGroupWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDBResourceGroupWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_dbresource_group_with_user_with_options_async(
        self,
        request: main_models.BindDBResourceGroupWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDBResourceGroupWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourceGroupWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDBResourceGroupWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_dbresource_group_with_user(
        self,
        request: main_models.BindDBResourceGroupWithUserRequest,
    ) -> main_models.BindDBResourceGroupWithUserResponse:
        runtime = RuntimeOptions()
        return self.bind_dbresource_group_with_user_with_options(request, runtime)

    async def bind_dbresource_group_with_user_async(
        self,
        request: main_models.BindDBResourceGroupWithUserRequest,
    ) -> main_models.BindDBResourceGroupWithUserResponse:
        runtime = RuntimeOptions()
        return await self.bind_dbresource_group_with_user_with_options_async(request, runtime)

    def bind_dbresource_pool_with_user_with_options(
        self,
        request: main_models.BindDBResourcePoolWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDBResourcePoolWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourcePoolWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDBResourcePoolWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_dbresource_pool_with_user_with_options_async(
        self,
        request: main_models.BindDBResourcePoolWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDBResourcePoolWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourcePoolWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDBResourcePoolWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_dbresource_pool_with_user(
        self,
        request: main_models.BindDBResourcePoolWithUserRequest,
    ) -> main_models.BindDBResourcePoolWithUserResponse:
        runtime = RuntimeOptions()
        return self.bind_dbresource_pool_with_user_with_options(request, runtime)

    async def bind_dbresource_pool_with_user_async(
        self,
        request: main_models.BindDBResourcePoolWithUserRequest,
    ) -> main_models.BindDBResourcePoolWithUserResponse:
        runtime = RuntimeOptions()
        return await self.bind_dbresource_pool_with_user_with_options_async(request, runtime)

    def cancel_active_operation_tasks_with_options(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_active_operation_tasks_with_options_async(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_active_operation_tasks(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
    ) -> main_models.CancelActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return self.cancel_active_operation_tasks_with_options(request, runtime)

    async def cancel_active_operation_tasks_async(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
    ) -> main_models.CancelActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return await self.cancel_active_operation_tasks_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleResponse:
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
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleResponse:
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
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        tmp_req: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        tmp_req.validate()
        request = main_models.CreateAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        tmp_req: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        tmp_req.validate()
        request = main_models.CreateAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: main_models.CreateDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not DaraCore.is_null(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not DaraCore.is_null(request.kms_id):
            query['KmsId'] = request.kms_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: main_models.CreateDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not DaraCore.is_null(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not DaraCore.is_null(request.kms_id):
            query['KmsId'] = request.kms_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster(
        self,
        request: main_models.CreateDBClusterRequest,
    ) -> main_models.CreateDBClusterResponse:
        runtime = RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: main_models.CreateDBClusterRequest,
    ) -> main_models.CreateDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbresource_group_with_options(
        self,
        tmp_req: main_models.CreateDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResourceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateDBResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.engine_params):
            request.engine_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbresource_group_with_options_async(
        self,
        tmp_req: main_models.CreateDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResourceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateDBResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.engine_params):
            request.engine_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbresource_group(
        self,
        request: main_models.CreateDBResourceGroupRequest,
    ) -> main_models.CreateDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_dbresource_group_with_options(request, runtime)

    async def create_dbresource_group_async(
        self,
        request: main_models.CreateDBResourceGroupRequest,
    ) -> main_models.CreateDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_dbresource_group_with_options_async(request, runtime)

    def create_dbresource_pool_with_options(
        self,
        request: main_models.CreateDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbresource_pool_with_options_async(
        self,
        request: main_models.CreateDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbresource_pool(
        self,
        request: main_models.CreateDBResourcePoolRequest,
    ) -> main_models.CreateDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return self.create_dbresource_pool_with_options(request, runtime)

    async def create_dbresource_pool_async(
        self,
        request: main_models.CreateDBResourcePoolRequest,
    ) -> main_models.CreateDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return await self.create_dbresource_pool_with_options_async(request, runtime)

    def create_elastic_plan_with_options(
        self,
        request: main_models.CreateElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not DaraCore.is_null(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not DaraCore.is_null(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not DaraCore.is_null(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not DaraCore.is_null(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not DaraCore.is_null(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not DaraCore.is_null(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not DaraCore.is_null(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not DaraCore.is_null(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_plan_with_options_async(
        self,
        request: main_models.CreateElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not DaraCore.is_null(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not DaraCore.is_null(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not DaraCore.is_null(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not DaraCore.is_null(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not DaraCore.is_null(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not DaraCore.is_null(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not DaraCore.is_null(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not DaraCore.is_null(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_plan(
        self,
        request: main_models.CreateElasticPlanRequest,
    ) -> main_models.CreateElasticPlanResponse:
        runtime = RuntimeOptions()
        return self.create_elastic_plan_with_options(request, runtime)

    async def create_elastic_plan_async(
        self,
        request: main_models.CreateElasticPlanRequest,
    ) -> main_models.CreateElasticPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_elastic_plan_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
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
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
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
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backups_with_options(
        self,
        request: main_models.DeleteBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackups',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backups_with_options_async(
        self,
        request: main_models.DeleteBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackups',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backups(
        self,
        request: main_models.DeleteBackupsRequest,
    ) -> main_models.DeleteBackupsResponse:
        runtime = RuntimeOptions()
        return self.delete_backups_with_options(request, runtime)

    async def delete_backups_async(
        self,
        request: main_models.DeleteBackupsRequest,
    ) -> main_models.DeleteBackupsResponse:
        runtime = RuntimeOptions()
        return await self.delete_backups_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: main_models.DeleteDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: main_models.DeleteDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: main_models.DeleteDBClusterRequest,
    ) -> main_models.DeleteDBClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: main_models.DeleteDBClusterRequest,
    ) -> main_models.DeleteDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_dbresource_group_with_options(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbresource_group_with_options_async(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbresource_group(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
    ) -> main_models.DeleteDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_dbresource_group_with_options(request, runtime)

    async def delete_dbresource_group_async(
        self,
        request: main_models.DeleteDBResourceGroupRequest,
    ) -> main_models.DeleteDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbresource_group_with_options_async(request, runtime)

    def delete_dbresource_pool_with_options(
        self,
        request: main_models.DeleteDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbresource_pool_with_options_async(
        self,
        request: main_models.DeleteDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbresource_pool(
        self,
        request: main_models.DeleteDBResourcePoolRequest,
    ) -> main_models.DeleteDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return self.delete_dbresource_pool_with_options(request, runtime)

    async def delete_dbresource_pool_async(
        self,
        request: main_models.DeleteDBResourcePoolRequest,
    ) -> main_models.DeleteDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbresource_pool_with_options_async(request, runtime)

    def delete_elastic_plan_with_options(
        self,
        request: main_models.DeleteElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_plan_with_options_async(
        self,
        request: main_models.DeleteElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_plan(
        self,
        request: main_models.DeleteElasticPlanRequest,
    ) -> main_models.DeleteElasticPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_elastic_plan_with_options(request, runtime)

    async def delete_elastic_plan_async(
        self,
        request: main_models.DeleteElasticPlanRequest,
    ) -> main_models.DeleteElasticPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_elastic_plan_with_options_async(request, runtime)

    def describe_abnormal_pattern_detection_with_options(
        self,
        request: main_models.DescribeAbnormalPatternDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAbnormalPatternDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAbnormalPatternDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAbnormalPatternDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abnormal_pattern_detection_with_options_async(
        self,
        request: main_models.DescribeAbnormalPatternDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAbnormalPatternDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAbnormalPatternDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAbnormalPatternDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abnormal_pattern_detection(
        self,
        request: main_models.DescribeAbnormalPatternDetectionRequest,
    ) -> main_models.DescribeAbnormalPatternDetectionResponse:
        runtime = RuntimeOptions()
        return self.describe_abnormal_pattern_detection_with_options(request, runtime)

    async def describe_abnormal_pattern_detection_async(
        self,
        request: main_models.DescribeAbnormalPatternDetectionRequest,
    ) -> main_models.DescribeAbnormalPatternDetectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_abnormal_pattern_detection_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: main_models.DescribeAccountsRequest,
    ) -> main_models.DescribeAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: main_models.DescribeAccountsRequest,
    ) -> main_models.DescribeAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_maintain_conf_with_options(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationMaintainConf',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_maintain_conf_with_options_async(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationMaintainConf',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_maintain_conf(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_maintain_conf_with_options(request, runtime)

    async def describe_active_operation_maintain_conf_async(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_maintain_conf_with_options_async(request, runtime)

    def describe_active_operation_tasks_with_options(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not DaraCore.is_null(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not DaraCore.is_null(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.ins_name):
            query['InsName'] = request.ins_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_tasks_with_options_async(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not DaraCore.is_null(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not DaraCore.is_null(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.ins_name):
            query['InsName'] = request.ins_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_tasks(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_tasks_with_options(request, runtime)

    async def describe_active_operation_tasks_async(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_tasks_with_options_async(request, runtime)

    def describe_advice_service_enabled_with_options(
        self,
        request: main_models.DescribeAdviceServiceEnabledRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdviceServiceEnabledResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdviceServiceEnabled',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdviceServiceEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advice_service_enabled_with_options_async(
        self,
        request: main_models.DescribeAdviceServiceEnabledRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdviceServiceEnabledResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdviceServiceEnabled',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdviceServiceEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advice_service_enabled(
        self,
        request: main_models.DescribeAdviceServiceEnabledRequest,
    ) -> main_models.DescribeAdviceServiceEnabledResponse:
        runtime = RuntimeOptions()
        return self.describe_advice_service_enabled_with_options(request, runtime)

    async def describe_advice_service_enabled_async(
        self,
        request: main_models.DescribeAdviceServiceEnabledRequest,
    ) -> main_models.DescribeAdviceServiceEnabledResponse:
        runtime = RuntimeOptions()
        return await self.describe_advice_service_enabled_with_options_async(request, runtime)

    def describe_all_accounts_with_options(
        self,
        request: main_models.DescribeAllAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllAccounts',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_accounts_with_options_async(
        self,
        request: main_models.DescribeAllAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllAccounts',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_accounts(
        self,
        request: main_models.DescribeAllAccountsRequest,
    ) -> main_models.DescribeAllAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_all_accounts_with_options(request, runtime)

    async def describe_all_accounts_async(
        self,
        request: main_models.DescribeAllAccountsRequest,
    ) -> main_models.DescribeAllAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_accounts_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: main_models.DescribeAllDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: main_models.DescribeAllDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_source(
        self,
        request: main_models.DescribeAllDataSourceRequest,
    ) -> main_models.DescribeAllDataSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: main_models.DescribeAllDataSourceRequest,
    ) -> main_models.DescribeAllDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_applied_advices_with_options(
        self,
        request: main_models.DescribeAppliedAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppliedAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppliedAdvices',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppliedAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_applied_advices_with_options_async(
        self,
        request: main_models.DescribeAppliedAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppliedAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppliedAdvices',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppliedAdvicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_applied_advices(
        self,
        request: main_models.DescribeAppliedAdvicesRequest,
    ) -> main_models.DescribeAppliedAdvicesResponse:
        runtime = RuntimeOptions()
        return self.describe_applied_advices_with_options(request, runtime)

    async def describe_applied_advices_async(
        self,
        request: main_models.DescribeAppliedAdvicesRequest,
    ) -> main_models.DescribeAppliedAdvicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_applied_advices_with_options_async(request, runtime)

    def describe_audit_log_config_with_options(
        self,
        request: main_models.DescribeAuditLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeAuditLogConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_config_with_options_async(
        self,
        request: main_models.DescribeAuditLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeAuditLogConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_config(
        self,
        request: main_models.DescribeAuditLogConfigRequest,
    ) -> main_models.DescribeAuditLogConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_log_config_with_options(request, runtime)

    async def describe_audit_log_config_async(
        self,
        request: main_models.DescribeAuditLogConfigRequest,
    ) -> main_models.DescribeAuditLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_log_config_with_options_async(request, runtime)

    def describe_audit_log_records_with_options(
        self,
        request: main_models.DescribeAuditLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.succeed):
            query['Succeed'] = request.succeed
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditLogRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_records_with_options_async(
        self,
        request: main_models.DescribeAuditLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.succeed):
            query['Succeed'] = request.succeed
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditLogRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_records(
        self,
        request: main_models.DescribeAuditLogRecordsRequest,
    ) -> main_models.DescribeAuditLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_log_records_with_options(request, runtime)

    async def describe_audit_log_records_async(
        self,
        request: main_models.DescribeAuditLogRecordsRequest,
    ) -> main_models.DescribeAuditLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_log_records_with_options_async(request, runtime)

    def describe_auto_renew_attribute_with_options(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoRenewAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_renew_attribute_with_options_async(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoRenewAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_renew_attribute(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_renew_attribute_with_options(request, runtime)

    async def describe_auto_renew_attribute_async(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_renew_attribute_with_options_async(request, runtime)

    def describe_available_advices_with_options(
        self,
        request: main_models.DescribeAvailableAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not DaraCore.is_null(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableAdvices',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_advices_with_options_async(
        self,
        request: main_models.DescribeAvailableAdvicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableAdvicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advice_date):
            query['AdviceDate'] = request.advice_date
        if not DaraCore.is_null(request.advice_type):
            query['AdviceType'] = request.advice_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_table_name):
            query['SchemaTableName'] = request.schema_table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableAdvices',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableAdvicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_advices(
        self,
        request: main_models.DescribeAvailableAdvicesRequest,
    ) -> main_models.DescribeAvailableAdvicesResponse:
        runtime = RuntimeOptions()
        return self.describe_available_advices_with_options(request, runtime)

    async def describe_available_advices_async(
        self,
        request: main_models.DescribeAvailableAdvicesRequest,
    ) -> main_models.DescribeAvailableAdvicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_available_advices_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: main_models.DescribeAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResource',
            version = '2019-03-15',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResource',
            version = '2019-03-15',
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

    def describe_backup_policy_with_options(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: main_models.DescribeBackupPolicyRequest,
    ) -> main_models.DescribeBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: main_models.DescribeBackupPolicyRequest,
    ) -> main_models.DescribeBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: main_models.DescribeBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.cross_role):
            query['CrossRole'] = request.cross_role
        if not DaraCore.is_null(request.cross_uid):
            query['CrossUid'] = request.cross_uid
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: main_models.DescribeBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.cross_role):
            query['CrossRole'] = request.cross_role
        if not DaraCore.is_null(request.cross_uid):
            query['CrossUid'] = request.cross_uid
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: main_models.DescribeBackupsRequest,
    ) -> main_models.DescribeBackupsResponse:
        runtime = RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: main_models.DescribeBackupsRequest,
    ) -> main_models.DescribeBackupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_bad_sql_detection_with_options(
        self,
        request: main_models.DescribeBadSqlDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBadSqlDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBadSqlDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBadSqlDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bad_sql_detection_with_options_async(
        self,
        request: main_models.DescribeBadSqlDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBadSqlDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBadSqlDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBadSqlDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bad_sql_detection(
        self,
        request: main_models.DescribeBadSqlDetectionRequest,
    ) -> main_models.DescribeBadSqlDetectionResponse:
        runtime = RuntimeOptions()
        return self.describe_bad_sql_detection_with_options(request, runtime)

    async def describe_bad_sql_detection_async(
        self,
        request: main_models.DescribeBadSqlDetectionRequest,
    ) -> main_models.DescribeBadSqlDetectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_bad_sql_detection_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: main_models.DescribeColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: main_models.DescribeColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns(
        self,
        request: main_models.DescribeColumnsRequest,
    ) -> main_models.DescribeColumnsResponse:
        runtime = RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: main_models.DescribeColumnsRequest,
    ) -> main_models.DescribeColumnsResponse:
        runtime = RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_compute_resource_with_options(
        self,
        request: main_models.DescribeComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.migrate):
            query['Migrate'] = request.migrate
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComputeResource',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComputeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compute_resource_with_options_async(
        self,
        request: main_models.DescribeComputeResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComputeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.migrate):
            query['Migrate'] = request.migrate
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComputeResource',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComputeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compute_resource(
        self,
        request: main_models.DescribeComputeResourceRequest,
    ) -> main_models.DescribeComputeResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_compute_resource_with_options(request, runtime)

    async def describe_compute_resource_async(
        self,
        request: main_models.DescribeComputeResourceRequest,
    ) -> main_models.DescribeComputeResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_compute_resource_with_options_async(request, runtime)

    def describe_connection_count_records_with_options(
        self,
        request: main_models.DescribeConnectionCountRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConnectionCountRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeConnectionCountRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConnectionCountRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_connection_count_records_with_options_async(
        self,
        request: main_models.DescribeConnectionCountRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConnectionCountRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeConnectionCountRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConnectionCountRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_connection_count_records(
        self,
        request: main_models.DescribeConnectionCountRecordsRequest,
    ) -> main_models.DescribeConnectionCountRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_connection_count_records_with_options(request, runtime)

    async def describe_connection_count_records_async(
        self,
        request: main_models.DescribeConnectionCountRecordsRequest,
    ) -> main_models.DescribeConnectionCountRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_connection_count_records_with_options_async(request, runtime)

    def describe_controller_detection_with_options(
        self,
        request: main_models.DescribeControllerDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeControllerDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeControllerDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeControllerDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_controller_detection_with_options_async(
        self,
        request: main_models.DescribeControllerDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeControllerDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeControllerDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeControllerDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_controller_detection(
        self,
        request: main_models.DescribeControllerDetectionRequest,
    ) -> main_models.DescribeControllerDetectionResponse:
        runtime = RuntimeOptions()
        return self.describe_controller_detection_with_options(request, runtime)

    async def describe_controller_detection_async(
        self,
        request: main_models.DescribeControllerDetectionRequest,
    ) -> main_models.DescribeControllerDetectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_controller_detection_with_options_async(request, runtime)

    def describe_dbcluster_access_white_list_with_options(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterAccessWhiteList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_access_white_list_with_options_async(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterAccessWhiteList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_access_white_list(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    async def describe_dbcluster_access_white_list_async(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_access_white_list_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_health_status_with_options(
        self,
        request: main_models.DescribeDBClusterHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterHealthStatus',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_health_status_with_options_async(
        self,
        request: main_models.DescribeDBClusterHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterHealthStatus',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_health_status(
        self,
        request: main_models.DescribeDBClusterHealthStatusRequest,
    ) -> main_models.DescribeDBClusterHealthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_health_status_with_options(request, runtime)

    async def describe_dbcluster_health_status_async(
        self,
        request: main_models.DescribeDBClusterHealthStatusRequest,
    ) -> main_models.DescribeDBClusterHealthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_health_status_with_options_async(request, runtime)

    def describe_dbcluster_net_info_with_options(
        self,
        request: main_models.DescribeDBClusterNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
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
            action = 'DescribeDBClusterNetInfo',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_net_info_with_options_async(
        self,
        request: main_models.DescribeDBClusterNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
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
            action = 'DescribeDBClusterNetInfo',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_net_info(
        self,
        request: main_models.DescribeDBClusterNetInfoRequest,
    ) -> main_models.DescribeDBClusterNetInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_net_info_with_options(request, runtime)

    async def describe_dbcluster_net_info_async(
        self,
        request: main_models.DescribeDBClusterNetInfoRequest,
    ) -> main_models.DescribeDBClusterNetInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_net_info_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
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
        if not DaraCore.is_null(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
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
        if not DaraCore.is_null(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbcluster_resource_pool_performance_with_options(
        self,
        request: main_models.DescribeDBClusterResourcePoolPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterResourcePoolPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterResourcePoolPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterResourcePoolPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_resource_pool_performance_with_options_async(
        self,
        request: main_models.DescribeDBClusterResourcePoolPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterResourcePoolPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterResourcePoolPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterResourcePoolPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_resource_pool_performance(
        self,
        request: main_models.DescribeDBClusterResourcePoolPerformanceRequest,
    ) -> main_models.DescribeDBClusterResourcePoolPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_resource_pool_performance_with_options(request, runtime)

    async def describe_dbcluster_resource_pool_performance_async(
        self,
        request: main_models.DescribeDBClusterResourcePoolPerformanceRequest,
    ) -> main_models.DescribeDBClusterResourcePoolPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_resource_pool_performance_with_options_async(request, runtime)

    def describe_dbcluster_sslwith_options(
        self,
        request: main_models.DescribeDBClusterSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterSSL',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_sslwith_options_async(
        self,
        request: main_models.DescribeDBClusterSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterSSL',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_ssl(
        self,
        request: main_models.DescribeDBClusterSSLRequest,
    ) -> main_models.DescribeDBClusterSSLResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_sslwith_options(request, runtime)

    async def describe_dbcluster_ssl_async(
        self,
        request: main_models.DescribeDBClusterSSLRequest,
    ) -> main_models.DescribeDBClusterSSLResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_sslwith_options_async(request, runtime)

    def describe_dbcluster_shard_number_with_options(
        self,
        request: main_models.DescribeDBClusterShardNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterShardNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterShardNumber',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterShardNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_shard_number_with_options_async(
        self,
        request: main_models.DescribeDBClusterShardNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterShardNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeDBClusterShardNumber',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterShardNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_shard_number(
        self,
        request: main_models.DescribeDBClusterShardNumberRequest,
    ) -> main_models.DescribeDBClusterShardNumberResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_shard_number_with_options(request, runtime)

    async def describe_dbcluster_shard_number_async(
        self,
        request: main_models.DescribeDBClusterShardNumberRequest,
    ) -> main_models.DescribeDBClusterShardNumberResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_shard_number_with_options_async(request, runtime)

    def describe_dbcluster_space_summary_with_options(
        self,
        request: main_models.DescribeDBClusterSpaceSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterSpaceSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterSpaceSummary',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterSpaceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_space_summary_with_options_async(
        self,
        request: main_models.DescribeDBClusterSpaceSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterSpaceSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterSpaceSummary',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterSpaceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_space_summary(
        self,
        request: main_models.DescribeDBClusterSpaceSummaryRequest,
    ) -> main_models.DescribeDBClusterSpaceSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_space_summary_with_options(request, runtime)

    async def describe_dbcluster_space_summary_async(
        self,
        request: main_models.DescribeDBClusterSpaceSummaryRequest,
    ) -> main_models.DescribeDBClusterSpaceSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_space_summary_with_options_async(request, runtime)

    def describe_dbcluster_status_with_options(
        self,
        request: main_models.DescribeDBClusterStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterStatusResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStatus',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_status_with_options_async(
        self,
        request: main_models.DescribeDBClusterStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterStatusResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStatus',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_status(
        self,
        request: main_models.DescribeDBClusterStatusRequest,
    ) -> main_models.DescribeDBClusterStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_status_with_options(request, runtime)

    async def describe_dbcluster_status_async(
        self,
        request: main_models.DescribeDBClusterStatusRequest,
    ) -> main_models.DescribeDBClusterStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_status_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: main_models.DescribeDBClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.dbversion):
            query['DBVersion'] = request.dbversion
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
            action = 'DescribeDBClusters',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: main_models.DescribeDBClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.dbversion):
            query['DBVersion'] = request.dbversion
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
            action = 'DescribeDBClusters',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: main_models.DescribeDBClustersRequest,
    ) -> main_models.DescribeDBClustersResponse:
        runtime = RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: main_models.DescribeDBClustersRequest,
    ) -> main_models.DescribeDBClustersResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbresource_group_with_options(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_group_with_options_async(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_group(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
    ) -> main_models.DescribeDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_dbresource_group_with_options(request, runtime)

    async def describe_dbresource_group_async(
        self,
        request: main_models.DescribeDBResourceGroupRequest,
    ) -> main_models.DescribeDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbresource_group_with_options_async(request, runtime)

    def describe_dbresource_pool_with_options(
        self,
        request: main_models.DescribeDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_pool_with_options_async(
        self,
        request: main_models.DescribeDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_pool(
        self,
        request: main_models.DescribeDBResourcePoolRequest,
    ) -> main_models.DescribeDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return self.describe_dbresource_pool_with_options(request, runtime)

    async def describe_dbresource_pool_async(
        self,
        request: main_models.DescribeDBResourcePoolRequest,
    ) -> main_models.DescribeDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbresource_pool_with_options_async(request, runtime)

    def describe_diagnosis_dimensions_with_options(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisDimensions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_dimensions_with_options_async(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisDimensions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_dimensions(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    async def describe_diagnosis_dimensions_async(
        self,
        request: main_models.DescribeDiagnosisDimensionsRequest,
    ) -> main_models.DescribeDiagnosisDimensionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_dimensions_with_options_async(request, runtime)

    def describe_diagnosis_monitor_performance_with_options(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisMonitorPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisMonitorPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_monitor_performance_with_options_async(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisMonitorPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisMonitorPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_monitor_performance(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_monitor_performance_with_options(request, runtime)

    async def describe_diagnosis_monitor_performance_async(
        self,
        request: main_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> main_models.DescribeDiagnosisMonitorPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_monitor_performance_with_options_async(request, runtime)

    def describe_diagnosis_records_with_options(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not DaraCore.is_null(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not DaraCore.is_null(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not DaraCore.is_null(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_records_with_options_async(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not DaraCore.is_null(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not DaraCore.is_null(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not DaraCore.is_null(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_records(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    async def describe_diagnosis_records_async(
        self,
        request: main_models.DescribeDiagnosisRecordsRequest,
    ) -> main_models.DescribeDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_records_with_options_async(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSQLInfo',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_sqlinfo_with_options_async(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSQLInfo',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_sqlinfo(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    async def describe_diagnosis_sqlinfo_async(
        self,
        request: main_models.DescribeDiagnosisSQLInfoRequest,
    ) -> main_models.DescribeDiagnosisSQLInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_sqlinfo_with_options_async(request, runtime)

    def describe_diagnosis_tasks_with_options(
        self,
        request: main_models.DescribeDiagnosisTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_tasks_with_options_async(
        self,
        request: main_models.DescribeDiagnosisTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_tasks(
        self,
        request: main_models.DescribeDiagnosisTasksRequest,
    ) -> main_models.DescribeDiagnosisTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnosis_tasks_with_options(request, runtime)

    async def describe_diagnosis_tasks_async(
        self,
        request: main_models.DescribeDiagnosisTasksRequest,
    ) -> main_models.DescribeDiagnosisTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnosis_tasks_with_options_async(request, runtime)

    def describe_download_records_with_options(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_records_with_options_async(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_records(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
    ) -> main_models.DescribeDownloadRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    async def describe_download_records_async(
        self,
        request: main_models.DescribeDownloadRecordsRequest,
    ) -> main_models.DescribeDownloadRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_records_with_options_async(request, runtime)

    def describe_eiurange_with_options(
        self,
        request: main_models.DescribeEIURangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEIURangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.sub_operation):
            query['SubOperation'] = request.sub_operation
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEIURange',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEIURangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eiurange_with_options_async(
        self,
        request: main_models.DescribeEIURangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEIURangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.sub_operation):
            query['SubOperation'] = request.sub_operation
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEIURange',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEIURangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eiurange(
        self,
        request: main_models.DescribeEIURangeRequest,
    ) -> main_models.DescribeEIURangeResponse:
        runtime = RuntimeOptions()
        return self.describe_eiurange_with_options(request, runtime)

    async def describe_eiurange_async(
        self,
        request: main_models.DescribeEIURangeRequest,
    ) -> main_models.DescribeEIURangeResponse:
        runtime = RuntimeOptions()
        return await self.describe_eiurange_with_options_async(request, runtime)

    def describe_elastic_daily_plan_with_options(
        self,
        request: main_models.DescribeElasticDailyPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticDailyPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_daily_plan_day):
            query['ElasticDailyPlanDay'] = request.elastic_daily_plan_day
        if not DaraCore.is_null(request.elastic_daily_plan_status_list):
            query['ElasticDailyPlanStatusList'] = request.elastic_daily_plan_status_list
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticDailyPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticDailyPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_daily_plan_with_options_async(
        self,
        request: main_models.DescribeElasticDailyPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticDailyPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_daily_plan_day):
            query['ElasticDailyPlanDay'] = request.elastic_daily_plan_day
        if not DaraCore.is_null(request.elastic_daily_plan_status_list):
            query['ElasticDailyPlanStatusList'] = request.elastic_daily_plan_status_list
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticDailyPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticDailyPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_daily_plan(
        self,
        request: main_models.DescribeElasticDailyPlanRequest,
    ) -> main_models.DescribeElasticDailyPlanResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_daily_plan_with_options(request, runtime)

    async def describe_elastic_daily_plan_async(
        self,
        request: main_models.DescribeElasticDailyPlanRequest,
    ) -> main_models.DescribeElasticDailyPlanResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_daily_plan_with_options_async(request, runtime)

    def describe_elastic_plan_with_options(
        self,
        request: main_models.DescribeElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_with_options_async(
        self,
        request: main_models.DescribeElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan(
        self,
        request: main_models.DescribeElasticPlanRequest,
    ) -> main_models.DescribeElasticPlanResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_plan_with_options(request, runtime)

    async def describe_elastic_plan_async(
        self,
        request: main_models.DescribeElasticPlanRequest,
    ) -> main_models.DescribeElasticPlanResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_plan_with_options_async(request, runtime)

    def describe_excessive_primary_keys_with_options(
        self,
        request: main_models.DescribeExcessivePrimaryKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExcessivePrimaryKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExcessivePrimaryKeys',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExcessivePrimaryKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_excessive_primary_keys_with_options_async(
        self,
        request: main_models.DescribeExcessivePrimaryKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExcessivePrimaryKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExcessivePrimaryKeys',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExcessivePrimaryKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_excessive_primary_keys(
        self,
        request: main_models.DescribeExcessivePrimaryKeysRequest,
    ) -> main_models.DescribeExcessivePrimaryKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_excessive_primary_keys_with_options(request, runtime)

    async def describe_excessive_primary_keys_async(
        self,
        request: main_models.DescribeExcessivePrimaryKeysRequest,
    ) -> main_models.DescribeExcessivePrimaryKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_excessive_primary_keys_with_options_async(request, runtime)

    def describe_executor_detection_with_options(
        self,
        request: main_models.DescribeExecutorDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExecutorDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExecutorDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExecutorDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_executor_detection_with_options_async(
        self,
        request: main_models.DescribeExecutorDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExecutorDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExecutorDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExecutorDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_executor_detection(
        self,
        request: main_models.DescribeExecutorDetectionRequest,
    ) -> main_models.DescribeExecutorDetectionResponse:
        runtime = RuntimeOptions()
        return self.describe_executor_detection_with_options(request, runtime)

    async def describe_executor_detection_async(
        self,
        request: main_models.DescribeExecutorDetectionRequest,
    ) -> main_models.DescribeExecutorDetectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_executor_detection_with_options_async(request, runtime)

    def describe_history_events_stat_with_options(
        self,
        request: main_models.DescribeHistoryEventsStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryEventsStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.archive_status):
            query['ArchiveStatus'] = request.archive_status
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryEventsStat',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryEventsStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_events_stat_with_options_async(
        self,
        request: main_models.DescribeHistoryEventsStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryEventsStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.archive_status):
            query['ArchiveStatus'] = request.archive_status
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryEventsStat',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryEventsStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_events_stat(
        self,
        request: main_models.DescribeHistoryEventsStatRequest,
    ) -> main_models.DescribeHistoryEventsStatResponse:
        runtime = RuntimeOptions()
        return self.describe_history_events_stat_with_options(request, runtime)

    async def describe_history_events_stat_async(
        self,
        request: main_models.DescribeHistoryEventsStatRequest,
    ) -> main_models.DescribeHistoryEventsStatResponse:
        runtime = RuntimeOptions()
        return await self.describe_history_events_stat_with_options_async(request, runtime)

    def describe_inclined_nodes_with_options(
        self,
        request: main_models.DescribeInclinedNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInclinedNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
            action = 'DescribeInclinedNodes',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInclinedNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inclined_nodes_with_options_async(
        self,
        request: main_models.DescribeInclinedNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInclinedNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
            action = 'DescribeInclinedNodes',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInclinedNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inclined_nodes(
        self,
        request: main_models.DescribeInclinedNodesRequest,
    ) -> main_models.DescribeInclinedNodesResponse:
        runtime = RuntimeOptions()
        return self.describe_inclined_nodes_with_options(request, runtime)

    async def describe_inclined_nodes_async(
        self,
        request: main_models.DescribeInclinedNodesRequest,
    ) -> main_models.DescribeInclinedNodesResponse:
        runtime = RuntimeOptions()
        return await self.describe_inclined_nodes_with_options_async(request, runtime)

    def describe_inclined_tables_with_options(
        self,
        request: main_models.DescribeInclinedTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInclinedTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInclinedTables',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInclinedTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inclined_tables_with_options_async(
        self,
        request: main_models.DescribeInclinedTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInclinedTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInclinedTables',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInclinedTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inclined_tables(
        self,
        request: main_models.DescribeInclinedTablesRequest,
    ) -> main_models.DescribeInclinedTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_inclined_tables_with_options(request, runtime)

    async def describe_inclined_tables_async(
        self,
        request: main_models.DescribeInclinedTablesRequest,
    ) -> main_models.DescribeInclinedTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_inclined_tables_with_options_async(request, runtime)

    def describe_kernel_version_with_options(
        self,
        request: main_models.DescribeKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeKernelVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kernel_version_with_options_async(
        self,
        request: main_models.DescribeKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'DescribeKernelVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kernel_version(
        self,
        request: main_models.DescribeKernelVersionRequest,
    ) -> main_models.DescribeKernelVersionResponse:
        runtime = RuntimeOptions()
        return self.describe_kernel_version_with_options(request, runtime)

    async def describe_kernel_version_async(
        self,
        request: main_models.DescribeKernelVersionRequest,
    ) -> main_models.DescribeKernelVersionResponse:
        runtime = RuntimeOptions()
        return await self.describe_kernel_version_with_options_async(request, runtime)

    def describe_kms_keys_with_options(
        self,
        request: main_models.DescribeKmsKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKmsKeysResponse:
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKmsKeys',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKmsKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kms_keys_with_options_async(
        self,
        request: main_models.DescribeKmsKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKmsKeysResponse:
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKmsKeys',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKmsKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kms_keys(
        self,
        request: main_models.DescribeKmsKeysRequest,
    ) -> main_models.DescribeKmsKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_kms_keys_with_options(request, runtime)

    async def describe_kms_keys_async(
        self,
        request: main_models.DescribeKmsKeysRequest,
    ) -> main_models.DescribeKmsKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_kms_keys_with_options_async(request, runtime)

    def describe_load_tasks_records_with_options(
        self,
        request: main_models.DescribeLoadTasksRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadTasksRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadTasksRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadTasksRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_tasks_records_with_options_async(
        self,
        request: main_models.DescribeLoadTasksRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoadTasksRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoadTasksRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoadTasksRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_tasks_records(
        self,
        request: main_models.DescribeLoadTasksRecordsRequest,
    ) -> main_models.DescribeLoadTasksRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_load_tasks_records_with_options(request, runtime)

    async def describe_load_tasks_records_async(
        self,
        request: main_models.DescribeLoadTasksRecordsRequest,
    ) -> main_models.DescribeLoadTasksRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_load_tasks_records_with_options_async(request, runtime)

    def describe_log_hub_attribute_with_options(
        self,
        request: main_models.DescribeLogHubAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogHubAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
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
            action = 'DescribeLogHubAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogHubAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_hub_attribute_with_options_async(
        self,
        request: main_models.DescribeLogHubAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogHubAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
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
            action = 'DescribeLogHubAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogHubAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_hub_attribute(
        self,
        request: main_models.DescribeLogHubAttributeRequest,
    ) -> main_models.DescribeLogHubAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_log_hub_attribute_with_options(request, runtime)

    async def describe_log_hub_attribute_async(
        self,
        request: main_models.DescribeLogHubAttributeRequest,
    ) -> main_models.DescribeLogHubAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_hub_attribute_with_options_async(request, runtime)

    def describe_log_store_keys_with_options(
        self,
        request: main_models.DescribeLogStoreKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
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
            action = 'DescribeLogStoreKeys',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_keys_with_options_async(
        self,
        request: main_models.DescribeLogStoreKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
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
            action = 'DescribeLogStoreKeys',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store_keys(
        self,
        request: main_models.DescribeLogStoreKeysRequest,
    ) -> main_models.DescribeLogStoreKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_log_store_keys_with_options(request, runtime)

    async def describe_log_store_keys_async(
        self,
        request: main_models.DescribeLogStoreKeysRequest,
    ) -> main_models.DescribeLogStoreKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_store_keys_with_options_async(request, runtime)

    def describe_loghub_detail_with_options(
        self,
        request: main_models.DescribeLoghubDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoghubDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_name):
            query['ExportName'] = request.export_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoghubDetail',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoghubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_loghub_detail_with_options_async(
        self,
        request: main_models.DescribeLoghubDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoghubDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_name):
            query['ExportName'] = request.export_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoghubDetail',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoghubDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_loghub_detail(
        self,
        request: main_models.DescribeLoghubDetailRequest,
    ) -> main_models.DescribeLoghubDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_loghub_detail_with_options(request, runtime)

    async def describe_loghub_detail_async(
        self,
        request: main_models.DescribeLoghubDetailRequest,
    ) -> main_models.DescribeLoghubDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_loghub_detail_with_options_async(request, runtime)

    def describe_maintenance_action_with_options(
        self,
        request: main_models.DescribeMaintenanceActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMaintenanceActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMaintenanceAction',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMaintenanceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_maintenance_action_with_options_async(
        self,
        request: main_models.DescribeMaintenanceActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMaintenanceActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMaintenanceAction',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMaintenanceActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_maintenance_action(
        self,
        request: main_models.DescribeMaintenanceActionRequest,
    ) -> main_models.DescribeMaintenanceActionResponse:
        runtime = RuntimeOptions()
        return self.describe_maintenance_action_with_options(request, runtime)

    async def describe_maintenance_action_async(
        self,
        request: main_models.DescribeMaintenanceActionRequest,
    ) -> main_models.DescribeMaintenanceActionResponse:
        runtime = RuntimeOptions()
        return await self.describe_maintenance_action_with_options_async(request, runtime)

    def describe_operator_permission_with_options(
        self,
        request: main_models.DescribeOperatorPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorPermission',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_operator_permission_with_options_async(
        self,
        request: main_models.DescribeOperatorPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOperatorPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOperatorPermission',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_operator_permission(
        self,
        request: main_models.DescribeOperatorPermissionRequest,
    ) -> main_models.DescribeOperatorPermissionResponse:
        runtime = RuntimeOptions()
        return self.describe_operator_permission_with_options(request, runtime)

    async def describe_operator_permission_async(
        self,
        request: main_models.DescribeOperatorPermissionRequest,
    ) -> main_models.DescribeOperatorPermissionResponse:
        runtime = RuntimeOptions()
        return await self.describe_operator_permission_with_options_async(request, runtime)

    def describe_oversize_non_partition_table_infos_with_options(
        self,
        request: main_models.DescribeOversizeNonPartitionTableInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOversizeNonPartitionTableInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOversizeNonPartitionTableInfos',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOversizeNonPartitionTableInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oversize_non_partition_table_infos_with_options_async(
        self,
        request: main_models.DescribeOversizeNonPartitionTableInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOversizeNonPartitionTableInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOversizeNonPartitionTableInfos',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOversizeNonPartitionTableInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oversize_non_partition_table_infos(
        self,
        request: main_models.DescribeOversizeNonPartitionTableInfosRequest,
    ) -> main_models.DescribeOversizeNonPartitionTableInfosResponse:
        runtime = RuntimeOptions()
        return self.describe_oversize_non_partition_table_infos_with_options(request, runtime)

    async def describe_oversize_non_partition_table_infos_async(
        self,
        request: main_models.DescribeOversizeNonPartitionTableInfosRequest,
    ) -> main_models.DescribeOversizeNonPartitionTableInfosResponse:
        runtime = RuntimeOptions()
        return await self.describe_oversize_non_partition_table_infos_with_options_async(request, runtime)

    def describe_pattern_performance_with_options(
        self,
        request: main_models.DescribePatternPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePatternPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePatternPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePatternPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pattern_performance_with_options_async(
        self,
        request: main_models.DescribePatternPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePatternPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePatternPerformance',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePatternPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pattern_performance(
        self,
        request: main_models.DescribePatternPerformanceRequest,
    ) -> main_models.DescribePatternPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_pattern_performance_with_options(request, runtime)

    async def describe_pattern_performance_async(
        self,
        request: main_models.DescribePatternPerformanceRequest,
    ) -> main_models.DescribePatternPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_pattern_performance_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: main_models.DescribeProcessListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.running_time):
            query['RunningTime'] = request.running_time
        if not DaraCore.is_null(request.show_full):
            query['ShowFull'] = request.show_full
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: main_models.DescribeProcessListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.running_time):
            query['RunningTime'] = request.running_time
        if not DaraCore.is_null(request.show_full):
            query['ShowFull'] = request.show_full
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_list(
        self,
        request: main_models.DescribeProcessListRequest,
    ) -> main_models.DescribeProcessListResponse:
        runtime = RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: main_models.DescribeProcessListRequest,
    ) -> main_models.DescribeProcessListResponse:
        runtime = RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def describe_rds_analysis_resource_quotas_with_options(
        self,
        request: main_models.DescribeRdsAnalysisResourceQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsAnalysisResourceQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.node_class):
            query['NodeClass'] = request.node_class
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsAnalysisResourceQuotas',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsAnalysisResourceQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_analysis_resource_quotas_with_options_async(
        self,
        request: main_models.DescribeRdsAnalysisResourceQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsAnalysisResourceQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_category):
            query['ClusterCategory'] = request.cluster_category
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.node_class):
            query['NodeClass'] = request.node_class
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsAnalysisResourceQuotas',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsAnalysisResourceQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_analysis_resource_quotas(
        self,
        request: main_models.DescribeRdsAnalysisResourceQuotasRequest,
    ) -> main_models.DescribeRdsAnalysisResourceQuotasResponse:
        runtime = RuntimeOptions()
        return self.describe_rds_analysis_resource_quotas_with_options(request, runtime)

    async def describe_rds_analysis_resource_quotas_async(
        self,
        request: main_models.DescribeRdsAnalysisResourceQuotasRequest,
    ) -> main_models.DescribeRdsAnalysisResourceQuotasResponse:
        runtime = RuntimeOptions()
        return await self.describe_rds_analysis_resource_quotas_with_options_async(request, runtime)

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
            version = '2019-03-15',
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
            version = '2019-03-15',
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

    def describe_regions_mixed_with_options(
        self,
        request: main_models.DescribeRegionsMixedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsMixedResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegionsMixed',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsMixedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_mixed_with_options_async(
        self,
        request: main_models.DescribeRegionsMixedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsMixedResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegionsMixed',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsMixedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions_mixed(
        self,
        request: main_models.DescribeRegionsMixedRequest,
    ) -> main_models.DescribeRegionsMixedResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_mixed_with_options(request, runtime)

    async def describe_regions_mixed_async(
        self,
        request: main_models.DescribeRegionsMixedRequest,
    ) -> main_models.DescribeRegionsMixedResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_mixed_with_options_async(request, runtime)

    def describe_resubmit_config_with_options(
        self,
        request: main_models.DescribeResubmitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResubmitConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResubmitConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResubmitConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resubmit_config_with_options_async(
        self,
        request: main_models.DescribeResubmitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResubmitConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResubmitConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResubmitConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resubmit_config(
        self,
        request: main_models.DescribeResubmitConfigRequest,
    ) -> main_models.DescribeResubmitConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_resubmit_config_with_options(request, runtime)

    async def describe_resubmit_config_async(
        self,
        request: main_models.DescribeResubmitConfigRequest,
    ) -> main_models.DescribeResubmitConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_resubmit_config_with_options_async(request, runtime)

    def describe_sqaconfig_with_options(
        self,
        request: main_models.DescribeSQAConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQAConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQAConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqaconfig_with_options_async(
        self,
        request: main_models.DescribeSQAConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQAConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQAConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQAConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqaconfig(
        self,
        request: main_models.DescribeSQAConfigRequest,
    ) -> main_models.DescribeSQAConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_sqaconfig_with_options(request, runtime)

    async def describe_sqaconfig_async(
        self,
        request: main_models.DescribeSQAConfigRequest,
    ) -> main_models.DescribeSQAConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_sqaconfig_with_options_async(request, runtime)

    def describe_sqlpatterns_with_options(
        self,
        request: main_models.DescribeSQLPatternsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLPatternsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_pattern_hash):
            query['SqlPatternHash'] = request.sql_pattern_hash
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPatterns',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlpatterns_with_options_async(
        self,
        request: main_models.DescribeSQLPatternsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLPatternsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_pattern_hash):
            query['SqlPatternHash'] = request.sql_pattern_hash
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPatterns',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLPatternsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlpatterns(
        self,
        request: main_models.DescribeSQLPatternsRequest,
    ) -> main_models.DescribeSQLPatternsResponse:
        runtime = RuntimeOptions()
        return self.describe_sqlpatterns_with_options(request, runtime)

    async def describe_sqlpatterns_async(
        self,
        request: main_models.DescribeSQLPatternsRequest,
    ) -> main_models.DescribeSQLPatternsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sqlpatterns_with_options_async(request, runtime)

    def describe_sqlplan_with_options(
        self,
        request: main_models.DescribeSQLPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlplan_with_options_async(
        self,
        request: main_models.DescribeSQLPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlplan(
        self,
        request: main_models.DescribeSQLPlanRequest,
    ) -> main_models.DescribeSQLPlanResponse:
        runtime = RuntimeOptions()
        return self.describe_sqlplan_with_options(request, runtime)

    async def describe_sqlplan_async(
        self,
        request: main_models.DescribeSQLPlanRequest,
    ) -> main_models.DescribeSQLPlanResponse:
        runtime = RuntimeOptions()
        return await self.describe_sqlplan_with_options_async(request, runtime)

    def describe_sqlplan_task_with_options(
        self,
        request: main_models.DescribeSQLPlanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLPlanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.stage_id):
            query['StageId'] = request.stage_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPlanTask',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLPlanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlplan_task_with_options_async(
        self,
        request: main_models.DescribeSQLPlanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLPlanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.stage_id):
            query['StageId'] = request.stage_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPlanTask',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLPlanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlplan_task(
        self,
        request: main_models.DescribeSQLPlanTaskRequest,
    ) -> main_models.DescribeSQLPlanTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_sqlplan_task_with_options(request, runtime)

    async def describe_sqlplan_task_async(
        self,
        request: main_models.DescribeSQLPlanTaskRequest,
    ) -> main_models.DescribeSQLPlanTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_sqlplan_task_with_options_async(request, runtime)

    def describe_schemas_with_options(
        self,
        request: main_models.DescribeSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchemas',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schemas_with_options_async(
        self,
        request: main_models.DescribeSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchemas',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schemas(
        self,
        request: main_models.DescribeSchemasRequest,
    ) -> main_models.DescribeSchemasResponse:
        runtime = RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    async def describe_schemas_async(
        self,
        request: main_models.DescribeSchemasRequest,
    ) -> main_models.DescribeSchemasResponse:
        runtime = RuntimeOptions()
        return await self.describe_schemas_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_id):
            query['ProcessID'] = request.process_id
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_id):
            query['ProcessID'] = request.process_id
        if not DaraCore.is_null(request.range):
            query['Range'] = request.range
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_sql_pattern_with_options(
        self,
        request: main_models.DescribeSqlPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlPatternResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_pattern):
            query['SqlPattern'] = request.sql_pattern
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlPattern',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_pattern_with_options_async(
        self,
        request: main_models.DescribeSqlPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlPatternResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_pattern):
            query['SqlPattern'] = request.sql_pattern
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlPattern',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_pattern(
        self,
        request: main_models.DescribeSqlPatternRequest,
    ) -> main_models.DescribeSqlPatternResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_pattern_with_options(request, runtime)

    async def describe_sql_pattern_async(
        self,
        request: main_models.DescribeSqlPatternRequest,
    ) -> main_models.DescribeSqlPatternResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_pattern_with_options_async(request, runtime)

    def describe_sync_available_dbcluster_list_with_options(
        self,
        request: main_models.DescribeSyncAvailableDBClusterListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncAvailableDBClusterListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not DaraCore.is_null(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncAvailableDBClusterList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncAvailableDBClusterListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_available_dbcluster_list_with_options_async(
        self,
        request: main_models.DescribeSyncAvailableDBClusterListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncAvailableDBClusterListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not DaraCore.is_null(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncAvailableDBClusterList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncAvailableDBClusterListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_available_dbcluster_list(
        self,
        request: main_models.DescribeSyncAvailableDBClusterListRequest,
    ) -> main_models.DescribeSyncAvailableDBClusterListResponse:
        runtime = RuntimeOptions()
        return self.describe_sync_available_dbcluster_list_with_options(request, runtime)

    async def describe_sync_available_dbcluster_list_async(
        self,
        request: main_models.DescribeSyncAvailableDBClusterListRequest,
    ) -> main_models.DescribeSyncAvailableDBClusterListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sync_available_dbcluster_list_with_options_async(request, runtime)

    def describe_sync_job_list_with_options(
        self,
        request: main_models.DescribeSyncJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.get_source_detail):
            query['GetSourceDetail'] = request.get_source_detail
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
        if not DaraCore.is_null(request.source_dbcluster_description):
            query['SourceDBClusterDescription'] = request.source_dbcluster_description
        if not DaraCore.is_null(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not DaraCore.is_null(request.source_dbtype):
            query['SourceDBType'] = request.source_dbtype
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncJobList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_job_list_with_options_async(
        self,
        request: main_models.DescribeSyncJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.get_source_detail):
            query['GetSourceDetail'] = request.get_source_detail
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
        if not DaraCore.is_null(request.source_dbcluster_description):
            query['SourceDBClusterDescription'] = request.source_dbcluster_description
        if not DaraCore.is_null(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not DaraCore.is_null(request.source_dbtype):
            query['SourceDBType'] = request.source_dbtype
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncJobList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_job_list(
        self,
        request: main_models.DescribeSyncJobListRequest,
    ) -> main_models.DescribeSyncJobListResponse:
        runtime = RuntimeOptions()
        return self.describe_sync_job_list_with_options(request, runtime)

    async def describe_sync_job_list_async(
        self,
        request: main_models.DescribeSyncJobListRequest,
    ) -> main_models.DescribeSyncJobListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sync_job_list_with_options_async(request, runtime)

    def describe_table_access_count_with_options(
        self,
        request: main_models.DescribeTableAccessCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableAccessCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableAccessCount',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableAccessCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_access_count_with_options_async(
        self,
        request: main_models.DescribeTableAccessCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableAccessCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableAccessCount',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableAccessCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_access_count(
        self,
        request: main_models.DescribeTableAccessCountRequest,
    ) -> main_models.DescribeTableAccessCountResponse:
        runtime = RuntimeOptions()
        return self.describe_table_access_count_with_options(request, runtime)

    async def describe_table_access_count_async(
        self,
        request: main_models.DescribeTableAccessCountRequest,
    ) -> main_models.DescribeTableAccessCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_table_access_count_with_options_async(request, runtime)

    def describe_table_detail_with_options(
        self,
        request: main_models.DescribeTableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableDetail',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_detail_with_options_async(
        self,
        request: main_models.DescribeTableDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableDetail',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_detail(
        self,
        request: main_models.DescribeTableDetailRequest,
    ) -> main_models.DescribeTableDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_table_detail_with_options(request, runtime)

    async def describe_table_detail_async(
        self,
        request: main_models.DescribeTableDetailRequest,
    ) -> main_models.DescribeTableDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_table_detail_with_options_async(request, runtime)

    def describe_table_partition_diagnose_with_options(
        self,
        request: main_models.DescribeTablePartitionDiagnoseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablePartitionDiagnoseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTablePartitionDiagnose',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablePartitionDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_partition_diagnose_with_options_async(
        self,
        request: main_models.DescribeTablePartitionDiagnoseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablePartitionDiagnoseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTablePartitionDiagnose',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablePartitionDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_partition_diagnose(
        self,
        request: main_models.DescribeTablePartitionDiagnoseRequest,
    ) -> main_models.DescribeTablePartitionDiagnoseResponse:
        runtime = RuntimeOptions()
        return self.describe_table_partition_diagnose_with_options(request, runtime)

    async def describe_table_partition_diagnose_async(
        self,
        request: main_models.DescribeTablePartitionDiagnoseRequest,
    ) -> main_models.DescribeTablePartitionDiagnoseResponse:
        runtime = RuntimeOptions()
        return await self.describe_table_partition_diagnose_with_options_async(request, runtime)

    def describe_table_statistics_with_options(
        self,
        request: main_models.DescribeTableStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableStatistics',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_statistics_with_options_async(
        self,
        request: main_models.DescribeTableStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTableStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableStatistics',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTableStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_statistics(
        self,
        request: main_models.DescribeTableStatisticsRequest,
    ) -> main_models.DescribeTableStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_table_statistics_with_options(request, runtime)

    async def describe_table_statistics_async(
        self,
        request: main_models.DescribeTableStatisticsRequest,
    ) -> main_models.DescribeTableStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_table_statistics_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: main_models.DescribeTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: main_models.DescribeTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: main_models.DescribeTablesRequest,
    ) -> main_models.DescribeTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: main_models.DescribeTablesRequest,
    ) -> main_models.DescribeTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_task_info_with_options(
        self,
        request: main_models.DescribeTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskInfo',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_info_with_options_async(
        self,
        request: main_models.DescribeTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskInfo',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_info(
        self,
        request: main_models.DescribeTaskInfoRequest,
    ) -> main_models.DescribeTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_task_info_with_options(request, runtime)

    async def describe_task_info_async(
        self,
        request: main_models.DescribeTaskInfoRequest,
    ) -> main_models.DescribeTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_task_info_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: main_models.DescribeVSwitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVSwitchesResponse:
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vsw_id):
            query['VswId'] = request.vsw_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVSwitches',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: main_models.DescribeVSwitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVSwitchesResponse:
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vsw_id):
            query['VswId'] = request.vsw_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVSwitches',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: main_models.DescribeVSwitchesRequest,
    ) -> main_models.DescribeVSwitchesResponse:
        runtime = RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: main_models.DescribeVSwitchesRequest,
    ) -> main_models.DescribeVSwitchesResponse:
        runtime = RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_vswitchs_with_options(
        self,
        request: main_models.DescribeVSwitchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVSwitchsResponse:
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVSwitchs',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVSwitchsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitchs_with_options_async(
        self,
        request: main_models.DescribeVSwitchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVSwitchsResponse:
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVSwitchs',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVSwitchsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitchs(
        self,
        request: main_models.DescribeVSwitchsRequest,
    ) -> main_models.DescribeVSwitchsResponse:
        runtime = RuntimeOptions()
        return self.describe_vswitchs_with_options(request, runtime)

    async def describe_vswitchs_async(
        self,
        request: main_models.DescribeVSwitchsRequest,
    ) -> main_models.DescribeVSwitchsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vswitchs_with_options_async(request, runtime)

    def describe_vpcs_with_options(
        self,
        request: main_models.DescribeVpcsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcsResponse:
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcs',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: main_models.DescribeVpcsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcsResponse:
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcs',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpcs(
        self,
        request: main_models.DescribeVpcsRequest,
    ) -> main_models.DescribeVpcsResponse:
        runtime = RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: main_models.DescribeVpcsRequest,
    ) -> main_models.DescribeVpcsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def describe_worker_detection_with_options(
        self,
        request: main_models.DescribeWorkerDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWorkerDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWorkerDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWorkerDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_worker_detection_with_options_async(
        self,
        request: main_models.DescribeWorkerDetectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWorkerDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWorkerDetection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWorkerDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_worker_detection(
        self,
        request: main_models.DescribeWorkerDetectionRequest,
    ) -> main_models.DescribeWorkerDetectionResponse:
        runtime = RuntimeOptions()
        return self.describe_worker_detection_with_options(request, runtime)

    async def describe_worker_detection_async(
        self,
        request: main_models.DescribeWorkerDetectionRequest,
    ) -> main_models.DescribeWorkerDetectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_worker_detection_with_options_async(request, runtime)

    def detach_user_eniwith_options(
        self,
        request: main_models.DetachUserENIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachUserENIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachUserENI',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachUserENIResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_user_eniwith_options_async(
        self,
        request: main_models.DetachUserENIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachUserENIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachUserENI',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachUserENIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_user_eni(
        self,
        request: main_models.DetachUserENIRequest,
    ) -> main_models.DetachUserENIResponse:
        runtime = RuntimeOptions()
        return self.detach_user_eniwith_options(request, runtime)

    async def detach_user_eni_async(
        self,
        request: main_models.DetachUserENIRequest,
    ) -> main_models.DetachUserENIResponse:
        runtime = RuntimeOptions()
        return await self.detach_user_eniwith_options_async(request, runtime)

    def disable_advice_service_with_options(
        self,
        request: main_models.DisableAdviceServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAdviceServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAdviceService',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAdviceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_advice_service_with_options_async(
        self,
        request: main_models.DisableAdviceServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAdviceServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAdviceService',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAdviceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_advice_service(
        self,
        request: main_models.DisableAdviceServiceRequest,
    ) -> main_models.DisableAdviceServiceResponse:
        runtime = RuntimeOptions()
        return self.disable_advice_service_with_options(request, runtime)

    async def disable_advice_service_async(
        self,
        request: main_models.DisableAdviceServiceRequest,
    ) -> main_models.DisableAdviceServiceResponse:
        runtime = RuntimeOptions()
        return await self.disable_advice_service_with_options_async(request, runtime)

    def download_diagnosis_records_with_options(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not DaraCore.is_null(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not DaraCore.is_null(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not DaraCore.is_null(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadDiagnosisRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_diagnosis_records_with_options_async(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not DaraCore.is_null(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not DaraCore.is_null(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not DaraCore.is_null(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not DaraCore.is_null(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadDiagnosisRecords',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_diagnosis_records(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    async def download_diagnosis_records_async(
        self,
        request: main_models.DownloadDiagnosisRecordsRequest,
    ) -> main_models.DownloadDiagnosisRecordsResponse:
        runtime = RuntimeOptions()
        return await self.download_diagnosis_records_with_options_async(request, runtime)

    def enable_advice_service_with_options(
        self,
        request: main_models.EnableAdviceServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAdviceServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAdviceService',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAdviceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_advice_service_with_options_async(
        self,
        request: main_models.EnableAdviceServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAdviceServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAdviceService',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAdviceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_advice_service(
        self,
        request: main_models.EnableAdviceServiceRequest,
    ) -> main_models.EnableAdviceServiceResponse:
        runtime = RuntimeOptions()
        return self.enable_advice_service_with_options(request, runtime)

    async def enable_advice_service_async(
        self,
        request: main_models.EnableAdviceServiceRequest,
    ) -> main_models.EnableAdviceServiceResponse:
        runtime = RuntimeOptions()
        return await self.enable_advice_service_with_options_async(request, runtime)

    def get_create_table_sqlwith_options(
        self,
        request: main_models.GetCreateTableSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateTableSQLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateTableSQL',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateTableSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_table_sqlwith_options_async(
        self,
        request: main_models.GetCreateTableSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateTableSQLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateTableSQL',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateTableSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_table_sql(
        self,
        request: main_models.GetCreateTableSQLRequest,
    ) -> main_models.GetCreateTableSQLResponse:
        runtime = RuntimeOptions()
        return self.get_create_table_sqlwith_options(request, runtime)

    async def get_create_table_sql_async(
        self,
        request: main_models.GetCreateTableSQLRequest,
    ) -> main_models.GetCreateTableSQLResponse:
        runtime = RuntimeOptions()
        return await self.get_create_table_sqlwith_options_async(request, runtime)

    def grant_operator_permission_with_options(
        self,
        request: main_models.GrantOperatorPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantOperatorPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.privileges):
            query['Privileges'] = request.privileges
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantOperatorPermission',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_operator_permission_with_options_async(
        self,
        request: main_models.GrantOperatorPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantOperatorPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.privileges):
            query['Privileges'] = request.privileges
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantOperatorPermission',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_operator_permission(
        self,
        request: main_models.GrantOperatorPermissionRequest,
    ) -> main_models.GrantOperatorPermissionResponse:
        runtime = RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    async def grant_operator_permission_async(
        self,
        request: main_models.GrantOperatorPermissionRequest,
    ) -> main_models.GrantOperatorPermissionResponse:
        runtime = RuntimeOptions()
        return await self.grant_operator_permission_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: main_models.KillProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillProcess',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: main_models.KillProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillProcess',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process(
        self,
        request: main_models.KillProcessRequest,
    ) -> main_models.KillProcessResponse:
        runtime = RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: main_models.KillProcessRequest,
    ) -> main_models.KillProcessResponse:
        runtime = RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

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
            version = '2019-03-15',
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
            version = '2019-03-15',
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

    def migrate_dbcluster_with_options(
        self,
        request: main_models.MigrateDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_form):
            query['ProductForm'] = request.product_form
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not DaraCore.is_null(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.shard_number):
            query['ShardNumber'] = request.shard_number
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not DaraCore.is_null(request.storage_resource_size):
            query['StorageResourceSize'] = request.storage_resource_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_dbcluster_with_options_async(
        self,
        request: main_models.MigrateDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_form):
            query['ProductForm'] = request.product_form
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not DaraCore.is_null(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.shard_number):
            query['ShardNumber'] = request.shard_number
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not DaraCore.is_null(request.storage_resource_size):
            query['StorageResourceSize'] = request.storage_resource_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_dbcluster(
        self,
        request: main_models.MigrateDBClusterRequest,
    ) -> main_models.MigrateDBClusterResponse:
        runtime = RuntimeOptions()
        return self.migrate_dbcluster_with_options(request, runtime)

    async def migrate_dbcluster_async(
        self,
        request: main_models.MigrateDBClusterRequest,
    ) -> main_models.MigrateDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.migrate_dbcluster_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
    ) -> main_models.ModifyAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
    ) -> main_models.ModifyAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_active_operation_maintain_conf_with_options(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle_time):
            query['CycleTime'] = request.cycle_time
        if not DaraCore.is_null(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintainConf',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_maintain_conf_with_options_async(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle_time):
            query['CycleTime'] = request.cycle_time
        if not DaraCore.is_null(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintainConf',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_maintain_conf(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return self.modify_active_operation_maintain_conf_with_options(request, runtime)

    async def modify_active_operation_maintain_conf_async(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return await self.modify_active_operation_maintain_conf_with_options_async(request, runtime)

    def modify_active_operation_tasks_with_options(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_tasks_with_options_async(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_tasks(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    async def modify_active_operation_tasks_async(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return await self.modify_active_operation_tasks_with_options_async(request, runtime)

    def modify_audit_log_config_with_options(
        self,
        request: main_models.ModifyAuditLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAuditLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_log_status):
            query['AuditLogStatus'] = request.audit_log_status
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'ModifyAuditLogConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_config_with_options_async(
        self,
        request: main_models.ModifyAuditLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAuditLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_log_status):
            query['AuditLogStatus'] = request.audit_log_status
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            action = 'ModifyAuditLogConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_config(
        self,
        request: main_models.ModifyAuditLogConfigRequest,
    ) -> main_models.ModifyAuditLogConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    async def modify_audit_log_config_async(
        self,
        request: main_models.ModifyAuditLogConfigRequest,
    ) -> main_models.ModifyAuditLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_audit_log_config_with_options_async(request, runtime)

    def modify_auto_renew_attribute_with_options(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoRenewAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_renew_attribute_with_options_async(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoRenewAttribute',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_renew_attribute(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_auto_renew_attribute_with_options(request, runtime)

    async def modify_auto_renew_attribute_async(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_auto_renew_attribute_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: main_models.ModifyBackupPolicyRequest,
    ) -> main_models.ModifyBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: main_models.ModifyBackupPolicyRequest,
    ) -> main_models.ModifyBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_cluster_connection_string_with_options(
        self,
        request: main_models.ModifyClusterConnectionStringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterConnectionStringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterConnectionString',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_connection_string_with_options_async(
        self,
        request: main_models.ModifyClusterConnectionStringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterConnectionStringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterConnectionString',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_connection_string(
        self,
        request: main_models.ModifyClusterConnectionStringRequest,
    ) -> main_models.ModifyClusterConnectionStringResponse:
        runtime = RuntimeOptions()
        return self.modify_cluster_connection_string_with_options(request, runtime)

    async def modify_cluster_connection_string_async(
        self,
        request: main_models.ModifyClusterConnectionStringRequest,
    ) -> main_models.ModifyClusterConnectionStringResponse:
        runtime = RuntimeOptions()
        return await self.modify_cluster_connection_string_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: main_models.ModifyDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.disk_performance_level):
            query['DiskPerformanceLevel'] = request.disk_performance_level
        if not DaraCore.is_null(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not DaraCore.is_null(request.elastic_ioresource_size):
            query['ElasticIOResourceSize'] = request.elastic_ioresource_size
        if not DaraCore.is_null(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
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
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: main_models.ModifyDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.disk_performance_level):
            query['DiskPerformanceLevel'] = request.disk_performance_level
        if not DaraCore.is_null(request.elastic_ioresource):
            query['ElasticIOResource'] = request.elastic_ioresource
        if not DaraCore.is_null(request.elastic_ioresource_size):
            query['ElasticIOResourceSize'] = request.elastic_ioresource_size
        if not DaraCore.is_null(request.executor_count):
            query['ExecutorCount'] = request.executor_count
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
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
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: main_models.ModifyDBClusterRequest,
    ) -> main_models.ModifyDBClusterResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: main_models.ModifyDBClusterRequest,
    ) -> main_models.ModifyDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_access_white_list_with_options(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not DaraCore.is_null(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterAccessWhiteList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_access_white_list_with_options_async(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not DaraCore.is_null(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterAccessWhiteList',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_access_white_list(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    async def modify_dbcluster_access_white_list_async(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_access_white_list_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterDescription',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterDescription',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterMaintainTime',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterMaintainTime',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbcluster_pay_type_with_options(
        self,
        request: main_models.ModifyDBClusterPayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterPayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterPayType',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_pay_type_with_options_async(
        self,
        request: main_models.ModifyDBClusterPayTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterPayTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterPayType',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterPayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_pay_type(
        self,
        request: main_models.ModifyDBClusterPayTypeRequest,
    ) -> main_models.ModifyDBClusterPayTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_pay_type_with_options(request, runtime)

    async def modify_dbcluster_pay_type_async(
        self,
        request: main_models.ModifyDBClusterPayTypeRequest,
    ) -> main_models.ModifyDBClusterPayTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_pay_type_with_options_async(request, runtime)

    def modify_dbcluster_resource_group_with_options(
        self,
        request: main_models.ModifyDBClusterResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_resource_group_with_options_async(
        self,
        request: main_models.ModifyDBClusterResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_resource_group(
        self,
        request: main_models.ModifyDBClusterResourceGroupRequest,
    ) -> main_models.ModifyDBClusterResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_resource_group_with_options(request, runtime)

    async def modify_dbcluster_resource_group_async(
        self,
        request: main_models.ModifyDBClusterResourceGroupRequest,
    ) -> main_models.ModifyDBClusterResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_resource_group_with_options_async(request, runtime)

    def modify_dbcluster_sslwith_options(
        self,
        request: main_models.ModifyDBClusterSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterSSL',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_sslwith_options_async(
        self,
        request: main_models.ModifyDBClusterSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterSSL',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_ssl(
        self,
        request: main_models.ModifyDBClusterSSLRequest,
    ) -> main_models.ModifyDBClusterSSLResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_sslwith_options(request, runtime)

    async def modify_dbcluster_ssl_async(
        self,
        request: main_models.ModifyDBClusterSSLRequest,
    ) -> main_models.ModifyDBClusterSSLResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_sslwith_options_async(request, runtime)

    def modify_dbcluster_shard_number_with_options(
        self,
        request: main_models.ModifyDBClusterShardNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterShardNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_shard_number):
            query['NewShardNumber'] = request.new_shard_number
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
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterShardNumber',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterShardNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_shard_number_with_options_async(
        self,
        request: main_models.ModifyDBClusterShardNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterShardNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_shard_number):
            query['NewShardNumber'] = request.new_shard_number
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
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterShardNumber',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterShardNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_shard_number(
        self,
        request: main_models.ModifyDBClusterShardNumberRequest,
    ) -> main_models.ModifyDBClusterShardNumberResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_shard_number_with_options(request, runtime)

    async def modify_dbcluster_shard_number_async(
        self,
        request: main_models.ModifyDBClusterShardNumberRequest,
    ) -> main_models.ModifyDBClusterShardNumberResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_shard_number_with_options_async(request, runtime)

    def modify_dbcluster_vip_with_options(
        self,
        request: main_models.ModifyDBClusterVipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterVipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterVip',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterVipResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_vip_with_options_async(
        self,
        request: main_models.ModifyDBClusterVipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterVipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterVip',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterVipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_vip(
        self,
        request: main_models.ModifyDBClusterVipRequest,
    ) -> main_models.ModifyDBClusterVipResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_vip_with_options(request, runtime)

    async def modify_dbcluster_vip_async(
        self,
        request: main_models.ModifyDBClusterVipRequest,
    ) -> main_models.ModifyDBClusterVipResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_vip_with_options_async(request, runtime)

    def modify_dbresource_group_with_options(
        self,
        tmp_req: main_models.ModifyDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBResourceGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyDBResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.engine_params):
            request.engine_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        if not DaraCore.is_null(tmp_req.pool_user_list):
            request.pool_user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.pool_user_list, 'PoolUserList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_user_list_shrink):
            query['PoolUserList'] = request.pool_user_list_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbresource_group_with_options_async(
        self,
        tmp_req: main_models.ModifyDBResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBResourceGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyDBResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.engine_params):
            request.engine_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.engine_params, 'EngineParams', 'json')
        if not DaraCore.is_null(tmp_req.pool_user_list):
            request.pool_user_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.pool_user_list, 'PoolUserList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_user_list_shrink):
            query['PoolUserList'] = request.pool_user_list_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourceGroup',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbresource_group(
        self,
        request: main_models.ModifyDBResourceGroupRequest,
    ) -> main_models.ModifyDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_dbresource_group_with_options(request, runtime)

    async def modify_dbresource_group_async(
        self,
        request: main_models.ModifyDBResourceGroupRequest,
    ) -> main_models.ModifyDBResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbresource_group_with_options_async(request, runtime)

    def modify_dbresource_pool_with_options(
        self,
        request: main_models.ModifyDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbresource_pool_with_options_async(
        self,
        request: main_models.ModifyDBResourcePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBResourcePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.node_num):
            query['NodeNum'] = request.node_num
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourcePool',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbresource_pool(
        self,
        request: main_models.ModifyDBResourcePoolRequest,
    ) -> main_models.ModifyDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return self.modify_dbresource_pool_with_options(request, runtime)

    async def modify_dbresource_pool_async(
        self,
        request: main_models.ModifyDBResourcePoolRequest,
    ) -> main_models.ModifyDBResourcePoolResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbresource_pool_with_options_async(request, runtime)

    def modify_elastic_plan_with_options(
        self,
        request: main_models.ModifyElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not DaraCore.is_null(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not DaraCore.is_null(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not DaraCore.is_null(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not DaraCore.is_null(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not DaraCore.is_null(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not DaraCore.is_null(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not DaraCore.is_null(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not DaraCore.is_null(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_plan_with_options_async(
        self,
        request: main_models.ModifyElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_enable):
            query['ElasticPlanEnable'] = request.elastic_plan_enable
        if not DaraCore.is_null(request.elastic_plan_end_day):
            query['ElasticPlanEndDay'] = request.elastic_plan_end_day
        if not DaraCore.is_null(request.elastic_plan_monthly_repeat):
            query['ElasticPlanMonthlyRepeat'] = request.elastic_plan_monthly_repeat
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.elastic_plan_node_num):
            query['ElasticPlanNodeNum'] = request.elastic_plan_node_num
        if not DaraCore.is_null(request.elastic_plan_start_day):
            query['ElasticPlanStartDay'] = request.elastic_plan_start_day
        if not DaraCore.is_null(request.elastic_plan_time_end):
            query['ElasticPlanTimeEnd'] = request.elastic_plan_time_end
        if not DaraCore.is_null(request.elastic_plan_time_start):
            query['ElasticPlanTimeStart'] = request.elastic_plan_time_start
        if not DaraCore.is_null(request.elastic_plan_type):
            query['ElasticPlanType'] = request.elastic_plan_type
        if not DaraCore.is_null(request.elastic_plan_weekly_repeat):
            query['ElasticPlanWeeklyRepeat'] = request.elastic_plan_weekly_repeat
        if not DaraCore.is_null(request.elastic_plan_worker_spec):
            query['ElasticPlanWorkerSpec'] = request.elastic_plan_worker_spec
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_pool_name):
            query['ResourcePoolName'] = request.resource_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticPlan',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_plan(
        self,
        request: main_models.ModifyElasticPlanRequest,
    ) -> main_models.ModifyElasticPlanResponse:
        runtime = RuntimeOptions()
        return self.modify_elastic_plan_with_options(request, runtime)

    async def modify_elastic_plan_async(
        self,
        request: main_models.ModifyElasticPlanRequest,
    ) -> main_models.ModifyElasticPlanResponse:
        runtime = RuntimeOptions()
        return await self.modify_elastic_plan_with_options_async(request, runtime)

    def modify_log_backup_policy_with_options(
        self,
        request: main_models.ModifyLogBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogBackupPolicy',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_backup_policy_with_options_async(
        self,
        request: main_models.ModifyLogBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogBackupPolicy',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_backup_policy(
        self,
        request: main_models.ModifyLogBackupPolicyRequest,
    ) -> main_models.ModifyLogBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_log_backup_policy_with_options(request, runtime)

    async def modify_log_backup_policy_async(
        self,
        request: main_models.ModifyLogBackupPolicyRequest,
    ) -> main_models.ModifyLogBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_log_backup_policy_with_options_async(request, runtime)

    def modify_log_hub_status_with_options(
        self,
        request: main_models.ModifyLogHubStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogHubStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogHubStatus',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogHubStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_hub_status_with_options_async(
        self,
        request: main_models.ModifyLogHubStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogHubStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogHubStatus',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogHubStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_hub_status(
        self,
        request: main_models.ModifyLogHubStatusRequest,
    ) -> main_models.ModifyLogHubStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_log_hub_status_with_options(request, runtime)

    async def modify_log_hub_status_async(
        self,
        request: main_models.ModifyLogHubStatusRequest,
    ) -> main_models.ModifyLogHubStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_log_hub_status_with_options_async(request, runtime)

    def modify_maintenance_action_with_options(
        self,
        request: main_models.ModifyMaintenanceActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaintenanceActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
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
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaintenanceAction',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaintenanceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_maintenance_action_with_options_async(
        self,
        request: main_models.ModifyMaintenanceActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaintenanceActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
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
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaintenanceAction',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaintenanceActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_maintenance_action(
        self,
        request: main_models.ModifyMaintenanceActionRequest,
    ) -> main_models.ModifyMaintenanceActionResponse:
        runtime = RuntimeOptions()
        return self.modify_maintenance_action_with_options(request, runtime)

    async def modify_maintenance_action_async(
        self,
        request: main_models.ModifyMaintenanceActionRequest,
    ) -> main_models.ModifyMaintenanceActionResponse:
        runtime = RuntimeOptions()
        return await self.modify_maintenance_action_with_options_async(request, runtime)

    def modify_resubmit_config_with_options(
        self,
        tmp_req: main_models.ModifyResubmitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResubmitConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyResubmitConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResubmitConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResubmitConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resubmit_config_with_options_async(
        self,
        tmp_req: main_models.ModifyResubmitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResubmitConfigResponse:
        tmp_req.validate()
        request = main_models.ModifyResubmitConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResubmitConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResubmitConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resubmit_config(
        self,
        request: main_models.ModifyResubmitConfigRequest,
    ) -> main_models.ModifyResubmitConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_resubmit_config_with_options(request, runtime)

    async def modify_resubmit_config_async(
        self,
        request: main_models.ModifyResubmitConfigRequest,
    ) -> main_models.ModifyResubmitConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_resubmit_config_with_options_async(request, runtime)

    def modify_sqaconfig_with_options(
        self,
        request: main_models.ModifySQAConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySQAConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sqastatus):
            query['SQAStatus'] = request.sqastatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySQAConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySQAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sqaconfig_with_options_async(
        self,
        request: main_models.ModifySQAConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySQAConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sqastatus):
            query['SQAStatus'] = request.sqastatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySQAConfig',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySQAConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sqaconfig(
        self,
        request: main_models.ModifySQAConfigRequest,
    ) -> main_models.ModifySQAConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_sqaconfig_with_options(request, runtime)

    async def modify_sqaconfig_async(
        self,
        request: main_models.ModifySQAConfigRequest,
    ) -> main_models.ModifySQAConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_sqaconfig_with_options_async(request, runtime)

    def modify_sync_job_with_options(
        self,
        request: main_models.ModifySyncJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySyncJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not DaraCore.is_null(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySyncJob',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySyncJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sync_job_with_options_async(
        self,
        request: main_models.ModifySyncJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySyncJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        if not DaraCore.is_null(request.source_dbcluster):
            query['SourceDBCluster'] = request.source_dbcluster
        if not DaraCore.is_null(request.sync_platform):
            query['SyncPlatform'] = request.sync_platform
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySyncJob',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySyncJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sync_job(
        self,
        request: main_models.ModifySyncJobRequest,
    ) -> main_models.ModifySyncJobResponse:
        runtime = RuntimeOptions()
        return self.modify_sync_job_with_options(request, runtime)

    async def modify_sync_job_async(
        self,
        request: main_models.ModifySyncJobRequest,
    ) -> main_models.ModifySyncJobResponse:
        runtime = RuntimeOptions()
        return await self.modify_sync_job_with_options_async(request, runtime)

    def operate_log_hub_with_options(
        self,
        request: main_models.OperateLogHubRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateLogHubResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create):
            query['Create'] = request.create
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not DaraCore.is_null(request.deliver_time):
            query['DeliverTime'] = request.deliver_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.filter_dirty_data):
            query['FilterDirtyData'] = request.filter_dirty_data
        if not DaraCore.is_null(request.log_hub_stores):
            query['LogHubStores'] = request.log_hub_stores
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateLogHub',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateLogHubResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_log_hub_with_options_async(
        self,
        request: main_models.OperateLogHubRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateLogHubResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create):
            query['Create'] = request.create
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.deliver_name):
            query['DeliverName'] = request.deliver_name
        if not DaraCore.is_null(request.deliver_time):
            query['DeliverTime'] = request.deliver_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.filter_dirty_data):
            query['FilterDirtyData'] = request.filter_dirty_data
        if not DaraCore.is_null(request.log_hub_stores):
            query['LogHubStores'] = request.log_hub_stores
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateLogHub',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateLogHubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_log_hub(
        self,
        request: main_models.OperateLogHubRequest,
    ) -> main_models.OperateLogHubResponse:
        runtime = RuntimeOptions()
        return self.operate_log_hub_with_options(request, runtime)

    async def operate_log_hub_async(
        self,
        request: main_models.OperateLogHubRequest,
    ) -> main_models.OperateLogHubResponse:
        runtime = RuntimeOptions()
        return await self.operate_log_hub_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseClusterPublicConnection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseClusterPublicConnection',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: main_models.ResetAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: main_models.ResetAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: main_models.ResetAccountPasswordRequest,
    ) -> main_models.ResetAccountPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: main_models.ResetAccountPasswordRequest,
    ) -> main_models.ResetAccountPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def revoke_operator_permission_with_options(
        self,
        request: main_models.RevokeOperatorPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeOperatorPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeOperatorPermission',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_operator_permission_with_options_async(
        self,
        request: main_models.RevokeOperatorPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeOperatorPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeOperatorPermission',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_operator_permission(
        self,
        request: main_models.RevokeOperatorPermissionRequest,
    ) -> main_models.RevokeOperatorPermissionResponse:
        runtime = RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    async def revoke_operator_permission_async(
        self,
        request: main_models.RevokeOperatorPermissionRequest,
    ) -> main_models.RevokeOperatorPermissionResponse:
        runtime = RuntimeOptions()
        return await self.revoke_operator_permission_with_options_async(request, runtime)

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
            version = '2019-03-15',
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
            version = '2019-03-15',
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

    def unbind_dbresource_group_with_user_with_options(
        self,
        request: main_models.UnbindDBResourceGroupWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDBResourceGroupWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourceGroupWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDBResourceGroupWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_dbresource_group_with_user_with_options_async(
        self,
        request: main_models.UnbindDBResourceGroupWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDBResourceGroupWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourceGroupWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDBResourceGroupWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_dbresource_group_with_user(
        self,
        request: main_models.UnbindDBResourceGroupWithUserRequest,
    ) -> main_models.UnbindDBResourceGroupWithUserResponse:
        runtime = RuntimeOptions()
        return self.unbind_dbresource_group_with_user_with_options(request, runtime)

    async def unbind_dbresource_group_with_user_async(
        self,
        request: main_models.UnbindDBResourceGroupWithUserRequest,
    ) -> main_models.UnbindDBResourceGroupWithUserResponse:
        runtime = RuntimeOptions()
        return await self.unbind_dbresource_group_with_user_with_options_async(request, runtime)

    def unbind_dbresource_pool_with_user_with_options(
        self,
        request: main_models.UnbindDBResourcePoolWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDBResourcePoolWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourcePoolWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDBResourcePoolWithUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_dbresource_pool_with_user_with_options_async(
        self,
        request: main_models.UnbindDBResourcePoolWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDBResourcePoolWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_name):
            query['PoolName'] = request.pool_name
        if not DaraCore.is_null(request.pool_user):
            query['PoolUser'] = request.pool_user
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourcePoolWithUser',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDBResourcePoolWithUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_dbresource_pool_with_user(
        self,
        request: main_models.UnbindDBResourcePoolWithUserRequest,
    ) -> main_models.UnbindDBResourcePoolWithUserResponse:
        runtime = RuntimeOptions()
        return self.unbind_dbresource_pool_with_user_with_options(request, runtime)

    async def unbind_dbresource_pool_with_user_async(
        self,
        request: main_models.UnbindDBResourcePoolWithUserRequest,
    ) -> main_models.UnbindDBResourcePoolWithUserResponse:
        runtime = RuntimeOptions()
        return await self.unbind_dbresource_pool_with_user_with_options_async(request, runtime)

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
            version = '2019-03-15',
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
            version = '2019-03-15',
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

    def upgrade_kernel_version_with_options(
        self,
        request: main_models.UpgradeKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeKernelVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_kernel_version_with_options_async(
        self,
        request: main_models.UpgradeKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeKernelVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_kernel_version(
        self,
        request: main_models.UpgradeKernelVersionRequest,
    ) -> main_models.UpgradeKernelVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_kernel_version_with_options(request, runtime)

    async def upgrade_kernel_version_async(
        self,
        request: main_models.UpgradeKernelVersionRequest,
    ) -> main_models.UpgradeKernelVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_kernel_version_with_options_async(request, runtime)
