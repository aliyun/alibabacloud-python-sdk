# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_schedulerx220190430 import models as schedulerx_220190430_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_delete_jobs_with_options(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_jobs(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_jobs_with_options(request, runtime)

    async def batch_delete_jobs_async(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_jobs_with_options_async(request, runtime)

    def batch_disable_jobs_with_options(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDisableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDisableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_disable_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDisableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDisableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_disable_jobs(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_disable_jobs_with_options(request, runtime)

    async def batch_disable_jobs_async(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_disable_jobs_with_options_async(request, runtime)

    def batch_enable_jobs_with_options(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchEnableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchEnableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_enable_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchEnableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchEnableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_enable_jobs(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_enable_jobs_with_options(request, runtime)

    async def batch_enable_jobs_async(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_enable_jobs_with_options_async(request, runtime)

    def create_app_group_with_options(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_group_with_options(request, runtime)

    async def create_app_group_async(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_group_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.jar_url):
            body['JarUrl'] = request.jar_url
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.jar_url):
            body['JarUrl'] = request.jar_url
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def delete_job_with_options(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    async def delete_job_async(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_with_options_async(request, runtime)

    def delete_workflow_with_options(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_workflow_with_options(request, runtime)

    async def delete_workflow_async(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_workflow_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> schedulerx_220190430_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> schedulerx_220190430_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def designate_workers_with_options(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DesignateWorkers',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DesignateWorkersResponse(),
            self.call_api(params, req, runtime)
        )

    async def designate_workers_with_options_async(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DesignateWorkers',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DesignateWorkersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def designate_workers(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return self.designate_workers_with_options(request, runtime)

    async def designate_workers_async(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.designate_workers_with_options_async(request, runtime)

    def disable_job_with_options(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_job_with_options_async(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_job(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_job_with_options(request, runtime)

    async def disable_job_async(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_job_with_options_async(request, runtime)

    def disable_workflow_with_options(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_workflow(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_workflow_with_options(request, runtime)

    async def disable_workflow_async(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_workflow_with_options_async(request, runtime)

    def enable_job_with_options(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_job_with_options_async(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_job(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_job_with_options(request, runtime)

    async def enable_job_async(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_job_with_options_async(request, runtime)

    def enable_workflow_with_options(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_workflow(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_workflow_with_options(request, runtime)

    async def enable_workflow_async(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_workflow_with_options_async(request, runtime)

    def execute_job_with_options(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_job_with_options_async(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_job(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_job_with_options(request, runtime)

    async def execute_job_async(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_job_with_options_async(request, runtime)

    def execute_workflow_with_options(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_workflow(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_workflow_with_options(request, runtime)

    async def execute_workflow_async(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_workflow_with_options_async(request, runtime)

    def get_job_info_with_options(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_info_with_options_async(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_info(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_info_with_options(request, runtime)

    async def get_job_info_async(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_info_with_options_async(request, runtime)

    def get_job_instance_with_options(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_instance_with_options_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_instance(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_instance_with_options(request, runtime)

    async def get_job_instance_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_instance_with_options_async(request, runtime)

    def get_job_instance_list_with_options(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstanceList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_instance_list_with_options_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstanceList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_instance_list(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_instance_list_with_options(request, runtime)

    async def get_job_instance_list_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_instance_list_with_options_async(request, runtime)

    def get_work_flow_with_options(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkFlow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_flow_with_options_async(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkFlow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_flow(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_work_flow_with_options(request, runtime)

    async def get_work_flow_async(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_work_flow_with_options_async(request, runtime)

    def get_worker_list_with_options(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkerList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_worker_list_with_options_async(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkerList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_worker_list(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_worker_list_with_options(request, runtime)

    async def get_worker_list_async(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_worker_list_with_options_async(request, runtime)

    def grant_permission_with_options(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grant_option):
            query['GrantOption'] = request.grant_option
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantPermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GrantPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_permission_with_options_async(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grant_option):
            query['GrantOption'] = request.grant_option
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantPermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GrantPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_permission(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_permission_with_options(request, runtime)

    async def grant_permission_async(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_permission_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def revoke_permission_with_options(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokePermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RevokePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_permission_with_options_async(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokePermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RevokePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_permission(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_permission_with_options(request, runtime)

    async def revoke_permission_async(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_permission_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def update_job_with_options(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.jar_url):
            body['JarUrl'] = request.jar_url
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.jar_url):
            body['JarUrl'] = request.jar_url
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    async def update_job_async(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_job_with_options_async(request, runtime)
