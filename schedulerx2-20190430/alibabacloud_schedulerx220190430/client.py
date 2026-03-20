# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_schedulerx220190430 import models as main_models
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
            'cn-beijing': 'schedulerx.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'schedulerx.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'schedulerx.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'schedulerx.cn-shenzhen.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('schedulerx2', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_delete_jobs_with_options(
        self,
        request: main_models.BatchDeleteJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_jobs_with_options_async(
        self,
        request: main_models.BatchDeleteJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_jobs(
        self,
        request: main_models.BatchDeleteJobsRequest,
    ) -> main_models.BatchDeleteJobsResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_jobs_with_options(request, runtime)

    async def batch_delete_jobs_async(
        self,
        request: main_models.BatchDeleteJobsRequest,
    ) -> main_models.BatchDeleteJobsResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_jobs_with_options_async(request, runtime)

    def batch_delete_route_strategy_with_options(
        self,
        request: main_models.BatchDeleteRouteStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteRouteStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteRouteStrategy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteRouteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_route_strategy_with_options_async(
        self,
        request: main_models.BatchDeleteRouteStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteRouteStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteRouteStrategy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteRouteStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_route_strategy(
        self,
        request: main_models.BatchDeleteRouteStrategyRequest,
    ) -> main_models.BatchDeleteRouteStrategyResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_route_strategy_with_options(request, runtime)

    async def batch_delete_route_strategy_async(
        self,
        request: main_models.BatchDeleteRouteStrategyRequest,
    ) -> main_models.BatchDeleteRouteStrategyResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_route_strategy_with_options_async(request, runtime)

    def batch_disable_jobs_with_options(
        self,
        request: main_models.BatchDisableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDisableJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDisableJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDisableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_disable_jobs_with_options_async(
        self,
        request: main_models.BatchDisableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDisableJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchDisableJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDisableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_disable_jobs(
        self,
        request: main_models.BatchDisableJobsRequest,
    ) -> main_models.BatchDisableJobsResponse:
        runtime = RuntimeOptions()
        return self.batch_disable_jobs_with_options(request, runtime)

    async def batch_disable_jobs_async(
        self,
        request: main_models.BatchDisableJobsRequest,
    ) -> main_models.BatchDisableJobsResponse:
        runtime = RuntimeOptions()
        return await self.batch_disable_jobs_with_options_async(request, runtime)

    def batch_enable_jobs_with_options(
        self,
        request: main_models.BatchEnableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchEnableJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchEnableJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchEnableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_enable_jobs_with_options_async(
        self,
        request: main_models.BatchEnableJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchEnableJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchEnableJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchEnableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_enable_jobs(
        self,
        request: main_models.BatchEnableJobsRequest,
    ) -> main_models.BatchEnableJobsResponse:
        runtime = RuntimeOptions()
        return self.batch_enable_jobs_with_options(request, runtime)

    async def batch_enable_jobs_async(
        self,
        request: main_models.BatchEnableJobsRequest,
    ) -> main_models.BatchEnableJobsResponse:
        runtime = RuntimeOptions()
        return await self.batch_enable_jobs_with_options_async(request, runtime)

    def create_app_group_with_options(
        self,
        request: main_models.CreateAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_with_options_async(
        self,
        request: main_models.CreateAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group(
        self,
        request: main_models.CreateAppGroupRequest,
    ) -> main_models.CreateAppGroupResponse:
        runtime = RuntimeOptions()
        return self.create_app_group_with_options(request, runtime)

    async def create_app_group_async(
        self,
        request: main_models.CreateAppGroupRequest,
    ) -> main_models.CreateAppGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_app_group_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        request: main_models.CreateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not DaraCore.is_null(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not DaraCore.is_null(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not DaraCore.is_null(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not DaraCore.is_null(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not DaraCore.is_null(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not DaraCore.is_null(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not DaraCore.is_null(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: main_models.CreateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not DaraCore.is_null(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not DaraCore.is_null(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not DaraCore.is_null(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not DaraCore.is_null(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not DaraCore.is_null(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not DaraCore.is_null(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not DaraCore.is_null(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_route_strategy_with_options(
        self,
        request: main_models.CreateRouteStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRouteStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strategy_content):
            query['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRouteStrategy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRouteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_route_strategy_with_options_async(
        self,
        request: main_models.CreateRouteStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRouteStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strategy_content):
            query['StrategyContent'] = request.strategy_content
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRouteStrategy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRouteStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_route_strategy(
        self,
        request: main_models.CreateRouteStrategyRequest,
    ) -> main_models.CreateRouteStrategyResponse:
        runtime = RuntimeOptions()
        return self.create_route_strategy_with_options(request, runtime)

    async def create_route_strategy_async(
        self,
        request: main_models.CreateRouteStrategyRequest,
    ) -> main_models.CreateRouteStrategyResponse:
        runtime = RuntimeOptions()
        return await self.create_route_strategy_with_options_async(request, runtime)

    def create_schedulerx_calendar_with_options(
        self,
        request: main_models.CreateSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchedulerxCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.month_days_content):
            body['MonthDaysContent'] = request.month_days_content
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchedulerxCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedulerx_calendar_with_options_async(
        self,
        request: main_models.CreateSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchedulerxCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.month_days_content):
            body['MonthDaysContent'] = request.month_days_content
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchedulerxCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedulerx_calendar(
        self,
        request: main_models.CreateSchedulerxCalendarRequest,
    ) -> main_models.CreateSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return self.create_schedulerx_calendar_with_options(request, runtime)

    async def create_schedulerx_calendar_async(
        self,
        request: main_models.CreateSchedulerxCalendarRequest,
    ) -> main_models.CreateSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return await self.create_schedulerx_calendar_with_options_async(request, runtime)

    def create_schedulerx_notification_policy_with_options(
        self,
        request: main_models.CreateSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchedulerxNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_time_range):
            body['ChannelTimeRange'] = request.channel_time_range
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchedulerxNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedulerx_notification_policy_with_options_async(
        self,
        request: main_models.CreateSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchedulerxNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_time_range):
            body['ChannelTimeRange'] = request.channel_time_range
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchedulerxNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedulerx_notification_policy(
        self,
        request: main_models.CreateSchedulerxNotificationPolicyRequest,
    ) -> main_models.CreateSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_schedulerx_notification_policy_with_options(request, runtime)

    async def create_schedulerx_notification_policy_async(
        self,
        request: main_models.CreateSchedulerxNotificationPolicyRequest,
    ) -> main_models.CreateSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_schedulerx_notification_policy_with_options_async(request, runtime)

    def create_workflow_with_options(
        self,
        request: main_models.CreateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workflow_with_options_async(
        self,
        request: main_models.CreateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkflowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workflow(
        self,
        request: main_models.CreateWorkflowRequest,
    ) -> main_models.CreateWorkflowResponse:
        runtime = RuntimeOptions()
        return self.create_workflow_with_options(request, runtime)

    async def create_workflow_async(
        self,
        request: main_models.CreateWorkflowRequest,
    ) -> main_models.CreateWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.create_workflow_with_options_async(request, runtime)

    def delete_app_group_with_options(
        self,
        request: main_models.DeleteAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_jobs):
            query['DeleteJobs'] = request.delete_jobs
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_group_with_options_async(
        self,
        request: main_models.DeleteAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_jobs):
            query['DeleteJobs'] = request.delete_jobs
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_group(
        self,
        request: main_models.DeleteAppGroupRequest,
    ) -> main_models.DeleteAppGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_app_group_with_options(request, runtime)

    async def delete_app_group_async(
        self,
        request: main_models.DeleteAppGroupRequest,
    ) -> main_models.DeleteAppGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_group_with_options_async(request, runtime)

    def delete_job_with_options(
        self,
        request: main_models.DeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: main_models.DeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        request: main_models.DeleteJobRequest,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    async def delete_job_async(
        self,
        request: main_models.DeleteJobRequest,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_job_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_route_strategy_with_options(
        self,
        request: main_models.DeleteRouteStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRouteStrategy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_strategy_with_options_async(
        self,
        request: main_models.DeleteRouteStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRouteStrategy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route_strategy(
        self,
        request: main_models.DeleteRouteStrategyRequest,
    ) -> main_models.DeleteRouteStrategyResponse:
        runtime = RuntimeOptions()
        return self.delete_route_strategy_with_options(request, runtime)

    async def delete_route_strategy_async(
        self,
        request: main_models.DeleteRouteStrategyRequest,
    ) -> main_models.DeleteRouteStrategyResponse:
        runtime = RuntimeOptions()
        return await self.delete_route_strategy_with_options_async(request, runtime)

    def delete_schedulerx_calendar_with_options(
        self,
        request: main_models.DeleteSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchedulerxCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchedulerxCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedulerx_calendar_with_options_async(
        self,
        request: main_models.DeleteSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchedulerxCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchedulerxCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedulerx_calendar(
        self,
        request: main_models.DeleteSchedulerxCalendarRequest,
    ) -> main_models.DeleteSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return self.delete_schedulerx_calendar_with_options(request, runtime)

    async def delete_schedulerx_calendar_async(
        self,
        request: main_models.DeleteSchedulerxCalendarRequest,
    ) -> main_models.DeleteSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return await self.delete_schedulerx_calendar_with_options_async(request, runtime)

    def delete_schedulerx_notification_policy_with_options(
        self,
        request: main_models.DeleteSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchedulerxNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchedulerxNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedulerx_notification_policy_with_options_async(
        self,
        request: main_models.DeleteSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchedulerxNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchedulerxNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedulerx_notification_policy(
        self,
        request: main_models.DeleteSchedulerxNotificationPolicyRequest,
    ) -> main_models.DeleteSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_schedulerx_notification_policy_with_options(request, runtime)

    async def delete_schedulerx_notification_policy_async(
        self,
        request: main_models.DeleteSchedulerxNotificationPolicyRequest,
    ) -> main_models.DeleteSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_schedulerx_notification_policy_with_options_async(request, runtime)

    def delete_workflow_with_options(
        self,
        request: main_models.DeleteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_with_options_async(
        self,
        request: main_models.DeleteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow(
        self,
        request: main_models.DeleteWorkflowRequest,
    ) -> main_models.DeleteWorkflowResponse:
        runtime = RuntimeOptions()
        return self.delete_workflow_with_options(request, runtime)

    async def delete_workflow_async(
        self,
        request: main_models.DeleteWorkflowRequest,
    ) -> main_models.DeleteWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.delete_workflow_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-04-30',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-04-30',
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

    def designate_workers_with_options(
        self,
        request: main_models.DesignateWorkersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DesignateWorkersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DesignateWorkers',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DesignateWorkersResponse(),
            self.call_api(params, req, runtime)
        )

    async def designate_workers_with_options_async(
        self,
        request: main_models.DesignateWorkersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DesignateWorkersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DesignateWorkers',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DesignateWorkersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def designate_workers(
        self,
        request: main_models.DesignateWorkersRequest,
    ) -> main_models.DesignateWorkersResponse:
        runtime = RuntimeOptions()
        return self.designate_workers_with_options(request, runtime)

    async def designate_workers_async(
        self,
        request: main_models.DesignateWorkersRequest,
    ) -> main_models.DesignateWorkersResponse:
        runtime = RuntimeOptions()
        return await self.designate_workers_with_options_async(request, runtime)

    def disable_job_with_options(
        self,
        request: main_models.DisableJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_job_with_options_async(
        self,
        request: main_models.DisableJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_job(
        self,
        request: main_models.DisableJobRequest,
    ) -> main_models.DisableJobResponse:
        runtime = RuntimeOptions()
        return self.disable_job_with_options(request, runtime)

    async def disable_job_async(
        self,
        request: main_models.DisableJobRequest,
    ) -> main_models.DisableJobResponse:
        runtime = RuntimeOptions()
        return await self.disable_job_with_options_async(request, runtime)

    def disable_workflow_with_options(
        self,
        request: main_models.DisableWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_workflow_with_options_async(
        self,
        request: main_models.DisableWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_workflow(
        self,
        request: main_models.DisableWorkflowRequest,
    ) -> main_models.DisableWorkflowResponse:
        runtime = RuntimeOptions()
        return self.disable_workflow_with_options(request, runtime)

    async def disable_workflow_async(
        self,
        request: main_models.DisableWorkflowRequest,
    ) -> main_models.DisableWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.disable_workflow_with_options_async(request, runtime)

    def enable_job_with_options(
        self,
        request: main_models.EnableJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_job_with_options_async(
        self,
        request: main_models.EnableJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_job(
        self,
        request: main_models.EnableJobRequest,
    ) -> main_models.EnableJobResponse:
        runtime = RuntimeOptions()
        return self.enable_job_with_options(request, runtime)

    async def enable_job_async(
        self,
        request: main_models.EnableJobRequest,
    ) -> main_models.EnableJobResponse:
        runtime = RuntimeOptions()
        return await self.enable_job_with_options_async(request, runtime)

    def enable_workflow_with_options(
        self,
        request: main_models.EnableWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_workflow_with_options_async(
        self,
        request: main_models.EnableWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_workflow(
        self,
        request: main_models.EnableWorkflowRequest,
    ) -> main_models.EnableWorkflowResponse:
        runtime = RuntimeOptions()
        return self.enable_workflow_with_options(request, runtime)

    async def enable_workflow_async(
        self,
        request: main_models.EnableWorkflowRequest,
    ) -> main_models.EnableWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.enable_workflow_with_options_async(request, runtime)

    def execute_job_with_options(
        self,
        request: main_models.ExecuteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_job_with_options_async(
        self,
        request: main_models.ExecuteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_job(
        self,
        request: main_models.ExecuteJobRequest,
    ) -> main_models.ExecuteJobResponse:
        runtime = RuntimeOptions()
        return self.execute_job_with_options(request, runtime)

    async def execute_job_async(
        self,
        request: main_models.ExecuteJobRequest,
    ) -> main_models.ExecuteJobResponse:
        runtime = RuntimeOptions()
        return await self.execute_job_with_options_async(request, runtime)

    def execute_workflow_with_options(
        self,
        request: main_models.ExecuteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_workflow_with_options_async(
        self,
        request: main_models.ExecuteWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteWorkflowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_workflow(
        self,
        request: main_models.ExecuteWorkflowRequest,
    ) -> main_models.ExecuteWorkflowResponse:
        runtime = RuntimeOptions()
        return self.execute_workflow_with_options(request, runtime)

    async def execute_workflow_async(
        self,
        request: main_models.ExecuteWorkflowRequest,
    ) -> main_models.ExecuteWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.execute_workflow_with_options_async(request, runtime)

    def get_app_group_with_options(
        self,
        request: main_models.GetAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_group_with_options_async(
        self,
        request: main_models.GetAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_group(
        self,
        request: main_models.GetAppGroupRequest,
    ) -> main_models.GetAppGroupResponse:
        runtime = RuntimeOptions()
        return self.get_app_group_with_options(request, runtime)

    async def get_app_group_async(
        self,
        request: main_models.GetAppGroupRequest,
    ) -> main_models.GetAppGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_app_group_with_options_async(request, runtime)

    def get_job_info_with_options(
        self,
        request: main_models.GetJobInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobInfo',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_info_with_options_async(
        self,
        request: main_models.GetJobInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobInfo',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_info(
        self,
        request: main_models.GetJobInfoRequest,
    ) -> main_models.GetJobInfoResponse:
        runtime = RuntimeOptions()
        return self.get_job_info_with_options(request, runtime)

    async def get_job_info_async(
        self,
        request: main_models.GetJobInfoRequest,
    ) -> main_models.GetJobInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_job_info_with_options_async(request, runtime)

    def get_job_instance_with_options(
        self,
        request: main_models.GetJobInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_instance_with_options_async(
        self,
        request: main_models.GetJobInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_instance(
        self,
        request: main_models.GetJobInstanceRequest,
    ) -> main_models.GetJobInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_job_instance_with_options(request, runtime)

    async def get_job_instance_async(
        self,
        request: main_models.GetJobInstanceRequest,
    ) -> main_models.GetJobInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_job_instance_with_options_async(request, runtime)

    def get_job_instance_list_with_options(
        self,
        request: main_models.GetJobInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInstanceListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobInstanceList',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_instance_list_with_options_async(
        self,
        request: main_models.GetJobInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInstanceListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobInstanceList',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_instance_list(
        self,
        request: main_models.GetJobInstanceListRequest,
    ) -> main_models.GetJobInstanceListResponse:
        runtime = RuntimeOptions()
        return self.get_job_instance_list_with_options(request, runtime)

    async def get_job_instance_list_async(
        self,
        request: main_models.GetJobInstanceListRequest,
    ) -> main_models.GetJobInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.get_job_instance_list_with_options_async(request, runtime)

    def get_log_with_options(
        self,
        request: main_models.GetLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLog',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_with_options_async(
        self,
        request: main_models.GetLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLog',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log(
        self,
        request: main_models.GetLogRequest,
    ) -> main_models.GetLogResponse:
        runtime = RuntimeOptions()
        return self.get_log_with_options(request, runtime)

    async def get_log_async(
        self,
        request: main_models.GetLogRequest,
    ) -> main_models.GetLogResponse:
        runtime = RuntimeOptions()
        return await self.get_log_with_options_async(request, runtime)

    def get_overview_with_options(
        self,
        request: main_models.GetOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOverview',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_overview_with_options_async(
        self,
        request: main_models.GetOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOverview',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_overview(
        self,
        request: main_models.GetOverviewRequest,
    ) -> main_models.GetOverviewResponse:
        runtime = RuntimeOptions()
        return self.get_overview_with_options(request, runtime)

    async def get_overview_async(
        self,
        request: main_models.GetOverviewRequest,
    ) -> main_models.GetOverviewResponse:
        runtime = RuntimeOptions()
        return await self.get_overview_with_options_async(request, runtime)

    def get_work_flow_with_options(
        self,
        request: main_models.GetWorkFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkFlowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkFlow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_flow_with_options_async(
        self,
        request: main_models.GetWorkFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkFlowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkFlow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_flow(
        self,
        request: main_models.GetWorkFlowRequest,
    ) -> main_models.GetWorkFlowResponse:
        runtime = RuntimeOptions()
        return self.get_work_flow_with_options(request, runtime)

    async def get_work_flow_async(
        self,
        request: main_models.GetWorkFlowRequest,
    ) -> main_models.GetWorkFlowResponse:
        runtime = RuntimeOptions()
        return await self.get_work_flow_with_options_async(request, runtime)

    def get_worker_list_with_options(
        self,
        request: main_models.GetWorkerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerList',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_worker_list_with_options_async(
        self,
        request: main_models.GetWorkerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkerListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkerList',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_worker_list(
        self,
        request: main_models.GetWorkerListRequest,
    ) -> main_models.GetWorkerListResponse:
        runtime = RuntimeOptions()
        return self.get_worker_list_with_options(request, runtime)

    async def get_worker_list_async(
        self,
        request: main_models.GetWorkerListRequest,
    ) -> main_models.GetWorkerListResponse:
        runtime = RuntimeOptions()
        return await self.get_worker_list_with_options_async(request, runtime)

    def get_workflow_instance_with_options(
        self,
        request: main_models.GetWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_instance_with_options_async(
        self,
        request: main_models.GetWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkflowInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkflowInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_instance(
        self,
        request: main_models.GetWorkflowInstanceRequest,
    ) -> main_models.GetWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_workflow_instance_with_options(request, runtime)

    async def get_workflow_instance_async(
        self,
        request: main_models.GetWorkflowInstanceRequest,
    ) -> main_models.GetWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_workflow_instance_with_options_async(request, runtime)

    def grant_permission_with_options(
        self,
        request: main_models.GrantPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grant_option):
            query['GrantOption'] = request.grant_option
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantPermission',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_permission_with_options_async(
        self,
        request: main_models.GrantPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grant_option):
            query['GrantOption'] = request.grant_option
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantPermission',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_permission(
        self,
        request: main_models.GrantPermissionRequest,
    ) -> main_models.GrantPermissionResponse:
        runtime = RuntimeOptions()
        return self.grant_permission_with_options(request, runtime)

    async def grant_permission_async(
        self,
        request: main_models.GrantPermissionRequest,
    ) -> main_models.GrantPermissionResponse:
        runtime = RuntimeOptions()
        return await self.grant_permission_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group_name):
            query['AppGroupName'] = request.app_group_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group_name):
            query['AppGroupName'] = request.app_group_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_job_script_history_with_options(
        self,
        request: main_models.ListJobScriptHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobScriptHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobScriptHistory',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobScriptHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_script_history_with_options_async(
        self,
        request: main_models.ListJobScriptHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobScriptHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobScriptHistory',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobScriptHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_script_history(
        self,
        request: main_models.ListJobScriptHistoryRequest,
    ) -> main_models.ListJobScriptHistoryResponse:
        runtime = RuntimeOptions()
        return self.list_job_script_history_with_options(request, runtime)

    async def list_job_script_history_async(
        self,
        request: main_models.ListJobScriptHistoryRequest,
    ) -> main_models.ListJobScriptHistoryResponse:
        runtime = RuntimeOptions()
        return await self.list_job_script_history_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: main_models.ListJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_work_flows_with_options(
        self,
        request: main_models.ListWorkFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_name):
            query['WorkflowName'] = request.workflow_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkFlows',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_flows_with_options_async(
        self,
        request: main_models.ListWorkFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workflow_name):
            query['WorkflowName'] = request.workflow_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkFlows',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_work_flows(
        self,
        request: main_models.ListWorkFlowsRequest,
    ) -> main_models.ListWorkFlowsResponse:
        runtime = RuntimeOptions()
        return self.list_work_flows_with_options(request, runtime)

    async def list_work_flows_async(
        self,
        request: main_models.ListWorkFlowsRequest,
    ) -> main_models.ListWorkFlowsResponse:
        runtime = RuntimeOptions()
        return await self.list_work_flows_with_options_async(request, runtime)

    def list_workflow_instance_with_options(
        self,
        request: main_models.ListWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_instance_with_options_async(
        self,
        request: main_models.ListWorkflowInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkflowInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkflowInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_instance(
        self,
        request: main_models.ListWorkflowInstanceRequest,
    ) -> main_models.ListWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_workflow_instance_with_options(request, runtime)

    async def list_workflow_instance_async(
        self,
        request: main_models.ListWorkflowInstanceRequest,
    ) -> main_models.ListWorkflowInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_workflow_instance_with_options_async(request, runtime)

    def manage_schedulerx_calendar_with_options(
        self,
        request: main_models.ManageSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageSchedulerxCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.incremental):
            body['Incremental'] = request.incremental
        if not DaraCore.is_null(request.month_days_content):
            body['MonthDaysContent'] = request.month_days_content
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSchedulerxCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_schedulerx_calendar_with_options_async(
        self,
        request: main_models.ManageSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageSchedulerxCalendarResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.calendar_name):
            body['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.incremental):
            body['Incremental'] = request.incremental
        if not DaraCore.is_null(request.month_days_content):
            body['MonthDaysContent'] = request.month_days_content
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            body['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSchedulerxCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_schedulerx_calendar(
        self,
        request: main_models.ManageSchedulerxCalendarRequest,
    ) -> main_models.ManageSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return self.manage_schedulerx_calendar_with_options(request, runtime)

    async def manage_schedulerx_calendar_async(
        self,
        request: main_models.ManageSchedulerxCalendarRequest,
    ) -> main_models.ManageSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return await self.manage_schedulerx_calendar_with_options_async(request, runtime)

    def manage_schedulerx_job_sync_with_options(
        self,
        tmp_req: main_models.ManageSchedulerxJobSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageSchedulerxJobSyncResponse:
        tmp_req.validate()
        request = main_models.ManageSchedulerxJobSyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_id_list):
            request.job_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_id_list, 'JobIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.job_id_list_shrink):
            body['JobIdList'] = request.job_id_list_shrink
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.original_group_id):
            body['OriginalGroupId'] = request.original_group_id
        if not DaraCore.is_null(request.original_namespace):
            body['OriginalNamespace'] = request.original_namespace
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_group_id):
            body['TargetGroupId'] = request.target_group_id
        if not DaraCore.is_null(request.target_namespace):
            body['TargetNamespace'] = request.target_namespace
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSchedulerxJobSync',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSchedulerxJobSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_schedulerx_job_sync_with_options_async(
        self,
        tmp_req: main_models.ManageSchedulerxJobSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageSchedulerxJobSyncResponse:
        tmp_req.validate()
        request = main_models.ManageSchedulerxJobSyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_id_list):
            request.job_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_id_list, 'JobIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.job_id_list_shrink):
            body['JobIdList'] = request.job_id_list_shrink
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.original_group_id):
            body['OriginalGroupId'] = request.original_group_id
        if not DaraCore.is_null(request.original_namespace):
            body['OriginalNamespace'] = request.original_namespace
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_group_id):
            body['TargetGroupId'] = request.target_group_id
        if not DaraCore.is_null(request.target_namespace):
            body['TargetNamespace'] = request.target_namespace
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSchedulerxJobSync',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSchedulerxJobSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_schedulerx_job_sync(
        self,
        request: main_models.ManageSchedulerxJobSyncRequest,
    ) -> main_models.ManageSchedulerxJobSyncResponse:
        runtime = RuntimeOptions()
        return self.manage_schedulerx_job_sync_with_options(request, runtime)

    async def manage_schedulerx_job_sync_async(
        self,
        request: main_models.ManageSchedulerxJobSyncRequest,
    ) -> main_models.ManageSchedulerxJobSyncResponse:
        runtime = RuntimeOptions()
        return await self.manage_schedulerx_job_sync_with_options_async(request, runtime)

    def manage_schedulerx_notification_policy_with_options(
        self,
        request: main_models.ManageSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageSchedulerxNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_time_range):
            body['ChannelTimeRange'] = request.channel_time_range
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSchedulerxNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_schedulerx_notification_policy_with_options_async(
        self,
        request: main_models.ManageSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageSchedulerxNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_time_range):
            body['ChannelTimeRange'] = request.channel_time_range
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageSchedulerxNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_schedulerx_notification_policy(
        self,
        request: main_models.ManageSchedulerxNotificationPolicyRequest,
    ) -> main_models.ManageSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return self.manage_schedulerx_notification_policy_with_options(request, runtime)

    async def manage_schedulerx_notification_policy_async(
        self,
        request: main_models.ManageSchedulerxNotificationPolicyRequest,
    ) -> main_models.ManageSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.manage_schedulerx_notification_policy_with_options_async(request, runtime)

    def read_schedulerx_calendar_with_options(
        self,
        request: main_models.ReadSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxCalendarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calendar_name):
            query['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.fetch_calendar_detail):
            query['FetchCalendarDetail'] = request.fetch_calendar_detail
        if not DaraCore.is_null(request.fetch_system_calendar):
            query['FetchSystemCalendar'] = request.fetch_system_calendar
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            query['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_schedulerx_calendar_with_options_async(
        self,
        request: main_models.ReadSchedulerxCalendarRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxCalendarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.calendar_name):
            query['CalendarName'] = request.calendar_name
        if not DaraCore.is_null(request.fetch_calendar_detail):
            query['FetchCalendarDetail'] = request.fetch_calendar_detail
        if not DaraCore.is_null(request.fetch_system_calendar):
            query['FetchSystemCalendar'] = request.fetch_system_calendar
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.year):
            query['Year'] = request.year
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxCalendar',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_schedulerx_calendar(
        self,
        request: main_models.ReadSchedulerxCalendarRequest,
    ) -> main_models.ReadSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return self.read_schedulerx_calendar_with_options(request, runtime)

    async def read_schedulerx_calendar_async(
        self,
        request: main_models.ReadSchedulerxCalendarRequest,
    ) -> main_models.ReadSchedulerxCalendarResponse:
        runtime = RuntimeOptions()
        return await self.read_schedulerx_calendar_with_options_async(request, runtime)

    def read_schedulerx_designate_detail_with_options(
        self,
        request: main_models.ReadSchedulerxDesignateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxDesignateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.designate_type):
            query['DesignateType'] = request.designate_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxDesignateDetail',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxDesignateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_schedulerx_designate_detail_with_options_async(
        self,
        request: main_models.ReadSchedulerxDesignateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxDesignateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.designate_type):
            query['DesignateType'] = request.designate_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxDesignateDetail',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxDesignateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_schedulerx_designate_detail(
        self,
        request: main_models.ReadSchedulerxDesignateDetailRequest,
    ) -> main_models.ReadSchedulerxDesignateDetailResponse:
        runtime = RuntimeOptions()
        return self.read_schedulerx_designate_detail_with_options(request, runtime)

    async def read_schedulerx_designate_detail_async(
        self,
        request: main_models.ReadSchedulerxDesignateDetailRequest,
    ) -> main_models.ReadSchedulerxDesignateDetailResponse:
        runtime = RuntimeOptions()
        return await self.read_schedulerx_designate_detail_with_options_async(request, runtime)

    def read_schedulerx_designate_info_with_options(
        self,
        request: main_models.ReadSchedulerxDesignateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxDesignateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxDesignateInfo',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxDesignateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_schedulerx_designate_info_with_options_async(
        self,
        request: main_models.ReadSchedulerxDesignateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxDesignateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxDesignateInfo',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxDesignateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_schedulerx_designate_info(
        self,
        request: main_models.ReadSchedulerxDesignateInfoRequest,
    ) -> main_models.ReadSchedulerxDesignateInfoResponse:
        runtime = RuntimeOptions()
        return self.read_schedulerx_designate_info_with_options(request, runtime)

    async def read_schedulerx_designate_info_async(
        self,
        request: main_models.ReadSchedulerxDesignateInfoRequest,
    ) -> main_models.ReadSchedulerxDesignateInfoResponse:
        runtime = RuntimeOptions()
        return await self.read_schedulerx_designate_info_with_options_async(request, runtime)

    def read_schedulerx_notification_policy_with_options(
        self,
        request: main_models.ReadSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxNotificationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_schedulerx_notification_policy_with_options_async(
        self,
        request: main_models.ReadSchedulerxNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadSchedulerxNotificationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadSchedulerxNotificationPolicy',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadSchedulerxNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_schedulerx_notification_policy(
        self,
        request: main_models.ReadSchedulerxNotificationPolicyRequest,
    ) -> main_models.ReadSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return self.read_schedulerx_notification_policy_with_options(request, runtime)

    async def read_schedulerx_notification_policy_async(
        self,
        request: main_models.ReadSchedulerxNotificationPolicyRequest,
    ) -> main_models.ReadSchedulerxNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.read_schedulerx_notification_policy_with_options_async(request, runtime)

    def rerun_job_with_options(
        self,
        request: main_models.RerunJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerunJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_time):
            body['DataTime'] = request.data_time
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RerunJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerunJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_job_with_options_async(
        self,
        request: main_models.RerunJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RerunJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_time):
            body['DataTime'] = request.data_time
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RerunJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RerunJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_job(
        self,
        request: main_models.RerunJobRequest,
    ) -> main_models.RerunJobResponse:
        runtime = RuntimeOptions()
        return self.rerun_job_with_options(request, runtime)

    async def rerun_job_async(
        self,
        request: main_models.RerunJobRequest,
    ) -> main_models.RerunJobResponse:
        runtime = RuntimeOptions()
        return await self.rerun_job_with_options_async(request, runtime)

    def retry_job_instance_with_options(
        self,
        request: main_models.RetryJobInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryJobInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryJobInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryJobInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_job_instance_with_options_async(
        self,
        request: main_models.RetryJobInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryJobInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryJobInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryJobInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_job_instance(
        self,
        request: main_models.RetryJobInstanceRequest,
    ) -> main_models.RetryJobInstanceResponse:
        runtime = RuntimeOptions()
        return self.retry_job_instance_with_options(request, runtime)

    async def retry_job_instance_async(
        self,
        request: main_models.RetryJobInstanceRequest,
    ) -> main_models.RetryJobInstanceResponse:
        runtime = RuntimeOptions()
        return await self.retry_job_instance_with_options_async(request, runtime)

    def revoke_permission_with_options(
        self,
        request: main_models.RevokePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokePermission',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_permission_with_options_async(
        self,
        request: main_models.RevokePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokePermission',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_permission(
        self,
        request: main_models.RevokePermissionRequest,
    ) -> main_models.RevokePermissionResponse:
        runtime = RuntimeOptions()
        return self.revoke_permission_with_options(request, runtime)

    async def revoke_permission_async(
        self,
        request: main_models.RevokePermissionRequest,
    ) -> main_models.RevokePermissionResponse:
        runtime = RuntimeOptions()
        return await self.revoke_permission_with_options_async(request, runtime)

    def set_job_instance_success_with_options(
        self,
        request: main_models.SetJobInstanceSuccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetJobInstanceSuccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetJobInstanceSuccess',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetJobInstanceSuccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_job_instance_success_with_options_async(
        self,
        request: main_models.SetJobInstanceSuccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetJobInstanceSuccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetJobInstanceSuccess',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetJobInstanceSuccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_job_instance_success(
        self,
        request: main_models.SetJobInstanceSuccessRequest,
    ) -> main_models.SetJobInstanceSuccessResponse:
        runtime = RuntimeOptions()
        return self.set_job_instance_success_with_options(request, runtime)

    async def set_job_instance_success_async(
        self,
        request: main_models.SetJobInstanceSuccessRequest,
    ) -> main_models.SetJobInstanceSuccessResponse:
        runtime = RuntimeOptions()
        return await self.set_job_instance_success_with_options_async(request, runtime)

    def set_wf_instance_success_with_options(
        self,
        request: main_models.SetWfInstanceSuccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWfInstanceSuccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.wf_instance_id):
            query['WfInstanceId'] = request.wf_instance_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWfInstanceSuccess',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWfInstanceSuccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_wf_instance_success_with_options_async(
        self,
        request: main_models.SetWfInstanceSuccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWfInstanceSuccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.wf_instance_id):
            query['WfInstanceId'] = request.wf_instance_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWfInstanceSuccess',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWfInstanceSuccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_wf_instance_success(
        self,
        request: main_models.SetWfInstanceSuccessRequest,
    ) -> main_models.SetWfInstanceSuccessResponse:
        runtime = RuntimeOptions()
        return self.set_wf_instance_success_with_options(request, runtime)

    async def set_wf_instance_success_async(
        self,
        request: main_models.SetWfInstanceSuccessRequest,
    ) -> main_models.SetWfInstanceSuccessResponse:
        runtime = RuntimeOptions()
        return await self.set_wf_instance_success_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: main_models.StopInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: main_models.StopInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: main_models.StopInstanceRequest,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def update_app_group_with_options(
        self,
        request: main_models.UpdateAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_log):
            query['EnableLog'] = request.enable_log
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.monitor_config_json):
            query['MonitorConfigJson'] = request.monitor_config_json
        if not DaraCore.is_null(request.monitor_contacts_json):
            query['MonitorContactsJson'] = request.monitor_contacts_json
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.notification_policy_name):
            query['NotificationPolicyName'] = request.notification_policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_group_with_options_async(
        self,
        request: main_models.UpdateAppGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_log):
            query['EnableLog'] = request.enable_log
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.monitor_config_json):
            query['MonitorConfigJson'] = request.monitor_config_json
        if not DaraCore.is_null(request.monitor_contacts_json):
            query['MonitorContactsJson'] = request.monitor_contacts_json
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.notification_policy_name):
            query['NotificationPolicyName'] = request.notification_policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppGroup',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_group(
        self,
        request: main_models.UpdateAppGroupRequest,
    ) -> main_models.UpdateAppGroupResponse:
        runtime = RuntimeOptions()
        return self.update_app_group_with_options(request, runtime)

    async def update_app_group_async(
        self,
        request: main_models.UpdateAppGroupRequest,
    ) -> main_models.UpdateAppGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_app_group_with_options_async(request, runtime)

    def update_job_with_options(
        self,
        request: main_models.UpdateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not DaraCore.is_null(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not DaraCore.is_null(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not DaraCore.is_null(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not DaraCore.is_null(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not DaraCore.is_null(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not DaraCore.is_null(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not DaraCore.is_null(request.task_dispatch_mode):
            body['TaskDispatchMode'] = request.task_dispatch_mode
        if not DaraCore.is_null(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not DaraCore.is_null(request.template):
            body['Template'] = request.template
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not DaraCore.is_null(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        request: main_models.UpdateJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not DaraCore.is_null(request.calendar):
            body['Calendar'] = request.calendar
        if not DaraCore.is_null(request.class_name):
            body['ClassName'] = request.class_name
        if not DaraCore.is_null(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not DaraCore.is_null(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not DaraCore.is_null(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not DaraCore.is_null(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not DaraCore.is_null(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not DaraCore.is_null(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not DaraCore.is_null(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not DaraCore.is_null(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not DaraCore.is_null(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not DaraCore.is_null(request.task_dispatch_mode):
            body['TaskDispatchMode'] = request.task_dispatch_mode
        if not DaraCore.is_null(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not DaraCore.is_null(request.template):
            body['Template'] = request.template
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not DaraCore.is_null(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not DaraCore.is_null(request.timezone):
            body['Timezone'] = request.timezone
        if not DaraCore.is_null(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    async def update_job_async(
        self,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        return await self.update_job_with_options_async(request, runtime)

    def update_job_script_with_options(
        self,
        request: main_models.UpdateJobScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_content):
            body['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJobScript',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_script_with_options_async(
        self,
        request: main_models.UpdateJobScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_content):
            body['ScriptContent'] = request.script_content
        if not DaraCore.is_null(request.version_description):
            body['VersionDescription'] = request.version_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJobScript',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job_script(
        self,
        request: main_models.UpdateJobScriptRequest,
    ) -> main_models.UpdateJobScriptResponse:
        runtime = RuntimeOptions()
        return self.update_job_script_with_options(request, runtime)

    async def update_job_script_async(
        self,
        request: main_models.UpdateJobScriptRequest,
    ) -> main_models.UpdateJobScriptResponse:
        runtime = RuntimeOptions()
        return await self.update_job_script_with_options_async(request, runtime)

    def update_namespace_with_options(
        self,
        request: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.update_namespace_with_options(request, runtime)

    async def update_namespace_async(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.update_namespace_with_options_async(request, runtime)

    def update_workflow_with_options(
        self,
        request: main_models.UpdateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_with_options_async(
        self,
        request: main_models.UpdateWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not DaraCore.is_null(request.time_type):
            body['TimeType'] = request.time_type
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflow',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow(
        self,
        request: main_models.UpdateWorkflowRequest,
    ) -> main_models.UpdateWorkflowResponse:
        runtime = RuntimeOptions()
        return self.update_workflow_with_options(request, runtime)

    async def update_workflow_async(
        self,
        request: main_models.UpdateWorkflowRequest,
    ) -> main_models.UpdateWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.update_workflow_with_options_async(request, runtime)

    def update_workflow_dag_with_options(
        self,
        request: main_models.UpdateWorkflowDagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.dag_json):
            body['DagJson'] = request.dag_json
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDag',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_dag_with_options_async(
        self,
        request: main_models.UpdateWorkflowDagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkflowDagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.dag_json):
            body['DagJson'] = request.dag_json
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not DaraCore.is_null(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkflowDag',
            version = '2019-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkflowDagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow_dag(
        self,
        request: main_models.UpdateWorkflowDagRequest,
    ) -> main_models.UpdateWorkflowDagResponse:
        runtime = RuntimeOptions()
        return self.update_workflow_dag_with_options(request, runtime)

    async def update_workflow_dag_async(
        self,
        request: main_models.UpdateWorkflowDagRequest,
    ) -> main_models.UpdateWorkflowDagResponse:
        runtime = RuntimeOptions()
        return await self.update_workflow_dag_with_options_async(request, runtime)
