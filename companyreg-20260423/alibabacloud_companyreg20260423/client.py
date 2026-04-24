# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_companyreg20260423 import models as main_models
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
            'ap-northeast-1': 'companyreg.aliyuncs.com',
            'ap-northeast-2-pop': 'companyreg.aliyuncs.com',
            'ap-south-1': 'companyreg.aliyuncs.com',
            'ap-southeast-1': 'companyreg.aliyuncs.com',
            'ap-southeast-2': 'companyreg.aliyuncs.com',
            'ap-southeast-3': 'companyreg.aliyuncs.com',
            'ap-southeast-5': 'companyreg.aliyuncs.com',
            'cn-beijing': 'companyreg.aliyuncs.com',
            'cn-beijing-finance-1': 'companyreg.aliyuncs.com',
            'cn-beijing-finance-pop': 'companyreg.aliyuncs.com',
            'cn-beijing-gov-1': 'companyreg.aliyuncs.com',
            'cn-beijing-nu16-b01': 'companyreg.aliyuncs.com',
            'cn-chengdu': 'companyreg.aliyuncs.com',
            'cn-edge-1': 'companyreg.aliyuncs.com',
            'cn-fujian': 'companyreg.aliyuncs.com',
            'cn-haidian-cm12-c01': 'companyreg.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'companyreg.aliyuncs.com',
            'cn-hangzhou-finance': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'companyreg.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'companyreg.aliyuncs.com',
            'cn-hangzhou-test-306': 'companyreg.aliyuncs.com',
            'cn-hongkong': 'companyreg.aliyuncs.com',
            'cn-hongkong-finance-pop': 'companyreg.aliyuncs.com',
            'cn-huhehaote': 'companyreg.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'companyreg.aliyuncs.com',
            'cn-north-2-gov-1': 'companyreg.aliyuncs.com',
            'cn-qingdao': 'companyreg.aliyuncs.com',
            'cn-qingdao-nebula': 'companyreg.aliyuncs.com',
            'cn-shanghai': 'companyreg.aliyuncs.com',
            'cn-shanghai-et15-b01': 'companyreg.aliyuncs.com',
            'cn-shanghai-et2-b01': 'companyreg.aliyuncs.com',
            'cn-shanghai-finance-1': 'companyreg.aliyuncs.com',
            'cn-shanghai-inner': 'companyreg.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'companyreg.aliyuncs.com',
            'cn-shenzhen': 'companyreg.aliyuncs.com',
            'cn-shenzhen-finance-1': 'companyreg.aliyuncs.com',
            'cn-shenzhen-inner': 'companyreg.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'companyreg.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'companyreg.aliyuncs.com',
            'cn-wuhan': 'companyreg.aliyuncs.com',
            'cn-wulanchabu': 'companyreg.aliyuncs.com',
            'cn-yushanfang': 'companyreg.aliyuncs.com',
            'cn-zhangbei': 'companyreg.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'companyreg.aliyuncs.com',
            'cn-zhangjiakou': 'companyreg.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'companyreg.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'companyreg.aliyuncs.com',
            'eu-central-1': 'companyreg.aliyuncs.com',
            'eu-west-1': 'companyreg.aliyuncs.com',
            'eu-west-1-oxs': 'companyreg.aliyuncs.com',
            'me-east-1': 'companyreg.aliyuncs.com',
            'rus-west-1-pop': 'companyreg.aliyuncs.com',
            'us-east-1': 'companyreg.aliyuncs.com',
            'us-west-1': 'companyreg.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('companyreg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_success_icp_data_with_options(
        self,
        request: main_models.QuerySuccessIcpDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySuccessIcpDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySuccessIcpData',
            version = '2026-04-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySuccessIcpDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_success_icp_data_with_options_async(
        self,
        request: main_models.QuerySuccessIcpDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySuccessIcpDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySuccessIcpData',
            version = '2026-04-23',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySuccessIcpDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_success_icp_data(
        self,
        request: main_models.QuerySuccessIcpDataRequest,
    ) -> main_models.QuerySuccessIcpDataResponse:
        runtime = RuntimeOptions()
        return self.query_success_icp_data_with_options(request, runtime)

    async def query_success_icp_data_async(
        self,
        request: main_models.QuerySuccessIcpDataRequest,
    ) -> main_models.QuerySuccessIcpDataResponse:
        runtime = RuntimeOptions()
        return await self.query_success_icp_data_with_options_async(request, runtime)
