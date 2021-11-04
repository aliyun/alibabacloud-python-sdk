# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_das20200116 import models as das20200116_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-shanghai': 'das.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('das', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_hdminstance_with_options(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AddHDMInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            self.do_rpcrequest('AddHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_hdminstance_with_options_async(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AddHDMInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            await self.do_rpcrequest_async('AddHDMInstance', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_hdminstance(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
    ) -> das20200116_models.AddHDMInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_hdminstance_with_options(request, runtime)

    async def add_hdminstance_async(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
    ) -> das20200116_models.AddHDMInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_hdminstance_with_options_async(request, runtime)

    def create_adam_bench_task_with_options(
        self,
        request: das20200116_models.CreateAdamBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateAdamBenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateAdamBenchTaskResponse(),
            self.do_rpcrequest('CreateAdamBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_adam_bench_task_with_options_async(
        self,
        request: das20200116_models.CreateAdamBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateAdamBenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateAdamBenchTaskResponse(),
            await self.do_rpcrequest_async('CreateAdamBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_adam_bench_task(
        self,
        request: das20200116_models.CreateAdamBenchTaskRequest,
    ) -> das20200116_models.CreateAdamBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_adam_bench_task_with_options(request, runtime)

    async def create_adam_bench_task_async(
        self,
        request: das20200116_models.CreateAdamBenchTaskRequest,
    ) -> das20200116_models.CreateAdamBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_adam_bench_task_with_options_async(request, runtime)

    def create_cache_analysis_job_with_options(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            self.do_rpcrequest('CreateCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            await self.do_rpcrequest_async('CreateCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cache_analysis_job(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_job_with_options(request, runtime)

    async def create_cache_analysis_job_async(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cache_analysis_job_with_options_async(request, runtime)

    def create_cloud_bench_tasks_with_options(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCloudBenchTasksResponse(),
            self.do_rpcrequest('CreateCloudBenchTasks', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cloud_bench_tasks_with_options_async(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateCloudBenchTasksResponse(),
            await self.do_rpcrequest_async('CreateCloudBenchTasks', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cloud_bench_tasks(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_bench_tasks_with_options(request, runtime)

    async def create_cloud_bench_tasks_async(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_bench_tasks_with_options_async(request, runtime)

    def create_diagnostic_report_with_options(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            self.do_rpcrequest('CreateDiagnosticReport', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            await self.do_rpcrequest_async('CreateDiagnosticReport', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_diagnostic_report(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def create_request_diagnosis_with_options(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateRequestDiagnosisResponse(),
            self.do_rpcrequest('CreateRequestDiagnosis', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_request_diagnosis_with_options_async(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.CreateRequestDiagnosisResponse(),
            await self.do_rpcrequest_async('CreateRequestDiagnosis', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_request_diagnosis(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_request_diagnosis_with_options(request, runtime)

    async def create_request_diagnosis_async(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_request_diagnosis_with_options_async(request, runtime)

    def describe_cache_analysis_job_with_options(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            await self.do_rpcrequest_async('DescribeCacheAnalysisJob', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_job(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_job_with_options(request, runtime)

    async def describe_cache_analysis_job_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_job_with_options_async(request, runtime)

    def describe_cache_analysis_jobs_with_options(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisJobs', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cache_analysis_jobs_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            await self.do_rpcrequest_async('DescribeCacheAnalysisJobs', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_jobs(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_jobs_with_options(request, runtime)

    async def describe_cache_analysis_jobs_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_jobs_with_options_async(request, runtime)

    def describe_cloud_bench_tasks_with_options(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudBenchTasksResponse(),
            self.do_rpcrequest('DescribeCloudBenchTasks', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloud_bench_tasks_with_options_async(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudBenchTasksResponse(),
            await self.do_rpcrequest_async('DescribeCloudBenchTasks', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_bench_tasks(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_bench_tasks_with_options(request, runtime)

    async def describe_cloud_bench_tasks_async(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_bench_tasks_with_options_async(request, runtime)

    def describe_cloudbench_task_with_options(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskResponse(),
            self.do_rpcrequest('DescribeCloudbenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloudbench_task_with_options_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskResponse(),
            await self.do_rpcrequest_async('DescribeCloudbenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloudbench_task(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_with_options(request, runtime)

    async def describe_cloudbench_task_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloudbench_task_with_options_async(request, runtime)

    def describe_cloudbench_task_config_with_options(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskConfigResponse(),
            self.do_rpcrequest('DescribeCloudbenchTaskConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloudbench_task_config_with_options_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskConfigResponse(),
            await self.do_rpcrequest_async('DescribeCloudbenchTaskConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloudbench_task_config(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_config_with_options(request, runtime)

    async def describe_cloudbench_task_config_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloudbench_task_config_with_options_async(request, runtime)

    def describe_diagnostic_report_list_with_options(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            self.do_rpcrequest('DescribeDiagnosticReportList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            await self.do_rpcrequest_async('DescribeDiagnosticReportList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnostic_report_list(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    async def describe_diagnostic_report_list_async(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_report_list_with_options_async(request, runtime)

    def describe_hot_big_keys_with_options(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotBigKeysResponse(),
            self.do_rpcrequest('DescribeHotBigKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hot_big_keys_with_options_async(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotBigKeysResponse(),
            await self.do_rpcrequest_async('DescribeHotBigKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hot_big_keys(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_big_keys_with_options(request, runtime)

    async def describe_hot_big_keys_async(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hot_big_keys_with_options_async(request, runtime)

    def describe_hot_keys_with_options(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            self.do_rpcrequest('DescribeHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hot_keys_with_options_async(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            await self.do_rpcrequest_async('DescribeHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hot_keys(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
    ) -> das20200116_models.DescribeHotKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_keys_with_options(request, runtime)

    async def describe_hot_keys_async(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
    ) -> das20200116_models.DescribeHotKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hot_keys_with_options_async(request, runtime)

    def describe_top_big_keys_with_options(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopBigKeysResponse(),
            self.do_rpcrequest('DescribeTopBigKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_top_big_keys_with_options_async(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopBigKeysResponse(),
            await self.do_rpcrequest_async('DescribeTopBigKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_top_big_keys(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_top_big_keys_with_options(request, runtime)

    async def describe_top_big_keys_async(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_big_keys_with_options_async(request, runtime)

    def describe_top_hot_keys_with_options(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopHotKeysResponse(),
            self.do_rpcrequest('DescribeTopHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_top_hot_keys_with_options_async(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopHotKeysResponse(),
            await self.do_rpcrequest_async('DescribeTopHotKeys', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_top_hot_keys(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_top_hot_keys_with_options(request, runtime)

    async def describe_top_hot_keys_async(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_hot_keys_with_options_async(request, runtime)

    def disable_all_sql_concurrency_control_rules_with_options(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
            self.do_rpcrequest('DisableAllSqlConcurrencyControlRules', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_all_sql_concurrency_control_rules_with_options_async(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
            await self.do_rpcrequest_async('DisableAllSqlConcurrencyControlRules', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_all_sql_concurrency_control_rules(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_all_sql_concurrency_control_rules_with_options(request, runtime)

    async def disable_all_sql_concurrency_control_rules_async(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_all_sql_concurrency_control_rules_with_options_async(request, runtime)

    def disable_sql_concurrency_control_with_options(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DisableSqlConcurrencyControlResponse(),
            self.do_rpcrequest('DisableSqlConcurrencyControl', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_sql_concurrency_control_with_options_async(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.DisableSqlConcurrencyControlResponse(),
            await self.do_rpcrequest_async('DisableSqlConcurrencyControl', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_sql_concurrency_control(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_concurrency_control_with_options(request, runtime)

    async def disable_sql_concurrency_control_async(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_sql_concurrency_control_with_options_async(request, runtime)

    def enable_sql_concurrency_control_with_options(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.EnableSqlConcurrencyControlResponse(),
            self.do_rpcrequest('EnableSqlConcurrencyControl', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_sql_concurrency_control_with_options_async(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.EnableSqlConcurrencyControlResponse(),
            await self.do_rpcrequest_async('EnableSqlConcurrencyControl', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_sql_concurrency_control(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_concurrency_control_with_options(request, runtime)

    async def enable_sql_concurrency_control_async(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_sql_concurrency_control_with_options_async(request, runtime)

    def get_auto_resource_optimize_config_with_options(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            self.do_rpcrequest('GetAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_auto_resource_optimize_config_with_options_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            await self.do_rpcrequest_async('GetAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auto_resource_optimize_config(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_resource_optimize_config_with_options(request, runtime)

    async def get_auto_resource_optimize_config_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_resource_optimize_config_with_options_async(request, runtime)

    def get_autonomous_notify_event_content_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventContent', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_event_content_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEventContent', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_event_content(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_content_with_options(request, runtime)

    async def get_autonomous_notify_event_content_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_event_content_with_options_async(request, runtime)

    def get_autonomous_notify_event_detail_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventDetailResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventDetail', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_event_detail_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventDetailResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEventDetail', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_event_detail(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_detail_with_options(request, runtime)

    async def get_autonomous_notify_event_detail_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventDetailRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_event_detail_with_options_async(request, runtime)

    def get_autonomous_notify_events_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEvents', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_events_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEvents', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_events(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_with_options(request, runtime)

    async def get_autonomous_notify_events_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_events_with_options_async(request, runtime)

    def get_autonomous_notify_events_in_range_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            self.do_rpcrequest('GetAutonomousNotifyEventsInRange', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_autonomous_notify_events_in_range_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            await self.do_rpcrequest_async('GetAutonomousNotifyEventsInRange', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_autonomous_notify_events_in_range(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_in_range_with_options(request, runtime)

    async def get_autonomous_notify_events_in_range_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_events_in_range_with_options_async(request, runtime)

    def get_endpoint_switch_task_with_options(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            self.do_rpcrequest('GetEndpointSwitchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_endpoint_switch_task_with_options_async(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            await self.do_rpcrequest_async('GetEndpointSwitchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_endpoint_switch_task(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    async def get_endpoint_switch_task_async(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_endpoint_switch_task_with_options_async(request, runtime)

    def get_event_overview_with_options(
        self,
        request: das20200116_models.GetEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEventOverviewResponse(),
            self.do_rpcrequest('GetEventOverview', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_event_overview_with_options_async(
        self,
        request: das20200116_models.GetEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetEventOverviewResponse(),
            await self.do_rpcrequest_async('GetEventOverview', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_event_overview(
        self,
        request: das20200116_models.GetEventOverviewRequest,
    ) -> das20200116_models.GetEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_overview_with_options(request, runtime)

    async def get_event_overview_async(
        self,
        request: das20200116_models.GetEventOverviewRequest,
    ) -> das20200116_models.GetEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_overview_with_options_async(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            self.do_rpcrequest('GetHDMAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hdmaliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            await self.do_rpcrequest_async('GetHDMAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hdmaliyun_resource_sync_result(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hdmaliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmaliyun_resource_sync_result_async(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hdmaliyun_resource_sync_result_with_options_async(request, runtime)

    def get_hdmlast_aliyun_resource_sync_result_with_options(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            self.do_rpcrequest('GetHDMLastAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hdmlast_aliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            await self.do_rpcrequest_async('GetHDMLastAliyunResourceSyncResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hdmlast_aliyun_resource_sync_result(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hdmlast_aliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmlast_aliyun_resource_sync_result_async(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hdmlast_aliyun_resource_sync_result_with_options_async(request, runtime)

    def get_instance_inspections_with_options(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            self.do_rpcrequest('GetInstanceInspections', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_inspections_with_options_async(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            await self.do_rpcrequest_async('GetInstanceInspections', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_inspections(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_inspections_with_options(request, runtime)

    async def get_instance_inspections_async(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_inspections_with_options_async(request, runtime)

    def get_request_diagnosis_page_with_options(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisPageResponse(),
            self.do_rpcrequest('GetRequestDiagnosisPage', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_request_diagnosis_page_with_options_async(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisPageResponse(),
            await self.do_rpcrequest_async('GetRequestDiagnosisPage', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_request_diagnosis_page(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_page_with_options(request, runtime)

    async def get_request_diagnosis_page_async(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_request_diagnosis_page_with_options_async(request, runtime)

    def get_request_diagnosis_result_with_options(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisResultResponse(),
            self.do_rpcrequest('GetRequestDiagnosisResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_request_diagnosis_result_with_options_async(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisResultResponse(),
            await self.do_rpcrequest_async('GetRequestDiagnosisResult', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_request_diagnosis_result(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_result_with_options(request, runtime)

    async def get_request_diagnosis_result_async(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_request_diagnosis_result_with_options_async(request, runtime)

    def get_resource_optimize_history_list_with_options(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            self.do_rpcrequest('GetResourceOptimizeHistoryList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_optimize_history_list_with_options_async(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            await self.do_rpcrequest_async('GetResourceOptimizeHistoryList', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_optimize_history_list(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_optimize_history_list_with_options(request, runtime)

    async def get_resource_optimize_history_list_async(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_optimize_history_list_with_options_async(request, runtime)

    def get_running_sql_concurrency_control_rules_with_options(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
            self.do_rpcrequest('GetRunningSqlConcurrencyControlRules', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_running_sql_concurrency_control_rules_with_options_async(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
            await self.do_rpcrequest_async('GetRunningSqlConcurrencyControlRules', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_running_sql_concurrency_control_rules(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_running_sql_concurrency_control_rules_with_options(request, runtime)

    async def get_running_sql_concurrency_control_rules_async(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_running_sql_concurrency_control_rules_with_options_async(request, runtime)

    def get_sql_concurrency_control_rules_history_with_options(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            self.do_rpcrequest('GetSqlConcurrencyControlRulesHistory', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sql_concurrency_control_rules_history_with_options_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            await self.do_rpcrequest_async('GetSqlConcurrencyControlRulesHistory', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sql_concurrency_control_rules_history(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sql_concurrency_control_rules_history_with_options(request, runtime)

    async def get_sql_concurrency_control_rules_history_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sql_concurrency_control_rules_history_with_options_async(request, runtime)

    def get_sql_optimize_advice_with_options(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlOptimizeAdviceResponse(),
            self.do_rpcrequest('GetSqlOptimizeAdvice', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sql_optimize_advice_with_options_async(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlOptimizeAdviceResponse(),
            await self.do_rpcrequest_async('GetSqlOptimizeAdvice', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sql_optimize_advice(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sql_optimize_advice_with_options(request, runtime)

    async def get_sql_optimize_advice_async(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sql_optimize_advice_with_options_async(request, runtime)

    def run_cloud_bench_task_with_options(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.RunCloudBenchTaskResponse(),
            self.do_rpcrequest('RunCloudBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_cloud_bench_task_with_options_async(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.RunCloudBenchTaskResponse(),
            await self.do_rpcrequest_async('RunCloudBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_cloud_bench_task(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_bench_task_with_options(request, runtime)

    async def run_cloud_bench_task_async(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_cloud_bench_task_with_options_async(request, runtime)

    def stop_cloud_bench_task_with_options(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopCloudBenchTaskResponse(),
            self.do_rpcrequest('StopCloudBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_cloud_bench_task_with_options_async(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopCloudBenchTaskResponse(),
            await self.do_rpcrequest_async('StopCloudBenchTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_cloud_bench_task(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_cloud_bench_task_with_options(request, runtime)

    async def stop_cloud_bench_task_async(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_cloud_bench_task_with_options_async(request, runtime)

    def stop_or_rollback_optimize_task_with_options(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            self.do_rpcrequest('StopOrRollbackOptimizeTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_or_rollback_optimize_task_with_options_async(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            await self.do_rpcrequest_async('StopOrRollbackOptimizeTask', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_or_rollback_optimize_task(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_or_rollback_optimize_task_with_options(request, runtime)

    async def stop_or_rollback_optimize_task_async(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_or_rollback_optimize_task_with_options_async(request, runtime)

    def sync_hdmaliyun_resource_with_options(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            self.do_rpcrequest('SyncHDMAliyunResource', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_hdmaliyun_resource_with_options_async(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            await self.do_rpcrequest_async('SyncHDMAliyunResource', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_hdmaliyun_resource(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_hdmaliyun_resource_with_options(request, runtime)

    async def sync_hdmaliyun_resource_async(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_hdmaliyun_resource_with_options_async(request, runtime)

    def turn_off_auto_resource_optimize_with_options(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            self.do_rpcrequest('TurnOffAutoResourceOptimize', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def turn_off_auto_resource_optimize_with_options_async(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            await self.do_rpcrequest_async('TurnOffAutoResourceOptimize', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def turn_off_auto_resource_optimize(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.turn_off_auto_resource_optimize_with_options(request, runtime)

    async def turn_off_auto_resource_optimize_async(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.turn_off_auto_resource_optimize_with_options_async(request, runtime)

    def update_auto_resource_optimize_config_with_options(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            self.do_rpcrequest('UpdateAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_auto_resource_optimize_config_with_options_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            await self.do_rpcrequest_async('UpdateAutoResourceOptimizeConfig', '2020-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_auto_resource_optimize_config(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_resource_optimize_config_with_options(request, runtime)

    async def update_auto_resource_optimize_config_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_resource_optimize_config_with_options_async(request, runtime)
