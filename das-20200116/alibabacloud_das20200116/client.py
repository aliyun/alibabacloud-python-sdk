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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.flush_account):
            query['FlushAccount'] = request.flush_account
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddHDMInstance',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.flush_account):
            query['FlushAccount'] = request.flush_account
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddHDMInstance',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not UtilClient.is_unset(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not UtilClient.is_unset(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not UtilClient.is_unset(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not UtilClient.is_unset(request.src_engine):
            query['SrcEngine'] = request.src_engine
        if not UtilClient.is_unset(request.src_engine_version):
            query['SrcEngineVersion'] = request.src_engine_version
        if not UtilClient.is_unset(request.src_max_qps):
            query['SrcMaxQps'] = request.src_max_qps
        if not UtilClient.is_unset(request.src_mean_qps):
            query['SrcMeanQps'] = request.src_mean_qps
        if not UtilClient.is_unset(request.src_sql_oss_addr):
            query['SrcSqlOssAddr'] = request.src_sql_oss_addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdamBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not UtilClient.is_unset(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not UtilClient.is_unset(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not UtilClient.is_unset(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not UtilClient.is_unset(request.src_engine):
            query['SrcEngine'] = request.src_engine
        if not UtilClient.is_unset(request.src_engine_version):
            query['SrcEngineVersion'] = request.src_engine_version
        if not UtilClient.is_unset(request.src_max_qps):
            query['SrcMaxQps'] = request.src_max_qps
        if not UtilClient.is_unset(request.src_mean_qps):
            query['SrcMeanQps'] = request.src_mean_qps
        if not UtilClient.is_unset(request.src_sql_oss_addr):
            query['SrcSqlOssAddr'] = request.src_sql_oss_addr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdamBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_connection_string):
            query['DstConnectionString'] = request.dst_connection_string
        if not UtilClient.is_unset(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not UtilClient.is_unset(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not UtilClient.is_unset(request.dst_type):
            query['DstType'] = request.dst_type
        if not UtilClient.is_unset(request.dts_job_class):
            query['DtsJobClass'] = request.dts_job_class
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_state):
            query['EndState'] = request.end_state
        if not UtilClient.is_unset(request.gateway_vpc_id):
            query['GatewayVpcId'] = request.gateway_vpc_id
        if not UtilClient.is_unset(request.gateway_vpc_ip):
            query['GatewayVpcIp'] = request.gateway_vpc_ip
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not UtilClient.is_unset(request.request_end_time):
            query['RequestEndTime'] = request.request_end_time
        if not UtilClient.is_unset(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not UtilClient.is_unset(request.smart_pressure_time):
            query['SmartPressureTime'] = request.smart_pressure_time
        if not UtilClient.is_unset(request.src_instance_id):
            query['SrcInstanceId'] = request.src_instance_id
        if not UtilClient.is_unset(request.src_public_ip):
            query['SrcPublicIp'] = request.src_public_ip
        if not UtilClient.is_unset(request.src_super_account):
            query['SrcSuperAccount'] = request.src_super_account
        if not UtilClient.is_unset(request.src_super_password):
            query['SrcSuperPassword'] = request.src_super_password
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.work_dir):
            query['WorkDir'] = request.work_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dst_connection_string):
            query['DstConnectionString'] = request.dst_connection_string
        if not UtilClient.is_unset(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not UtilClient.is_unset(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not UtilClient.is_unset(request.dst_type):
            query['DstType'] = request.dst_type
        if not UtilClient.is_unset(request.dts_job_class):
            query['DtsJobClass'] = request.dts_job_class
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_state):
            query['EndState'] = request.end_state
        if not UtilClient.is_unset(request.gateway_vpc_id):
            query['GatewayVpcId'] = request.gateway_vpc_id
        if not UtilClient.is_unset(request.gateway_vpc_ip):
            query['GatewayVpcIp'] = request.gateway_vpc_ip
        if not UtilClient.is_unset(request.rate):
            query['Rate'] = request.rate
        if not UtilClient.is_unset(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not UtilClient.is_unset(request.request_end_time):
            query['RequestEndTime'] = request.request_end_time
        if not UtilClient.is_unset(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not UtilClient.is_unset(request.smart_pressure_time):
            query['SmartPressureTime'] = request.smart_pressure_time
        if not UtilClient.is_unset(request.src_instance_id):
            query['SrcInstanceId'] = request.src_instance_id
        if not UtilClient.is_unset(request.src_public_ip):
            query['SrcPublicIp'] = request.src_public_ip
        if not UtilClient.is_unset(request.src_super_account):
            query['SrcSuperAccount'] = request.src_super_account
        if not UtilClient.is_unset(request.src_super_password):
            query['SrcSuperPassword'] = request.src_super_password
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.work_dir):
            query['WorkDir'] = request.work_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def create_kill_instance_session_task_with_options(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_user):
            query['DbUser'] = request.db_user
        if not UtilClient.is_unset(request.db_user_password):
            query['DbUserPassword'] = request.db_user_password
        if not UtilClient.is_unset(request.ignored_users):
            query['IgnoredUsers'] = request.ignored_users
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.kill_all_sessions):
            query['KillAllSessions'] = request.kill_all_sessions
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.session_ids):
            query['SessionIds'] = request.session_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKillInstanceSessionTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateKillInstanceSessionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kill_instance_session_task_with_options_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_user):
            query['DbUser'] = request.db_user
        if not UtilClient.is_unset(request.db_user_password):
            query['DbUserPassword'] = request.db_user_password
        if not UtilClient.is_unset(request.ignored_users):
            query['IgnoredUsers'] = request.ignored_users
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.kill_all_sessions):
            query['KillAllSessions'] = request.kill_all_sessions
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.session_ids):
            query['SessionIds'] = request.session_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKillInstanceSessionTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.CreateKillInstanceSessionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kill_instance_session_task(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_kill_instance_session_task_with_options(request, runtime)

    async def create_kill_instance_session_task_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_kill_instance_session_task_with_options_async(request, runtime)

    def create_request_diagnosis_with_options(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRequestDiagnosis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql):
            query['Sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRequestDiagnosis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def delete_cloud_bench_task_with_options(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DeleteCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_bench_task_with_options_async(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DeleteCloudBenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_bench_task(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_bench_task_with_options(request, runtime)

    async def delete_cloud_bench_task_async(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_bench_task_with_options_async(request, runtime)

    def delete_stop_gateway_with_options(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStopGateway',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DeleteStopGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stop_gateway_with_options_async(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStopGateway',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DeleteStopGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stop_gateway(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stop_gateway_with_options(request, runtime)

    async def delete_stop_gateway_async(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stop_gateway_with_options_async(request, runtime)

    def describe_auto_scaling_config_with_options(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoScalingConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_scaling_config_with_options_async(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoScalingConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_scaling_config(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scaling_config_with_options(request, runtime)

    async def describe_auto_scaling_config_async(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_scaling_config_with_options_async(request, runtime)

    def describe_cache_analysis_job_with_options(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJob',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJobs',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCacheAnalysisJobs',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudBenchTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTaskConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudbenchTaskConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def describe_instance_das_pro_with_options(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDasPro',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeInstanceDasProResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_das_pro_with_options_async(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDasPro',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DescribeInstanceDasProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_das_pro(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_das_pro_with_options(request, runtime)

    async def describe_instance_das_pro_async(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_das_pro_with_options_async(request, runtime)

    def describe_top_big_keys_with_options(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopBigKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopHotKeys',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAllSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAllSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def disable_auto_resource_optimize_rules_with_options(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAutoResourceOptimizeRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableAutoResourceOptimizeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_resource_optimize_rules_with_options_async(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAutoResourceOptimizeRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableAutoResourceOptimizeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_resource_optimize_rules(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_resource_optimize_rules_with_options(request, runtime)

    async def disable_auto_resource_optimize_rules_async(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_resource_optimize_rules_with_options_async(request, runtime)

    def disable_auto_throttle_rules_with_options(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAutoThrottleRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableAutoThrottleRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_throttle_rules_with_options_async(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAutoThrottleRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableAutoThrottleRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_throttle_rules(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_throttle_rules_with_options(request, runtime)

    async def disable_auto_throttle_rules_async(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_throttle_rules_with_options_async(request, runtime)

    def disable_das_pro_with_options(
        self,
        request: das20200116_models.DisableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableDasProResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDasPro',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableDasProResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_das_pro_with_options_async(
        self,
        request: das20200116_models.DisableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableDasProResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDasPro',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableDasProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_das_pro(
        self,
        request: das20200116_models.DisableDasProRequest,
    ) -> das20200116_models.DisableDasProResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_das_pro_with_options(request, runtime)

    async def disable_das_pro_async(
        self,
        request: das20200116_models.DisableDasProRequest,
    ) -> das20200116_models.DisableDasProResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_das_pro_with_options_async(request, runtime)

    def disable_instance_das_config_with_options(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstanceDasConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableInstanceDasConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_instance_das_config_with_options_async(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstanceDasConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.DisableInstanceDasConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_instance_das_config(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_das_config_with_options(request, runtime)

    async def disable_instance_das_config_async(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_das_config_with_options_async(request, runtime)

    def disable_sql_concurrency_control_with_options(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def enable_das_pro_with_options(
        self,
        request: das20200116_models.EnableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableDasProResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_retention):
            query['SqlRetention'] = request.sql_retention
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDasPro',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.EnableDasProResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_das_pro_with_options_async(
        self,
        request: das20200116_models.EnableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableDasProResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_retention):
            query['SqlRetention'] = request.sql_retention
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDasPro',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.EnableDasProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_das_pro(
        self,
        request: das20200116_models.EnableDasProRequest,
    ) -> das20200116_models.EnableDasProResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_das_pro_with_options(request, runtime)

    async def enable_das_pro_async(
        self,
        request: das20200116_models.EnableDasProRequest,
    ) -> das20200116_models.EnableDasProResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_das_pro_with_options_async(request, runtime)

    def enable_sql_concurrency_control_with_options(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency_control_time):
            query['ConcurrencyControlTime'] = request.concurrency_control_time
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.sql_keywords):
            query['SqlKeywords'] = request.sql_keywords
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.concurrency_control_time):
            query['ConcurrencyControlTime'] = request.concurrency_control_time
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.sql_keywords):
            query['SqlKeywords'] = request.sql_keywords
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlConcurrencyControl',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def get_async_error_request_list_by_code_with_options(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestListByCode',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestListByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_error_request_list_by_code_with_options_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestListByCode',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestListByCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_error_request_list_by_code(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_list_by_code_with_options(request, runtime)

    async def get_async_error_request_list_by_code_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_error_request_list_by_code_with_options_async(request, runtime)

    def get_async_error_request_stat_by_code_with_options(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestStatByCode',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestStatByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_error_request_stat_by_code_with_options_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestStatByCode',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestStatByCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_error_request_stat_by_code(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_stat_by_code_with_options(request, runtime)

    async def get_async_error_request_stat_by_code_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_error_request_stat_by_code_with_options_async(request, runtime)

    def get_async_error_request_stat_result_with_options(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql_id_list):
            query['SqlIdList'] = request.sql_id_list
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestStatResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestStatResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_error_request_stat_result_with_options_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql_id_list):
            query['SqlIdList'] = request.sql_id_list
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncErrorRequestStatResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAsyncErrorRequestStatResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_error_request_stat_result(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_stat_result_with_options(request, runtime)

    async def get_async_error_request_stat_result_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_error_request_stat_result_with_options_async(request, runtime)

    def get_auto_resource_optimize_rules_with_options(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoResourceOptimizeRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_resource_optimize_rules_with_options_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoResourceOptimizeRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoResourceOptimizeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_resource_optimize_rules(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_resource_optimize_rules_with_options(request, runtime)

    async def get_auto_resource_optimize_rules_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_resource_optimize_rules_with_options_async(request, runtime)

    def get_auto_throttle_rules_with_options(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoThrottleRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoThrottleRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_throttle_rules_with_options_async(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoThrottleRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetAutoThrottleRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_throttle_rules(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_throttle_rules_with_options(request, runtime)

    async def get_auto_throttle_rules_async(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_throttle_rules_with_options_async(request, runtime)

    def get_autonomous_notify_event_content_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.span_id):
            query['SpanId'] = request.span_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventContent',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.span_id):
            query['SpanId'] = request.span_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventContent',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_context):
            query['EventContext'] = request.event_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.min_level):
            query['MinLevel'] = request.min_level
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_offset):
            query['PageOffset'] = request.page_offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventsInRange',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_context):
            query['EventContext'] = request.event_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.min_level):
            query['MinLevel'] = request.min_level
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_offset):
            query['PageOffset'] = request.page_offset
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutonomousNotifyEventsInRange',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def get_das_pro_service_usage_with_options(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDasProServiceUsage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetDasProServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_das_pro_service_usage_with_options_async(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDasProServiceUsage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetDasProServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_das_pro_service_usage(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_das_pro_service_usage_with_options(request, runtime)

    async def get_das_pro_service_usage_async(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_das_pro_service_usage_with_options_async(request, runtime)

    def get_endpoint_switch_task_with_options(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEndpointSwitchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEndpointSwitchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def get_error_request_sample_with_options(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql_id):
            query['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErrorRequestSample',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetErrorRequestSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_error_request_sample_with_options_async(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql_id):
            query['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErrorRequestSample',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetErrorRequestSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_error_request_sample(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_error_request_sample_with_options(request, runtime)

    async def get_error_request_sample_async(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_error_request_sample_with_options_async(request, runtime)

    def get_event_subscription_with_options(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventSubscription',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetEventSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_subscription_with_options_async(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventSubscription',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetEventSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_subscription(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_subscription_with_options(request, runtime)

    async def get_event_subscription_async(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_subscription_with_options_async(request, runtime)

    def get_full_request_origin_stat_by_instance_id_with_options(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFullRequestOriginStatByInstanceId',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetFullRequestOriginStatByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_full_request_origin_stat_by_instance_id_with_options_async(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFullRequestOriginStatByInstanceId',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetFullRequestOriginStatByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_full_request_origin_stat_by_instance_id(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_full_request_origin_stat_by_instance_id_with_options(request, runtime)

    async def get_full_request_origin_stat_by_instance_id_async(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_full_request_origin_stat_by_instance_id_with_options_async(request, runtime)

    def get_full_request_sample_by_instance_id_with_options(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        body = {}
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFullRequestSampleByInstanceId',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetFullRequestSampleByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_full_request_sample_by_instance_id_with_options_async(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        body = {}
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFullRequestSampleByInstanceId',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetFullRequestSampleByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_full_request_sample_by_instance_id(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_full_request_sample_by_instance_id_with_options(request, runtime)

    async def get_full_request_sample_by_instance_id_async(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_full_request_sample_by_instance_id_with_options_async(request, runtime)

    def get_full_request_stat_result_by_instance_id_with_options(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.origin_host):
            query['OriginHost'] = request.origin_host
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sql_id):
            query['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFullRequestStatResultByInstanceId',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetFullRequestStatResultByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_full_request_stat_result_by_instance_id_with_options_async(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.origin_host):
            query['OriginHost'] = request.origin_host
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.sql_id):
            query['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFullRequestStatResultByInstanceId',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetFullRequestStatResultByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_full_request_stat_result_by_instance_id(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_full_request_stat_result_by_instance_id_with_options(request, runtime)

    async def get_full_request_stat_result_by_instance_id_async(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_full_request_stat_result_by_instance_id_with_options_async(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHDMAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHDMAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHDMLastAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHDMLastAliyunResourceSyncResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_map):
            query['SearchMap'] = request.search_map
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceInspections',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_map):
            query['SearchMap'] = request.search_map
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceInspections',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def get_instance_sql_optimize_statistic_with_options(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_enable):
            query['FilterEnable'] = request.filter_enable
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.use_merging):
            query['UseMerging'] = request.use_merging
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceSqlOptimizeStatistic',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceSqlOptimizeStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_sql_optimize_statistic_with_options_async(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_enable):
            query['FilterEnable'] = request.filter_enable
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.use_merging):
            query['UseMerging'] = request.use_merging
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceSqlOptimizeStatistic',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetInstanceSqlOptimizeStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_sql_optimize_statistic(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_sql_optimize_statistic_with_options(request, runtime)

    async def get_instance_sql_optimize_statistic_async(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_sql_optimize_statistic_with_options_async(request, runtime)

    def get_kill_instance_session_task_result_with_options(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKillInstanceSessionTaskResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetKillInstanceSessionTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kill_instance_session_task_result_with_options_async(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKillInstanceSessionTaskResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetKillInstanceSessionTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kill_instance_session_task_result(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_kill_instance_session_task_result_with_options(request, runtime)

    async def get_kill_instance_session_task_result_async(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_kill_instance_session_task_result_with_options_async(request, runtime)

    def get_partitions_heatmap_with_options(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPartitionsHeatmap',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetPartitionsHeatmapResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_partitions_heatmap_with_options_async(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPartitionsHeatmap',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetPartitionsHeatmapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_partitions_heatmap(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_partitions_heatmap_with_options(request, runtime)

    async def get_partitions_heatmap_async(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_partitions_heatmap_with_options_async(request, runtime)

    def get_query_optimize_data_stats_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataStats',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_data_stats_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataStats',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_data_stats(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_stats_with_options(request, runtime)

    async def get_query_optimize_data_stats_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_data_stats_with_options_async(request, runtime)

    def get_query_optimize_data_top_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataTop',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_data_top_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataTop',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_data_top(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_top_with_options(request, runtime)

    async def get_query_optimize_data_top_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_data_top_with_options_async(request, runtime)

    def get_query_optimize_data_trend_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataTrend',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_data_trend_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeDataTrend',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeDataTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_data_trend(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_trend_with_options(request, runtime)

    async def get_query_optimize_data_trend_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_data_trend_with_options_async(request, runtime)

    def get_query_optimize_exec_error_sample_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeExecErrorSample',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeExecErrorSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_exec_error_sample_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeExecErrorSample',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeExecErrorSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_exec_error_sample(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_exec_error_sample_with_options(request, runtime)

    async def get_query_optimize_exec_error_sample_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_exec_error_sample_with_options_async(request, runtime)

    def get_query_optimize_exec_error_stats_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeExecErrorStats',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeExecErrorStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_exec_error_stats_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeExecErrorStats',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeExecErrorStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_exec_error_stats(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_exec_error_stats_with_options(request, runtime)

    async def get_query_optimize_exec_error_stats_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_exec_error_stats_with_options_async(request, runtime)

    def get_query_optimize_rule_list_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeRuleList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_rule_list_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeRuleList',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_rule_list(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_rule_list_with_options(request, runtime)

    async def get_query_optimize_rule_list_async(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_rule_list_with_options_async(request, runtime)

    def get_query_optimize_solution_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeSolution',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_solution_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeSolution',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetQueryOptimizeSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_solution(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_solution_with_options(request, runtime)

    async def get_query_optimize_solution_async(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_solution_with_options_async(request, runtime)

    def get_redis_all_session_with_options(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRedisAllSession',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRedisAllSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_redis_all_session_with_options_async(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRedisAllSession',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.GetRedisAllSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_redis_all_session(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_redis_all_session_with_options(request, runtime)

    async def get_redis_all_session_async(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_redis_all_session_with_options_async(request, runtime)

    def get_request_diagnosis_page_with_options(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisPage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisPage',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRequestDiagnosisResult',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def get_running_sql_concurrency_control_rules_with_options(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningSqlConcurrencyControlRules',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_text):
            query['SqlText'] = request.sql_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlKeywordsFromSqlText',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_text):
            query['SqlText'] = request.sql_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlKeywordsFromSqlText',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlRulesHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlConcurrencyControlRulesHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_dt):
            query['EndDt'] = request.end_dt
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.start_dt):
            query['StartDt'] = request.start_dt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlOptimizeAdvice',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.end_dt):
            query['EndDt'] = request.end_dt
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.start_dt):
            query['StartDt'] = request.start_dt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlOptimizeAdvice',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def kill_instance_all_session_with_options(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillInstanceAllSession',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.KillInstanceAllSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_instance_all_session_with_options_async(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillInstanceAllSession',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.KillInstanceAllSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_instance_all_session(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_instance_all_session_with_options(request, runtime)

    async def kill_instance_all_session_async(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_instance_all_session_with_options_async(request, runtime)

    def modify_auto_scaling_config_with_options(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.shard):
            query['Shard'] = request.shard
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoScalingConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.ModifyAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_scaling_config_with_options_async(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.shard):
            query['Shard'] = request.shard
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoScalingConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.ModifyAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_scaling_config(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_scaling_config_with_options(request, runtime)

    async def modify_auto_scaling_config_async(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_scaling_config_with_options_async(request, runtime)

    def run_cloud_bench_task_with_options(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def set_event_subscription_with_options(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.event_context):
            query['EventContext'] = request.event_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.min_interval):
            query['MinInterval'] = request.min_interval
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEventSubscription',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.SetEventSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_event_subscription_with_options_async(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.event_context):
            query['EventContext'] = request.event_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.min_interval):
            query['MinInterval'] = request.min_interval
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEventSubscription',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.SetEventSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_event_subscription(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_event_subscription_with_options(request, runtime)

    async def set_event_subscription_async(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_event_subscription_with_options_async(request, runtime)

    def stop_cloud_bench_task_with_options(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudBenchTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def sync_hdmaliyun_resource_with_options(
        self,
        request: das20200116_models.SyncHDMAliyunResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SyncHDMAliyunResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.wait_for_modify_security_ips):
            query['WaitForModifySecurityIps'] = request.wait_for_modify_security_ips
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncHDMAliyunResource',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.wait_for_modify_security_ips):
            query['WaitForModifySecurityIps'] = request.wait_for_modify_security_ips
        if not UtilClient.is_unset(request.context):
            query['__context'] = request.context
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncHDMAliyunResource',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def update_auto_resource_optimize_rules_async_with_options(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.result_id):
            query['ResultId'] = request.result_id
        if not UtilClient.is_unset(request.table_fragmentation_ratio):
            query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        if not UtilClient.is_unset(request.table_space_size):
            query['TableSpaceSize'] = request.table_space_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoResourceOptimizeRulesAsync',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_resource_optimize_rules_async_with_options_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.result_id):
            query['ResultId'] = request.result_id
        if not UtilClient.is_unset(request.table_fragmentation_ratio):
            query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        if not UtilClient.is_unset(request.table_space_size):
            query['TableSpaceSize'] = request.table_space_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoResourceOptimizeRulesAsync',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_resource_optimize_rules_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_resource_optimize_rules_async_with_options(request, runtime)

    async def update_auto_resource_optimize_rules_async_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_resource_optimize_rules_async_with_options_async(request, runtime)

    def update_auto_sql_optimize_status_with_options(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoSqlOptimizeStatus',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoSqlOptimizeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_sql_optimize_status_with_options_async(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoSqlOptimizeStatus',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoSqlOptimizeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_sql_optimize_status(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_sql_optimize_status_with_options(request, runtime)

    async def update_auto_sql_optimize_status_async(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_sql_optimize_status_with_options_async(request, runtime)

    def update_auto_throttle_rules_async_with_options(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.abnormal_duration):
            query['AbnormalDuration'] = request.abnormal_duration
        if not UtilClient.is_unset(request.active_sessions):
            query['ActiveSessions'] = request.active_sessions
        if not UtilClient.is_unset(request.allow_throttle_end_time):
            query['AllowThrottleEndTime'] = request.allow_throttle_end_time
        if not UtilClient.is_unset(request.allow_throttle_start_time):
            query['AllowThrottleStartTime'] = request.allow_throttle_start_time
        if not UtilClient.is_unset(request.auto_kill_session):
            query['AutoKillSession'] = request.auto_kill_session
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.cpu_session_relation):
            query['CpuSessionRelation'] = request.cpu_session_relation
        if not UtilClient.is_unset(request.cpu_usage):
            query['CpuUsage'] = request.cpu_usage
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_throttle_time):
            query['MaxThrottleTime'] = request.max_throttle_time
        if not UtilClient.is_unset(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoThrottleRulesAsync',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoThrottleRulesAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_throttle_rules_async_with_options_async(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.abnormal_duration):
            query['AbnormalDuration'] = request.abnormal_duration
        if not UtilClient.is_unset(request.active_sessions):
            query['ActiveSessions'] = request.active_sessions
        if not UtilClient.is_unset(request.allow_throttle_end_time):
            query['AllowThrottleEndTime'] = request.allow_throttle_end_time
        if not UtilClient.is_unset(request.allow_throttle_start_time):
            query['AllowThrottleStartTime'] = request.allow_throttle_start_time
        if not UtilClient.is_unset(request.auto_kill_session):
            query['AutoKillSession'] = request.auto_kill_session
        if not UtilClient.is_unset(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not UtilClient.is_unset(request.cpu_session_relation):
            query['CpuSessionRelation'] = request.cpu_session_relation
        if not UtilClient.is_unset(request.cpu_usage):
            query['CpuUsage'] = request.cpu_usage
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_throttle_time):
            query['MaxThrottleTime'] = request.max_throttle_time
        if not UtilClient.is_unset(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoThrottleRulesAsync',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            das20200116_models.UpdateAutoThrottleRulesAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_throttle_rules_async(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_throttle_rules_async_with_options(request, runtime)

    async def update_auto_throttle_rules_async_async(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_throttle_rules_async_with_options_async(request, runtime)
