# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_ft20210101 import models as ft_20210101_models
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
            'ap-northeast-2-pop': 'ft.aliyuncs.com',
            'ap-south-1': 'ft.aliyuncs.com',
            'ap-southeast-1': 'ft.aliyuncs.com',
            'ap-southeast-2': 'ft.aliyuncs.com',
            'ap-southeast-3': 'ft.aliyuncs.com',
            'ap-southeast-5': 'ft.aliyuncs.com',
            'cn-beijing': 'ft.aliyuncs.com',
            'cn-beijing-finance-1': 'ft.aliyuncs.com',
            'cn-beijing-finance-pop': 'ft.aliyuncs.com',
            'cn-beijing-gov-1': 'ft.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ft.aliyuncs.com',
            'cn-chengdu': 'ft.aliyuncs.com',
            'cn-edge-1': 'ft.aliyuncs.com',
            'cn-fujian': 'ft.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ft.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ft.aliyuncs.com',
            'cn-hangzhou-finance': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ft.aliyuncs.com',
            'cn-hangzhou-test-306': 'ft.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ft.aliyuncs.com',
            'cn-huhehaote': 'ft.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ft.aliyuncs.com',
            'cn-qingdao': 'ft.aliyuncs.com',
            'cn-qingdao-nebula': 'ft.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ft.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ft.aliyuncs.com',
            'cn-shanghai-finance-1': 'ft.aliyuncs.com',
            'cn-shanghai-inner': 'ft.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ft.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ft.aliyuncs.com',
            'cn-shenzhen-inner': 'ft.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ft.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ft.aliyuncs.com',
            'cn-wuhan': 'ft.aliyuncs.com',
            'cn-wulanchabu': 'ft.aliyuncs.com',
            'cn-yushanfang': 'ft.aliyuncs.com',
            'cn-zhangbei': 'ft.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ft.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ft.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ft.aliyuncs.com',
            'eu-central-1': 'ft.aliyuncs.com',
            'eu-west-1': 'ft.aliyuncs.com',
            'eu-west-1-oxs': 'ft.aliyuncs.com',
            'me-east-1': 'ft.aliyuncs.com',
            'rus-west-1-pop': 'ft.aliyuncs.com',
            'us-west-1': 'ft.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ft', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def data_rate_limit_test_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.DataRateLimitTestResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DataRateLimitTest',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.DataRateLimitTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def data_rate_limit_test_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.DataRateLimitTestResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DataRateLimitTest',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.DataRateLimitTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def data_rate_limit_test(self) -> ft_20210101_models.DataRateLimitTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.data_rate_limit_test_with_options(runtime)

    async def data_rate_limit_test_async(self) -> ft_20210101_models.DataRateLimitTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.data_rate_limit_test_with_options_async(runtime)

    def normal_rpc_hsf_api_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.NormalRpcHsfApiResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='NormalRpcHsfApi',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.NormalRpcHsfApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def normal_rpc_hsf_api_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.NormalRpcHsfApiResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='NormalRpcHsfApi',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.NormalRpcHsfApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def normal_rpc_hsf_api(self) -> ft_20210101_models.NormalRpcHsfApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.normal_rpc_hsf_api_with_options(runtime)

    async def normal_rpc_hsf_api_async(self) -> ft_20210101_models.NormalRpcHsfApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.normal_rpc_hsf_api_with_options_async(runtime)

    def normal_rpc_http_api_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.NormalRpcHttpApiResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='NormalRpcHttpApi',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.NormalRpcHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def normal_rpc_http_api_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.NormalRpcHttpApiResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='NormalRpcHttpApi',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.NormalRpcHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def normal_rpc_http_api(self) -> ft_20210101_models.NormalRpcHttpApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.normal_rpc_http_api_with_options(runtime)

    async def normal_rpc_http_api_async(self) -> ft_20210101_models.NormalRpcHttpApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.normal_rpc_http_api_with_options_async(runtime)

    def rpc_data_upload_with_options(
        self,
        request: ft_20210101_models.RpcDataUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.RpcDataUploadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_1):
            query['query1'] = request.query_1
        if not UtilClient.is_unset(request.query_2):
            query['query2'] = request.query_2
        body = {}
        if not UtilClient.is_unset(request.large_param):
            body['largeParam'] = request.large_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RpcDataUpload',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.RpcDataUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def rpc_data_upload_with_options_async(
        self,
        request: ft_20210101_models.RpcDataUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.RpcDataUploadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_1):
            query['query1'] = request.query_1
        if not UtilClient.is_unset(request.query_2):
            query['query2'] = request.query_2
        body = {}
        if not UtilClient.is_unset(request.large_param):
            body['largeParam'] = request.large_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RpcDataUpload',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.RpcDataUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rpc_data_upload(
        self,
        request: ft_20210101_models.RpcDataUploadRequest,
    ) -> ft_20210101_models.RpcDataUploadResponse:
        runtime = util_models.RuntimeOptions()
        return self.rpc_data_upload_with_options(request, runtime)

    async def rpc_data_upload_async(
        self,
        request: ft_20210101_models.RpcDataUploadRequest,
    ) -> ft_20210101_models.RpcDataUploadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rpc_data_upload_with_options_async(request, runtime)

    def rpc_data_upload_and_download_with_options(
        self,
        request: ft_20210101_models.RpcDataUploadAndDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.RpcDataUploadAndDownloadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_1):
            query['query1'] = request.query_1
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RpcDataUploadAndDownload',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.RpcDataUploadAndDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def rpc_data_upload_and_download_with_options_async(
        self,
        request: ft_20210101_models.RpcDataUploadAndDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.RpcDataUploadAndDownloadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_1):
            query['query1'] = request.query_1
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RpcDataUploadAndDownload',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.RpcDataUploadAndDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rpc_data_upload_and_download(
        self,
        request: ft_20210101_models.RpcDataUploadAndDownloadRequest,
    ) -> ft_20210101_models.RpcDataUploadAndDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return self.rpc_data_upload_and_download_with_options(request, runtime)

    async def rpc_data_upload_and_download_async(
        self,
        request: ft_20210101_models.RpcDataUploadAndDownloadRequest,
    ) -> ft_20210101_models.RpcDataUploadAndDownloadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rpc_data_upload_and_download_with_options_async(request, runtime)

    def rpc_data_upload_test_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.RpcDataUploadTestResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RpcDataUploadTest',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.RpcDataUploadTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def rpc_data_upload_test_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20210101_models.RpcDataUploadTestResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RpcDataUploadTest',
            version='2021-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ft_20210101_models.RpcDataUploadTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rpc_data_upload_test(self) -> ft_20210101_models.RpcDataUploadTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.rpc_data_upload_test_with_options(runtime)

    async def rpc_data_upload_test_async(self) -> ft_20210101_models.RpcDataUploadTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rpc_data_upload_test_with_options_async(runtime)
