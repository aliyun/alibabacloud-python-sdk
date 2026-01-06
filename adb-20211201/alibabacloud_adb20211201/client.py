# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_adb20211201 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateClusterPublicConnection',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateClusterPublicConnection',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachUserENI',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachUserENI',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def bind_account_with_options(
        self,
        request: main_models.BindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.ram_user):
            query['RamUser'] = request.ram_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_account_with_options_async(
        self,
        request: main_models.BindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.ram_user):
            query['RamUser'] = request.ram_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_account(
        self,
        request: main_models.BindAccountRequest,
    ) -> main_models.BindAccountResponse:
        runtime = RuntimeOptions()
        return self.bind_account_with_options(request, runtime)

    async def bind_account_async(
        self,
        request: main_models.BindAccountRequest,
    ) -> main_models.BindAccountResponse:
        runtime = RuntimeOptions()
        return await self.bind_account_with_options_async(request, runtime)

    def bind_dbresource_group_with_user_with_options(
        self,
        request: main_models.BindDBResourceGroupWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDBResourceGroupWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourceGroupWithUser',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDBResourceGroupWithUser',
            version = '2021-12-01',
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

    def cancel_spark_repl_statement_with_options(
        self,
        request: main_models.CancelSparkReplStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSparkReplStatementResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelSparkReplStatement',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSparkReplStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_spark_repl_statement_with_options_async(
        self,
        request: main_models.CancelSparkReplStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSparkReplStatementResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelSparkReplStatement',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSparkReplStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_spark_repl_statement(
        self,
        request: main_models.CancelSparkReplStatementRequest,
    ) -> main_models.CancelSparkReplStatementResponse:
        runtime = RuntimeOptions()
        return self.cancel_spark_repl_statement_with_options(request, runtime)

    async def cancel_spark_repl_statement_async(
        self,
        request: main_models.CancelSparkReplStatementRequest,
    ) -> main_models.CancelSparkReplStatementResponse:
        runtime = RuntimeOptions()
        return await self.cancel_spark_repl_statement_with_options_async(request, runtime)

    def cancel_spark_warehouse_batch_sqlwith_options(
        self,
        request: main_models.CancelSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agency):
            body['Agency'] = request.agency
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.query_id):
            body['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSparkWarehouseBatchSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_spark_warehouse_batch_sqlwith_options_async(
        self,
        request: main_models.CancelSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agency):
            body['Agency'] = request.agency
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.query_id):
            body['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSparkWarehouseBatchSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_spark_warehouse_batch_sql(
        self,
        request: main_models.CancelSparkWarehouseBatchSQLRequest,
    ) -> main_models.CancelSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return self.cancel_spark_warehouse_batch_sqlwith_options(request, runtime)

    async def cancel_spark_warehouse_batch_sql_async(
        self,
        request: main_models.CancelSparkWarehouseBatchSQLRequest,
    ) -> main_models.CancelSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return await self.cancel_spark_warehouse_batch_sqlwith_options_async(request, runtime)

    def check_bind_ram_user_with_options(
        self,
        request: main_models.CheckBindRamUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckBindRamUserResponse:
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
            action = 'CheckBindRamUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckBindRamUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_bind_ram_user_with_options_async(
        self,
        request: main_models.CheckBindRamUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckBindRamUserResponse:
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
            action = 'CheckBindRamUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckBindRamUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_bind_ram_user(
        self,
        request: main_models.CheckBindRamUserRequest,
    ) -> main_models.CheckBindRamUserResponse:
        runtime = RuntimeOptions()
        return self.check_bind_ram_user_with_options(request, runtime)

    async def check_bind_ram_user_async(
        self,
        request: main_models.CheckBindRamUserRequest,
    ) -> main_models.CheckBindRamUserResponse:
        runtime = RuntimeOptions()
        return await self.check_bind_ram_user_with_options_async(request, runtime)

    def check_sample_data_set_with_options(
        self,
        request: main_models.CheckSampleDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSampleDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSampleDataSet',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSampleDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sample_data_set_with_options_async(
        self,
        request: main_models.CheckSampleDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSampleDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSampleDataSet',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSampleDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sample_data_set(
        self,
        request: main_models.CheckSampleDataSetRequest,
    ) -> main_models.CheckSampleDataSetResponse:
        runtime = RuntimeOptions()
        return self.check_sample_data_set_with_options(request, runtime)

    async def check_sample_data_set_async(
        self,
        request: main_models.CheckSampleDataSetRequest,
    ) -> main_models.CheckSampleDataSetResponse:
        runtime = RuntimeOptions()
        return await self.check_sample_data_set_with_options_async(request, runtime)

    def configure_result_export_with_options(
        self,
        tmp_req: main_models.ConfigureResultExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureResultExportResponse:
        tmp_req.validate()
        request = main_models.ConfigureResultExportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.oss_info):
            request.oss_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.oss_info, 'OssInfo', 'json')
        if not DaraCore.is_null(tmp_req.sls_info):
            request.sls_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sls_info, 'SlsInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.oss_info_shrink):
            body['OssInfo'] = request.oss_info_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_info_shrink):
            body['SlsInfo'] = request.sls_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureResultExport',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureResultExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_result_export_with_options_async(
        self,
        tmp_req: main_models.ConfigureResultExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureResultExportResponse:
        tmp_req.validate()
        request = main_models.ConfigureResultExportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.oss_info):
            request.oss_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.oss_info, 'OssInfo', 'json')
        if not DaraCore.is_null(tmp_req.sls_info):
            request.sls_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sls_info, 'SlsInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.oss_info_shrink):
            body['OssInfo'] = request.oss_info_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_info_shrink):
            body['SlsInfo'] = request.sls_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureResultExport',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureResultExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_result_export(
        self,
        request: main_models.ConfigureResultExportRequest,
    ) -> main_models.ConfigureResultExportResponse:
        runtime = RuntimeOptions()
        return self.configure_result_export_with_options(request, runtime)

    async def configure_result_export_async(
        self,
        request: main_models.ConfigureResultExportRequest,
    ) -> main_models.ConfigureResultExportResponse:
        runtime = RuntimeOptions()
        return await self.configure_result_export_with_options_async(request, runtime)

    def create_apsjob_with_options(
        self,
        request: main_models.CreateAPSJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAPSJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_name):
            body['ApsJobName'] = request.aps_job_name
        if not DaraCore.is_null(request.db_list):
            body['DbList'] = request.db_list
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            body['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_password):
            body['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            body['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.partition_list):
            body['PartitionList'] = request.partition_list
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            body['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_password):
            body['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_region):
            body['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            body['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.target_table_mode):
            body['TargetTableMode'] = request.target_table_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAPSJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAPSJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_apsjob_with_options_async(
        self,
        request: main_models.CreateAPSJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAPSJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_name):
            body['ApsJobName'] = request.aps_job_name
        if not DaraCore.is_null(request.db_list):
            body['DbList'] = request.db_list
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            body['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_password):
            body['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            body['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.partition_list):
            body['PartitionList'] = request.partition_list
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            body['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_password):
            body['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_region):
            body['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            body['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.target_table_mode):
            body['TargetTableMode'] = request.target_table_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAPSJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAPSJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_apsjob(
        self,
        request: main_models.CreateAPSJobRequest,
    ) -> main_models.CreateAPSJobResponse:
        runtime = RuntimeOptions()
        return self.create_apsjob_with_options(request, runtime)

    async def create_apsjob_async(
        self,
        request: main_models.CreateAPSJobRequest,
    ) -> main_models.CreateAPSJobResponse:
        runtime = RuntimeOptions()
        return await self.create_apsjob_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2021-12-01',
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
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2021-12-01',
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

    def create_aps_copy_workload_with_options(
        self,
        request: main_models.CreateApsCopyWorkloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsCopyWorkloadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        if not DaraCore.is_null(request.workload_type):
            body['WorkloadType'] = request.workload_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsCopyWorkload',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsCopyWorkloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aps_copy_workload_with_options_async(
        self,
        request: main_models.CreateApsCopyWorkloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsCopyWorkloadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        if not DaraCore.is_null(request.workload_type):
            body['WorkloadType'] = request.workload_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsCopyWorkload',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsCopyWorkloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aps_copy_workload(
        self,
        request: main_models.CreateApsCopyWorkloadRequest,
    ) -> main_models.CreateApsCopyWorkloadResponse:
        runtime = RuntimeOptions()
        return self.create_aps_copy_workload_with_options(request, runtime)

    async def create_aps_copy_workload_async(
        self,
        request: main_models.CreateApsCopyWorkloadRequest,
    ) -> main_models.CreateApsCopyWorkloadResponse:
        runtime = RuntimeOptions()
        return await self.create_aps_copy_workload_with_options_async(request, runtime)

    def create_aps_datasoure_with_options(
        self,
        tmp_req: main_models.CreateApsDatasoureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsDatasoureResponse:
        tmp_req.validate()
        request = main_models.CreateApsDatasoureShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.databricks_info):
            request.databricks_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.databricks_info, 'DatabricksInfo', 'json')
        if not DaraCore.is_null(tmp_req.hive_info):
            request.hive_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.hive_info, 'HiveInfo', 'json')
        if not DaraCore.is_null(tmp_req.kafka_info):
            request.kafka_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.kafka_info, 'KafkaInfo', 'json')
        if not DaraCore.is_null(tmp_req.polar_dbmysql_info):
            request.polar_dbmysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.polar_dbmysql_info, 'PolarDBMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.polar_dbxinfo):
            request.polar_dbxinfo_shrink = Utils.array_to_string_with_specified_style(tmp_req.polar_dbxinfo, 'PolarDBXInfo', 'json')
        if not DaraCore.is_null(tmp_req.rds_mysql_info):
            request.rds_mysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.rds_mysql_info, 'RdsMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.sls_info):
            request.sls_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sls_info, 'SlsInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.databricks_info_shrink):
            body['DatabricksInfo'] = request.databricks_info_shrink
        if not DaraCore.is_null(request.datasource_description):
            body['DatasourceDescription'] = request.datasource_description
        if not DaraCore.is_null(request.datasource_name):
            body['DatasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.datasource_type):
            body['DatasourceType'] = request.datasource_type
        if not DaraCore.is_null(request.hive_info_shrink):
            body['HiveInfo'] = request.hive_info_shrink
        if not DaraCore.is_null(request.kafka_info_shrink):
            body['KafkaInfo'] = request.kafka_info_shrink
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.polar_dbmysql_info_shrink):
            body['PolarDBMysqlInfo'] = request.polar_dbmysql_info_shrink
        if not DaraCore.is_null(request.polar_dbxinfo_shrink):
            body['PolarDBXInfo'] = request.polar_dbxinfo_shrink
        if not DaraCore.is_null(request.rds_mysql_info_shrink):
            body['RdsMysqlInfo'] = request.rds_mysql_info_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_info_shrink):
            body['SlsInfo'] = request.sls_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsDatasoure',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsDatasoureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aps_datasoure_with_options_async(
        self,
        tmp_req: main_models.CreateApsDatasoureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsDatasoureResponse:
        tmp_req.validate()
        request = main_models.CreateApsDatasoureShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.databricks_info):
            request.databricks_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.databricks_info, 'DatabricksInfo', 'json')
        if not DaraCore.is_null(tmp_req.hive_info):
            request.hive_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.hive_info, 'HiveInfo', 'json')
        if not DaraCore.is_null(tmp_req.kafka_info):
            request.kafka_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.kafka_info, 'KafkaInfo', 'json')
        if not DaraCore.is_null(tmp_req.polar_dbmysql_info):
            request.polar_dbmysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.polar_dbmysql_info, 'PolarDBMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.polar_dbxinfo):
            request.polar_dbxinfo_shrink = Utils.array_to_string_with_specified_style(tmp_req.polar_dbxinfo, 'PolarDBXInfo', 'json')
        if not DaraCore.is_null(tmp_req.rds_mysql_info):
            request.rds_mysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.rds_mysql_info, 'RdsMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.sls_info):
            request.sls_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sls_info, 'SlsInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.databricks_info_shrink):
            body['DatabricksInfo'] = request.databricks_info_shrink
        if not DaraCore.is_null(request.datasource_description):
            body['DatasourceDescription'] = request.datasource_description
        if not DaraCore.is_null(request.datasource_name):
            body['DatasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.datasource_type):
            body['DatasourceType'] = request.datasource_type
        if not DaraCore.is_null(request.hive_info_shrink):
            body['HiveInfo'] = request.hive_info_shrink
        if not DaraCore.is_null(request.kafka_info_shrink):
            body['KafkaInfo'] = request.kafka_info_shrink
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.polar_dbmysql_info_shrink):
            body['PolarDBMysqlInfo'] = request.polar_dbmysql_info_shrink
        if not DaraCore.is_null(request.polar_dbxinfo_shrink):
            body['PolarDBXInfo'] = request.polar_dbxinfo_shrink
        if not DaraCore.is_null(request.rds_mysql_info_shrink):
            body['RdsMysqlInfo'] = request.rds_mysql_info_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_info_shrink):
            body['SlsInfo'] = request.sls_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsDatasoure',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsDatasoureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aps_datasoure(
        self,
        request: main_models.CreateApsDatasoureRequest,
    ) -> main_models.CreateApsDatasoureResponse:
        runtime = RuntimeOptions()
        return self.create_aps_datasoure_with_options(request, runtime)

    async def create_aps_datasoure_async(
        self,
        request: main_models.CreateApsDatasoureRequest,
    ) -> main_models.CreateApsDatasoureResponse:
        runtime = RuntimeOptions()
        return await self.create_aps_datasoure_with_options_async(request, runtime)

    def create_aps_hive_job_with_options(
        self,
        request: main_models.CreateApsHiveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsHiveJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_config):
            body['AdvancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.conflict_strategy):
            body['ConflictStrategy'] = request.conflict_strategy
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.full_compute_unit):
            body['FullComputeUnit'] = request.full_compute_unit
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.parallelism):
            body['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.sync_allow_expression):
            body['SyncAllowExpression'] = request.sync_allow_expression
        if not DaraCore.is_null(request.sync_deny_expression):
            body['SyncDenyExpression'] = request.sync_deny_expression
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsHiveJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsHiveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aps_hive_job_with_options_async(
        self,
        request: main_models.CreateApsHiveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsHiveJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.advanced_config):
            body['AdvancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.conflict_strategy):
            body['ConflictStrategy'] = request.conflict_strategy
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.full_compute_unit):
            body['FullComputeUnit'] = request.full_compute_unit
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.parallelism):
            body['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.sync_allow_expression):
            body['SyncAllowExpression'] = request.sync_allow_expression
        if not DaraCore.is_null(request.sync_deny_expression):
            body['SyncDenyExpression'] = request.sync_deny_expression
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsHiveJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsHiveJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aps_hive_job(
        self,
        request: main_models.CreateApsHiveJobRequest,
    ) -> main_models.CreateApsHiveJobResponse:
        runtime = RuntimeOptions()
        return self.create_aps_hive_job_with_options(request, runtime)

    async def create_aps_hive_job_async(
        self,
        request: main_models.CreateApsHiveJobRequest,
    ) -> main_models.CreateApsHiveJobResponse:
        runtime = RuntimeOptions()
        return await self.create_aps_hive_job_with_options_async(request, runtime)

    def create_aps_kafka_hudi_job_with_options(
        self,
        tmp_req: main_models.CreateApsKafkaHudiJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsKafkaHudiJobResponse:
        tmp_req.validate()
        request = main_models.CreateApsKafkaHudiJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.partition_specs):
            request.partition_specs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_specs, 'PartitionSpecs', 'json')
        body = {}
        if not DaraCore.is_null(request.across_role):
            body['AcrossRole'] = request.across_role
        if not DaraCore.is_null(request.across_uid):
            body['AcrossUid'] = request.across_uid
        if not DaraCore.is_null(request.advanced_config):
            body['AdvancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.columns_shrink):
            body['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.data_format_type):
            body['DataFormatType'] = request.data_format_type
        if not DaraCore.is_null(request.data_output_format):
            body['DataOutputFormat'] = request.data_output_format
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.full_compute_unit):
            body['FullComputeUnit'] = request.full_compute_unit
        if not DaraCore.is_null(request.hudi_advanced_config):
            body['HudiAdvancedConfig'] = request.hudi_advanced_config
        if not DaraCore.is_null(request.incremental_compute_unit):
            body['IncrementalComputeUnit'] = request.incremental_compute_unit
        if not DaraCore.is_null(request.json_parse_level):
            body['JsonParseLevel'] = request.json_parse_level
        if not DaraCore.is_null(request.kafka_cluster_id):
            body['KafkaClusterId'] = request.kafka_cluster_id
        if not DaraCore.is_null(request.kafka_topic):
            body['KafkaTopic'] = request.kafka_topic
        if not DaraCore.is_null(request.lakehouse_id):
            body['LakehouseId'] = request.lakehouse_id
        if not DaraCore.is_null(request.max_offsets_per_trigger):
            body['MaxOffsetsPerTrigger'] = request.max_offsets_per_trigger
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.output_format):
            body['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.partition_specs_shrink):
            body['PartitionSpecs'] = request.partition_specs_shrink
        if not DaraCore.is_null(request.primary_key_definition):
            body['PrimaryKeyDefinition'] = request.primary_key_definition
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.source_region_id):
            body['SourceRegionId'] = request.source_region_id
        if not DaraCore.is_null(request.starting_offsets):
            body['StartingOffsets'] = request.starting_offsets
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.target_generate_rule):
            body['TargetGenerateRule'] = request.target_generate_rule
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsKafkaHudiJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsKafkaHudiJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aps_kafka_hudi_job_with_options_async(
        self,
        tmp_req: main_models.CreateApsKafkaHudiJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsKafkaHudiJobResponse:
        tmp_req.validate()
        request = main_models.CreateApsKafkaHudiJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.partition_specs):
            request.partition_specs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_specs, 'PartitionSpecs', 'json')
        body = {}
        if not DaraCore.is_null(request.across_role):
            body['AcrossRole'] = request.across_role
        if not DaraCore.is_null(request.across_uid):
            body['AcrossUid'] = request.across_uid
        if not DaraCore.is_null(request.advanced_config):
            body['AdvancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.columns_shrink):
            body['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.data_format_type):
            body['DataFormatType'] = request.data_format_type
        if not DaraCore.is_null(request.data_output_format):
            body['DataOutputFormat'] = request.data_output_format
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.full_compute_unit):
            body['FullComputeUnit'] = request.full_compute_unit
        if not DaraCore.is_null(request.hudi_advanced_config):
            body['HudiAdvancedConfig'] = request.hudi_advanced_config
        if not DaraCore.is_null(request.incremental_compute_unit):
            body['IncrementalComputeUnit'] = request.incremental_compute_unit
        if not DaraCore.is_null(request.json_parse_level):
            body['JsonParseLevel'] = request.json_parse_level
        if not DaraCore.is_null(request.kafka_cluster_id):
            body['KafkaClusterId'] = request.kafka_cluster_id
        if not DaraCore.is_null(request.kafka_topic):
            body['KafkaTopic'] = request.kafka_topic
        if not DaraCore.is_null(request.lakehouse_id):
            body['LakehouseId'] = request.lakehouse_id
        if not DaraCore.is_null(request.max_offsets_per_trigger):
            body['MaxOffsetsPerTrigger'] = request.max_offsets_per_trigger
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.output_format):
            body['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.partition_specs_shrink):
            body['PartitionSpecs'] = request.partition_specs_shrink
        if not DaraCore.is_null(request.primary_key_definition):
            body['PrimaryKeyDefinition'] = request.primary_key_definition
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.source_region_id):
            body['SourceRegionId'] = request.source_region_id
        if not DaraCore.is_null(request.starting_offsets):
            body['StartingOffsets'] = request.starting_offsets
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.target_generate_rule):
            body['TargetGenerateRule'] = request.target_generate_rule
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsKafkaHudiJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsKafkaHudiJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aps_kafka_hudi_job(
        self,
        request: main_models.CreateApsKafkaHudiJobRequest,
    ) -> main_models.CreateApsKafkaHudiJobResponse:
        runtime = RuntimeOptions()
        return self.create_aps_kafka_hudi_job_with_options(request, runtime)

    async def create_aps_kafka_hudi_job_async(
        self,
        request: main_models.CreateApsKafkaHudiJobRequest,
    ) -> main_models.CreateApsKafkaHudiJobResponse:
        runtime = RuntimeOptions()
        return await self.create_aps_kafka_hudi_job_with_options_async(request, runtime)

    def create_aps_sls_adbjob_with_options(
        self,
        tmp_req: main_models.CreateApsSlsADBJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsSlsADBJobResponse:
        tmp_req.validate()
        request = main_models.CreateApsSlsADBJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.partition_specs):
            request.partition_specs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_specs, 'PartitionSpecs', 'json')
        if not DaraCore.is_null(tmp_req.unix_timestamp_convert):
            request.unix_timestamp_convert_shrink = Utils.array_to_string_with_specified_style(tmp_req.unix_timestamp_convert, 'UnixTimestampConvert', 'json')
        body = {}
        if not DaraCore.is_null(request.across_role):
            body['AcrossRole'] = request.across_role
        if not DaraCore.is_null(request.across_uid):
            body['AcrossUid'] = request.across_uid
        if not DaraCore.is_null(request.advanced_config):
            body['AdvancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.columns_shrink):
            body['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.dirty_data_handle_mode):
            body['DirtyDataHandleMode'] = request.dirty_data_handle_mode
        if not DaraCore.is_null(request.dirty_data_process_pattern):
            body['DirtyDataProcessPattern'] = request.dirty_data_process_pattern
        if not DaraCore.is_null(request.exactly_once):
            body['ExactlyOnce'] = request.exactly_once
        if not DaraCore.is_null(request.full_compute_unit):
            body['FullComputeUnit'] = request.full_compute_unit
        if not DaraCore.is_null(request.hudi_advanced_config):
            body['HudiAdvancedConfig'] = request.hudi_advanced_config
        if not DaraCore.is_null(request.incremental_compute_unit):
            body['IncrementalComputeUnit'] = request.incremental_compute_unit
        if not DaraCore.is_null(request.lakehouse_id):
            body['LakehouseId'] = request.lakehouse_id
        if not DaraCore.is_null(request.max_offsets_per_trigger):
            body['MaxOffsetsPerTrigger'] = request.max_offsets_per_trigger
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.output_format):
            body['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.partition_specs_shrink):
            body['PartitionSpecs'] = request.partition_specs_shrink
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.primary_key_definition):
            body['PrimaryKeyDefinition'] = request.primary_key_definition
        if not DaraCore.is_null(request.project):
            body['Project'] = request.project
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.source_region_id):
            body['SourceRegionId'] = request.source_region_id
        if not DaraCore.is_null(request.starting_offsets):
            body['StartingOffsets'] = request.starting_offsets
        if not DaraCore.is_null(request.store):
            body['Store'] = request.store
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.target_generate_rule):
            body['TargetGenerateRule'] = request.target_generate_rule
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.unix_timestamp_convert_shrink):
            body['UnixTimestampConvert'] = request.unix_timestamp_convert_shrink
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsSlsADBJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsSlsADBJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aps_sls_adbjob_with_options_async(
        self,
        tmp_req: main_models.CreateApsSlsADBJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsSlsADBJobResponse:
        tmp_req.validate()
        request = main_models.CreateApsSlsADBJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.partition_specs):
            request.partition_specs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_specs, 'PartitionSpecs', 'json')
        if not DaraCore.is_null(tmp_req.unix_timestamp_convert):
            request.unix_timestamp_convert_shrink = Utils.array_to_string_with_specified_style(tmp_req.unix_timestamp_convert, 'UnixTimestampConvert', 'json')
        body = {}
        if not DaraCore.is_null(request.across_role):
            body['AcrossRole'] = request.across_role
        if not DaraCore.is_null(request.across_uid):
            body['AcrossUid'] = request.across_uid
        if not DaraCore.is_null(request.advanced_config):
            body['AdvancedConfig'] = request.advanced_config
        if not DaraCore.is_null(request.columns_shrink):
            body['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.dirty_data_handle_mode):
            body['DirtyDataHandleMode'] = request.dirty_data_handle_mode
        if not DaraCore.is_null(request.dirty_data_process_pattern):
            body['DirtyDataProcessPattern'] = request.dirty_data_process_pattern
        if not DaraCore.is_null(request.exactly_once):
            body['ExactlyOnce'] = request.exactly_once
        if not DaraCore.is_null(request.full_compute_unit):
            body['FullComputeUnit'] = request.full_compute_unit
        if not DaraCore.is_null(request.hudi_advanced_config):
            body['HudiAdvancedConfig'] = request.hudi_advanced_config
        if not DaraCore.is_null(request.incremental_compute_unit):
            body['IncrementalComputeUnit'] = request.incremental_compute_unit
        if not DaraCore.is_null(request.lakehouse_id):
            body['LakehouseId'] = request.lakehouse_id
        if not DaraCore.is_null(request.max_offsets_per_trigger):
            body['MaxOffsetsPerTrigger'] = request.max_offsets_per_trigger
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.output_format):
            body['OutputFormat'] = request.output_format
        if not DaraCore.is_null(request.partition_specs_shrink):
            body['PartitionSpecs'] = request.partition_specs_shrink
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.primary_key_definition):
            body['PrimaryKeyDefinition'] = request.primary_key_definition
        if not DaraCore.is_null(request.project):
            body['Project'] = request.project
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.source_region_id):
            body['SourceRegionId'] = request.source_region_id
        if not DaraCore.is_null(request.starting_offsets):
            body['StartingOffsets'] = request.starting_offsets
        if not DaraCore.is_null(request.store):
            body['Store'] = request.store
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.target_generate_rule):
            body['TargetGenerateRule'] = request.target_generate_rule
        if not DaraCore.is_null(request.target_type):
            body['TargetType'] = request.target_type
        if not DaraCore.is_null(request.unix_timestamp_convert_shrink):
            body['UnixTimestampConvert'] = request.unix_timestamp_convert_shrink
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsSlsADBJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsSlsADBJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aps_sls_adbjob(
        self,
        request: main_models.CreateApsSlsADBJobRequest,
    ) -> main_models.CreateApsSlsADBJobResponse:
        runtime = RuntimeOptions()
        return self.create_aps_sls_adbjob_with_options(request, runtime)

    async def create_aps_sls_adbjob_async(
        self,
        request: main_models.CreateApsSlsADBJobRequest,
    ) -> main_models.CreateApsSlsADBJobResponse:
        runtime = RuntimeOptions()
        return await self.create_aps_sls_adbjob_with_options_async(request, runtime)

    def create_aps_webhook_with_options(
        self,
        tmp_req: main_models.CreateApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsWebhookResponse:
        tmp_req.validate()
        request = main_models.CreateApsWebhookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.webhook):
            request.webhook_shrink = Utils.array_to_string_with_specified_style(tmp_req.webhook, 'Webhook', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webhook_shrink):
            body['Webhook'] = request.webhook_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aps_webhook_with_options_async(
        self,
        tmp_req: main_models.CreateApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApsWebhookResponse:
        tmp_req.validate()
        request = main_models.CreateApsWebhookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.webhook):
            request.webhook_shrink = Utils.array_to_string_with_specified_style(tmp_req.webhook, 'Webhook', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webhook_shrink):
            body['Webhook'] = request.webhook_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApsWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aps_webhook(
        self,
        request: main_models.CreateApsWebhookRequest,
    ) -> main_models.CreateApsWebhookResponse:
        runtime = RuntimeOptions()
        return self.create_aps_webhook_with_options(request, runtime)

    async def create_aps_webhook_async(
        self,
        request: main_models.CreateApsWebhookRequest,
    ) -> main_models.CreateApsWebhookResponse:
        runtime = RuntimeOptions()
        return await self.create_aps_webhook_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
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
            action = 'CreateBackup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
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
            action = 'CreateBackup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: main_models.CreateDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.clone_source_region_id):
            query['CloneSourceRegionId'] = request.clone_source_region_id
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not DaraCore.is_null(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.kms_id):
            query['KmsId'] = request.kms_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.product_form):
            query['ProductForm'] = request.product_form
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not DaraCore.is_null(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.restore_to_time):
            query['RestoreToTime'] = request.restore_to_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.source_db_cluster_id):
            query['SourceDbClusterId'] = request.source_db_cluster_id
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
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
            version = '2021-12-01',
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
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.clone_source_region_id):
            query['CloneSourceRegionId'] = request.clone_source_region_id
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.disk_encryption):
            query['DiskEncryption'] = request.disk_encryption
        if not DaraCore.is_null(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.kms_id):
            query['KmsId'] = request.kms_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.product_form):
            query['ProductForm'] = request.product_form
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not DaraCore.is_null(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.restore_to_time):
            query['RestoreToTime'] = request.restore_to_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.secondary_vswitch_id):
            query['SecondaryVSwitchId'] = request.secondary_vswitch_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.source_db_cluster_id):
            query['SourceDbClusterId'] = request.source_db_cluster_id
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(tmp_req.gpu_elastic_plan):
            request.gpu_elastic_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.gpu_elastic_plan, 'GpuElasticPlan', 'json')
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_stop_interval):
            query['AutoStopInterval'] = request.auto_stop_interval
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.gpu_elastic_plan_shrink):
            query['GpuElasticPlan'] = request.gpu_elastic_plan_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.max_gpu_quantity):
            query['MaxGpuQuantity'] = request.max_gpu_quantity
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.min_gpu_quantity):
            query['MinGpuQuantity'] = request.min_gpu_quantity
        if not DaraCore.is_null(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        if not DaraCore.is_null(request.spec_name):
            query['SpecName'] = request.spec_name
        if not DaraCore.is_null(request.target_resource_group_name):
            query['TargetResourceGroupName'] = request.target_resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourceGroup',
            version = '2021-12-01',
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
        if not DaraCore.is_null(tmp_req.gpu_elastic_plan):
            request.gpu_elastic_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.gpu_elastic_plan, 'GpuElasticPlan', 'json')
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_stop_interval):
            query['AutoStopInterval'] = request.auto_stop_interval
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.gpu_elastic_plan_shrink):
            query['GpuElasticPlan'] = request.gpu_elastic_plan_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.max_gpu_quantity):
            query['MaxGpuQuantity'] = request.max_gpu_quantity
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.min_gpu_quantity):
            query['MinGpuQuantity'] = request.min_gpu_quantity
        if not DaraCore.is_null(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        if not DaraCore.is_null(request.spec_name):
            query['SpecName'] = request.spec_name
        if not DaraCore.is_null(request.target_resource_group_name):
            query['TargetResourceGroupName'] = request.target_resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBResourceGroup',
            version = '2021-12-01',
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

    def create_elastic_plan_with_options(
        self,
        request: main_models.CreateElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_scale):
            query['AutoScale'] = request.auto_scale
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_size):
            query['TargetSize'] = request.target_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticPlan',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.auto_scale):
            query['AutoScale'] = request.auto_scale
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_size):
            query['TargetSize'] = request.target_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticPlan',
            version = '2021-12-01',
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

    def create_lake_storage_with_options(
        self,
        tmp_req: main_models.CreateLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLakeStorageResponse:
        tmp_req.validate()
        request = main_models.CreateLakeStorageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.permissions_shrink):
            body['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLakeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lake_storage_with_options_async(
        self,
        tmp_req: main_models.CreateLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLakeStorageResponse:
        tmp_req.validate()
        request = main_models.CreateLakeStorageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.permissions_shrink):
            body['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLakeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lake_storage(
        self,
        request: main_models.CreateLakeStorageRequest,
    ) -> main_models.CreateLakeStorageResponse:
        runtime = RuntimeOptions()
        return self.create_lake_storage_with_options(request, runtime)

    async def create_lake_storage_async(
        self,
        request: main_models.CreateLakeStorageRequest,
    ) -> main_models.CreateLakeStorageResponse:
        runtime = RuntimeOptions()
        return await self.create_lake_storage_with_options_async(request, runtime)

    def create_materialized_view_recommend_with_options(
        self,
        request: main_models.CreateMaterializedViewRecommendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaterializedViewRecommendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.min_rewrite_query_count):
            query['MinRewriteQueryCount'] = request.min_rewrite_query_count
        if not DaraCore.is_null(request.min_rewrite_query_pattern):
            query['MinRewriteQueryPattern'] = request.min_rewrite_query_pattern
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
        if not DaraCore.is_null(request.scan_queries_range):
            query['ScanQueriesRange'] = request.scan_queries_range
        if not DaraCore.is_null(request.scheduling_day):
            query['SchedulingDay'] = request.scheduling_day
        if not DaraCore.is_null(request.scheduling_policy):
            query['SchedulingPolicy'] = request.scheduling_policy
        if not DaraCore.is_null(request.slow_query_threshold):
            query['SlowQueryThreshold'] = request.slow_query_threshold
        if not DaraCore.is_null(request.specified_time):
            query['SpecifiedTime'] = request.specified_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaterializedViewRecommend',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMaterializedViewRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_materialized_view_recommend_with_options_async(
        self,
        request: main_models.CreateMaterializedViewRecommendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaterializedViewRecommendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.min_rewrite_query_count):
            query['MinRewriteQueryCount'] = request.min_rewrite_query_count
        if not DaraCore.is_null(request.min_rewrite_query_pattern):
            query['MinRewriteQueryPattern'] = request.min_rewrite_query_pattern
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
        if not DaraCore.is_null(request.scan_queries_range):
            query['ScanQueriesRange'] = request.scan_queries_range
        if not DaraCore.is_null(request.scheduling_day):
            query['SchedulingDay'] = request.scheduling_day
        if not DaraCore.is_null(request.scheduling_policy):
            query['SchedulingPolicy'] = request.scheduling_policy
        if not DaraCore.is_null(request.slow_query_threshold):
            query['SlowQueryThreshold'] = request.slow_query_threshold
        if not DaraCore.is_null(request.specified_time):
            query['SpecifiedTime'] = request.specified_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaterializedViewRecommend',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMaterializedViewRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_materialized_view_recommend(
        self,
        request: main_models.CreateMaterializedViewRecommendRequest,
    ) -> main_models.CreateMaterializedViewRecommendResponse:
        runtime = RuntimeOptions()
        return self.create_materialized_view_recommend_with_options(request, runtime)

    async def create_materialized_view_recommend_async(
        self,
        request: main_models.CreateMaterializedViewRecommendRequest,
    ) -> main_models.CreateMaterializedViewRecommendResponse:
        runtime = RuntimeOptions()
        return await self.create_materialized_view_recommend_with_options_async(request, runtime)

    def create_oss_sub_directory_with_options(
        self,
        request: main_models.CreateOssSubDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssSubDirectoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssSubDirectory',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssSubDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_sub_directory_with_options_async(
        self,
        request: main_models.CreateOssSubDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssSubDirectoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssSubDirectory',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssSubDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_sub_directory(
        self,
        request: main_models.CreateOssSubDirectoryRequest,
    ) -> main_models.CreateOssSubDirectoryResponse:
        runtime = RuntimeOptions()
        return self.create_oss_sub_directory_with_options(request, runtime)

    async def create_oss_sub_directory_async(
        self,
        request: main_models.CreateOssSubDirectoryRequest,
    ) -> main_models.CreateOssSubDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.create_oss_sub_directory_with_options_async(request, runtime)

    def create_performance_view_with_options(
        self,
        tmp_req: main_models.CreatePerformanceViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePerformanceViewResponse:
        tmp_req.validate()
        request = main_models.CreatePerformanceViewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_detail):
            request.view_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.create_from_view_type):
            query['CreateFromViewType'] = request.create_from_view_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.fill_origin_view_keys):
            query['FillOriginViewKeys'] = request.fill_origin_view_keys
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
        if not DaraCore.is_null(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePerformanceView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePerformanceViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_performance_view_with_options_async(
        self,
        tmp_req: main_models.CreatePerformanceViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePerformanceViewResponse:
        tmp_req.validate()
        request = main_models.CreatePerformanceViewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_detail):
            request.view_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.create_from_view_type):
            query['CreateFromViewType'] = request.create_from_view_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.fill_origin_view_keys):
            query['FillOriginViewKeys'] = request.fill_origin_view_keys
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
        if not DaraCore.is_null(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePerformanceView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePerformanceViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_performance_view(
        self,
        request: main_models.CreatePerformanceViewRequest,
    ) -> main_models.CreatePerformanceViewResponse:
        runtime = RuntimeOptions()
        return self.create_performance_view_with_options(request, runtime)

    async def create_performance_view_async(
        self,
        request: main_models.CreatePerformanceViewRequest,
    ) -> main_models.CreatePerformanceViewResponse:
        runtime = RuntimeOptions()
        return await self.create_performance_view_with_options_async(request, runtime)

    def create_spark_template_with_options(
        self,
        request: main_models.CreateSparkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSparkTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSparkTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSparkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_spark_template_with_options_async(
        self,
        request: main_models.CreateSparkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSparkTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSparkTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSparkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_spark_template(
        self,
        request: main_models.CreateSparkTemplateRequest,
    ) -> main_models.CreateSparkTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_spark_template_with_options(request, runtime)

    async def create_spark_template_async(
        self,
        request: main_models.CreateSparkTemplateRequest,
    ) -> main_models.CreateSparkTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_spark_template_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2021-12-01',
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

    def delete_aps_datasoure_with_options(
        self,
        request: main_models.DeleteApsDatasoureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApsDatasoureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApsDatasoure',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApsDatasoureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aps_datasoure_with_options_async(
        self,
        request: main_models.DeleteApsDatasoureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApsDatasoureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApsDatasoure',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApsDatasoureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aps_datasoure(
        self,
        request: main_models.DeleteApsDatasoureRequest,
    ) -> main_models.DeleteApsDatasoureResponse:
        runtime = RuntimeOptions()
        return self.delete_aps_datasoure_with_options(request, runtime)

    async def delete_aps_datasoure_async(
        self,
        request: main_models.DeleteApsDatasoureRequest,
    ) -> main_models.DeleteApsDatasoureResponse:
        runtime = RuntimeOptions()
        return await self.delete_aps_datasoure_with_options_async(request, runtime)

    def delete_aps_job_with_options(
        self,
        request: main_models.DeleteApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aps_job_with_options_async(
        self,
        request: main_models.DeleteApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aps_job(
        self,
        request: main_models.DeleteApsJobRequest,
    ) -> main_models.DeleteApsJobResponse:
        runtime = RuntimeOptions()
        return self.delete_aps_job_with_options(request, runtime)

    async def delete_aps_job_async(
        self,
        request: main_models.DeleteApsJobRequest,
    ) -> main_models.DeleteApsJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_aps_job_with_options_async(request, runtime)

    def delete_aps_webhook_with_options(
        self,
        request: main_models.DeleteApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApsWebhookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApsWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aps_webhook_with_options_async(
        self,
        request: main_models.DeleteApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApsWebhookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApsWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aps_webhook(
        self,
        request: main_models.DeleteApsWebhookRequest,
    ) -> main_models.DeleteApsWebhookResponse:
        runtime = RuntimeOptions()
        return self.delete_aps_webhook_with_options(request, runtime)

    async def delete_aps_webhook_async(
        self,
        request: main_models.DeleteApsWebhookRequest,
    ) -> main_models.DeleteApsWebhookResponse:
        runtime = RuntimeOptions()
        return await self.delete_aps_webhook_with_options_async(request, runtime)

    def delete_backups_with_options(
        self,
        request: main_models.DeleteBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_ids):
            query['BackupIds'] = request.backup_ids
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
            action = 'DeleteBackups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        query = {}
        if not DaraCore.is_null(request.backup_ids):
            query['BackupIds'] = request.backup_ids
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
            action = 'DeleteBackups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourceGroup',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBResourceGroup',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticPlan',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticPlan',
            version = '2021-12-01',
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

    def delete_lake_storage_with_options(
        self,
        request: main_models.DeleteLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLakeStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.lake_storage_id):
            body['LakeStorageId'] = request.lake_storage_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLakeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lake_storage_with_options_async(
        self,
        request: main_models.DeleteLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLakeStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.lake_storage_id):
            body['LakeStorageId'] = request.lake_storage_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLakeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lake_storage(
        self,
        request: main_models.DeleteLakeStorageRequest,
    ) -> main_models.DeleteLakeStorageResponse:
        runtime = RuntimeOptions()
        return self.delete_lake_storage_with_options(request, runtime)

    async def delete_lake_storage_async(
        self,
        request: main_models.DeleteLakeStorageRequest,
    ) -> main_models.DeleteLakeStorageResponse:
        runtime = RuntimeOptions()
        return await self.delete_lake_storage_with_options_async(request, runtime)

    def delete_materialized_view_recommend_with_options(
        self,
        request: main_models.DeleteMaterializedViewRecommendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterializedViewRecommendResponse:
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
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterializedViewRecommend',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterializedViewRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_materialized_view_recommend_with_options_async(
        self,
        request: main_models.DeleteMaterializedViewRecommendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterializedViewRecommendResponse:
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
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterializedViewRecommend',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterializedViewRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_materialized_view_recommend(
        self,
        request: main_models.DeleteMaterializedViewRecommendRequest,
    ) -> main_models.DeleteMaterializedViewRecommendResponse:
        runtime = RuntimeOptions()
        return self.delete_materialized_view_recommend_with_options(request, runtime)

    async def delete_materialized_view_recommend_async(
        self,
        request: main_models.DeleteMaterializedViewRecommendRequest,
    ) -> main_models.DeleteMaterializedViewRecommendResponse:
        runtime = RuntimeOptions()
        return await self.delete_materialized_view_recommend_with_options_async(request, runtime)

    def delete_performance_view_with_options(
        self,
        request: main_models.DeletePerformanceViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePerformanceViewResponse:
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
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePerformanceView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePerformanceViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_performance_view_with_options_async(
        self,
        request: main_models.DeletePerformanceViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePerformanceViewResponse:
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
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePerformanceView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePerformanceViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_performance_view(
        self,
        request: main_models.DeletePerformanceViewRequest,
    ) -> main_models.DeletePerformanceViewResponse:
        runtime = RuntimeOptions()
        return self.delete_performance_view_with_options(request, runtime)

    async def delete_performance_view_async(
        self,
        request: main_models.DeletePerformanceViewRequest,
    ) -> main_models.DeletePerformanceViewResponse:
        runtime = RuntimeOptions()
        return await self.delete_performance_view_with_options_async(request, runtime)

    def delete_spark_template_with_options(
        self,
        request: main_models.DeleteSparkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSparkTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSparkTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSparkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_spark_template_with_options_async(
        self,
        request: main_models.DeleteSparkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSparkTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSparkTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSparkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_spark_template(
        self,
        request: main_models.DeleteSparkTemplateRequest,
    ) -> main_models.DeleteSparkTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_spark_template_with_options(request, runtime)

    async def delete_spark_template_async(
        self,
        request: main_models.DeleteSparkTemplateRequest,
    ) -> main_models.DeleteSparkTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_spark_template_with_options_async(request, runtime)

    def delete_spark_template_file_with_options(
        self,
        request: main_models.DeleteSparkTemplateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSparkTemplateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSparkTemplateFile',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSparkTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_spark_template_file_with_options_async(
        self,
        request: main_models.DeleteSparkTemplateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSparkTemplateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSparkTemplateFile',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSparkTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_spark_template_file(
        self,
        request: main_models.DeleteSparkTemplateFileRequest,
    ) -> main_models.DeleteSparkTemplateFileResponse:
        runtime = RuntimeOptions()
        return self.delete_spark_template_file_with_options(request, runtime)

    async def delete_spark_template_file_async(
        self,
        request: main_models.DeleteSparkTemplateFileRequest,
    ) -> main_models.DeleteSparkTemplateFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_spark_template_file_with_options_async(request, runtime)

    def describe_apsadbinstances_with_options(
        self,
        request: main_models.DescribeAPSADBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAPSADBInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAPSADBInstances',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAPSADBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apsadbinstances_with_options_async(
        self,
        request: main_models.DescribeAPSADBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAPSADBInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAPSADBInstances',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAPSADBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apsadbinstances(
        self,
        request: main_models.DescribeAPSADBInstancesRequest,
    ) -> main_models.DescribeAPSADBInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_apsadbinstances_with_options(request, runtime)

    async def describe_apsadbinstances_async(
        self,
        request: main_models.DescribeAPSADBInstancesRequest,
    ) -> main_models.DescribeAPSADBInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_apsadbinstances_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_account_all_privileges_with_options(
        self,
        request: main_models.DescribeAccountAllPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountAllPrivilegesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountAllPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountAllPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_all_privileges_with_options_async(
        self,
        request: main_models.DescribeAccountAllPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountAllPrivilegesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountAllPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountAllPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_all_privileges(
        self,
        request: main_models.DescribeAccountAllPrivilegesRequest,
    ) -> main_models.DescribeAccountAllPrivilegesResponse:
        runtime = RuntimeOptions()
        return self.describe_account_all_privileges_with_options(request, runtime)

    async def describe_account_all_privileges_async(
        self,
        request: main_models.DescribeAccountAllPrivilegesRequest,
    ) -> main_models.DescribeAccountAllPrivilegesResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_all_privileges_with_options_async(request, runtime)

    def describe_account_privilege_objects_with_options(
        self,
        request: main_models.DescribeAccountPrivilegeObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountPrivilegeObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountPrivilegeObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountPrivilegeObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_privilege_objects_with_options_async(
        self,
        request: main_models.DescribeAccountPrivilegeObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountPrivilegeObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountPrivilegeObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountPrivilegeObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_privilege_objects(
        self,
        request: main_models.DescribeAccountPrivilegeObjectsRequest,
    ) -> main_models.DescribeAccountPrivilegeObjectsResponse:
        runtime = RuntimeOptions()
        return self.describe_account_privilege_objects_with_options(request, runtime)

    async def describe_account_privilege_objects_async(
        self,
        request: main_models.DescribeAccountPrivilegeObjectsRequest,
    ) -> main_models.DescribeAccountPrivilegeObjectsResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_privilege_objects_with_options_async(request, runtime)

    def describe_account_privileges_with_options(
        self,
        request: main_models.DescribeAccountPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountPrivilegesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_privileges_with_options_async(
        self,
        request: main_models.DescribeAccountPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountPrivilegesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.column_privilege_object):
            query['ColumnPrivilegeObject'] = request.column_privilege_object
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database_privilege_object):
            query['DatabasePrivilegeObject'] = request.database_privilege_object
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_privilege_object):
            query['TablePrivilegeObject'] = request.table_privilege_object
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_privileges(
        self,
        request: main_models.DescribeAccountPrivilegesRequest,
    ) -> main_models.DescribeAccountPrivilegesResponse:
        runtime = RuntimeOptions()
        return self.describe_account_privileges_with_options(request, runtime)

    async def describe_account_privileges_async(
        self,
        request: main_models.DescribeAccountPrivilegesRequest,
    ) -> main_models.DescribeAccountPrivilegesResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_privileges_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2021-12-01',
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

    def describe_adb_my_sql_columns_with_options(
        self,
        request: main_models.DescribeAdbMySqlColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlColumns',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_columns_with_options_async(
        self,
        request: main_models.DescribeAdbMySqlColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlColumns',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_columns(
        self,
        request: main_models.DescribeAdbMySqlColumnsRequest,
    ) -> main_models.DescribeAdbMySqlColumnsResponse:
        runtime = RuntimeOptions()
        return self.describe_adb_my_sql_columns_with_options(request, runtime)

    async def describe_adb_my_sql_columns_async(
        self,
        request: main_models.DescribeAdbMySqlColumnsRequest,
    ) -> main_models.DescribeAdbMySqlColumnsResponse:
        runtime = RuntimeOptions()
        return await self.describe_adb_my_sql_columns_with_options_async(request, runtime)

    def describe_adb_my_sql_indexes_with_options(
        self,
        request: main_models.DescribeAdbMySqlIndexesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlIndexesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlIndexes',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlIndexesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_indexes_with_options_async(
        self,
        request: main_models.DescribeAdbMySqlIndexesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlIndexesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlIndexes',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlIndexesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_indexes(
        self,
        request: main_models.DescribeAdbMySqlIndexesRequest,
    ) -> main_models.DescribeAdbMySqlIndexesResponse:
        runtime = RuntimeOptions()
        return self.describe_adb_my_sql_indexes_with_options(request, runtime)

    async def describe_adb_my_sql_indexes_async(
        self,
        request: main_models.DescribeAdbMySqlIndexesRequest,
    ) -> main_models.DescribeAdbMySqlIndexesResponse:
        runtime = RuntimeOptions()
        return await self.describe_adb_my_sql_indexes_with_options_async(request, runtime)

    def describe_adb_my_sql_schemas_with_options(
        self,
        request: main_models.DescribeAdbMySqlSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlSchemasResponse:
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
            action = 'DescribeAdbMySqlSchemas',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_schemas_with_options_async(
        self,
        request: main_models.DescribeAdbMySqlSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlSchemasResponse:
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
            action = 'DescribeAdbMySqlSchemas',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_schemas(
        self,
        request: main_models.DescribeAdbMySqlSchemasRequest,
    ) -> main_models.DescribeAdbMySqlSchemasResponse:
        runtime = RuntimeOptions()
        return self.describe_adb_my_sql_schemas_with_options(request, runtime)

    async def describe_adb_my_sql_schemas_async(
        self,
        request: main_models.DescribeAdbMySqlSchemasRequest,
    ) -> main_models.DescribeAdbMySqlSchemasResponse:
        runtime = RuntimeOptions()
        return await self.describe_adb_my_sql_schemas_with_options_async(request, runtime)

    def describe_adb_my_sql_table_meta_with_options(
        self,
        request: main_models.DescribeAdbMySqlTableMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlTableMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlTableMeta',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_table_meta_with_options_async(
        self,
        request: main_models.DescribeAdbMySqlTableMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlTableMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlTableMeta',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_table_meta(
        self,
        request: main_models.DescribeAdbMySqlTableMetaRequest,
    ) -> main_models.DescribeAdbMySqlTableMetaResponse:
        runtime = RuntimeOptions()
        return self.describe_adb_my_sql_table_meta_with_options(request, runtime)

    async def describe_adb_my_sql_table_meta_async(
        self,
        request: main_models.DescribeAdbMySqlTableMetaRequest,
    ) -> main_models.DescribeAdbMySqlTableMetaResponse:
        runtime = RuntimeOptions()
        return await self.describe_adb_my_sql_table_meta_with_options_async(request, runtime)

    def describe_adb_my_sql_tables_with_options(
        self,
        request: main_models.DescribeAdbMySqlTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlTables',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_tables_with_options_async(
        self,
        request: main_models.DescribeAdbMySqlTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAdbMySqlTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAdbMySqlTables',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAdbMySqlTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_tables(
        self,
        request: main_models.DescribeAdbMySqlTablesRequest,
    ) -> main_models.DescribeAdbMySqlTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_adb_my_sql_tables_with_options(request, runtime)

    async def describe_adb_my_sql_tables_async(
        self,
        request: main_models.DescribeAdbMySqlTablesRequest,
    ) -> main_models.DescribeAdbMySqlTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_adb_my_sql_tables_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_all_data_source_with_options(
        self,
        request: main_models.DescribeAllDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_aps_action_logs_with_options(
        self,
        request: main_models.DescribeApsActionLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsActionLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
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
        if not DaraCore.is_null(request.stage):
            query['Stage'] = request.stage
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsActionLogs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsActionLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_action_logs_with_options_async(
        self,
        request: main_models.DescribeApsActionLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsActionLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
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
        if not DaraCore.is_null(request.stage):
            query['Stage'] = request.stage
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsActionLogs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsActionLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_action_logs(
        self,
        request: main_models.DescribeApsActionLogsRequest,
    ) -> main_models.DescribeApsActionLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_action_logs_with_options(request, runtime)

    async def describe_aps_action_logs_async(
        self,
        request: main_models.DescribeApsActionLogsRequest,
    ) -> main_models.DescribeApsActionLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_action_logs_with_options_async(request, runtime)

    def describe_aps_datasource_with_options(
        self,
        request: main_models.DescribeApsDatasourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsDatasource',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_datasource_with_options_async(
        self,
        request: main_models.DescribeApsDatasourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsDatasource',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_datasource(
        self,
        request: main_models.DescribeApsDatasourceRequest,
    ) -> main_models.DescribeApsDatasourceResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_datasource_with_options(request, runtime)

    async def describe_aps_datasource_async(
        self,
        request: main_models.DescribeApsDatasourceRequest,
    ) -> main_models.DescribeApsDatasourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_datasource_with_options_async(request, runtime)

    def describe_aps_datasources_with_options(
        self,
        request: main_models.DescribeApsDatasourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsDatasourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_name):
            body['DatasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.datasource_type):
            body['DatasourceType'] = request.datasource_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsDatasources',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsDatasourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_datasources_with_options_async(
        self,
        request: main_models.DescribeApsDatasourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsDatasourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_name):
            body['DatasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.datasource_type):
            body['DatasourceType'] = request.datasource_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsDatasources',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsDatasourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_datasources(
        self,
        request: main_models.DescribeApsDatasourcesRequest,
    ) -> main_models.DescribeApsDatasourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_datasources_with_options(request, runtime)

    async def describe_aps_datasources_async(
        self,
        request: main_models.DescribeApsDatasourcesRequest,
    ) -> main_models.DescribeApsDatasourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_datasources_with_options_async(request, runtime)

    def describe_aps_hive_workload_with_options(
        self,
        request: main_models.DescribeApsHiveWorkloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsHiveWorkloadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsHiveWorkload',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsHiveWorkloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_hive_workload_with_options_async(
        self,
        request: main_models.DescribeApsHiveWorkloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsHiveWorkloadResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsHiveWorkload',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsHiveWorkloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_hive_workload(
        self,
        request: main_models.DescribeApsHiveWorkloadRequest,
    ) -> main_models.DescribeApsHiveWorkloadResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_hive_workload_with_options(request, runtime)

    async def describe_aps_hive_workload_async(
        self,
        request: main_models.DescribeApsHiveWorkloadRequest,
    ) -> main_models.DescribeApsHiveWorkloadResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_hive_workload_with_options_async(request, runtime)

    def describe_aps_job_detail_with_options(
        self,
        request: main_models.DescribeApsJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsJobDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsJobDetail',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_job_detail_with_options_async(
        self,
        request: main_models.DescribeApsJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsJobDetailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsJobDetail',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_job_detail(
        self,
        request: main_models.DescribeApsJobDetailRequest,
    ) -> main_models.DescribeApsJobDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_job_detail_with_options(request, runtime)

    async def describe_aps_job_detail_async(
        self,
        request: main_models.DescribeApsJobDetailRequest,
    ) -> main_models.DescribeApsJobDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_job_detail_with_options_async(request, runtime)

    def describe_aps_jobs_with_options(
        self,
        request: main_models.DescribeApsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_name):
            body['ApsJobName'] = request.aps_job_name
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_jobs_with_options_async(
        self,
        request: main_models.DescribeApsJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_name):
            body['ApsJobName'] = request.aps_job_name
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_jobs(
        self,
        request: main_models.DescribeApsJobsRequest,
    ) -> main_models.DescribeApsJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_jobs_with_options(request, runtime)

    async def describe_aps_jobs_async(
        self,
        request: main_models.DescribeApsJobsRequest,
    ) -> main_models.DescribeApsJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_jobs_with_options_async(request, runtime)

    def describe_aps_migration_workloads_with_options(
        self,
        request: main_models.DescribeApsMigrationWorkloadsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsMigrationWorkloadsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsMigrationWorkloads',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsMigrationWorkloadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_migration_workloads_with_options_async(
        self,
        request: main_models.DescribeApsMigrationWorkloadsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsMigrationWorkloadsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.oss_location):
            body['OssLocation'] = request.oss_location
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsMigrationWorkloads',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsMigrationWorkloadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_migration_workloads(
        self,
        request: main_models.DescribeApsMigrationWorkloadsRequest,
    ) -> main_models.DescribeApsMigrationWorkloadsResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_migration_workloads_with_options(request, runtime)

    async def describe_aps_migration_workloads_async(
        self,
        request: main_models.DescribeApsMigrationWorkloadsRequest,
    ) -> main_models.DescribeApsMigrationWorkloadsResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_migration_workloads_with_options_async(request, runtime)

    def describe_aps_progress_with_options(
        self,
        request: main_models.DescribeApsProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsProgressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsProgress',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_progress_with_options_async(
        self,
        request: main_models.DescribeApsProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsProgressResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsProgress',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_progress(
        self,
        request: main_models.DescribeApsProgressRequest,
    ) -> main_models.DescribeApsProgressResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_progress_with_options(request, runtime)

    async def describe_aps_progress_async(
        self,
        request: main_models.DescribeApsProgressRequest,
    ) -> main_models.DescribeApsProgressResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_progress_with_options_async(request, runtime)

    def describe_aps_resource_groups_with_options(
        self,
        request: main_models.DescribeApsResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsResourceGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsResourceGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_resource_groups_with_options_async(
        self,
        request: main_models.DescribeApsResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApsResourceGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApsResourceGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApsResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_resource_groups(
        self,
        request: main_models.DescribeApsResourceGroupsRequest,
    ) -> main_models.DescribeApsResourceGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_aps_resource_groups_with_options(request, runtime)

    async def describe_aps_resource_groups_async(
        self,
        request: main_models.DescribeApsResourceGroupsRequest,
    ) -> main_models.DescribeApsResourceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_aps_resource_groups_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
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
            version = '2021-12-01',
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

    def describe_auto_renewal_attribute_with_options(
        self,
        tmp_req: main_models.DescribeAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoRenewalAttributeResponse:
        tmp_req.validate()
        request = main_models.DescribeAutoRenewalAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dbcluster_id):
            request.dbcluster_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbcluster_id, 'DBClusterId', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id_shrink):
            query['DBClusterId'] = request.dbcluster_id_shrink
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
            action = 'DescribeAutoRenewalAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_renewal_attribute_with_options_async(
        self,
        tmp_req: main_models.DescribeAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoRenewalAttributeResponse:
        tmp_req.validate()
        request = main_models.DescribeAutoRenewalAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dbcluster_id):
            request.dbcluster_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.dbcluster_id, 'DBClusterId', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id_shrink):
            query['DBClusterId'] = request.dbcluster_id_shrink
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
            action = 'DescribeAutoRenewalAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_renewal_attribute(
        self,
        request: main_models.DescribeAutoRenewalAttributeRequest,
    ) -> main_models.DescribeAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_renewal_attribute_with_options(request, runtime)

    async def describe_auto_renewal_attribute_async(
        self,
        request: main_models.DescribeAutoRenewalAttributeRequest,
    ) -> main_models.DescribeAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_renewal_attribute_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.remote):
            query['Remote'] = request.remote
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.remote):
            query['Remote'] = request.remote
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_cluster_access_white_list_with_options(
        self,
        request: main_models.DescribeClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAccessWhiteList',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_access_white_list_with_options_async(
        self,
        request: main_models.DescribeClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAccessWhiteList',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_access_white_list(
        self,
        request: main_models.DescribeClusterAccessWhiteListRequest,
    ) -> main_models.DescribeClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_access_white_list_with_options(request, runtime)

    async def describe_cluster_access_white_list_async(
        self,
        request: main_models.DescribeClusterAccessWhiteListRequest,
    ) -> main_models.DescribeClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_access_white_list_with_options_async(request, runtime)

    def describe_cluster_net_info_with_options(
        self,
        request: main_models.DescribeClusterNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNetInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_net_info_with_options_async(
        self,
        request: main_models.DescribeClusterNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNetInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_net_info(
        self,
        request: main_models.DescribeClusterNetInfoRequest,
    ) -> main_models.DescribeClusterNetInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_net_info_with_options(request, runtime)

    async def describe_cluster_net_info_async(
        self,
        request: main_models.DescribeClusterNetInfoRequest,
    ) -> main_models.DescribeClusterNetInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_net_info_with_options_async(request, runtime)

    def describe_cluster_resource_detail_with_options(
        self,
        request: main_models.DescribeClusterResourceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResourceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterResourceDetail',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResourceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_resource_detail_with_options_async(
        self,
        request: main_models.DescribeClusterResourceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResourceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterResourceDetail',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResourceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_resource_detail(
        self,
        request: main_models.DescribeClusterResourceDetailRequest,
    ) -> main_models.DescribeClusterResourceDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_resource_detail_with_options(request, runtime)

    async def describe_cluster_resource_detail_async(
        self,
        request: main_models.DescribeClusterResourceDetailRequest,
    ) -> main_models.DescribeClusterResourceDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_resource_detail_with_options_async(request, runtime)

    def describe_cluster_resource_usage_with_options(
        self,
        request: main_models.DescribeClusterResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResourceUsageResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_resource_usage_with_options_async(
        self,
        request: main_models.DescribeClusterResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResourceUsageResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_resource_usage(
        self,
        request: main_models.DescribeClusterResourceUsageRequest,
    ) -> main_models.DescribeClusterResourceUsageResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_resource_usage_with_options(request, runtime)

    async def describe_cluster_resource_usage_async(
        self,
        request: main_models.DescribeClusterResourceUsageRequest,
    ) -> main_models.DescribeClusterResourceUsageResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_resource_usage_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: main_models.DescribeColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2021-12-01',
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

    def describe_compaction_service_switch_with_options(
        self,
        request: main_models.DescribeCompactionServiceSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCompactionServiceSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCompactionServiceSwitch',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCompactionServiceSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compaction_service_switch_with_options_async(
        self,
        request: main_models.DescribeCompactionServiceSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCompactionServiceSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCompactionServiceSwitch',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCompactionServiceSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compaction_service_switch(
        self,
        request: main_models.DescribeCompactionServiceSwitchRequest,
    ) -> main_models.DescribeCompactionServiceSwitchResponse:
        runtime = RuntimeOptions()
        return self.describe_compaction_service_switch_with_options(request, runtime)

    async def describe_compaction_service_switch_async(
        self,
        request: main_models.DescribeCompactionServiceSwitchRequest,
    ) -> main_models.DescribeCompactionServiceSwitchResponse:
        runtime = RuntimeOptions()
        return await self.describe_compaction_service_switch_with_options_async(request, runtime)

    def describe_compute_resource_usage_with_options(
        self,
        request: main_models.DescribeComputeResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComputeResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComputeResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComputeResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compute_resource_usage_with_options_async(
        self,
        request: main_models.DescribeComputeResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComputeResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComputeResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComputeResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compute_resource_usage(
        self,
        request: main_models.DescribeComputeResourceUsageRequest,
    ) -> main_models.DescribeComputeResourceUsageResponse:
        runtime = RuntimeOptions()
        return self.describe_compute_resource_usage_with_options(request, runtime)

    async def describe_compute_resource_usage_async(
        self,
        request: main_models.DescribeComputeResourceUsageRequest,
    ) -> main_models.DescribeComputeResourceUsageResponse:
        runtime = RuntimeOptions()
        return await self.describe_compute_resource_usage_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_dbcluster_attribute_with_options(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterAttribute',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterAttribute',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2021-12-01',
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

    def describe_dbcluster_sslwith_options(
        self,
        request: main_models.DescribeDBClusterSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterSSLResponse:
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
            action = 'DescribeDBClusterSSL',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterSSL',
            version = '2021-12-01',
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

    def describe_dbcluster_space_summary_with_options(
        self,
        request: main_models.DescribeDBClusterSpaceSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterSpaceSummaryResponse:
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
            action = 'DescribeDBClusterSpaceSummary',
            version = '2021-12-01',
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
            action = 'DescribeDBClusterSpaceSummary',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStatus',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStatus',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusters',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_version):
            query['ProductVersion'] = request.product_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusters',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceGroup',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBResourceGroup',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.process_rc_host):
            query['ProcessRcHost'] = request.process_rc_host
        if not DaraCore.is_null(request.process_start_time):
            query['ProcessStartTime'] = request.process_start_time
        if not DaraCore.is_null(request.process_state):
            query['ProcessState'] = request.process_state
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSQLInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.process_rc_host):
            query['ProcessRcHost'] = request.process_rc_host
        if not DaraCore.is_null(request.process_start_time):
            query['ProcessStartTime'] = request.process_start_time
        if not DaraCore.is_null(request.process_state):
            query['ProcessState'] = request.process_state
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSQLInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_elastic_plan_attribute_with_options(
        self,
        request: main_models.DescribeElasticPlanAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlanAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_attribute_with_options_async(
        self,
        request: main_models.DescribeElasticPlanAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlanAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan_attribute(
        self,
        request: main_models.DescribeElasticPlanAttributeRequest,
    ) -> main_models.DescribeElasticPlanAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_plan_attribute_with_options(request, runtime)

    async def describe_elastic_plan_attribute_async(
        self,
        request: main_models.DescribeElasticPlanAttributeRequest,
    ) -> main_models.DescribeElasticPlanAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_plan_attribute_with_options_async(request, runtime)

    def describe_elastic_plan_jobs_with_options(
        self,
        request: main_models.DescribeElasticPlanJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlanJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_jobs_with_options_async(
        self,
        request: main_models.DescribeElasticPlanJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlanJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan_jobs(
        self,
        request: main_models.DescribeElasticPlanJobsRequest,
    ) -> main_models.DescribeElasticPlanJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_plan_jobs_with_options(request, runtime)

    async def describe_elastic_plan_jobs_async(
        self,
        request: main_models.DescribeElasticPlanJobsRequest,
    ) -> main_models.DescribeElasticPlanJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_plan_jobs_with_options_async(request, runtime)

    def describe_elastic_plan_specifications_with_options(
        self,
        request: main_models.DescribeElasticPlanSpecificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanSpecificationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlanSpecifications',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plan_specifications_with_options_async(
        self,
        request: main_models.DescribeElasticPlanSpecificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlanSpecificationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlanSpecifications',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlanSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plan_specifications(
        self,
        request: main_models.DescribeElasticPlanSpecificationsRequest,
    ) -> main_models.DescribeElasticPlanSpecificationsResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_plan_specifications_with_options(request, runtime)

    async def describe_elastic_plan_specifications_async(
        self,
        request: main_models.DescribeElasticPlanSpecificationsRequest,
    ) -> main_models.DescribeElasticPlanSpecificationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_plan_specifications_with_options_async(request, runtime)

    def describe_elastic_plans_with_options(
        self,
        request: main_models.DescribeElasticPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlans',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_plans_with_options_async(
        self,
        request: main_models.DescribeElasticPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticPlans',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_plans(
        self,
        request: main_models.DescribeElasticPlansRequest,
    ) -> main_models.DescribeElasticPlansResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_plans_with_options(request, runtime)

    async def describe_elastic_plans_async(
        self,
        request: main_models.DescribeElasticPlansRequest,
    ) -> main_models.DescribeElasticPlansResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_plans_with_options_async(request, runtime)

    def describe_enabled_privileges_with_options(
        self,
        request: main_models.DescribeEnabledPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnabledPrivilegesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnabledPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnabledPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enabled_privileges_with_options_async(
        self,
        request: main_models.DescribeEnabledPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnabledPrivilegesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnabledPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnabledPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enabled_privileges(
        self,
        request: main_models.DescribeEnabledPrivilegesRequest,
    ) -> main_models.DescribeEnabledPrivilegesResponse:
        runtime = RuntimeOptions()
        return self.describe_enabled_privileges_with_options(request, runtime)

    async def describe_enabled_privileges_async(
        self,
        request: main_models.DescribeEnabledPrivilegesRequest,
    ) -> main_models.DescribeEnabledPrivilegesResponse:
        runtime = RuntimeOptions()
        return await self.describe_enabled_privileges_with_options_async(request, runtime)

    def describe_essd_cache_config_with_options(
        self,
        request: main_models.DescribeEssdCacheConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEssdCacheConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEssdCacheConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEssdCacheConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_essd_cache_config_with_options_async(
        self,
        request: main_models.DescribeEssdCacheConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEssdCacheConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEssdCacheConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEssdCacheConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_essd_cache_config(
        self,
        request: main_models.DescribeEssdCacheConfigRequest,
    ) -> main_models.DescribeEssdCacheConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_essd_cache_config_with_options(request, runtime)

    async def describe_essd_cache_config_async(
        self,
        request: main_models.DescribeEssdCacheConfigRequest,
    ) -> main_models.DescribeEssdCacheConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_essd_cache_config_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_history_tasks_with_options(
        self,
        request: main_models.DescribeHistoryTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_tasks_with_options_async(
        self,
        request: main_models.DescribeHistoryTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_tasks(
        self,
        request: main_models.DescribeHistoryTasksRequest,
    ) -> main_models.DescribeHistoryTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_history_tasks_with_options(request, runtime)

    async def describe_history_tasks_async(
        self,
        request: main_models.DescribeHistoryTasksRequest,
    ) -> main_models.DescribeHistoryTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_history_tasks_with_options_async(request, runtime)

    def describe_history_tasks_stat_with_options(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasksStat',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_tasks_stat_with_options_async(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasksStat',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_tasks_stat(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        runtime = RuntimeOptions()
        return self.describe_history_tasks_stat_with_options(request, runtime)

    async def describe_history_tasks_stat_async(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        runtime = RuntimeOptions()
        return await self.describe_history_tasks_stat_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInclinedTables',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInclinedTables',
            version = '2021-12-01',
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

    def describe_job_resource_usage_with_options(
        self,
        request: main_models.DescribeJobResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_resource_usage_with_options_async(
        self,
        request: main_models.DescribeJobResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_resource_usage(
        self,
        request: main_models.DescribeJobResourceUsageRequest,
    ) -> main_models.DescribeJobResourceUsageResponse:
        runtime = RuntimeOptions()
        return self.describe_job_resource_usage_with_options(request, runtime)

    async def describe_job_resource_usage_async(
        self,
        request: main_models.DescribeJobResourceUsageRequest,
    ) -> main_models.DescribeJobResourceUsageResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_resource_usage_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_llmanswer_with_sse(
        self,
        request: main_models.DescribeLLMAnswerRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.DescribeLLMAnswerResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
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
            action = 'DescribeLLMAnswer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.DescribeLLMAnswerResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def describe_llmanswer_with_sse_async(
        self,
        request: main_models.DescribeLLMAnswerRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.DescribeLLMAnswerResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
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
            action = 'DescribeLLMAnswer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.DescribeLLMAnswerResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def describe_llmanswer_with_options(
        self,
        request: main_models.DescribeLLMAnswerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLLMAnswerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
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
            action = 'DescribeLLMAnswer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLLMAnswerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_llmanswer_with_options_async(
        self,
        request: main_models.DescribeLLMAnswerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLLMAnswerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
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
            action = 'DescribeLLMAnswer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLLMAnswerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_llmanswer(
        self,
        request: main_models.DescribeLLMAnswerRequest,
    ) -> main_models.DescribeLLMAnswerResponse:
        runtime = RuntimeOptions()
        return self.describe_llmanswer_with_options(request, runtime)

    async def describe_llmanswer_async(
        self,
        request: main_models.DescribeLLMAnswerRequest,
    ) -> main_models.DescribeLLMAnswerResponse:
        runtime = RuntimeOptions()
        return await self.describe_llmanswer_with_options_async(request, runtime)

    def describe_llmsimilar_questions_with_options(
        self,
        request: main_models.DescribeLLMSimilarQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLLMSimilarQuestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
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
            action = 'DescribeLLMSimilarQuestions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLLMSimilarQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_llmsimilar_questions_with_options_async(
        self,
        request: main_models.DescribeLLMSimilarQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLLMSimilarQuestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
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
            action = 'DescribeLLMSimilarQuestions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLLMSimilarQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_llmsimilar_questions(
        self,
        request: main_models.DescribeLLMSimilarQuestionsRequest,
    ) -> main_models.DescribeLLMSimilarQuestionsResponse:
        runtime = RuntimeOptions()
        return self.describe_llmsimilar_questions_with_options(request, runtime)

    async def describe_llmsimilar_questions_async(
        self,
        request: main_models.DescribeLLMSimilarQuestionsRequest,
    ) -> main_models.DescribeLLMSimilarQuestionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_llmsimilar_questions_with_options_async(request, runtime)

    def describe_lake_cache_size_with_options(
        self,
        request: main_models.DescribeLakeCacheSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLakeCacheSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLakeCacheSize',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLakeCacheSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lake_cache_size_with_options_async(
        self,
        request: main_models.DescribeLakeCacheSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLakeCacheSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLakeCacheSize',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLakeCacheSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lake_cache_size(
        self,
        request: main_models.DescribeLakeCacheSizeRequest,
    ) -> main_models.DescribeLakeCacheSizeResponse:
        runtime = RuntimeOptions()
        return self.describe_lake_cache_size_with_options(request, runtime)

    async def describe_lake_cache_size_async(
        self,
        request: main_models.DescribeLakeCacheSizeRequest,
    ) -> main_models.DescribeLakeCacheSizeResponse:
        runtime = RuntimeOptions()
        return await self.describe_lake_cache_size_with_options_async(request, runtime)

    def describe_mvrecommend_results_with_options(
        self,
        request: main_models.DescribeMVRecommendResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMVRecommendResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_inner):
            query['ActionInner'] = request.action_inner
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sub_query_id):
            query['SubQueryId'] = request.sub_query_id
        if not DaraCore.is_null(request.subtask_id):
            query['SubtaskId'] = request.subtask_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMVRecommendResults',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMVRecommendResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mvrecommend_results_with_options_async(
        self,
        request: main_models.DescribeMVRecommendResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMVRecommendResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_inner):
            query['ActionInner'] = request.action_inner
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sub_query_id):
            query['SubQueryId'] = request.sub_query_id
        if not DaraCore.is_null(request.subtask_id):
            query['SubtaskId'] = request.subtask_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMVRecommendResults',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMVRecommendResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mvrecommend_results(
        self,
        request: main_models.DescribeMVRecommendResultsRequest,
    ) -> main_models.DescribeMVRecommendResultsResponse:
        runtime = RuntimeOptions()
        return self.describe_mvrecommend_results_with_options(request, runtime)

    async def describe_mvrecommend_results_async(
        self,
        request: main_models.DescribeMVRecommendResultsRequest,
    ) -> main_models.DescribeMVRecommendResultsResponse:
        runtime = RuntimeOptions()
        return await self.describe_mvrecommend_results_with_options_async(request, runtime)

    def describe_mv_recommend_sub_tasks_with_options(
        self,
        request: main_models.DescribeMvRecommendSubTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMvRecommendSubTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_inner):
            query['ActionInner'] = request.action_inner
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subtask_id):
            query['SubtaskId'] = request.subtask_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMvRecommendSubTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMvRecommendSubTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mv_recommend_sub_tasks_with_options_async(
        self,
        request: main_models.DescribeMvRecommendSubTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMvRecommendSubTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_inner):
            query['ActionInner'] = request.action_inner
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.subtask_id):
            query['SubtaskId'] = request.subtask_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMvRecommendSubTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMvRecommendSubTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mv_recommend_sub_tasks(
        self,
        request: main_models.DescribeMvRecommendSubTasksRequest,
    ) -> main_models.DescribeMvRecommendSubTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_mv_recommend_sub_tasks_with_options(request, runtime)

    async def describe_mv_recommend_sub_tasks_async(
        self,
        request: main_models.DescribeMvRecommendSubTasksRequest,
    ) -> main_models.DescribeMvRecommendSubTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_mv_recommend_sub_tasks_with_options_async(request, runtime)

    def describe_mv_recommend_tasks_with_options(
        self,
        request: main_models.DescribeMvRecommendTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMvRecommendTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_inner):
            query['ActionInner'] = request.action_inner
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMvRecommendTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMvRecommendTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mv_recommend_tasks_with_options_async(
        self,
        request: main_models.DescribeMvRecommendTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMvRecommendTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_inner):
            query['ActionInner'] = request.action_inner
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMvRecommendTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMvRecommendTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mv_recommend_tasks(
        self,
        request: main_models.DescribeMvRecommendTasksRequest,
    ) -> main_models.DescribeMvRecommendTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_mv_recommend_tasks_with_options(request, runtime)

    async def describe_mv_recommend_tasks_async(
        self,
        request: main_models.DescribeMvRecommendTasksRequest,
    ) -> main_models.DescribeMvRecommendTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_mv_recommend_tasks_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_performance_view_attribute_with_options(
        self,
        request: main_models.DescribePerformanceViewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePerformanceViewAttributeResponse:
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
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePerformanceViewAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePerformanceViewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_performance_view_attribute_with_options_async(
        self,
        request: main_models.DescribePerformanceViewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePerformanceViewAttributeResponse:
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
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePerformanceViewAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePerformanceViewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_performance_view_attribute(
        self,
        request: main_models.DescribePerformanceViewAttributeRequest,
    ) -> main_models.DescribePerformanceViewAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_performance_view_attribute_with_options(request, runtime)

    async def describe_performance_view_attribute_async(
        self,
        request: main_models.DescribePerformanceViewAttributeRequest,
    ) -> main_models.DescribePerformanceViewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_performance_view_attribute_with_options_async(request, runtime)

    def describe_performance_views_with_options(
        self,
        request: main_models.DescribePerformanceViewsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePerformanceViewsResponse:
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
            action = 'DescribePerformanceViews',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePerformanceViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_performance_views_with_options_async(
        self,
        request: main_models.DescribePerformanceViewsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePerformanceViewsResponse:
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
            action = 'DescribePerformanceViews',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePerformanceViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_performance_views(
        self,
        request: main_models.DescribePerformanceViewsRequest,
    ) -> main_models.DescribePerformanceViewsResponse:
        runtime = RuntimeOptions()
        return self.describe_performance_views_with_options(request, runtime)

    async def describe_performance_views_async(
        self,
        request: main_models.DescribePerformanceViewsRequest,
    ) -> main_models.DescribePerformanceViewsResponse:
        runtime = RuntimeOptions()
        return await self.describe_performance_views_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_resource_group_spec_with_options(
        self,
        request: main_models.DescribeResourceGroupSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceGroupSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_type):
            query['ResourceGroupType'] = request.resource_group_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceGroupSpec',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceGroupSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_group_spec_with_options_async(
        self,
        request: main_models.DescribeResourceGroupSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceGroupSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_type):
            query['ResourceGroupType'] = request.resource_group_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceGroupSpec',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceGroupSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_group_spec(
        self,
        request: main_models.DescribeResourceGroupSpecRequest,
    ) -> main_models.DescribeResourceGroupSpecResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_group_spec_with_options(request, runtime)

    async def describe_resource_group_spec_async(
        self,
        request: main_models.DescribeResourceGroupSpecRequest,
    ) -> main_models.DescribeResourceGroupSpecResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_group_spec_with_options_async(request, runtime)

    def describe_result_export_config_with_options(
        self,
        request: main_models.DescribeResultExportConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResultExportConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResultExportConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResultExportConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_result_export_config_with_options_async(
        self,
        request: main_models.DescribeResultExportConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResultExportConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResultExportConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResultExportConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_result_export_config(
        self,
        request: main_models.DescribeResultExportConfigRequest,
    ) -> main_models.DescribeResultExportConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_result_export_config_with_options(request, runtime)

    async def describe_result_export_config_async(
        self,
        request: main_models.DescribeResultExportConfigRequest,
    ) -> main_models.DescribeResultExportConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_result_export_config_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPatterns',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLPatterns',
            version = '2021-12-01',
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

    def describe_sqlweb_socket_domain_with_options(
        self,
        request: main_models.DescribeSQLWebSocketDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLWebSocketDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLWebSocketDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLWebSocketDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlweb_socket_domain_with_options_async(
        self,
        request: main_models.DescribeSQLWebSocketDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSQLWebSocketDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSQLWebSocketDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSQLWebSocketDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlweb_socket_domain(
        self,
        request: main_models.DescribeSQLWebSocketDomainRequest,
    ) -> main_models.DescribeSQLWebSocketDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_sqlweb_socket_domain_with_options(request, runtime)

    async def describe_sqlweb_socket_domain_async(
        self,
        request: main_models.DescribeSQLWebSocketDomainRequest,
    ) -> main_models.DescribeSQLWebSocketDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_sqlweb_socket_domain_with_options_async(request, runtime)

    def describe_schemas_with_options(
        self,
        request: main_models.DescribeSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSchemasResponse:
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
            action = 'DescribeSchemas',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchemas',
            version = '2021-12-01',
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

    def describe_spark_app_diagnosis_info_with_options(
        self,
        request: main_models.DescribeSparkAppDiagnosisInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkAppDiagnosisInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkAppDiagnosisInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkAppDiagnosisInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_app_diagnosis_info_with_options_async(
        self,
        request: main_models.DescribeSparkAppDiagnosisInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkAppDiagnosisInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkAppDiagnosisInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkAppDiagnosisInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_app_diagnosis_info(
        self,
        request: main_models.DescribeSparkAppDiagnosisInfoRequest,
    ) -> main_models.DescribeSparkAppDiagnosisInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_app_diagnosis_info_with_options(request, runtime)

    async def describe_spark_app_diagnosis_info_async(
        self,
        request: main_models.DescribeSparkAppDiagnosisInfoRequest,
    ) -> main_models.DescribeSparkAppDiagnosisInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_app_diagnosis_info_with_options_async(request, runtime)

    def describe_spark_app_type_with_options(
        self,
        request: main_models.DescribeSparkAppTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkAppTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkAppType',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkAppTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_app_type_with_options_async(
        self,
        request: main_models.DescribeSparkAppTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkAppTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkAppType',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkAppTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_app_type(
        self,
        request: main_models.DescribeSparkAppTypeRequest,
    ) -> main_models.DescribeSparkAppTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_app_type_with_options(request, runtime)

    async def describe_spark_app_type_async(
        self,
        request: main_models.DescribeSparkAppTypeRequest,
    ) -> main_models.DescribeSparkAppTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_app_type_with_options_async(request, runtime)

    def describe_spark_audit_log_records_with_options(
        self,
        request: main_models.DescribeSparkAuditLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkAuditLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sqltext):
            query['SQLText'] = request.sqltext
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statement_id):
            query['StatementId'] = request.statement_id
        if not DaraCore.is_null(request.statement_source):
            query['StatementSource'] = request.statement_source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.total_time):
            query['TotalTime'] = request.total_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkAuditLogRecords',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkAuditLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_audit_log_records_with_options_async(
        self,
        request: main_models.DescribeSparkAuditLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkAuditLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sqltext):
            query['SQLText'] = request.sqltext
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statement_id):
            query['StatementId'] = request.statement_id
        if not DaraCore.is_null(request.statement_source):
            query['StatementSource'] = request.statement_source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.total_time):
            query['TotalTime'] = request.total_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkAuditLogRecords',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkAuditLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_audit_log_records(
        self,
        request: main_models.DescribeSparkAuditLogRecordsRequest,
    ) -> main_models.DescribeSparkAuditLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_audit_log_records_with_options(request, runtime)

    async def describe_spark_audit_log_records_async(
        self,
        request: main_models.DescribeSparkAuditLogRecordsRequest,
    ) -> main_models.DescribeSparkAuditLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_audit_log_records_with_options_async(request, runtime)

    def describe_spark_code_log_with_options(
        self,
        request: main_models.DescribeSparkCodeLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkCodeLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkCodeLog',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkCodeLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_log_with_options_async(
        self,
        request: main_models.DescribeSparkCodeLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkCodeLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkCodeLog',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkCodeLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_log(
        self,
        request: main_models.DescribeSparkCodeLogRequest,
    ) -> main_models.DescribeSparkCodeLogResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_code_log_with_options(request, runtime)

    async def describe_spark_code_log_async(
        self,
        request: main_models.DescribeSparkCodeLogRequest,
    ) -> main_models.DescribeSparkCodeLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_code_log_with_options_async(request, runtime)

    def describe_spark_code_output_with_options(
        self,
        request: main_models.DescribeSparkCodeOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkCodeOutputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkCodeOutput',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkCodeOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_output_with_options_async(
        self,
        request: main_models.DescribeSparkCodeOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkCodeOutputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkCodeOutput',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkCodeOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_output(
        self,
        request: main_models.DescribeSparkCodeOutputRequest,
    ) -> main_models.DescribeSparkCodeOutputResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_code_output_with_options(request, runtime)

    async def describe_spark_code_output_async(
        self,
        request: main_models.DescribeSparkCodeOutputRequest,
    ) -> main_models.DescribeSparkCodeOutputResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_code_output_with_options_async(request, runtime)

    def describe_spark_code_web_ui_with_options(
        self,
        request: main_models.DescribeSparkCodeWebUiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkCodeWebUiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkCodeWebUi',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkCodeWebUiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_web_ui_with_options_async(
        self,
        request: main_models.DescribeSparkCodeWebUiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkCodeWebUiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkCodeWebUi',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkCodeWebUiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_web_ui(
        self,
        request: main_models.DescribeSparkCodeWebUiRequest,
    ) -> main_models.DescribeSparkCodeWebUiResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_code_web_ui_with_options(request, runtime)

    async def describe_spark_code_web_ui_async(
        self,
        request: main_models.DescribeSparkCodeWebUiRequest,
    ) -> main_models.DescribeSparkCodeWebUiResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_code_web_ui_with_options_async(request, runtime)

    def describe_spark_sqldiagnosis_attribute_with_options(
        self,
        request: main_models.DescribeSparkSQLDiagnosisAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkSQLDiagnosisAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.inner_query_id):
            query['InnerQueryId'] = request.inner_query_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkSQLDiagnosisAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkSQLDiagnosisAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_sqldiagnosis_attribute_with_options_async(
        self,
        request: main_models.DescribeSparkSQLDiagnosisAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkSQLDiagnosisAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.inner_query_id):
            query['InnerQueryId'] = request.inner_query_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkSQLDiagnosisAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkSQLDiagnosisAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_sqldiagnosis_attribute(
        self,
        request: main_models.DescribeSparkSQLDiagnosisAttributeRequest,
    ) -> main_models.DescribeSparkSQLDiagnosisAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_sqldiagnosis_attribute_with_options(request, runtime)

    async def describe_spark_sqldiagnosis_attribute_async(
        self,
        request: main_models.DescribeSparkSQLDiagnosisAttributeRequest,
    ) -> main_models.DescribeSparkSQLDiagnosisAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_sqldiagnosis_attribute_with_options_async(request, runtime)

    def describe_spark_sqldiagnosis_list_with_options(
        self,
        request: main_models.DescribeSparkSQLDiagnosisListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkSQLDiagnosisListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.max_start_time):
            query['MaxStartTime'] = request.max_start_time
        if not DaraCore.is_null(request.min_start_time):
            query['MinStartTime'] = request.min_start_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.statement_id):
            query['StatementId'] = request.statement_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkSQLDiagnosisList',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkSQLDiagnosisListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_sqldiagnosis_list_with_options_async(
        self,
        request: main_models.DescribeSparkSQLDiagnosisListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSparkSQLDiagnosisListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.max_start_time):
            query['MaxStartTime'] = request.max_start_time
        if not DaraCore.is_null(request.min_start_time):
            query['MinStartTime'] = request.min_start_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.statement_id):
            query['StatementId'] = request.statement_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSparkSQLDiagnosisList',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSparkSQLDiagnosisListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_sqldiagnosis_list(
        self,
        request: main_models.DescribeSparkSQLDiagnosisListRequest,
    ) -> main_models.DescribeSparkSQLDiagnosisListResponse:
        runtime = RuntimeOptions()
        return self.describe_spark_sqldiagnosis_list_with_options(request, runtime)

    async def describe_spark_sqldiagnosis_list_async(
        self,
        request: main_models.DescribeSparkSQLDiagnosisListRequest,
    ) -> main_models.DescribeSparkSQLDiagnosisListResponse:
        runtime = RuntimeOptions()
        return await self.describe_spark_sqldiagnosis_list_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def describe_storage_resource_usage_with_options(
        self,
        request: main_models.DescribeStorageResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStorageResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStorageResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStorageResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_resource_usage_with_options_async(
        self,
        request: main_models.DescribeStorageResourceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStorageResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStorageResourceUsage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStorageResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_resource_usage(
        self,
        request: main_models.DescribeStorageResourceUsageRequest,
    ) -> main_models.DescribeStorageResourceUsageResponse:
        runtime = RuntimeOptions()
        return self.describe_storage_resource_usage_with_options(request, runtime)

    async def describe_storage_resource_usage_async(
        self,
        request: main_models.DescribeStorageResourceUsageRequest,
    ) -> main_models.DescribeStorageResourceUsageResponse:
        runtime = RuntimeOptions()
        return await self.describe_storage_resource_usage_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableDetail',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableDetail',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTablePartitionDiagnose',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTablePartitionDiagnose',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableStatistics',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTableStatistics',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2021-12-01',
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

    def describe_user_quota_with_options(
        self,
        request: main_models.DescribeUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserQuotaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserQuota',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_quota_with_options_async(
        self,
        request: main_models.DescribeUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserQuotaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserQuota',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_quota(
        self,
        request: main_models.DescribeUserQuotaRequest,
    ) -> main_models.DescribeUserQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_user_quota_with_options(request, runtime)

    async def describe_user_quota_async(
        self,
        request: main_models.DescribeUserQuotaRequest,
    ) -> main_models.DescribeUserQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_quota_with_options_async(request, runtime)

    def describe_view_jobs_with_options(
        self,
        request: main_models.DescribeViewJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeViewJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_view_name):
            query['FilterViewName'] = request.filter_view_name
        if not DaraCore.is_null(request.filter_view_type):
            query['FilterViewType'] = request.filter_view_type
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeViewJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeViewJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_view_jobs_with_options_async(
        self,
        request: main_models.DescribeViewJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeViewJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_view_name):
            query['FilterViewName'] = request.filter_view_name
        if not DaraCore.is_null(request.filter_view_type):
            query['FilterViewType'] = request.filter_view_type
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeViewJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeViewJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_view_jobs(
        self,
        request: main_models.DescribeViewJobsRequest,
    ) -> main_models.DescribeViewJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_view_jobs_with_options(request, runtime)

    async def describe_view_jobs_async(
        self,
        request: main_models.DescribeViewJobsRequest,
    ) -> main_models.DescribeViewJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_view_jobs_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachUserENI',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachUserENI',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def disable_elastic_plan_with_options(
        self,
        request: main_models.DisableElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableElasticPlan',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_elastic_plan_with_options_async(
        self,
        request: main_models.DisableElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableElasticPlan',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_elastic_plan(
        self,
        request: main_models.DisableElasticPlanRequest,
    ) -> main_models.DisableElasticPlanResponse:
        runtime = RuntimeOptions()
        return self.disable_elastic_plan_with_options(request, runtime)

    async def disable_elastic_plan_async(
        self,
        request: main_models.DisableElasticPlanRequest,
    ) -> main_models.DisableElasticPlanResponse:
        runtime = RuntimeOptions()
        return await self.disable_elastic_plan_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def download_instance_cacertificate_with_options(
        self,
        request: main_models.DownloadInstanceCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadInstanceCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadInstanceCACertificate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadInstanceCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_instance_cacertificate_with_options_async(
        self,
        request: main_models.DownloadInstanceCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadInstanceCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadInstanceCACertificate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadInstanceCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_instance_cacertificate(
        self,
        request: main_models.DownloadInstanceCACertificateRequest,
    ) -> main_models.DownloadInstanceCACertificateResponse:
        runtime = RuntimeOptions()
        return self.download_instance_cacertificate_with_options(request, runtime)

    async def download_instance_cacertificate_async(
        self,
        request: main_models.DownloadInstanceCACertificateRequest,
    ) -> main_models.DownloadInstanceCACertificateResponse:
        runtime = RuntimeOptions()
        return await self.download_instance_cacertificate_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def enable_elastic_plan_with_options(
        self,
        request: main_models.EnableElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableElasticPlan',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableElasticPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_elastic_plan_with_options_async(
        self,
        request: main_models.EnableElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableElasticPlan',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableElasticPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_elastic_plan(
        self,
        request: main_models.EnableElasticPlanRequest,
    ) -> main_models.EnableElasticPlanResponse:
        runtime = RuntimeOptions()
        return self.enable_elastic_plan_with_options(request, runtime)

    async def enable_elastic_plan_async(
        self,
        request: main_models.EnableElasticPlanRequest,
    ) -> main_models.EnableElasticPlanResponse:
        runtime = RuntimeOptions()
        return await self.enable_elastic_plan_with_options_async(request, runtime)

    def execute_spark_repl_statement_with_options(
        self,
        request: main_models.ExecuteSparkReplStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSparkReplStatementResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.code_type):
            body['CodeType'] = request.code_type
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSparkReplStatement',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSparkReplStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_spark_repl_statement_with_options_async(
        self,
        request: main_models.ExecuteSparkReplStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSparkReplStatementResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.code):
            body['Code'] = request.code
        if not DaraCore.is_null(request.code_type):
            body['CodeType'] = request.code_type
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSparkReplStatement',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSparkReplStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_spark_repl_statement(
        self,
        request: main_models.ExecuteSparkReplStatementRequest,
    ) -> main_models.ExecuteSparkReplStatementResponse:
        runtime = RuntimeOptions()
        return self.execute_spark_repl_statement_with_options(request, runtime)

    async def execute_spark_repl_statement_async(
        self,
        request: main_models.ExecuteSparkReplStatementRequest,
    ) -> main_models.ExecuteSparkReplStatementResponse:
        runtime = RuntimeOptions()
        return await self.execute_spark_repl_statement_with_options_async(request, runtime)

    def execute_spark_warehouse_batch_sqlwith_options(
        self,
        request: main_models.ExecuteSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agency):
            body['Agency'] = request.agency
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.execute_result_limit):
            body['ExecuteResultLimit'] = request.execute_result_limit
        if not DaraCore.is_null(request.execute_time_limit_in_seconds):
            body['ExecuteTimeLimitInSeconds'] = request.execute_time_limit_in_seconds
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.runtime_config):
            body['RuntimeConfig'] = request.runtime_config
        if not DaraCore.is_null(request.schema):
            body['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSparkWarehouseBatchSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_spark_warehouse_batch_sqlwith_options_async(
        self,
        request: main_models.ExecuteSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agency):
            body['Agency'] = request.agency
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.execute_result_limit):
            body['ExecuteResultLimit'] = request.execute_result_limit
        if not DaraCore.is_null(request.execute_time_limit_in_seconds):
            body['ExecuteTimeLimitInSeconds'] = request.execute_time_limit_in_seconds
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.runtime_config):
            body['RuntimeConfig'] = request.runtime_config
        if not DaraCore.is_null(request.schema):
            body['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSparkWarehouseBatchSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_spark_warehouse_batch_sql(
        self,
        request: main_models.ExecuteSparkWarehouseBatchSQLRequest,
    ) -> main_models.ExecuteSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return self.execute_spark_warehouse_batch_sqlwith_options(request, runtime)

    async def execute_spark_warehouse_batch_sql_async(
        self,
        request: main_models.ExecuteSparkWarehouseBatchSQLRequest,
    ) -> main_models.ExecuteSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return await self.execute_spark_warehouse_batch_sqlwith_options_async(request, runtime)

    def exist_running_sqlengine_with_options(
        self,
        request: main_models.ExistRunningSQLEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExistRunningSQLEngineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExistRunningSQLEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExistRunningSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def exist_running_sqlengine_with_options_async(
        self,
        request: main_models.ExistRunningSQLEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExistRunningSQLEngineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExistRunningSQLEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExistRunningSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exist_running_sqlengine(
        self,
        request: main_models.ExistRunningSQLEngineRequest,
    ) -> main_models.ExistRunningSQLEngineResponse:
        runtime = RuntimeOptions()
        return self.exist_running_sqlengine_with_options(request, runtime)

    async def exist_running_sqlengine_async(
        self,
        request: main_models.ExistRunningSQLEngineRequest,
    ) -> main_models.ExistRunningSQLEngineResponse:
        runtime = RuntimeOptions()
        return await self.exist_running_sqlengine_with_options_async(request, runtime)

    def get_adbspark_necessary_rampermissions_with_options(
        self,
        request: main_models.GetADBSparkNecessaryRAMPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetADBSparkNecessaryRAMPermissionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetADBSparkNecessaryRAMPermissions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetADBSparkNecessaryRAMPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_adbspark_necessary_rampermissions_with_options_async(
        self,
        request: main_models.GetADBSparkNecessaryRAMPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetADBSparkNecessaryRAMPermissionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetADBSparkNecessaryRAMPermissions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetADBSparkNecessaryRAMPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_adbspark_necessary_rampermissions(
        self,
        request: main_models.GetADBSparkNecessaryRAMPermissionsRequest,
    ) -> main_models.GetADBSparkNecessaryRAMPermissionsResponse:
        runtime = RuntimeOptions()
        return self.get_adbspark_necessary_rampermissions_with_options(request, runtime)

    async def get_adbspark_necessary_rampermissions_async(
        self,
        request: main_models.GetADBSparkNecessaryRAMPermissionsRequest,
    ) -> main_models.GetADBSparkNecessaryRAMPermissionsResponse:
        runtime = RuntimeOptions()
        return await self.get_adbspark_necessary_rampermissions_with_options_async(request, runtime)

    def get_aps_managed_databases_with_options(
        self,
        request: main_models.GetApsManagedDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApsManagedDatabasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetApsManagedDatabases',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApsManagedDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aps_managed_databases_with_options_async(
        self,
        request: main_models.GetApsManagedDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApsManagedDatabasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetApsManagedDatabases',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApsManagedDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aps_managed_databases(
        self,
        request: main_models.GetApsManagedDatabasesRequest,
    ) -> main_models.GetApsManagedDatabasesResponse:
        runtime = RuntimeOptions()
        return self.get_aps_managed_databases_with_options(request, runtime)

    async def get_aps_managed_databases_async(
        self,
        request: main_models.GetApsManagedDatabasesRequest,
    ) -> main_models.GetApsManagedDatabasesResponse:
        runtime = RuntimeOptions()
        return await self.get_aps_managed_databases_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def get_database_objects_with_options(
        self,
        request: main_models.GetDatabaseObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_schema_name):
            query['FilterSchemaName'] = request.filter_schema_name
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabaseObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_objects_with_options_async(
        self,
        request: main_models.GetDatabaseObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_schema_name):
            query['FilterSchemaName'] = request.filter_schema_name
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabaseObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database_objects(
        self,
        request: main_models.GetDatabaseObjectsRequest,
    ) -> main_models.GetDatabaseObjectsResponse:
        runtime = RuntimeOptions()
        return self.get_database_objects_with_options(request, runtime)

    async def get_database_objects_async(
        self,
        request: main_models.GetDatabaseObjectsRequest,
    ) -> main_models.GetDatabaseObjectsResponse:
        runtime = RuntimeOptions()
        return await self.get_database_objects_with_options_async(request, runtime)

    def get_lake_storage_with_options(
        self,
        request: main_models.GetLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLakeStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lake_storage_id):
            query['LakeStorageId'] = request.lake_storage_id
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLakeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lake_storage_with_options_async(
        self,
        request: main_models.GetLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLakeStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.lake_storage_id):
            query['LakeStorageId'] = request.lake_storage_id
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLakeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lake_storage(
        self,
        request: main_models.GetLakeStorageRequest,
    ) -> main_models.GetLakeStorageResponse:
        runtime = RuntimeOptions()
        return self.get_lake_storage_with_options(request, runtime)

    async def get_lake_storage_async(
        self,
        request: main_models.GetLakeStorageRequest,
    ) -> main_models.GetLakeStorageResponse:
        runtime = RuntimeOptions()
        return await self.get_lake_storage_with_options_async(request, runtime)

    def get_spark_app_attempt_log_with_options(
        self,
        request: main_models.GetSparkAppAttemptLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppAttemptLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.attempt_id):
            body['AttemptId'] = request.attempt_id
        if not DaraCore.is_null(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppAttemptLog',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppAttemptLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_attempt_log_with_options_async(
        self,
        request: main_models.GetSparkAppAttemptLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppAttemptLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.attempt_id):
            body['AttemptId'] = request.attempt_id
        if not DaraCore.is_null(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppAttemptLog',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppAttemptLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_attempt_log(
        self,
        request: main_models.GetSparkAppAttemptLogRequest,
    ) -> main_models.GetSparkAppAttemptLogResponse:
        runtime = RuntimeOptions()
        return self.get_spark_app_attempt_log_with_options(request, runtime)

    async def get_spark_app_attempt_log_async(
        self,
        request: main_models.GetSparkAppAttemptLogRequest,
    ) -> main_models.GetSparkAppAttemptLogResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_app_attempt_log_with_options_async(request, runtime)

    def get_spark_app_info_with_options(
        self,
        request: main_models.GetSparkAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_info_with_options_async(
        self,
        request: main_models.GetSparkAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_info(
        self,
        request: main_models.GetSparkAppInfoRequest,
    ) -> main_models.GetSparkAppInfoResponse:
        runtime = RuntimeOptions()
        return self.get_spark_app_info_with_options(request, runtime)

    async def get_spark_app_info_async(
        self,
        request: main_models.GetSparkAppInfoRequest,
    ) -> main_models.GetSparkAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_app_info_with_options_async(request, runtime)

    def get_spark_app_log_with_options(
        self,
        request: main_models.GetSparkAppLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppLog',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_log_with_options_async(
        self,
        request: main_models.GetSparkAppLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppLog',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_log(
        self,
        request: main_models.GetSparkAppLogRequest,
    ) -> main_models.GetSparkAppLogResponse:
        runtime = RuntimeOptions()
        return self.get_spark_app_log_with_options(request, runtime)

    async def get_spark_app_log_async(
        self,
        request: main_models.GetSparkAppLogRequest,
    ) -> main_models.GetSparkAppLogResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_app_log_with_options_async(request, runtime)

    def get_spark_app_metrics_with_options(
        self,
        request: main_models.GetSparkAppMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppMetrics',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_metrics_with_options_async(
        self,
        request: main_models.GetSparkAppMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppMetrics',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_metrics(
        self,
        request: main_models.GetSparkAppMetricsRequest,
    ) -> main_models.GetSparkAppMetricsResponse:
        runtime = RuntimeOptions()
        return self.get_spark_app_metrics_with_options(request, runtime)

    async def get_spark_app_metrics_async(
        self,
        request: main_models.GetSparkAppMetricsRequest,
    ) -> main_models.GetSparkAppMetricsResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_app_metrics_with_options_async(request, runtime)

    def get_spark_app_state_with_options(
        self,
        request: main_models.GetSparkAppStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppState',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_state_with_options_async(
        self,
        request: main_models.GetSparkAppStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppState',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_state(
        self,
        request: main_models.GetSparkAppStateRequest,
    ) -> main_models.GetSparkAppStateResponse:
        runtime = RuntimeOptions()
        return self.get_spark_app_state_with_options(request, runtime)

    async def get_spark_app_state_async(
        self,
        request: main_models.GetSparkAppStateRequest,
    ) -> main_models.GetSparkAppStateResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_app_state_with_options_async(request, runtime)

    def get_spark_app_web_ui_address_with_options(
        self,
        request: main_models.GetSparkAppWebUiAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppWebUiAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppWebUiAddress',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppWebUiAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_web_ui_address_with_options_async(
        self,
        request: main_models.GetSparkAppWebUiAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkAppWebUiAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkAppWebUiAddress',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkAppWebUiAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_web_ui_address(
        self,
        request: main_models.GetSparkAppWebUiAddressRequest,
    ) -> main_models.GetSparkAppWebUiAddressResponse:
        runtime = RuntimeOptions()
        return self.get_spark_app_web_ui_address_with_options(request, runtime)

    async def get_spark_app_web_ui_address_async(
        self,
        request: main_models.GetSparkAppWebUiAddressRequest,
    ) -> main_models.GetSparkAppWebUiAddressResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_app_web_ui_address_with_options_async(request, runtime)

    def get_spark_config_log_path_with_options(
        self,
        request: main_models.GetSparkConfigLogPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkConfigLogPathResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkConfigLogPath',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkConfigLogPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_config_log_path_with_options_async(
        self,
        request: main_models.GetSparkConfigLogPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkConfigLogPathResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkConfigLogPath',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkConfigLogPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_config_log_path(
        self,
        request: main_models.GetSparkConfigLogPathRequest,
    ) -> main_models.GetSparkConfigLogPathResponse:
        runtime = RuntimeOptions()
        return self.get_spark_config_log_path_with_options(request, runtime)

    async def get_spark_config_log_path_async(
        self,
        request: main_models.GetSparkConfigLogPathRequest,
    ) -> main_models.GetSparkConfigLogPathResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_config_log_path_with_options_async(request, runtime)

    def get_spark_log_analyze_task_with_options(
        self,
        request: main_models.GetSparkLogAnalyzeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkLogAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkLogAnalyzeTask',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_log_analyze_task_with_options_async(
        self,
        request: main_models.GetSparkLogAnalyzeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkLogAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkLogAnalyzeTask',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_log_analyze_task(
        self,
        request: main_models.GetSparkLogAnalyzeTaskRequest,
    ) -> main_models.GetSparkLogAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        return self.get_spark_log_analyze_task_with_options(request, runtime)

    async def get_spark_log_analyze_task_async(
        self,
        request: main_models.GetSparkLogAnalyzeTaskRequest,
    ) -> main_models.GetSparkLogAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_log_analyze_task_with_options_async(request, runtime)

    def get_spark_repl_session_with_options(
        self,
        request: main_models.GetSparkReplSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkReplSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkReplSession',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkReplSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_repl_session_with_options_async(
        self,
        request: main_models.GetSparkReplSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkReplSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkReplSession',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkReplSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_repl_session(
        self,
        request: main_models.GetSparkReplSessionRequest,
    ) -> main_models.GetSparkReplSessionResponse:
        runtime = RuntimeOptions()
        return self.get_spark_repl_session_with_options(request, runtime)

    async def get_spark_repl_session_async(
        self,
        request: main_models.GetSparkReplSessionRequest,
    ) -> main_models.GetSparkReplSessionResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_repl_session_with_options_async(request, runtime)

    def get_spark_repl_statement_with_options(
        self,
        request: main_models.GetSparkReplStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkReplStatementResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkReplStatement',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkReplStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_repl_statement_with_options_async(
        self,
        request: main_models.GetSparkReplStatementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkReplStatementResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkReplStatement',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkReplStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_repl_statement(
        self,
        request: main_models.GetSparkReplStatementRequest,
    ) -> main_models.GetSparkReplStatementResponse:
        runtime = RuntimeOptions()
        return self.get_spark_repl_statement_with_options(request, runtime)

    async def get_spark_repl_statement_async(
        self,
        request: main_models.GetSparkReplStatementRequest,
    ) -> main_models.GetSparkReplStatementResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_repl_statement_with_options_async(request, runtime)

    def get_spark_sqlengine_state_with_options(
        self,
        request: main_models.GetSparkSQLEngineStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkSQLEngineStateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkSQLEngineState',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkSQLEngineStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_sqlengine_state_with_options_async(
        self,
        request: main_models.GetSparkSQLEngineStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkSQLEngineStateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkSQLEngineState',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkSQLEngineStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_sqlengine_state(
        self,
        request: main_models.GetSparkSQLEngineStateRequest,
    ) -> main_models.GetSparkSQLEngineStateResponse:
        runtime = RuntimeOptions()
        return self.get_spark_sqlengine_state_with_options(request, runtime)

    async def get_spark_sqlengine_state_async(
        self,
        request: main_models.GetSparkSQLEngineStateRequest,
    ) -> main_models.GetSparkSQLEngineStateResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_sqlengine_state_with_options_async(request, runtime)

    def get_spark_template_file_content_with_options(
        self,
        request: main_models.GetSparkTemplateFileContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkTemplateFileContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkTemplateFileContent',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkTemplateFileContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_file_content_with_options_async(
        self,
        request: main_models.GetSparkTemplateFileContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkTemplateFileContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkTemplateFileContent',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkTemplateFileContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_file_content(
        self,
        request: main_models.GetSparkTemplateFileContentRequest,
    ) -> main_models.GetSparkTemplateFileContentResponse:
        runtime = RuntimeOptions()
        return self.get_spark_template_file_content_with_options(request, runtime)

    async def get_spark_template_file_content_async(
        self,
        request: main_models.GetSparkTemplateFileContentRequest,
    ) -> main_models.GetSparkTemplateFileContentResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_template_file_content_with_options_async(request, runtime)

    def get_spark_template_folder_tree_with_options(
        self,
        request: main_models.GetSparkTemplateFolderTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkTemplateFolderTreeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkTemplateFolderTree',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkTemplateFolderTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_folder_tree_with_options_async(
        self,
        request: main_models.GetSparkTemplateFolderTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkTemplateFolderTreeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkTemplateFolderTree',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkTemplateFolderTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_folder_tree(
        self,
        request: main_models.GetSparkTemplateFolderTreeRequest,
    ) -> main_models.GetSparkTemplateFolderTreeResponse:
        runtime = RuntimeOptions()
        return self.get_spark_template_folder_tree_with_options(request, runtime)

    async def get_spark_template_folder_tree_async(
        self,
        request: main_models.GetSparkTemplateFolderTreeRequest,
    ) -> main_models.GetSparkTemplateFolderTreeResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_template_folder_tree_with_options_async(request, runtime)

    def get_spark_template_full_tree_with_options(
        self,
        request: main_models.GetSparkTemplateFullTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkTemplateFullTreeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkTemplateFullTree',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkTemplateFullTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_full_tree_with_options_async(
        self,
        request: main_models.GetSparkTemplateFullTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkTemplateFullTreeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkTemplateFullTree',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkTemplateFullTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_full_tree(
        self,
        request: main_models.GetSparkTemplateFullTreeRequest,
    ) -> main_models.GetSparkTemplateFullTreeResponse:
        runtime = RuntimeOptions()
        return self.get_spark_template_full_tree_with_options(request, runtime)

    async def get_spark_template_full_tree_async(
        self,
        request: main_models.GetSparkTemplateFullTreeRequest,
    ) -> main_models.GetSparkTemplateFullTreeResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_template_full_tree_with_options_async(request, runtime)

    def get_spark_warehouse_batch_sqlwith_options(
        self,
        request: main_models.GetSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agency):
            body['Agency'] = request.agency
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.query_id):
            body['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkWarehouseBatchSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_warehouse_batch_sqlwith_options_async(
        self,
        request: main_models.GetSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agency):
            body['Agency'] = request.agency
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.query_id):
            body['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkWarehouseBatchSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_warehouse_batch_sql(
        self,
        request: main_models.GetSparkWarehouseBatchSQLRequest,
    ) -> main_models.GetSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return self.get_spark_warehouse_batch_sqlwith_options(request, runtime)

    async def get_spark_warehouse_batch_sql_async(
        self,
        request: main_models.GetSparkWarehouseBatchSQLRequest,
    ) -> main_models.GetSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_warehouse_batch_sqlwith_options_async(request, runtime)

    def get_table_with_options(
        self,
        request: main_models.GetTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        request: main_models.GetTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        request: main_models.GetTableRequest,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        return self.get_table_with_options(request, runtime)

    async def get_table_async(
        self,
        request: main_models.GetTableRequest,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        return await self.get_table_with_options_async(request, runtime)

    def get_table_columns_with_options(
        self,
        request: main_models.GetTableColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.column_name):
            query['ColumnName'] = request.column_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumns',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_columns_with_options_async(
        self,
        request: main_models.GetTableColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.column_name):
            query['ColumnName'] = request.column_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumns',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_columns(
        self,
        request: main_models.GetTableColumnsRequest,
    ) -> main_models.GetTableColumnsResponse:
        runtime = RuntimeOptions()
        return self.get_table_columns_with_options(request, runtime)

    async def get_table_columns_async(
        self,
        request: main_models.GetTableColumnsRequest,
    ) -> main_models.GetTableColumnsResponse:
        runtime = RuntimeOptions()
        return await self.get_table_columns_with_options_async(request, runtime)

    def get_table_ddlwith_options(
        self,
        request: main_models.GetTableDDLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableDDLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableDDL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableDDLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_ddlwith_options_async(
        self,
        request: main_models.GetTableDDLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableDDLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableDDL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableDDLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_ddl(
        self,
        request: main_models.GetTableDDLRequest,
    ) -> main_models.GetTableDDLResponse:
        runtime = RuntimeOptions()
        return self.get_table_ddlwith_options(request, runtime)

    async def get_table_ddl_async(
        self,
        request: main_models.GetTableDDLRequest,
    ) -> main_models.GetTableDDLResponse:
        runtime = RuntimeOptions()
        return await self.get_table_ddlwith_options_async(request, runtime)

    def get_table_objects_with_options(
        self,
        request: main_models.GetTableObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_description):
            query['FilterDescription'] = request.filter_description
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_tbl_name):
            query['FilterTblName'] = request.filter_tbl_name
        if not DaraCore.is_null(request.filter_tbl_type):
            query['FilterTblType'] = request.filter_tbl_type
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_objects_with_options_async(
        self,
        request: main_models.GetTableObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_description):
            query['FilterDescription'] = request.filter_description
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_tbl_name):
            query['FilterTblName'] = request.filter_tbl_name
        if not DaraCore.is_null(request.filter_tbl_type):
            query['FilterTblType'] = request.filter_tbl_type
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_objects(
        self,
        request: main_models.GetTableObjectsRequest,
    ) -> main_models.GetTableObjectsResponse:
        runtime = RuntimeOptions()
        return self.get_table_objects_with_options(request, runtime)

    async def get_table_objects_async(
        self,
        request: main_models.GetTableObjectsRequest,
    ) -> main_models.GetTableObjectsResponse:
        runtime = RuntimeOptions()
        return await self.get_table_objects_with_options_async(request, runtime)

    def get_view_ddlwith_options(
        self,
        request: main_models.GetViewDDLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViewDDLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViewDDL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViewDDLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_view_ddlwith_options_async(
        self,
        request: main_models.GetViewDDLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViewDDLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViewDDL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViewDDLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_view_ddl(
        self,
        request: main_models.GetViewDDLRequest,
    ) -> main_models.GetViewDDLResponse:
        runtime = RuntimeOptions()
        return self.get_view_ddlwith_options(request, runtime)

    async def get_view_ddl_async(
        self,
        request: main_models.GetViewDDLRequest,
    ) -> main_models.GetViewDDLResponse:
        runtime = RuntimeOptions()
        return await self.get_view_ddlwith_options_async(request, runtime)

    def get_view_objects_with_options(
        self,
        request: main_models.GetViewObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViewObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_view_name):
            query['FilterViewName'] = request.filter_view_name
        if not DaraCore.is_null(request.filter_view_type):
            query['FilterViewType'] = request.filter_view_type
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.show_mv_base_table):
            query['ShowMvBaseTable'] = request.show_mv_base_table
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViewObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViewObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_view_objects_with_options_async(
        self,
        request: main_models.GetViewObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViewObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filter_owner):
            query['FilterOwner'] = request.filter_owner
        if not DaraCore.is_null(request.filter_view_name):
            query['FilterViewName'] = request.filter_view_name
        if not DaraCore.is_null(request.filter_view_type):
            query['FilterViewType'] = request.filter_view_type
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.show_mv_base_table):
            query['ShowMvBaseTable'] = request.show_mv_base_table
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViewObjects',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViewObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_view_objects(
        self,
        request: main_models.GetViewObjectsRequest,
    ) -> main_models.GetViewObjectsResponse:
        runtime = RuntimeOptions()
        return self.get_view_objects_with_options(request, runtime)

    async def get_view_objects_async(
        self,
        request: main_models.GetViewObjectsRequest,
    ) -> main_models.GetViewObjectsResponse:
        runtime = RuntimeOptions()
        return await self.get_view_objects_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillProcess',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillProcess',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def kill_spark_app_with_options(
        self,
        request: main_models.KillSparkAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillSparkAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'KillSparkApp',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillSparkAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_app_with_options_async(
        self,
        request: main_models.KillSparkAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillSparkAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'KillSparkApp',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillSparkAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_app(
        self,
        request: main_models.KillSparkAppRequest,
    ) -> main_models.KillSparkAppResponse:
        runtime = RuntimeOptions()
        return self.kill_spark_app_with_options(request, runtime)

    async def kill_spark_app_async(
        self,
        request: main_models.KillSparkAppRequest,
    ) -> main_models.KillSparkAppResponse:
        runtime = RuntimeOptions()
        return await self.kill_spark_app_with_options_async(request, runtime)

    def kill_spark_log_analyze_task_with_options(
        self,
        request: main_models.KillSparkLogAnalyzeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillSparkLogAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'KillSparkLogAnalyzeTask',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_log_analyze_task_with_options_async(
        self,
        request: main_models.KillSparkLogAnalyzeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillSparkLogAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'KillSparkLogAnalyzeTask',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_log_analyze_task(
        self,
        request: main_models.KillSparkLogAnalyzeTaskRequest,
    ) -> main_models.KillSparkLogAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        return self.kill_spark_log_analyze_task_with_options(request, runtime)

    async def kill_spark_log_analyze_task_async(
        self,
        request: main_models.KillSparkLogAnalyzeTaskRequest,
    ) -> main_models.KillSparkLogAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        return await self.kill_spark_log_analyze_task_with_options_async(request, runtime)

    def kill_spark_sqlengine_with_options(
        self,
        request: main_models.KillSparkSQLEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillSparkSQLEngineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'KillSparkSQLEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillSparkSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_sqlengine_with_options_async(
        self,
        request: main_models.KillSparkSQLEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillSparkSQLEngineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'KillSparkSQLEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillSparkSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_sqlengine(
        self,
        request: main_models.KillSparkSQLEngineRequest,
    ) -> main_models.KillSparkSQLEngineResponse:
        runtime = RuntimeOptions()
        return self.kill_spark_sqlengine_with_options(request, runtime)

    async def kill_spark_sqlengine_async(
        self,
        request: main_models.KillSparkSQLEngineRequest,
    ) -> main_models.KillSparkSQLEngineResponse:
        runtime = RuntimeOptions()
        return await self.kill_spark_sqlengine_with_options_async(request, runtime)

    def list_aps_lifecycle_strategy_with_options(
        self,
        request: main_models.ListApsLifecycleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsLifecycleStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsLifecycleStrategy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsLifecycleStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aps_lifecycle_strategy_with_options_async(
        self,
        request: main_models.ListApsLifecycleStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsLifecycleStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsLifecycleStrategy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsLifecycleStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aps_lifecycle_strategy(
        self,
        request: main_models.ListApsLifecycleStrategyRequest,
    ) -> main_models.ListApsLifecycleStrategyResponse:
        runtime = RuntimeOptions()
        return self.list_aps_lifecycle_strategy_with_options(request, runtime)

    async def list_aps_lifecycle_strategy_async(
        self,
        request: main_models.ListApsLifecycleStrategyRequest,
    ) -> main_models.ListApsLifecycleStrategyResponse:
        runtime = RuntimeOptions()
        return await self.list_aps_lifecycle_strategy_with_options_async(request, runtime)

    def list_aps_optimization_strategy_with_options(
        self,
        request: main_models.ListApsOptimizationStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsOptimizationStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsOptimizationStrategy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsOptimizationStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aps_optimization_strategy_with_options_async(
        self,
        request: main_models.ListApsOptimizationStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsOptimizationStrategyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsOptimizationStrategy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsOptimizationStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aps_optimization_strategy(
        self,
        request: main_models.ListApsOptimizationStrategyRequest,
    ) -> main_models.ListApsOptimizationStrategyResponse:
        runtime = RuntimeOptions()
        return self.list_aps_optimization_strategy_with_options(request, runtime)

    async def list_aps_optimization_strategy_async(
        self,
        request: main_models.ListApsOptimizationStrategyRequest,
    ) -> main_models.ListApsOptimizationStrategyResponse:
        runtime = RuntimeOptions()
        return await self.list_aps_optimization_strategy_with_options_async(request, runtime)

    def list_aps_optimization_tasks_with_options(
        self,
        request: main_models.ListApsOptimizationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsOptimizationTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsOptimizationTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsOptimizationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aps_optimization_tasks_with_options_async(
        self,
        request: main_models.ListApsOptimizationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsOptimizationTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsOptimizationTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsOptimizationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aps_optimization_tasks(
        self,
        request: main_models.ListApsOptimizationTasksRequest,
    ) -> main_models.ListApsOptimizationTasksResponse:
        runtime = RuntimeOptions()
        return self.list_aps_optimization_tasks_with_options(request, runtime)

    async def list_aps_optimization_tasks_async(
        self,
        request: main_models.ListApsOptimizationTasksRequest,
    ) -> main_models.ListApsOptimizationTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_aps_optimization_tasks_with_options_async(request, runtime)

    def list_aps_webhook_with_options(
        self,
        request: main_models.ListApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsWebhookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aps_webhook_with_options_async(
        self,
        request: main_models.ListApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApsWebhookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApsWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aps_webhook(
        self,
        request: main_models.ListApsWebhookRequest,
    ) -> main_models.ListApsWebhookResponse:
        runtime = RuntimeOptions()
        return self.list_aps_webhook_with_options(request, runtime)

    async def list_aps_webhook_async(
        self,
        request: main_models.ListApsWebhookRequest,
    ) -> main_models.ListApsWebhookResponse:
        runtime = RuntimeOptions()
        return await self.list_aps_webhook_with_options_async(request, runtime)

    def list_lake_storages_with_options(
        self,
        request: main_models.ListLakeStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLakeStoragesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLakeStorages',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLakeStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lake_storages_with_options_async(
        self,
        request: main_models.ListLakeStoragesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLakeStoragesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLakeStorages',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLakeStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lake_storages(
        self,
        request: main_models.ListLakeStoragesRequest,
    ) -> main_models.ListLakeStoragesResponse:
        runtime = RuntimeOptions()
        return self.list_lake_storages_with_options(request, runtime)

    async def list_lake_storages_async(
        self,
        request: main_models.ListLakeStoragesRequest,
    ) -> main_models.ListLakeStoragesResponse:
        runtime = RuntimeOptions()
        return await self.list_lake_storages_with_options_async(request, runtime)

    def list_result_export_job_history_with_options(
        self,
        tmp_req: main_models.ListResultExportJobHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResultExportJobHistoryResponse:
        tmp_req.validate()
        request = main_models.ListResultExportJobHistoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order):
            request.order_shrink = Utils.array_to_string_with_specified_style(tmp_req.order, 'Order', 'json')
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database_user):
            body['DatabaseUser'] = request.database_user
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_shrink):
            body['Order'] = request.order_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status_list_shrink):
            body['StatusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResultExportJobHistory',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResultExportJobHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_result_export_job_history_with_options_async(
        self,
        tmp_req: main_models.ListResultExportJobHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResultExportJobHistoryResponse:
        tmp_req.validate()
        request = main_models.ListResultExportJobHistoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order):
            request.order_shrink = Utils.array_to_string_with_specified_style(tmp_req.order, 'Order', 'json')
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.database_user):
            body['DatabaseUser'] = request.database_user
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_shrink):
            body['Order'] = request.order_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status_list_shrink):
            body['StatusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResultExportJobHistory',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResultExportJobHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_result_export_job_history(
        self,
        request: main_models.ListResultExportJobHistoryRequest,
    ) -> main_models.ListResultExportJobHistoryResponse:
        runtime = RuntimeOptions()
        return self.list_result_export_job_history_with_options(request, runtime)

    async def list_result_export_job_history_async(
        self,
        request: main_models.ListResultExportJobHistoryRequest,
    ) -> main_models.ListResultExportJobHistoryResponse:
        runtime = RuntimeOptions()
        return await self.list_result_export_job_history_with_options_async(request, runtime)

    def list_spark_app_attempts_with_options(
        self,
        request: main_models.ListSparkAppAttemptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkAppAttemptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkAppAttempts',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkAppAttemptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_app_attempts_with_options_async(
        self,
        request: main_models.ListSparkAppAttemptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkAppAttemptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkAppAttempts',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkAppAttemptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_app_attempts(
        self,
        request: main_models.ListSparkAppAttemptsRequest,
    ) -> main_models.ListSparkAppAttemptsResponse:
        runtime = RuntimeOptions()
        return self.list_spark_app_attempts_with_options(request, runtime)

    async def list_spark_app_attempts_async(
        self,
        request: main_models.ListSparkAppAttemptsRequest,
    ) -> main_models.ListSparkAppAttemptsResponse:
        runtime = RuntimeOptions()
        return await self.list_spark_app_attempts_with_options_async(request, runtime)

    def list_spark_apps_with_options(
        self,
        request: main_models.ListSparkAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkApps',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_apps_with_options_async(
        self,
        request: main_models.ListSparkAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkApps',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_apps(
        self,
        request: main_models.ListSparkAppsRequest,
    ) -> main_models.ListSparkAppsResponse:
        runtime = RuntimeOptions()
        return self.list_spark_apps_with_options(request, runtime)

    async def list_spark_apps_async(
        self,
        request: main_models.ListSparkAppsRequest,
    ) -> main_models.ListSparkAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_spark_apps_with_options_async(request, runtime)

    def list_spark_log_analyze_tasks_with_options(
        self,
        request: main_models.ListSparkLogAnalyzeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkLogAnalyzeTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkLogAnalyzeTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkLogAnalyzeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_log_analyze_tasks_with_options_async(
        self,
        request: main_models.ListSparkLogAnalyzeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkLogAnalyzeTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkLogAnalyzeTasks',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkLogAnalyzeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_log_analyze_tasks(
        self,
        request: main_models.ListSparkLogAnalyzeTasksRequest,
    ) -> main_models.ListSparkLogAnalyzeTasksResponse:
        runtime = RuntimeOptions()
        return self.list_spark_log_analyze_tasks_with_options(request, runtime)

    async def list_spark_log_analyze_tasks_async(
        self,
        request: main_models.ListSparkLogAnalyzeTasksRequest,
    ) -> main_models.ListSparkLogAnalyzeTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_spark_log_analyze_tasks_with_options_async(request, runtime)

    def list_spark_template_file_ids_with_options(
        self,
        request: main_models.ListSparkTemplateFileIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkTemplateFileIdsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkTemplateFileIds',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkTemplateFileIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_template_file_ids_with_options_async(
        self,
        request: main_models.ListSparkTemplateFileIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkTemplateFileIdsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkTemplateFileIds',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkTemplateFileIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_template_file_ids(
        self,
        request: main_models.ListSparkTemplateFileIdsRequest,
    ) -> main_models.ListSparkTemplateFileIdsResponse:
        runtime = RuntimeOptions()
        return self.list_spark_template_file_ids_with_options(request, runtime)

    async def list_spark_template_file_ids_async(
        self,
        request: main_models.ListSparkTemplateFileIdsRequest,
    ) -> main_models.ListSparkTemplateFileIdsResponse:
        runtime = RuntimeOptions()
        return await self.list_spark_template_file_ids_with_options_async(request, runtime)

    def list_spark_warehouse_batch_sqlwith_options(
        self,
        request: main_models.ListSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkWarehouseBatchSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_warehouse_batch_sqlwith_options_async(
        self,
        request: main_models.ListSparkWarehouseBatchSQLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSparkWarehouseBatchSQLResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSparkWarehouseBatchSQL',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSparkWarehouseBatchSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_warehouse_batch_sql(
        self,
        request: main_models.ListSparkWarehouseBatchSQLRequest,
    ) -> main_models.ListSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return self.list_spark_warehouse_batch_sqlwith_options(request, runtime)

    async def list_spark_warehouse_batch_sql_async(
        self,
        request: main_models.ListSparkWarehouseBatchSQLRequest,
    ) -> main_models.ListSparkWarehouseBatchSQLResponse:
        runtime = RuntimeOptions()
        return await self.list_spark_warehouse_batch_sqlwith_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def load_sample_data_set_with_options(
        self,
        request: main_models.LoadSampleDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadSampleDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadSampleDataSet',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadSampleDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_sample_data_set_with_options_async(
        self,
        request: main_models.LoadSampleDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadSampleDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadSampleDataSet',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadSampleDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_sample_data_set(
        self,
        request: main_models.LoadSampleDataSetRequest,
    ) -> main_models.LoadSampleDataSetResponse:
        runtime = RuntimeOptions()
        return self.load_sample_data_set_with_options(request, runtime)

    async def load_sample_data_set_async(
        self,
        request: main_models.LoadSampleDataSetRequest,
    ) -> main_models.LoadSampleDataSetResponse:
        runtime = RuntimeOptions()
        return await self.load_sample_data_set_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2021-12-01',
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

    def modify_account_privileges_with_options(
        self,
        tmp_req: main_models.ModifyAccountPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountPrivilegesResponse:
        tmp_req.validate()
        request = main_models.ModifyAccountPrivilegesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_privileges):
            request.account_privileges_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_privileges, 'AccountPrivileges', 'json')
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_privileges_shrink):
            query['AccountPrivileges'] = request.account_privileges_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_privileges_with_options_async(
        self,
        tmp_req: main_models.ModifyAccountPrivilegesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountPrivilegesResponse:
        tmp_req.validate()
        request = main_models.ModifyAccountPrivilegesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_privileges):
            request.account_privileges_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_privileges, 'AccountPrivileges', 'json')
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_privileges_shrink):
            query['AccountPrivileges'] = request.account_privileges_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountPrivileges',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_privileges(
        self,
        request: main_models.ModifyAccountPrivilegesRequest,
    ) -> main_models.ModifyAccountPrivilegesResponse:
        runtime = RuntimeOptions()
        return self.modify_account_privileges_with_options(request, runtime)

    async def modify_account_privileges_async(
        self,
        request: main_models.ModifyAccountPrivilegesRequest,
    ) -> main_models.ModifyAccountPrivilegesResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_privileges_with_options_async(request, runtime)

    def modify_aps_datasoure_with_options(
        self,
        tmp_req: main_models.ModifyApsDatasoureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsDatasoureResponse:
        tmp_req.validate()
        request = main_models.ModifyApsDatasoureShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.kafka_info):
            request.kafka_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.kafka_info, 'KafkaInfo', 'json')
        if not DaraCore.is_null(tmp_req.lakehouse_id):
            request.lakehouse_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.lakehouse_id, 'LakehouseId', 'json')
        if not DaraCore.is_null(tmp_req.polar_dbmysql_info):
            request.polar_dbmysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.polar_dbmysql_info, 'PolarDBMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.rds_mysql_info):
            request.rds_mysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.rds_mysql_info, 'RdsMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.sls_info):
            request.sls_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sls_info, 'SlsInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_description):
            body['DatasourceDescription'] = request.datasource_description
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.datasource_name):
            body['DatasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.kafka_info_shrink):
            body['KafkaInfo'] = request.kafka_info_shrink
        if not DaraCore.is_null(request.lakehouse_id_shrink):
            body['LakehouseId'] = request.lakehouse_id_shrink
        if not DaraCore.is_null(request.polar_dbmysql_info_shrink):
            body['PolarDBMysqlInfo'] = request.polar_dbmysql_info_shrink
        if not DaraCore.is_null(request.rds_mysql_info_shrink):
            body['RdsMysqlInfo'] = request.rds_mysql_info_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_info_shrink):
            body['SlsInfo'] = request.sls_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsDatasoure',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsDatasoureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aps_datasoure_with_options_async(
        self,
        tmp_req: main_models.ModifyApsDatasoureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsDatasoureResponse:
        tmp_req.validate()
        request = main_models.ModifyApsDatasoureShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.kafka_info):
            request.kafka_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.kafka_info, 'KafkaInfo', 'json')
        if not DaraCore.is_null(tmp_req.lakehouse_id):
            request.lakehouse_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.lakehouse_id, 'LakehouseId', 'json')
        if not DaraCore.is_null(tmp_req.polar_dbmysql_info):
            request.polar_dbmysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.polar_dbmysql_info, 'PolarDBMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.rds_mysql_info):
            request.rds_mysql_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.rds_mysql_info, 'RdsMysqlInfo', 'json')
        if not DaraCore.is_null(tmp_req.sls_info):
            request.sls_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sls_info, 'SlsInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.datasource_description):
            body['DatasourceDescription'] = request.datasource_description
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.datasource_name):
            body['DatasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.kafka_info_shrink):
            body['KafkaInfo'] = request.kafka_info_shrink
        if not DaraCore.is_null(request.lakehouse_id_shrink):
            body['LakehouseId'] = request.lakehouse_id_shrink
        if not DaraCore.is_null(request.polar_dbmysql_info_shrink):
            body['PolarDBMysqlInfo'] = request.polar_dbmysql_info_shrink
        if not DaraCore.is_null(request.rds_mysql_info_shrink):
            body['RdsMysqlInfo'] = request.rds_mysql_info_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_info_shrink):
            body['SlsInfo'] = request.sls_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsDatasoure',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsDatasoureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_aps_datasoure(
        self,
        request: main_models.ModifyApsDatasoureRequest,
    ) -> main_models.ModifyApsDatasoureResponse:
        runtime = RuntimeOptions()
        return self.modify_aps_datasoure_with_options(request, runtime)

    async def modify_aps_datasoure_async(
        self,
        request: main_models.ModifyApsDatasoureRequest,
    ) -> main_models.ModifyApsDatasoureResponse:
        runtime = RuntimeOptions()
        return await self.modify_aps_datasoure_with_options_async(request, runtime)

    def modify_aps_job_with_options(
        self,
        request: main_models.ModifyApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.db_list):
            body['DbList'] = request.db_list
        if not DaraCore.is_null(request.partition_list):
            body['PartitionList'] = request.partition_list
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aps_job_with_options_async(
        self,
        request: main_models.ModifyApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.db_list):
            body['DbList'] = request.db_list
        if not DaraCore.is_null(request.partition_list):
            body['PartitionList'] = request.partition_list
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_aps_job(
        self,
        request: main_models.ModifyApsJobRequest,
    ) -> main_models.ModifyApsJobResponse:
        runtime = RuntimeOptions()
        return self.modify_aps_job_with_options(request, runtime)

    async def modify_aps_job_async(
        self,
        request: main_models.ModifyApsJobRequest,
    ) -> main_models.ModifyApsJobResponse:
        runtime = RuntimeOptions()
        return await self.modify_aps_job_with_options_async(request, runtime)

    def modify_aps_sls_adbjob_with_options(
        self,
        tmp_req: main_models.ModifyApsSlsADBJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsSlsADBJobResponse:
        tmp_req.validate()
        request = main_models.ModifyApsSlsADBJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        body = {}
        if not DaraCore.is_null(request.columns_shrink):
            body['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.dirty_data_process_pattern):
            body['DirtyDataProcessPattern'] = request.dirty_data_process_pattern
        if not DaraCore.is_null(request.exactly_once):
            body['ExactlyOnce'] = request.exactly_once
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.starting_offsets):
            body['StartingOffsets'] = request.starting_offsets
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.unix_timestamp_convert):
            body['UnixTimestampConvert'] = request.unix_timestamp_convert
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsSlsADBJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsSlsADBJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aps_sls_adbjob_with_options_async(
        self,
        tmp_req: main_models.ModifyApsSlsADBJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsSlsADBJobResponse:
        tmp_req.validate()
        request = main_models.ModifyApsSlsADBJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        body = {}
        if not DaraCore.is_null(request.columns_shrink):
            body['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.dirty_data_process_pattern):
            body['DirtyDataProcessPattern'] = request.dirty_data_process_pattern
        if not DaraCore.is_null(request.exactly_once):
            body['ExactlyOnce'] = request.exactly_once
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.starting_offsets):
            body['StartingOffsets'] = request.starting_offsets
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        if not DaraCore.is_null(request.unix_timestamp_convert):
            body['UnixTimestampConvert'] = request.unix_timestamp_convert
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsSlsADBJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsSlsADBJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_aps_sls_adbjob(
        self,
        request: main_models.ModifyApsSlsADBJobRequest,
    ) -> main_models.ModifyApsSlsADBJobResponse:
        runtime = RuntimeOptions()
        return self.modify_aps_sls_adbjob_with_options(request, runtime)

    async def modify_aps_sls_adbjob_async(
        self,
        request: main_models.ModifyApsSlsADBJobRequest,
    ) -> main_models.ModifyApsSlsADBJobResponse:
        runtime = RuntimeOptions()
        return await self.modify_aps_sls_adbjob_with_options_async(request, runtime)

    def modify_aps_workload_name_with_options(
        self,
        request: main_models.ModifyApsWorkloadNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsWorkloadNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsWorkloadName',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsWorkloadNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_aps_workload_name_with_options_async(
        self,
        request: main_models.ModifyApsWorkloadNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApsWorkloadNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workload_id):
            body['WorkloadId'] = request.workload_id
        if not DaraCore.is_null(request.workload_name):
            body['WorkloadName'] = request.workload_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApsWorkloadName',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApsWorkloadNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_aps_workload_name(
        self,
        request: main_models.ModifyApsWorkloadNameRequest,
    ) -> main_models.ModifyApsWorkloadNameResponse:
        runtime = RuntimeOptions()
        return self.modify_aps_workload_name_with_options(request, runtime)

    async def modify_aps_workload_name_async(
        self,
        request: main_models.ModifyApsWorkloadNameRequest,
    ) -> main_models.ModifyApsWorkloadNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_aps_workload_name_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
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
            version = '2021-12-01',
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

    def modify_auto_renewal_attribute_with_options(
        self,
        request: main_models.ModifyAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoRenewalAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renewal_period):
            query['AutoRenewalPeriod'] = request.auto_renewal_period
        if not DaraCore.is_null(request.auto_renewal_period_unit):
            query['AutoRenewalPeriodUnit'] = request.auto_renewal_period_unit
        if not DaraCore.is_null(request.auto_renewal_status):
            query['AutoRenewalStatus'] = request.auto_renewal_status
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
            action = 'ModifyAutoRenewalAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_renewal_attribute_with_options_async(
        self,
        request: main_models.ModifyAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoRenewalAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renewal_period):
            query['AutoRenewalPeriod'] = request.auto_renewal_period
        if not DaraCore.is_null(request.auto_renewal_period_unit):
            query['AutoRenewalPeriodUnit'] = request.auto_renewal_period_unit
        if not DaraCore.is_null(request.auto_renewal_status):
            query['AutoRenewalStatus'] = request.auto_renewal_status
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
            action = 'ModifyAutoRenewalAttribute',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_renewal_attribute(
        self,
        request: main_models.ModifyAutoRenewalAttributeRequest,
    ) -> main_models.ModifyAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_auto_renewal_attribute_with_options(request, runtime)

    async def modify_auto_renewal_attribute_async(
        self,
        request: main_models.ModifyAutoRenewalAttributeRequest,
    ) -> main_models.ModifyAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_auto_renewal_attribute_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def modify_clickhouse_engine_with_options(
        self,
        request: main_models.ModifyClickhouseEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClickhouseEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClickhouseEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClickhouseEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_clickhouse_engine_with_options_async(
        self,
        request: main_models.ModifyClickhouseEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClickhouseEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClickhouseEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClickhouseEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_clickhouse_engine(
        self,
        request: main_models.ModifyClickhouseEngineRequest,
    ) -> main_models.ModifyClickhouseEngineResponse:
        runtime = RuntimeOptions()
        return self.modify_clickhouse_engine_with_options(request, runtime)

    async def modify_clickhouse_engine_async(
        self,
        request: main_models.ModifyClickhouseEngineRequest,
    ) -> main_models.ModifyClickhouseEngineResponse:
        runtime = RuntimeOptions()
        return await self.modify_clickhouse_engine_with_options_async(request, runtime)

    def modify_cluster_access_white_list_with_options(
        self,
        request: main_models.ModifyClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterAccessWhiteListResponse:
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
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterAccessWhiteList',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_access_white_list_with_options_async(
        self,
        request: main_models.ModifyClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterAccessWhiteListResponse:
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
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterAccessWhiteList',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_access_white_list(
        self,
        request: main_models.ModifyClusterAccessWhiteListRequest,
    ) -> main_models.ModifyClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return self.modify_cluster_access_white_list_with_options(request, runtime)

    async def modify_cluster_access_white_list_async(
        self,
        request: main_models.ModifyClusterAccessWhiteListRequest,
    ) -> main_models.ModifyClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.modify_cluster_access_white_list_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterConnectionString',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterConnectionString',
            version = '2021-12-01',
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

    def modify_compaction_service_switch_with_options(
        self,
        request: main_models.ModifyCompactionServiceSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCompactionServiceSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_compaction_service):
            query['EnableCompactionService'] = request.enable_compaction_service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCompactionServiceSwitch',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCompactionServiceSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_compaction_service_switch_with_options_async(
        self,
        request: main_models.ModifyCompactionServiceSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCompactionServiceSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_compaction_service):
            query['EnableCompactionService'] = request.enable_compaction_service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCompactionServiceSwitch',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCompactionServiceSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_compaction_service_switch(
        self,
        request: main_models.ModifyCompactionServiceSwitchRequest,
    ) -> main_models.ModifyCompactionServiceSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_compaction_service_switch_with_options(request, runtime)

    async def modify_compaction_service_switch_async(
        self,
        request: main_models.ModifyCompactionServiceSwitchRequest,
    ) -> main_models.ModifyCompactionServiceSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_compaction_service_switch_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: main_models.ModifyDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not DaraCore.is_null(request.product_form):
            query['ProductForm'] = request.product_form
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not DaraCore.is_null(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not DaraCore.is_null(request.product_form):
            query['ProductForm'] = request.product_form
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reserved_node_count):
            query['ReservedNodeCount'] = request.reserved_node_count
        if not DaraCore.is_null(request.reserved_node_size):
            query['ReservedNodeSize'] = request.reserved_node_size
        if not DaraCore.is_null(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterDescription',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterDescription',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterMaintainTime',
            version = '2021-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterMaintainTime',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterSSL',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterSSL',
            version = '2021-12-01',
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

    def modify_dbcluster_vip_with_options(
        self,
        request: main_models.ModifyDBClusterVipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterVipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_string):
            query['ConnectString'] = request.connect_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterVip',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.connect_string):
            query['ConnectString'] = request.connect_string
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterVip',
            version = '2021-12-01',
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
        if not DaraCore.is_null(tmp_req.gpu_elastic_plan):
            request.gpu_elastic_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.gpu_elastic_plan, 'GpuElasticPlan', 'json')
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_stop_interval):
            query['AutoStopInterval'] = request.auto_stop_interval
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.gpu_elastic_plan_shrink):
            query['GpuElasticPlan'] = request.gpu_elastic_plan_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.max_gpu_quantity):
            query['MaxGpuQuantity'] = request.max_gpu_quantity
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.min_gpu_quantity):
            query['MinGpuQuantity'] = request.min_gpu_quantity
        if not DaraCore.is_null(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        if not DaraCore.is_null(request.spec_name):
            query['SpecName'] = request.spec_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_resource_group_name):
            query['TargetResourceGroupName'] = request.target_resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourceGroup',
            version = '2021-12-01',
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
        if not DaraCore.is_null(tmp_req.gpu_elastic_plan):
            request.gpu_elastic_plan_shrink = Utils.array_to_string_with_specified_style(tmp_req.gpu_elastic_plan, 'GpuElasticPlan', 'json')
        if not DaraCore.is_null(tmp_req.ray_config):
            request.ray_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ray_config, 'RayConfig', 'json')
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_stop_interval):
            query['AutoStopInterval'] = request.auto_stop_interval
        if not DaraCore.is_null(request.cluster_mode):
            query['ClusterMode'] = request.cluster_mode
        if not DaraCore.is_null(request.cluster_size_resource):
            query['ClusterSizeResource'] = request.cluster_size_resource
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_spot):
            query['EnableSpot'] = request.enable_spot
        if not DaraCore.is_null(request.engine_params_shrink):
            query['EngineParams'] = request.engine_params_shrink
        if not DaraCore.is_null(request.gpu_elastic_plan_shrink):
            query['GpuElasticPlan'] = request.gpu_elastic_plan_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.max_cluster_count):
            query['MaxClusterCount'] = request.max_cluster_count
        if not DaraCore.is_null(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not DaraCore.is_null(request.max_gpu_quantity):
            query['MaxGpuQuantity'] = request.max_gpu_quantity
        if not DaraCore.is_null(request.min_cluster_count):
            query['MinClusterCount'] = request.min_cluster_count
        if not DaraCore.is_null(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        if not DaraCore.is_null(request.min_gpu_quantity):
            query['MinGpuQuantity'] = request.min_gpu_quantity
        if not DaraCore.is_null(request.ray_config_shrink):
            query['RayConfig'] = request.ray_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rules_shrink):
            query['Rules'] = request.rules_shrink
        if not DaraCore.is_null(request.spec_name):
            query['SpecName'] = request.spec_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_resource_group_name):
            query['TargetResourceGroupName'] = request.target_resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBResourceGroup',
            version = '2021-12-01',
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

    def modify_elastic_plan_with_options(
        self,
        request: main_models.ModifyElasticPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_size):
            query['TargetSize'] = request.target_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticPlan',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.elastic_plan_name):
            query['ElasticPlanName'] = request.elastic_plan_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.target_size):
            query['TargetSize'] = request.target_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticPlan',
            version = '2021-12-01',
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

    def modify_essd_cache_config_with_options(
        self,
        request: main_models.ModifyEssdCacheConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEssdCacheConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_essd_cache):
            query['EnableEssdCache'] = request.enable_essd_cache
        if not DaraCore.is_null(request.essd_cache_size):
            query['EssdCacheSize'] = request.essd_cache_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEssdCacheConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEssdCacheConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_essd_cache_config_with_options_async(
        self,
        request: main_models.ModifyEssdCacheConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEssdCacheConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_essd_cache):
            query['EnableEssdCache'] = request.enable_essd_cache
        if not DaraCore.is_null(request.essd_cache_size):
            query['EssdCacheSize'] = request.essd_cache_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEssdCacheConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEssdCacheConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_essd_cache_config(
        self,
        request: main_models.ModifyEssdCacheConfigRequest,
    ) -> main_models.ModifyEssdCacheConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_essd_cache_config_with_options(request, runtime)

    async def modify_essd_cache_config_async(
        self,
        request: main_models.ModifyEssdCacheConfigRequest,
    ) -> main_models.ModifyEssdCacheConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_essd_cache_config_with_options_async(request, runtime)

    def modify_lake_cache_size_with_options(
        self,
        request: main_models.ModifyLakeCacheSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLakeCacheSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_lake_cache):
            query['EnableLakeCache'] = request.enable_lake_cache
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLakeCacheSize',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLakeCacheSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lake_cache_size_with_options_async(
        self,
        request: main_models.ModifyLakeCacheSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLakeCacheSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.enable_lake_cache):
            query['EnableLakeCache'] = request.enable_lake_cache
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLakeCacheSize',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLakeCacheSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lake_cache_size(
        self,
        request: main_models.ModifyLakeCacheSizeRequest,
    ) -> main_models.ModifyLakeCacheSizeResponse:
        runtime = RuntimeOptions()
        return self.modify_lake_cache_size_with_options(request, runtime)

    async def modify_lake_cache_size_async(
        self,
        request: main_models.ModifyLakeCacheSizeRequest,
    ) -> main_models.ModifyLakeCacheSizeResponse:
        runtime = RuntimeOptions()
        return await self.modify_lake_cache_size_with_options_async(request, runtime)

    def modify_materialized_view_with_options(
        self,
        request: main_models.ModifyMaterializedViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterializedViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.enable_delay_alert):
            query['EnableDelayAlert'] = request.enable_delay_alert
        if not DaraCore.is_null(request.enable_failure_alert):
            query['EnableFailureAlert'] = request.enable_failure_alert
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.latency_tolerance):
            query['LatencyTolerance'] = request.latency_tolerance
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_write):
            query['QueryWrite'] = request.query_write
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterializedView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterializedViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_materialized_view_with_options_async(
        self,
        request: main_models.ModifyMaterializedViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterializedViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.enable_delay_alert):
            query['EnableDelayAlert'] = request.enable_delay_alert
        if not DaraCore.is_null(request.enable_failure_alert):
            query['EnableFailureAlert'] = request.enable_failure_alert
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.latency_tolerance):
            query['LatencyTolerance'] = request.latency_tolerance
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_write):
            query['QueryWrite'] = request.query_write
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterializedView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterializedViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_materialized_view(
        self,
        request: main_models.ModifyMaterializedViewRequest,
    ) -> main_models.ModifyMaterializedViewResponse:
        runtime = RuntimeOptions()
        return self.modify_materialized_view_with_options(request, runtime)

    async def modify_materialized_view_async(
        self,
        request: main_models.ModifyMaterializedViewRequest,
    ) -> main_models.ModifyMaterializedViewResponse:
        runtime = RuntimeOptions()
        return await self.modify_materialized_view_with_options_async(request, runtime)

    def modify_materialized_view_recommend_with_options(
        self,
        request: main_models.ModifyMaterializedViewRecommendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterializedViewRecommendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.min_rewrite_query_count):
            query['MinRewriteQueryCount'] = request.min_rewrite_query_count
        if not DaraCore.is_null(request.min_rewrite_query_pattern):
            query['MinRewriteQueryPattern'] = request.min_rewrite_query_pattern
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
        if not DaraCore.is_null(request.scan_queries_range):
            query['ScanQueriesRange'] = request.scan_queries_range
        if not DaraCore.is_null(request.scheduling_day):
            query['SchedulingDay'] = request.scheduling_day
        if not DaraCore.is_null(request.scheduling_policy):
            query['SchedulingPolicy'] = request.scheduling_policy
        if not DaraCore.is_null(request.slow_query_threshold):
            query['SlowQueryThreshold'] = request.slow_query_threshold
        if not DaraCore.is_null(request.specified_time):
            query['SpecifiedTime'] = request.specified_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterializedViewRecommend',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterializedViewRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_materialized_view_recommend_with_options_async(
        self,
        request: main_models.ModifyMaterializedViewRecommendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaterializedViewRecommendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.min_rewrite_query_count):
            query['MinRewriteQueryCount'] = request.min_rewrite_query_count
        if not DaraCore.is_null(request.min_rewrite_query_pattern):
            query['MinRewriteQueryPattern'] = request.min_rewrite_query_pattern
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
        if not DaraCore.is_null(request.scan_queries_range):
            query['ScanQueriesRange'] = request.scan_queries_range
        if not DaraCore.is_null(request.scheduling_day):
            query['SchedulingDay'] = request.scheduling_day
        if not DaraCore.is_null(request.scheduling_policy):
            query['SchedulingPolicy'] = request.scheduling_policy
        if not DaraCore.is_null(request.slow_query_threshold):
            query['SlowQueryThreshold'] = request.slow_query_threshold
        if not DaraCore.is_null(request.specified_time):
            query['SpecifiedTime'] = request.specified_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaterializedViewRecommend',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaterializedViewRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_materialized_view_recommend(
        self,
        request: main_models.ModifyMaterializedViewRecommendRequest,
    ) -> main_models.ModifyMaterializedViewRecommendResponse:
        runtime = RuntimeOptions()
        return self.modify_materialized_view_recommend_with_options(request, runtime)

    async def modify_materialized_view_recommend_async(
        self,
        request: main_models.ModifyMaterializedViewRecommendRequest,
    ) -> main_models.ModifyMaterializedViewRecommendResponse:
        runtime = RuntimeOptions()
        return await self.modify_materialized_view_recommend_with_options_async(request, runtime)

    def modify_performance_view_with_options(
        self,
        tmp_req: main_models.ModifyPerformanceViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPerformanceViewResponse:
        tmp_req.validate()
        request = main_models.ModifyPerformanceViewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_detail):
            request.view_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
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
        if not DaraCore.is_null(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPerformanceView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPerformanceViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_performance_view_with_options_async(
        self,
        tmp_req: main_models.ModifyPerformanceViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPerformanceViewResponse:
        tmp_req.validate()
        request = main_models.ModifyPerformanceViewShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_detail):
            request.view_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_detail, 'ViewDetail', 'json')
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
        if not DaraCore.is_null(request.view_detail_shrink):
            query['ViewDetail'] = request.view_detail_shrink
        if not DaraCore.is_null(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPerformanceView',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPerformanceViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_performance_view(
        self,
        request: main_models.ModifyPerformanceViewRequest,
    ) -> main_models.ModifyPerformanceViewResponse:
        runtime = RuntimeOptions()
        return self.modify_performance_view_with_options(request, runtime)

    async def modify_performance_view_async(
        self,
        request: main_models.ModifyPerformanceViewRequest,
    ) -> main_models.ModifyPerformanceViewResponse:
        runtime = RuntimeOptions()
        return await self.modify_performance_view_with_options_async(request, runtime)

    def modify_sql_template_position_with_options(
        self,
        request: main_models.ModifySqlTemplatePositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySqlTemplatePositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_template_group_id):
            query['TargetTemplateGroupId'] = request.target_template_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySqlTemplatePosition',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySqlTemplatePositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sql_template_position_with_options_async(
        self,
        request: main_models.ModifySqlTemplatePositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySqlTemplatePositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_template_group_id):
            query['TargetTemplateGroupId'] = request.target_template_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySqlTemplatePosition',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySqlTemplatePositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sql_template_position(
        self,
        request: main_models.ModifySqlTemplatePositionRequest,
    ) -> main_models.ModifySqlTemplatePositionResponse:
        runtime = RuntimeOptions()
        return self.modify_sql_template_position_with_options(request, runtime)

    async def modify_sql_template_position_async(
        self,
        request: main_models.ModifySqlTemplatePositionRequest,
    ) -> main_models.ModifySqlTemplatePositionResponse:
        runtime = RuntimeOptions()
        return await self.modify_sql_template_position_with_options_async(request, runtime)

    def modify_user_eni_vswitch_options_with_options(
        self,
        request: main_models.ModifyUserEniVswitchOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserEniVswitchOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
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
        body = {}
        if not DaraCore.is_null(request.v_switch_options):
            body['VSwitchOptions'] = request.v_switch_options
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserEniVswitchOptions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserEniVswitchOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_eni_vswitch_options_with_options_async(
        self,
        request: main_models.ModifyUserEniVswitchOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserEniVswitchOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
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
        body = {}
        if not DaraCore.is_null(request.v_switch_options):
            body['VSwitchOptions'] = request.v_switch_options
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserEniVswitchOptions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserEniVswitchOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_eni_vswitch_options(
        self,
        request: main_models.ModifyUserEniVswitchOptionsRequest,
    ) -> main_models.ModifyUserEniVswitchOptionsResponse:
        runtime = RuntimeOptions()
        return self.modify_user_eni_vswitch_options_with_options(request, runtime)

    async def modify_user_eni_vswitch_options_async(
        self,
        request: main_models.ModifyUserEniVswitchOptionsRequest,
    ) -> main_models.ModifyUserEniVswitchOptionsResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_eni_vswitch_options_with_options_async(request, runtime)

    def preload_spark_app_metrics_with_options(
        self,
        request: main_models.PreloadSparkAppMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreloadSparkAppMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreloadSparkAppMetrics',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreloadSparkAppMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_spark_app_metrics_with_options_async(
        self,
        request: main_models.PreloadSparkAppMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreloadSparkAppMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreloadSparkAppMetrics',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreloadSparkAppMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_spark_app_metrics(
        self,
        request: main_models.PreloadSparkAppMetricsRequest,
    ) -> main_models.PreloadSparkAppMetricsResponse:
        runtime = RuntimeOptions()
        return self.preload_spark_app_metrics_with_options(request, runtime)

    async def preload_spark_app_metrics_async(
        self,
        request: main_models.PreloadSparkAppMetricsRequest,
    ) -> main_models.PreloadSparkAppMetricsResponse:
        runtime = RuntimeOptions()
        return await self.preload_spark_app_metrics_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseClusterPublicConnection',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseClusterPublicConnection',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2021-12-01',
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
            version = '2021-12-01',
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
            version = '2021-12-01',
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

    def set_spark_app_log_root_path_with_options(
        self,
        request: main_models.SetSparkAppLogRootPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSparkAppLogRootPathResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.oss_log_path):
            body['OssLogPath'] = request.oss_log_path
        if not DaraCore.is_null(request.use_default_oss):
            body['UseDefaultOss'] = request.use_default_oss
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSparkAppLogRootPath',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSparkAppLogRootPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_spark_app_log_root_path_with_options_async(
        self,
        request: main_models.SetSparkAppLogRootPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSparkAppLogRootPathResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.oss_log_path):
            body['OssLogPath'] = request.oss_log_path
        if not DaraCore.is_null(request.use_default_oss):
            body['UseDefaultOss'] = request.use_default_oss
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSparkAppLogRootPath',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSparkAppLogRootPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_spark_app_log_root_path(
        self,
        request: main_models.SetSparkAppLogRootPathRequest,
    ) -> main_models.SetSparkAppLogRootPathResponse:
        runtime = RuntimeOptions()
        return self.set_spark_app_log_root_path_with_options(request, runtime)

    async def set_spark_app_log_root_path_async(
        self,
        request: main_models.SetSparkAppLogRootPathRequest,
    ) -> main_models.SetSparkAppLogRootPathResponse:
        runtime = RuntimeOptions()
        return await self.set_spark_app_log_root_path_with_options_async(request, runtime)

    def start_aps_job_with_options(
        self,
        request: main_models.StartApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartApsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_aps_job_with_options_async(
        self,
        request: main_models.StartApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartApsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_aps_job(
        self,
        request: main_models.StartApsJobRequest,
    ) -> main_models.StartApsJobResponse:
        runtime = RuntimeOptions()
        return self.start_aps_job_with_options(request, runtime)

    async def start_aps_job_async(
        self,
        request: main_models.StartApsJobRequest,
    ) -> main_models.StartApsJobResponse:
        runtime = RuntimeOptions()
        return await self.start_aps_job_with_options_async(request, runtime)

    def start_spark_repl_session_with_options(
        self,
        request: main_models.StartSparkReplSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSparkReplSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSparkReplSession',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSparkReplSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_spark_repl_session_with_options_async(
        self,
        request: main_models.StartSparkReplSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSparkReplSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSparkReplSession',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSparkReplSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_spark_repl_session(
        self,
        request: main_models.StartSparkReplSessionRequest,
    ) -> main_models.StartSparkReplSessionResponse:
        runtime = RuntimeOptions()
        return self.start_spark_repl_session_with_options(request, runtime)

    async def start_spark_repl_session_async(
        self,
        request: main_models.StartSparkReplSessionRequest,
    ) -> main_models.StartSparkReplSessionResponse:
        runtime = RuntimeOptions()
        return await self.start_spark_repl_session_with_options_async(request, runtime)

    def start_spark_sqlengine_with_options(
        self,
        request: main_models.StartSparkSQLEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSparkSQLEngineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.jars):
            body['Jars'] = request.jars
        if not DaraCore.is_null(request.max_executor):
            body['MaxExecutor'] = request.max_executor
        if not DaraCore.is_null(request.min_executor):
            body['MinExecutor'] = request.min_executor
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.slot_num):
            body['SlotNum'] = request.slot_num
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSparkSQLEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSparkSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_spark_sqlengine_with_options_async(
        self,
        request: main_models.StartSparkSQLEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSparkSQLEngineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.jars):
            body['Jars'] = request.jars
        if not DaraCore.is_null(request.max_executor):
            body['MaxExecutor'] = request.max_executor
        if not DaraCore.is_null(request.min_executor):
            body['MinExecutor'] = request.min_executor
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.slot_num):
            body['SlotNum'] = request.slot_num
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSparkSQLEngine',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSparkSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_spark_sqlengine(
        self,
        request: main_models.StartSparkSQLEngineRequest,
    ) -> main_models.StartSparkSQLEngineResponse:
        runtime = RuntimeOptions()
        return self.start_spark_sqlengine_with_options(request, runtime)

    async def start_spark_sqlengine_async(
        self,
        request: main_models.StartSparkSQLEngineRequest,
    ) -> main_models.StartSparkSQLEngineResponse:
        runtime = RuntimeOptions()
        return await self.start_spark_sqlengine_with_options_async(request, runtime)

    def submit_result_export_job_with_options(
        self,
        request: main_models.SubmitResultExportJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitResultExportJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            body['Engine'] = request.engine
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.sql):
            body['SQL'] = request.sql
        if not DaraCore.is_null(request.schema):
            body['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitResultExportJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitResultExportJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_result_export_job_with_options_async(
        self,
        request: main_models.SubmitResultExportJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitResultExportJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.engine):
            body['Engine'] = request.engine
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            body['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.sql):
            body['SQL'] = request.sql
        if not DaraCore.is_null(request.schema):
            body['Schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitResultExportJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitResultExportJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_result_export_job(
        self,
        request: main_models.SubmitResultExportJobRequest,
    ) -> main_models.SubmitResultExportJobResponse:
        runtime = RuntimeOptions()
        return self.submit_result_export_job_with_options(request, runtime)

    async def submit_result_export_job_async(
        self,
        request: main_models.SubmitResultExportJobRequest,
    ) -> main_models.SubmitResultExportJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_result_export_job_with_options_async(request, runtime)

    def submit_spark_app_with_options(
        self,
        request: main_models.SubmitSparkAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSparkAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not DaraCore.is_null(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSparkApp',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSparkAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_app_with_options_async(
        self,
        request: main_models.SubmitSparkAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSparkAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not DaraCore.is_null(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not DaraCore.is_null(request.app_name):
            body['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            body['AppType'] = request.app_type
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not DaraCore.is_null(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSparkApp',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSparkAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_app(
        self,
        request: main_models.SubmitSparkAppRequest,
    ) -> main_models.SubmitSparkAppResponse:
        runtime = RuntimeOptions()
        return self.submit_spark_app_with_options(request, runtime)

    async def submit_spark_app_async(
        self,
        request: main_models.SubmitSparkAppRequest,
    ) -> main_models.SubmitSparkAppResponse:
        runtime = RuntimeOptions()
        return await self.submit_spark_app_with_options_async(request, runtime)

    def submit_spark_log_analyze_task_with_options(
        self,
        request: main_models.SubmitSparkLogAnalyzeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSparkLogAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSparkLogAnalyzeTask',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_log_analyze_task_with_options_async(
        self,
        request: main_models.SubmitSparkLogAnalyzeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSparkLogAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSparkLogAnalyzeTask',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_log_analyze_task(
        self,
        request: main_models.SubmitSparkLogAnalyzeTaskRequest,
    ) -> main_models.SubmitSparkLogAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_spark_log_analyze_task_with_options(request, runtime)

    async def submit_spark_log_analyze_task_async(
        self,
        request: main_models.SubmitSparkLogAnalyzeTaskRequest,
    ) -> main_models.SubmitSparkLogAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_spark_log_analyze_task_with_options_async(request, runtime)

    def suspend_aps_job_with_options(
        self,
        request: main_models.SuspendApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendApsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_aps_job_with_options_async(
        self,
        request: main_models.SuspendApsJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendApsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aps_job_id):
            body['ApsJobId'] = request.aps_job_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendApsJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendApsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_aps_job(
        self,
        request: main_models.SuspendApsJobRequest,
    ) -> main_models.SuspendApsJobResponse:
        runtime = RuntimeOptions()
        return self.suspend_aps_job_with_options(request, runtime)

    async def suspend_aps_job_async(
        self,
        request: main_models.SuspendApsJobRequest,
    ) -> main_models.SuspendApsJobResponse:
        runtime = RuntimeOptions()
        return await self.suspend_aps_job_with_options_async(request, runtime)

    def unbind_account_with_options(
        self,
        request: main_models.UnbindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_account_with_options_async(
        self,
        request: main_models.UnbindAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_account(
        self,
        request: main_models.UnbindAccountRequest,
    ) -> main_models.UnbindAccountResponse:
        runtime = RuntimeOptions()
        return self.unbind_account_with_options(request, runtime)

    async def unbind_account_async(
        self,
        request: main_models.UnbindAccountRequest,
    ) -> main_models.UnbindAccountResponse:
        runtime = RuntimeOptions()
        return await self.unbind_account_with_options_async(request, runtime)

    def unbind_dbresource_group_with_user_with_options(
        self,
        request: main_models.UnbindDBResourceGroupWithUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDBResourceGroupWithUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourceGroupWithUser',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_user):
            query['GroupUser'] = request.group_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDBResourceGroupWithUser',
            version = '2021-12-01',
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

    def update_aps_webhook_with_options(
        self,
        tmp_req: main_models.UpdateApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApsWebhookResponse:
        tmp_req.validate()
        request = main_models.UpdateApsWebhookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.webhook):
            request.webhook_shrink = Utils.array_to_string_with_specified_style(tmp_req.webhook, 'Webhook', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webhook_shrink):
            body['Webhook'] = request.webhook_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApsWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aps_webhook_with_options_async(
        self,
        tmp_req: main_models.UpdateApsWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApsWebhookResponse:
        tmp_req.validate()
        request = main_models.UpdateApsWebhookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.webhook):
            request.webhook_shrink = Utils.array_to_string_with_specified_style(tmp_req.webhook, 'Webhook', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.webhook_shrink):
            body['Webhook'] = request.webhook_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApsWebhook',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApsWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aps_webhook(
        self,
        request: main_models.UpdateApsWebhookRequest,
    ) -> main_models.UpdateApsWebhookResponse:
        runtime = RuntimeOptions()
        return self.update_aps_webhook_with_options(request, runtime)

    async def update_aps_webhook_async(
        self,
        request: main_models.UpdateApsWebhookRequest,
    ) -> main_models.UpdateApsWebhookResponse:
        runtime = RuntimeOptions()
        return await self.update_aps_webhook_with_options_async(request, runtime)

    def update_lake_storage_with_options(
        self,
        tmp_req: main_models.UpdateLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLakeStorageResponse:
        tmp_req.validate()
        request = main_models.UpdateLakeStorageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.lake_storage_id):
            body['LakeStorageId'] = request.lake_storage_id
        if not DaraCore.is_null(request.permissions_shrink):
            body['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLakeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_lake_storage_with_options_async(
        self,
        tmp_req: main_models.UpdateLakeStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLakeStorageResponse:
        tmp_req.validate()
        request = main_models.UpdateLakeStorageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        body = {}
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.lake_storage_id):
            body['LakeStorageId'] = request.lake_storage_id
        if not DaraCore.is_null(request.permissions_shrink):
            body['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLakeStorage',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLakeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_lake_storage(
        self,
        request: main_models.UpdateLakeStorageRequest,
    ) -> main_models.UpdateLakeStorageResponse:
        runtime = RuntimeOptions()
        return self.update_lake_storage_with_options(request, runtime)

    async def update_lake_storage_async(
        self,
        request: main_models.UpdateLakeStorageRequest,
    ) -> main_models.UpdateLakeStorageResponse:
        runtime = RuntimeOptions()
        return await self.update_lake_storage_with_options_async(request, runtime)

    def update_spark_template_file_with_options(
        self,
        request: main_models.UpdateSparkTemplateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSparkTemplateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSparkTemplateFile',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSparkTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_spark_template_file_with_options_async(
        self,
        request: main_models.UpdateSparkTemplateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSparkTemplateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSparkTemplateFile',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSparkTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_spark_template_file(
        self,
        request: main_models.UpdateSparkTemplateFileRequest,
    ) -> main_models.UpdateSparkTemplateFileResponse:
        runtime = RuntimeOptions()
        return self.update_spark_template_file_with_options(request, runtime)

    async def update_spark_template_file_async(
        self,
        request: main_models.UpdateSparkTemplateFileRequest,
    ) -> main_models.UpdateSparkTemplateFileResponse:
        runtime = RuntimeOptions()
        return await self.update_spark_template_file_with_options_async(request, runtime)

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
            version = '2021-12-01',
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
            version = '2021-12-01',
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
