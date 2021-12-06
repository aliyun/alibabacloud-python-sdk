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
        query = {}
        query['Engine'] = request.engine
        query['FlushAccount'] = request.flush_account
        query['InstanceAlias'] = request.instance_alias
        query['InstanceArea'] = request.instance_area
        query['InstanceId'] = request.instance_id
        query['Ip'] = request.ip
        query['NetworkType'] = request.network_type
        query['Password'] = request.password
        query['Port'] = request.port
        query['Region'] = request.region
        query['Username'] = request.username
        query['VpcId'] = request.vpc_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddHDMInstance',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_hdminstance_with_options_async(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AddHDMInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Engine'] = request.engine
        query['FlushAccount'] = request.flush_account
        query['InstanceAlias'] = request.instance_alias
        query['InstanceArea'] = request.instance_area
        query['InstanceId'] = request.instance_id
        query['Ip'] = request.ip
        query['NetworkType'] = request.network_type
        query['Password'] = request.password
        query['Port'] = request.port
        query['Region'] = request.region
        query['Username'] = request.username
        query['VpcId'] = request.vpc_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddHDMInstance',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.AddHDMInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Description'] = request.description
        query['DstInstanceId'] = request.dst_instance_id
        query['DstSuperAccount'] = request.dst_super_account
        query['DstSuperPassword'] = request.dst_super_password
        query['Rate'] = request.rate
        query['RequestDuration'] = request.request_duration
        query['RequestStartTime'] = request.request_start_time
        query['SrcEngine'] = request.src_engine
        query['SrcEngineVersion'] = request.src_engine_version
        query['SrcMaxQps'] = request.src_max_qps
        query['SrcMeanQps'] = request.src_mean_qps
        query['SrcSqlOssAddr'] = request.src_sql_oss_addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAdamBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateAdamBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_adam_bench_task_with_options_async(
        self,
        request: das20200116_models.CreateAdamBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateAdamBenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DstInstanceId'] = request.dst_instance_id
        query['DstSuperAccount'] = request.dst_super_account
        query['DstSuperPassword'] = request.dst_super_password
        query['Rate'] = request.rate
        query['RequestDuration'] = request.request_duration
        query['RequestStartTime'] = request.request_start_time
        query['SrcEngine'] = request.src_engine
        query['SrcEngineVersion'] = request.src_engine_version
        query['SrcMaxQps'] = request.src_max_qps
        query['SrcMeanQps'] = request.src_mean_qps
        query['SrcSqlOssAddr'] = request.src_sql_oss_addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAdamBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateAdamBenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['BackupSetId'] = request.backup_set_id
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupSetId'] = request.backup_set_id
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateCacheAnalysisJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Amount'] = request.amount
        query['BackupId'] = request.backup_id
        query['BackupTime'] = request.backup_time
        query['ClientType'] = request.client_type
        query['Description'] = request.description
        query['DstConnectionString'] = request.dst_connection_string
        query['DstInstanceId'] = request.dst_instance_id
        query['DstPort'] = request.dst_port
        query['DstSuperAccount'] = request.dst_super_account
        query['DstSuperPassword'] = request.dst_super_password
        query['DstType'] = request.dst_type
        query['DtsJobClass'] = request.dts_job_class
        query['DtsJobId'] = request.dts_job_id
        query['EndState'] = request.end_state
        query['GatewayVpcId'] = request.gateway_vpc_id
        query['GatewayVpcIp'] = request.gateway_vpc_ip
        query['Rate'] = request.rate
        query['RequestDuration'] = request.request_duration
        query['RequestEndTime'] = request.request_end_time
        query['RequestStartTime'] = request.request_start_time
        query['SmartPressureTime'] = request.smart_pressure_time
        query['SrcInstanceId'] = request.src_instance_id
        query['SrcPublicIp'] = request.src_public_ip
        query['SrcSuperAccount'] = request.src_super_account
        query['SrcSuperPassword'] = request.src_super_password
        query['TaskType'] = request.task_type
        query['WorkDir'] = request.work_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateCloudBenchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_bench_tasks_with_options_async(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Amount'] = request.amount
        query['BackupId'] = request.backup_id
        query['BackupTime'] = request.backup_time
        query['ClientType'] = request.client_type
        query['Description'] = request.description
        query['DstConnectionString'] = request.dst_connection_string
        query['DstInstanceId'] = request.dst_instance_id
        query['DstPort'] = request.dst_port
        query['DstSuperAccount'] = request.dst_super_account
        query['DstSuperPassword'] = request.dst_super_password
        query['DstType'] = request.dst_type
        query['DtsJobClass'] = request.dts_job_class
        query['DtsJobId'] = request.dts_job_id
        query['EndState'] = request.end_state
        query['GatewayVpcId'] = request.gateway_vpc_id
        query['GatewayVpcIp'] = request.gateway_vpc_ip
        query['Rate'] = request.rate
        query['RequestDuration'] = request.request_duration
        query['RequestEndTime'] = request.request_end_time
        query['RequestStartTime'] = request.request_start_time
        query['SmartPressureTime'] = request.smart_pressure_time
        query['SrcInstanceId'] = request.src_instance_id
        query['SrcPublicIp'] = request.src_public_ip
        query['SrcSuperAccount'] = request.src_super_account
        query['SrcSuperPassword'] = request.src_super_password
        query['TaskType'] = request.task_type
        query['WorkDir'] = request.work_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateCloudBenchTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['EndTime'] = request.end_time
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateDiagnosticReportResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Database'] = request.database
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRequestDiagnosis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateRequestDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_request_diagnosis_with_options_async(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Database'] = request.database
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRequestDiagnosis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateRequestDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJobs',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_jobs_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJobs',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCacheAnalysisJobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndTime'] = request.end_time
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudBenchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_bench_tasks_with_options_async(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudBenchTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloudbench_task_with_options_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTaskConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloudbench_task_config_with_options_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTaskConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeCloudbenchTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['EndTime'] = request.end_time
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['EndTime'] = request.end_time
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeDiagnosticReportListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHotBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotBigKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hot_big_keys_with_options_async(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHotBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotBigKeysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hot_keys_with_options_async(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeHotKeysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTopBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopBigKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_big_keys_with_options_async(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTopBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopBigKeysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTopHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopHotKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_hot_keys_with_options_async(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTopHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeTopHotKeysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableAllSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_all_sql_concurrency_control_rules_with_options_async(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableAllSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableSqlConcurrencyControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sql_concurrency_control_with_options_async(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableSqlConcurrencyControlResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConcurrencyControlTime'] = request.concurrency_control_time
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['MaxConcurrency'] = request.max_concurrency
        query['SqlKeywords'] = request.sql_keywords
        query['SqlType'] = request.sql_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.EnableSqlConcurrencyControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sql_concurrency_control_with_options_async(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConcurrencyControlTime'] = request.concurrency_control_time
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['MaxConcurrency'] = request.max_concurrency
        query['SqlKeywords'] = request.sql_keywords
        query['SqlType'] = request.sql_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.EnableSqlConcurrencyControlResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_resource_optimize_config_with_options_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['SpanId'] = request.span_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventContent',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_autonomous_notify_event_content_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['SpanId'] = request.span_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventContent',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventContentResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_autonomous_notify_events_in_range_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['EventContext'] = request.event_context
        query['InstanceId'] = request.instance_id
        query['Level'] = request.level
        query['MinLevel'] = request.min_level
        query['NodeId'] = request.node_id
        query['PageOffset'] = request.page_offset
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventsInRange',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_autonomous_notify_events_in_range_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['EventContext'] = request.event_context
        query['InstanceId'] = request.instance_id
        query['Level'] = request.level
        query['MinLevel'] = request.min_level
        query['NodeId'] = request.node_id
        query['PageOffset'] = request.page_offset
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventsInRange',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['TaskId'] = request.task_id
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEndpointSwitchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_endpoint_switch_task_with_options_async(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEndpointSwitchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetEndpointSwitchTaskResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_hdmaliyun_resource_sync_result_with_options(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHDMAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hdmaliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHDMAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHDMLastAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hdmlast_aliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHDMLastAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndTime'] = request.end_time
        query['Engine'] = request.engine
        query['InstanceArea'] = request.instance_area
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['SearchMap'] = request.search_map
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetInstanceInspections',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_inspections_with_options_async(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['Engine'] = request.engine
        query['InstanceArea'] = request.instance_area
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['SearchMap'] = request.search_map
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetInstanceInspections',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceInspectionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisPage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_request_diagnosis_page_with_options_async(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['NodeId'] = request.node_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisPage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisPageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InstanceId'] = request.instance_id
        query['MessageId'] = request.message_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_request_diagnosis_result_with_options_async(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['MessageId'] = request.message_id
        query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRequestDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessKey'] = request.access_key
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Page'] = request.page
        query['PageSize'] = request.page_size
        query['Signature'] = request.signature
        query['StartTime'] = request.start_time
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetResourceOptimizeHistoryList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_optimize_history_list_with_options_async(
        self,
        request: das20200116_models.GetResourceOptimizeHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetResourceOptimizeHistoryListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['EndTime'] = request.end_time
        query['InstanceId'] = request.instance_id
        query['Page'] = request.page
        query['PageSize'] = request.page_size
        query['Signature'] = request.signature
        query['StartTime'] = request.start_time
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetResourceOptimizeHistoryList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetResourceOptimizeHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRunningSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_running_sql_concurrency_control_rules_with_options_async(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRunningSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_sql_concurrency_control_keywords_from_sql_text_with_options(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['SqlText'] = request.sql_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlKeywordsFromSqlText',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_concurrency_control_keywords_from_sql_text_with_options_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['SqlText'] = request.sql_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlKeywordsFromSqlText',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_concurrency_control_keywords_from_sql_text(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sql_concurrency_control_keywords_from_sql_text_with_options(request, runtime)

    async def get_sql_concurrency_control_keywords_from_sql_text_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sql_concurrency_control_keywords_from_sql_text_with_options_async(request, runtime)

    def get_sql_concurrency_control_rules_history_with_options(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlRulesHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_concurrency_control_rules_history_with_options_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['InstanceId'] = request.instance_id
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlRulesHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndDt'] = request.end_dt
        query['Engine'] = request.engine
        query['InstanceIds'] = request.instance_ids
        query['StartDt'] = request.start_dt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlOptimizeAdvice',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlOptimizeAdviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_optimize_advice_with_options_async(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsoleContext'] = request.console_context
        query['EndDt'] = request.end_dt
        query['Engine'] = request.engine
        query['InstanceIds'] = request.instance_ids
        query['StartDt'] = request.start_dt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSqlOptimizeAdvice',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetSqlOptimizeAdviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.RunCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cloud_bench_task_with_options_async(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.RunCloudBenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.StopCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cloud_bench_task_with_options_async(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.StopCloudBenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['StopOrRollback'] = request.stop_or_rollback
        query['TaskType'] = request.task_type
        query['TaskUuid'] = request.task_uuid
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopOrRollbackOptimizeTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_or_rollback_optimize_task_with_options_async(
        self,
        request: das20200116_models.StopOrRollbackOptimizeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopOrRollbackOptimizeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['StopOrRollback'] = request.stop_or_rollback
        query['TaskType'] = request.task_type
        query['TaskUuid'] = request.task_uuid
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopOrRollbackOptimizeTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.StopOrRollbackOptimizeTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Async'] = request.async_
        query['ResourceTypes'] = request.resource_types
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['WaitForModifySecurityIps'] = request.wait_for_modify_security_ips
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SyncHDMAliyunResource',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_hdmaliyun_resource_with_options_async(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Async'] = request.async_
        query['ResourceTypes'] = request.resource_types
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['WaitForModifySecurityIps'] = request.wait_for_modify_security_ips
        query['__context'] = request.context
        query['accessKey'] = request.access_key
        query['signature'] = request.signature
        query['skipAuth'] = request.skip_auth
        query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SyncHDMAliyunResource',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.SyncHDMAliyunResourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TurnOffAutoResourceOptimize',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def turn_off_auto_resource_optimize_with_options_async(
        self,
        request: das20200116_models.TurnOffAutoResourceOptimizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.TurnOffAutoResourceOptimizeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TurnOffAutoResourceOptimize',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.TurnOffAutoResourceOptimizeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AccessKey'] = request.access_key
        query['AutoDefragment'] = request.auto_defragment
        query['AutoDuplicateIndexDelete'] = request.auto_duplicate_index_delete
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        query['TableSpaceSize'] = request.table_space_size
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_resource_optimize_config_with_options_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['AutoDefragment'] = request.auto_defragment
        query['AutoDuplicateIndexDelete'] = request.auto_duplicate_index_delete
        query['InstanceId'] = request.instance_id
        query['Signature'] = request.signature
        query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        query['TableSpaceSize'] = request.table_space_size
        query['Uid'] = request.uid
        query['UserId'] = request.user_id
        query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAutoResourceOptimizeConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
