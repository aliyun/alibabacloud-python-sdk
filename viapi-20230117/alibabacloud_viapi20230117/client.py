# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_viapi20230117 import models as viapi_20230117_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('viapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_waiting_async_job_with_options(
        self,
        request: viapi_20230117_models.CancelWaitingAsyncJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20230117_models.CancelWaitingAsyncJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelWaitingAsyncJob',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20230117_models.CancelWaitingAsyncJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_waiting_async_job_with_options_async(
        self,
        request: viapi_20230117_models.CancelWaitingAsyncJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20230117_models.CancelWaitingAsyncJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelWaitingAsyncJob',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20230117_models.CancelWaitingAsyncJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_waiting_async_job(
        self,
        request: viapi_20230117_models.CancelWaitingAsyncJobRequest,
    ) -> viapi_20230117_models.CancelWaitingAsyncJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_waiting_async_job_with_options(request, runtime)

    async def cancel_waiting_async_job_async(
        self,
        request: viapi_20230117_models.CancelWaitingAsyncJobRequest,
    ) -> viapi_20230117_models.CancelWaitingAsyncJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_waiting_async_job_with_options_async(request, runtime)

    def get_async_job_result_with_options(
        self,
        request: viapi_20230117_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20230117_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20230117_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: viapi_20230117_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20230117_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20230117_models.GetAsyncJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_job_result(
        self,
        request: viapi_20230117_models.GetAsyncJobResultRequest,
    ) -> viapi_20230117_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: viapi_20230117_models.GetAsyncJobResultRequest,
    ) -> viapi_20230117_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def query_async_job_list_with_options(
        self,
        request: viapi_20230117_models.QueryAsyncJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20230117_models.QueryAsyncJobListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pop_api_name):
            body['PopApiName'] = request.pop_api_name
        if not UtilClient.is_unset(request.pop_product):
            body['PopProduct'] = request.pop_product
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAsyncJobList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20230117_models.QueryAsyncJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_async_job_list_with_options_async(
        self,
        request: viapi_20230117_models.QueryAsyncJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_20230117_models.QueryAsyncJobListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pop_api_name):
            body['PopApiName'] = request.pop_api_name
        if not UtilClient.is_unset(request.pop_product):
            body['PopProduct'] = request.pop_product
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAsyncJobList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_20230117_models.QueryAsyncJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_async_job_list(
        self,
        request: viapi_20230117_models.QueryAsyncJobListRequest,
    ) -> viapi_20230117_models.QueryAsyncJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_async_job_list_with_options(request, runtime)

    async def query_async_job_list_async(
        self,
        request: viapi_20230117_models.QueryAsyncJobListRequest,
    ) -> viapi_20230117_models.QueryAsyncJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_async_job_list_with_options_async(request, runtime)
