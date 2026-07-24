# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_alikafkastreaming20260202 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('alikafkastreaming', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_sql_content_with_options(
        self,
        request: main_models.CheckSqlContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSqlContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_content):
            query['SqlContent'] = request.sql_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSqlContent',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSqlContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sql_content_with_options_async(
        self,
        request: main_models.CheckSqlContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSqlContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_content):
            query['SqlContent'] = request.sql_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSqlContent',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSqlContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sql_content(
        self,
        request: main_models.CheckSqlContentRequest,
    ) -> main_models.CheckSqlContentResponse:
        runtime = RuntimeOptions()
        return self.check_sql_content_with_options(request, runtime)

    async def check_sql_content_async(
        self,
        request: main_models.CheckSqlContentRequest,
    ) -> main_models.CheckSqlContentResponse:
        runtime = RuntimeOptions()
        return await self.check_sql_content_with_options_async(request, runtime)

    def create_compute_instance_with_options(
        self,
        request: main_models.CreateComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_instance_with_options_async(
        self,
        request: main_models.CreateComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.paid_type):
            query['PaidType'] = request.paid_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_instance(
        self,
        request: main_models.CreateComputeInstanceRequest,
    ) -> main_models.CreateComputeInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_compute_instance_with_options(request, runtime)

    async def create_compute_instance_async(
        self,
        request: main_models.CreateComputeInstanceRequest,
    ) -> main_models.CreateComputeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_compute_instance_with_options_async(request, runtime)

    def create_compute_job_with_options(
        self,
        request: main_models.CreateComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cu_limit):
            query['CuLimit'] = request.cu_limit
        if not DaraCore.is_null(request.cu_reserved):
            query['CuReserved'] = request.cu_reserved
        if not DaraCore.is_null(request.draft_sql):
            query['DraftSql'] = request.draft_sql
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_config):
            query['JobConfig'] = request.job_config
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.upgrade_mode):
            query['UpgradeMode'] = request.upgrade_mode
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_job_with_options_async(
        self,
        request: main_models.CreateComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cu_limit):
            query['CuLimit'] = request.cu_limit
        if not DaraCore.is_null(request.cu_reserved):
            query['CuReserved'] = request.cu_reserved
        if not DaraCore.is_null(request.draft_sql):
            query['DraftSql'] = request.draft_sql
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_config):
            query['JobConfig'] = request.job_config
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.upgrade_mode):
            query['UpgradeMode'] = request.upgrade_mode
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_job(
        self,
        request: main_models.CreateComputeJobRequest,
    ) -> main_models.CreateComputeJobResponse:
        runtime = RuntimeOptions()
        return self.create_compute_job_with_options(request, runtime)

    async def create_compute_job_async(
        self,
        request: main_models.CreateComputeJobRequest,
    ) -> main_models.CreateComputeJobResponse:
        runtime = RuntimeOptions()
        return await self.create_compute_job_with_options_async(request, runtime)

    def delete_compute_instance_with_options(
        self,
        request: main_models.DeleteComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compute_instance_with_options_async(
        self,
        request: main_models.DeleteComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compute_instance(
        self,
        request: main_models.DeleteComputeInstanceRequest,
    ) -> main_models.DeleteComputeInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_compute_instance_with_options(request, runtime)

    async def delete_compute_instance_async(
        self,
        request: main_models.DeleteComputeInstanceRequest,
    ) -> main_models.DeleteComputeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_compute_instance_with_options_async(request, runtime)

    def delete_compute_job_with_options(
        self,
        request: main_models.DeleteComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compute_job_with_options_async(
        self,
        request: main_models.DeleteComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compute_job(
        self,
        request: main_models.DeleteComputeJobRequest,
    ) -> main_models.DeleteComputeJobResponse:
        runtime = RuntimeOptions()
        return self.delete_compute_job_with_options(request, runtime)

    async def delete_compute_job_async(
        self,
        request: main_models.DeleteComputeJobRequest,
    ) -> main_models.DeleteComputeJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_compute_job_with_options_async(request, runtime)

    def get_compute_instance_with_options(
        self,
        request: main_models.GetComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_instance_with_options_async(
        self,
        request: main_models.GetComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_instance(
        self,
        request: main_models.GetComputeInstanceRequest,
    ) -> main_models.GetComputeInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_compute_instance_with_options(request, runtime)

    async def get_compute_instance_async(
        self,
        request: main_models.GetComputeInstanceRequest,
    ) -> main_models.GetComputeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_compute_instance_with_options_async(request, runtime)

    def get_compute_job_with_options(
        self,
        request: main_models.GetComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_job_with_options_async(
        self,
        request: main_models.GetComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_job(
        self,
        request: main_models.GetComputeJobRequest,
    ) -> main_models.GetComputeJobResponse:
        runtime = RuntimeOptions()
        return self.get_compute_job_with_options(request, runtime)

    async def get_compute_job_async(
        self,
        request: main_models.GetComputeJobRequest,
    ) -> main_models.GetComputeJobResponse:
        runtime = RuntimeOptions()
        return await self.get_compute_job_with_options_async(request, runtime)

    def get_job_debug_data_with_options(
        self,
        request: main_models.GetJobDebugDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDebugDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobDebugData',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDebugDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_debug_data_with_options_async(
        self,
        request: main_models.GetJobDebugDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDebugDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobDebugData',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDebugDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_debug_data(
        self,
        request: main_models.GetJobDebugDataRequest,
    ) -> main_models.GetJobDebugDataResponse:
        runtime = RuntimeOptions()
        return self.get_job_debug_data_with_options(request, runtime)

    async def get_job_debug_data_async(
        self,
        request: main_models.GetJobDebugDataRequest,
    ) -> main_models.GetJobDebugDataResponse:
        runtime = RuntimeOptions()
        return await self.get_job_debug_data_with_options_async(request, runtime)

    def list_compute_instances_with_options(
        self,
        tmp_req: main_models.ListComputeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeInstancesResponse:
        tmp_req.validate()
        request = main_models.ListComputeInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeInstances',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_instances_with_options_async(
        self,
        tmp_req: main_models.ListComputeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeInstancesResponse:
        tmp_req.validate()
        request = main_models.ListComputeInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeInstances',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_instances(
        self,
        request: main_models.ListComputeInstancesRequest,
    ) -> main_models.ListComputeInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_compute_instances_with_options(request, runtime)

    async def list_compute_instances_async(
        self,
        request: main_models.ListComputeInstancesRequest,
    ) -> main_models.ListComputeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_compute_instances_with_options_async(request, runtime)

    def list_compute_instances_in_page_with_options(
        self,
        tmp_req: main_models.ListComputeInstancesInPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeInstancesInPageResponse:
        tmp_req.validate()
        request = main_models.ListComputeInstancesInPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeInstancesInPage',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeInstancesInPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_instances_in_page_with_options_async(
        self,
        tmp_req: main_models.ListComputeInstancesInPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeInstancesInPageResponse:
        tmp_req.validate()
        request = main_models.ListComputeInstancesInPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeInstancesInPage',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeInstancesInPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_instances_in_page(
        self,
        request: main_models.ListComputeInstancesInPageRequest,
    ) -> main_models.ListComputeInstancesInPageResponse:
        runtime = RuntimeOptions()
        return self.list_compute_instances_in_page_with_options(request, runtime)

    async def list_compute_instances_in_page_async(
        self,
        request: main_models.ListComputeInstancesInPageRequest,
    ) -> main_models.ListComputeInstancesInPageResponse:
        runtime = RuntimeOptions()
        return await self.list_compute_instances_in_page_with_options_async(request, runtime)

    def list_compute_jobs_with_options(
        self,
        request: main_models.ListComputeJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeJobs',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_jobs_with_options_async(
        self,
        request: main_models.ListComputeJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeJobs',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_jobs(
        self,
        request: main_models.ListComputeJobsRequest,
    ) -> main_models.ListComputeJobsResponse:
        runtime = RuntimeOptions()
        return self.list_compute_jobs_with_options(request, runtime)

    async def list_compute_jobs_async(
        self,
        request: main_models.ListComputeJobsRequest,
    ) -> main_models.ListComputeJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_compute_jobs_with_options_async(request, runtime)

    def list_supported_connectors_with_options(
        self,
        request: main_models.ListSupportedConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportedConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportedConnectors',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportedConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_supported_connectors_with_options_async(
        self,
        request: main_models.ListSupportedConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportedConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSupportedConnectors',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportedConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_supported_connectors(
        self,
        request: main_models.ListSupportedConnectorsRequest,
    ) -> main_models.ListSupportedConnectorsResponse:
        runtime = RuntimeOptions()
        return self.list_supported_connectors_with_options(request, runtime)

    async def list_supported_connectors_async(
        self,
        request: main_models.ListSupportedConnectorsRequest,
    ) -> main_models.ListSupportedConnectorsResponse:
        runtime = RuntimeOptions()
        return await self.list_supported_connectors_with_options_async(request, runtime)

    def reopen_compute_instance_with_options(
        self,
        request: main_models.ReopenComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReopenComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReopenComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReopenComputeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reopen_compute_instance_with_options_async(
        self,
        request: main_models.ReopenComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReopenComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReopenComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReopenComputeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reopen_compute_instance(
        self,
        request: main_models.ReopenComputeInstanceRequest,
    ) -> main_models.ReopenComputeInstanceResponse:
        runtime = RuntimeOptions()
        return self.reopen_compute_instance_with_options(request, runtime)

    async def reopen_compute_instance_async(
        self,
        request: main_models.ReopenComputeInstanceRequest,
    ) -> main_models.ReopenComputeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.reopen_compute_instance_with_options_async(request, runtime)

    def restart_compute_job_with_options(
        self,
        request: main_models.RestartComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartComputeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_compute_job_with_options_async(
        self,
        request: main_models.RestartComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartComputeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_compute_job(
        self,
        request: main_models.RestartComputeJobRequest,
    ) -> main_models.RestartComputeJobResponse:
        runtime = RuntimeOptions()
        return self.restart_compute_job_with_options(request, runtime)

    async def restart_compute_job_async(
        self,
        request: main_models.RestartComputeJobRequest,
    ) -> main_models.RestartComputeJobResponse:
        runtime = RuntimeOptions()
        return await self.restart_compute_job_with_options_async(request, runtime)

    def start_compute_instance_with_options(
        self,
        tmp_req: main_models.StartComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartComputeInstanceResponse:
        tmp_req.validate()
        request = main_models.StartComputeInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.selected_zones):
            query['SelectedZones'] = request.selected_zones
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.v_switch_ids_shrink):
            query['VSwitchIds'] = request.v_switch_ids_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartComputeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_compute_instance_with_options_async(
        self,
        tmp_req: main_models.StartComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartComputeInstanceResponse:
        tmp_req.validate()
        request = main_models.StartComputeInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.selected_zones):
            query['SelectedZones'] = request.selected_zones
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.v_switch_ids_shrink):
            query['VSwitchIds'] = request.v_switch_ids_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartComputeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_compute_instance(
        self,
        request: main_models.StartComputeInstanceRequest,
    ) -> main_models.StartComputeInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_compute_instance_with_options(request, runtime)

    async def start_compute_instance_async(
        self,
        request: main_models.StartComputeInstanceRequest,
    ) -> main_models.StartComputeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_compute_instance_with_options_async(request, runtime)

    def start_compute_job_with_options(
        self,
        request: main_models.StartComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cu_limit):
            query['CuLimit'] = request.cu_limit
        if not DaraCore.is_null(request.cu_reserved):
            query['CuReserved'] = request.cu_reserved
        if not DaraCore.is_null(request.draft_sql):
            query['DraftSql'] = request.draft_sql
        if not DaraCore.is_null(request.draft_sql_start):
            query['DraftSqlStart'] = request.draft_sql_start
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.recovery_mode):
            query['RecoveryMode'] = request.recovery_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartComputeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_compute_job_with_options_async(
        self,
        request: main_models.StartComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cu_limit):
            query['CuLimit'] = request.cu_limit
        if not DaraCore.is_null(request.cu_reserved):
            query['CuReserved'] = request.cu_reserved
        if not DaraCore.is_null(request.draft_sql):
            query['DraftSql'] = request.draft_sql
        if not DaraCore.is_null(request.draft_sql_start):
            query['DraftSqlStart'] = request.draft_sql_start
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.recovery_mode):
            query['RecoveryMode'] = request.recovery_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartComputeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_compute_job(
        self,
        request: main_models.StartComputeJobRequest,
    ) -> main_models.StartComputeJobResponse:
        runtime = RuntimeOptions()
        return self.start_compute_job_with_options(request, runtime)

    async def start_compute_job_async(
        self,
        request: main_models.StartComputeJobRequest,
    ) -> main_models.StartComputeJobResponse:
        runtime = RuntimeOptions()
        return await self.start_compute_job_with_options_async(request, runtime)

    def stop_compute_instance_with_options(
        self,
        request: main_models.StopComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopComputeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_compute_instance_with_options_async(
        self,
        request: main_models.StopComputeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopComputeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopComputeInstance',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopComputeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_compute_instance(
        self,
        request: main_models.StopComputeInstanceRequest,
    ) -> main_models.StopComputeInstanceResponse:
        runtime = RuntimeOptions()
        return self.stop_compute_instance_with_options(request, runtime)

    async def stop_compute_instance_async(
        self,
        request: main_models.StopComputeInstanceRequest,
    ) -> main_models.StopComputeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.stop_compute_instance_with_options_async(request, runtime)

    def stop_compute_job_with_options(
        self,
        request: main_models.StopComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopComputeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_compute_job_with_options_async(
        self,
        request: main_models.StopComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopComputeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_compute_job(
        self,
        request: main_models.StopComputeJobRequest,
    ) -> main_models.StopComputeJobResponse:
        runtime = RuntimeOptions()
        return self.stop_compute_job_with_options(request, runtime)

    async def stop_compute_job_async(
        self,
        request: main_models.StopComputeJobRequest,
    ) -> main_models.StopComputeJobResponse:
        runtime = RuntimeOptions()
        return await self.stop_compute_job_with_options_async(request, runtime)

    def update_compute_instance_name_with_options(
        self,
        request: main_models.UpdateComputeInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeInstanceName',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_instance_name_with_options_async(
        self,
        request: main_models.UpdateComputeInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeInstanceName',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_instance_name(
        self,
        request: main_models.UpdateComputeInstanceNameRequest,
    ) -> main_models.UpdateComputeInstanceNameResponse:
        runtime = RuntimeOptions()
        return self.update_compute_instance_name_with_options(request, runtime)

    async def update_compute_instance_name_async(
        self,
        request: main_models.UpdateComputeInstanceNameRequest,
    ) -> main_models.UpdateComputeInstanceNameResponse:
        runtime = RuntimeOptions()
        return await self.update_compute_instance_name_with_options_async(request, runtime)

    def update_compute_job_with_options(
        self,
        request: main_models.UpdateComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.upgrade_mode):
            query['UpgradeMode'] = request.upgrade_mode
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_job_with_options_async(
        self,
        request: main_models.UpdateComputeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.upgrade_mode):
            query['UpgradeMode'] = request.upgrade_mode
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeJob',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_job(
        self,
        request: main_models.UpdateComputeJobRequest,
    ) -> main_models.UpdateComputeJobResponse:
        runtime = RuntimeOptions()
        return self.update_compute_job_with_options(request, runtime)

    async def update_compute_job_async(
        self,
        request: main_models.UpdateComputeJobRequest,
    ) -> main_models.UpdateComputeJobResponse:
        runtime = RuntimeOptions()
        return await self.update_compute_job_with_options_async(request, runtime)

    def update_compute_job_cu_with_options(
        self,
        request: main_models.UpdateComputeJobCuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeJobCuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cu_limit):
            query['CuLimit'] = request.cu_limit
        if not DaraCore.is_null(request.cu_reserved):
            query['CuReserved'] = request.cu_reserved
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeJobCu',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeJobCuResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_job_cu_with_options_async(
        self,
        request: main_models.UpdateComputeJobCuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeJobCuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cu_limit):
            query['CuLimit'] = request.cu_limit
        if not DaraCore.is_null(request.cu_reserved):
            query['CuReserved'] = request.cu_reserved
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeJobCu',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeJobCuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_job_cu(
        self,
        request: main_models.UpdateComputeJobCuRequest,
    ) -> main_models.UpdateComputeJobCuResponse:
        runtime = RuntimeOptions()
        return self.update_compute_job_cu_with_options(request, runtime)

    async def update_compute_job_cu_async(
        self,
        request: main_models.UpdateComputeJobCuRequest,
    ) -> main_models.UpdateComputeJobCuResponse:
        runtime = RuntimeOptions()
        return await self.update_compute_job_cu_with_options_async(request, runtime)

    def update_compute_job_draft_sql_with_options(
        self,
        request: main_models.UpdateComputeJobDraftSqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeJobDraftSqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.draft_sql):
            query['DraftSql'] = request.draft_sql
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeJobDraftSql',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeJobDraftSqlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_job_draft_sql_with_options_async(
        self,
        request: main_models.UpdateComputeJobDraftSqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeJobDraftSqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.draft_sql):
            query['DraftSql'] = request.draft_sql
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeJobDraftSql',
            version = '2026-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeJobDraftSqlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_job_draft_sql(
        self,
        request: main_models.UpdateComputeJobDraftSqlRequest,
    ) -> main_models.UpdateComputeJobDraftSqlResponse:
        runtime = RuntimeOptions()
        return self.update_compute_job_draft_sql_with_options(request, runtime)

    async def update_compute_job_draft_sql_async(
        self,
        request: main_models.UpdateComputeJobDraftSqlRequest,
    ) -> main_models.UpdateComputeJobDraftSqlResponse:
        runtime = RuntimeOptions()
        return await self.update_compute_job_draft_sql_with_options_async(request, runtime)
