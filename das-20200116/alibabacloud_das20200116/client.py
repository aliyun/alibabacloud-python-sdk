# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_das20200116 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_hdminstance_with_options(
        self,
        request: main_models.AddHDMInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHDMInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.flush_account):
            query['FlushAccount'] = request.flush_account
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddHDMInstance',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHDMInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_hdminstance_with_options_async(
        self,
        request: main_models.AddHDMInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHDMInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.flush_account):
            query['FlushAccount'] = request.flush_account
        if not DaraCore.is_null(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not DaraCore.is_null(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddHDMInstance',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHDMInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_hdminstance(
        self,
        request: main_models.AddHDMInstanceRequest,
    ) -> main_models.AddHDMInstanceResponse:
        runtime = RuntimeOptions()
        return self.add_hdminstance_with_options(request, runtime)

    async def add_hdminstance_async(
        self,
        request: main_models.AddHDMInstanceRequest,
    ) -> main_models.AddHDMInstanceResponse:
        runtime = RuntimeOptions()
        return await self.add_hdminstance_with_options_async(request, runtime)

    def create_cache_analysis_job_with_options(
        self,
        request: main_models.CreateCacheAnalysisJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCacheAnalysisJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.separators):
            query['Separators'] = request.separators
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCacheAnalysisJob',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCacheAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cache_analysis_job_with_options_async(
        self,
        request: main_models.CreateCacheAnalysisJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCacheAnalysisJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.separators):
            query['Separators'] = request.separators
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCacheAnalysisJob',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCacheAnalysisJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cache_analysis_job(
        self,
        request: main_models.CreateCacheAnalysisJobRequest,
    ) -> main_models.CreateCacheAnalysisJobResponse:
        runtime = RuntimeOptions()
        return self.create_cache_analysis_job_with_options(request, runtime)

    async def create_cache_analysis_job_async(
        self,
        request: main_models.CreateCacheAnalysisJobRequest,
    ) -> main_models.CreateCacheAnalysisJobResponse:
        runtime = RuntimeOptions()
        return await self.create_cache_analysis_job_with_options_async(request, runtime)

    def create_cloud_bench_tasks_with_options(
        self,
        request: main_models.CreateCloudBenchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudBenchTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dst_connection_string):
            query['DstConnectionString'] = request.dst_connection_string
        if not DaraCore.is_null(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not DaraCore.is_null(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.dts_job_class):
            query['DtsJobClass'] = request.dts_job_class
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_state):
            query['EndState'] = request.end_state
        if not DaraCore.is_null(request.gateway_vpc_id):
            query['GatewayVpcId'] = request.gateway_vpc_id
        if not DaraCore.is_null(request.gateway_vpc_ip):
            query['GatewayVpcIp'] = request.gateway_vpc_ip
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not DaraCore.is_null(request.request_end_time):
            query['RequestEndTime'] = request.request_end_time
        if not DaraCore.is_null(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not DaraCore.is_null(request.smart_pressure_time):
            query['SmartPressureTime'] = request.smart_pressure_time
        if not DaraCore.is_null(request.src_instance_id):
            query['SrcInstanceId'] = request.src_instance_id
        if not DaraCore.is_null(request.src_public_ip):
            query['SrcPublicIp'] = request.src_public_ip
        if not DaraCore.is_null(request.src_super_account):
            query['SrcSuperAccount'] = request.src_super_account
        if not DaraCore.is_null(request.src_super_password):
            query['SrcSuperPassword'] = request.src_super_password
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.work_dir):
            query['WorkDir'] = request.work_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudBenchTasks',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudBenchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_bench_tasks_with_options_async(
        self,
        request: main_models.CreateCloudBenchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudBenchTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dst_connection_string):
            query['DstConnectionString'] = request.dst_connection_string
        if not DaraCore.is_null(request.dst_instance_id):
            query['DstInstanceId'] = request.dst_instance_id
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.dst_super_account):
            query['DstSuperAccount'] = request.dst_super_account
        if not DaraCore.is_null(request.dst_super_password):
            query['DstSuperPassword'] = request.dst_super_password
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.dts_job_class):
            query['DtsJobClass'] = request.dts_job_class
        if not DaraCore.is_null(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not DaraCore.is_null(request.end_state):
            query['EndState'] = request.end_state
        if not DaraCore.is_null(request.gateway_vpc_id):
            query['GatewayVpcId'] = request.gateway_vpc_id
        if not DaraCore.is_null(request.gateway_vpc_ip):
            query['GatewayVpcIp'] = request.gateway_vpc_ip
        if not DaraCore.is_null(request.rate):
            query['Rate'] = request.rate
        if not DaraCore.is_null(request.request_duration):
            query['RequestDuration'] = request.request_duration
        if not DaraCore.is_null(request.request_end_time):
            query['RequestEndTime'] = request.request_end_time
        if not DaraCore.is_null(request.request_start_time):
            query['RequestStartTime'] = request.request_start_time
        if not DaraCore.is_null(request.smart_pressure_time):
            query['SmartPressureTime'] = request.smart_pressure_time
        if not DaraCore.is_null(request.src_instance_id):
            query['SrcInstanceId'] = request.src_instance_id
        if not DaraCore.is_null(request.src_public_ip):
            query['SrcPublicIp'] = request.src_public_ip
        if not DaraCore.is_null(request.src_super_account):
            query['SrcSuperAccount'] = request.src_super_account
        if not DaraCore.is_null(request.src_super_password):
            query['SrcSuperPassword'] = request.src_super_password
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.work_dir):
            query['WorkDir'] = request.work_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudBenchTasks',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudBenchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_bench_tasks(
        self,
        request: main_models.CreateCloudBenchTasksRequest,
    ) -> main_models.CreateCloudBenchTasksResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_bench_tasks_with_options(request, runtime)

    async def create_cloud_bench_tasks_async(
        self,
        request: main_models.CreateCloudBenchTasksRequest,
    ) -> main_models.CreateCloudBenchTasksResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_bench_tasks_with_options_async(request, runtime)

    def create_diagnostic_report_with_options(
        self,
        request: main_models.CreateDiagnosticReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosticReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnosticReport',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: main_models.CreateDiagnosticReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosticReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnosticReport',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosticReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnostic_report(
        self,
        request: main_models.CreateDiagnosticReportRequest,
    ) -> main_models.CreateDiagnosticReportResponse:
        runtime = RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: main_models.CreateDiagnosticReportRequest,
    ) -> main_models.CreateDiagnosticReportResponse:
        runtime = RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def create_kill_instance_session_task_with_options(
        self,
        request: main_models.CreateKillInstanceSessionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKillInstanceSessionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_user):
            query['DbUser'] = request.db_user
        if not DaraCore.is_null(request.db_user_password):
            query['DbUserPassword'] = request.db_user_password
        if not DaraCore.is_null(request.ignored_users):
            query['IgnoredUsers'] = request.ignored_users
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.kill_all_sessions):
            query['KillAllSessions'] = request.kill_all_sessions
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.session_ids):
            query['SessionIds'] = request.session_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKillInstanceSessionTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKillInstanceSessionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kill_instance_session_task_with_options_async(
        self,
        request: main_models.CreateKillInstanceSessionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKillInstanceSessionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_user):
            query['DbUser'] = request.db_user
        if not DaraCore.is_null(request.db_user_password):
            query['DbUserPassword'] = request.db_user_password
        if not DaraCore.is_null(request.ignored_users):
            query['IgnoredUsers'] = request.ignored_users
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.kill_all_sessions):
            query['KillAllSessions'] = request.kill_all_sessions
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.session_ids):
            query['SessionIds'] = request.session_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKillInstanceSessionTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKillInstanceSessionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kill_instance_session_task(
        self,
        request: main_models.CreateKillInstanceSessionTaskRequest,
    ) -> main_models.CreateKillInstanceSessionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_kill_instance_session_task_with_options(request, runtime)

    async def create_kill_instance_session_task_async(
        self,
        request: main_models.CreateKillInstanceSessionTaskRequest,
    ) -> main_models.CreateKillInstanceSessionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_kill_instance_session_task_with_options_async(request, runtime)

    def create_kill_instance_session_task_with_maintain_user_with_options(
        self,
        request: main_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignored_users):
            query['IgnoredUsers'] = request.ignored_users
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.kill_all_sessions):
            query['KillAllSessions'] = request.kill_all_sessions
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.session_ids):
            query['SessionIds'] = request.session_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKillInstanceSessionTaskWithMaintainUser',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kill_instance_session_task_with_maintain_user_with_options_async(
        self,
        request: main_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ignored_users):
            query['IgnoredUsers'] = request.ignored_users
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.kill_all_sessions):
            query['KillAllSessions'] = request.kill_all_sessions
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.session_ids):
            query['SessionIds'] = request.session_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKillInstanceSessionTaskWithMaintainUser',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kill_instance_session_task_with_maintain_user(
        self,
        request: main_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
    ) -> main_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        runtime = RuntimeOptions()
        return self.create_kill_instance_session_task_with_maintain_user_with_options(request, runtime)

    async def create_kill_instance_session_task_with_maintain_user_async(
        self,
        request: main_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
    ) -> main_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        runtime = RuntimeOptions()
        return await self.create_kill_instance_session_task_with_maintain_user_with_options_async(request, runtime)

    def create_latest_dead_lock_analysis_with_options(
        self,
        request: main_models.CreateLatestDeadLockAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLatestDeadLockAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLatestDeadLockAnalysis',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLatestDeadLockAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_latest_dead_lock_analysis_with_options_async(
        self,
        request: main_models.CreateLatestDeadLockAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLatestDeadLockAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLatestDeadLockAnalysis',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLatestDeadLockAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_latest_dead_lock_analysis(
        self,
        request: main_models.CreateLatestDeadLockAnalysisRequest,
    ) -> main_models.CreateLatestDeadLockAnalysisResponse:
        runtime = RuntimeOptions()
        return self.create_latest_dead_lock_analysis_with_options(request, runtime)

    async def create_latest_dead_lock_analysis_async(
        self,
        request: main_models.CreateLatestDeadLockAnalysisRequest,
    ) -> main_models.CreateLatestDeadLockAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.create_latest_dead_lock_analysis_with_options_async(request, runtime)

    def create_query_optimize_tag_with_options(
        self,
        request: main_models.CreateQueryOptimizeTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueryOptimizeTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_ids):
            query['SqlIds'] = request.sql_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueryOptimizeTag',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueryOptimizeTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_query_optimize_tag_with_options_async(
        self,
        request: main_models.CreateQueryOptimizeTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueryOptimizeTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_ids):
            query['SqlIds'] = request.sql_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueryOptimizeTag',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueryOptimizeTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_query_optimize_tag(
        self,
        request: main_models.CreateQueryOptimizeTagRequest,
    ) -> main_models.CreateQueryOptimizeTagResponse:
        runtime = RuntimeOptions()
        return self.create_query_optimize_tag_with_options(request, runtime)

    async def create_query_optimize_tag_async(
        self,
        request: main_models.CreateQueryOptimizeTagRequest,
    ) -> main_models.CreateQueryOptimizeTagResponse:
        runtime = RuntimeOptions()
        return await self.create_query_optimize_tag_with_options_async(request, runtime)

    def create_request_diagnosis_with_options(
        self,
        request: main_models.CreateRequestDiagnosisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRequestDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRequestDiagnosis',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRequestDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_request_diagnosis_with_options_async(
        self,
        request: main_models.CreateRequestDiagnosisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRequestDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql):
            query['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRequestDiagnosis',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRequestDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_request_diagnosis(
        self,
        request: main_models.CreateRequestDiagnosisRequest,
    ) -> main_models.CreateRequestDiagnosisResponse:
        runtime = RuntimeOptions()
        return self.create_request_diagnosis_with_options(request, runtime)

    async def create_request_diagnosis_async(
        self,
        request: main_models.CreateRequestDiagnosisRequest,
    ) -> main_models.CreateRequestDiagnosisResponse:
        runtime = RuntimeOptions()
        return await self.create_request_diagnosis_with_options_async(request, runtime)

    def create_security_ipgroup_with_options(
        self,
        request: main_models.CreateSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_ipgroup_with_options_async(
        self,
        request: main_models.CreateSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_ipgroup(
        self,
        request: main_models.CreateSecurityIPGroupRequest,
    ) -> main_models.CreateSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.create_security_ipgroup_with_options(request, runtime)

    async def create_security_ipgroup_async(
        self,
        request: main_models.CreateSecurityIPGroupRequest,
    ) -> main_models.CreateSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_security_ipgroup_with_options_async(request, runtime)

    def create_sql_log_task_with_options(
        self,
        request: main_models.CreateSqlLogTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlLogTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlLogTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSqlLogTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sql_log_task_with_options_async(
        self,
        request: main_models.CreateSqlLogTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlLogTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlLogTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSqlLogTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sql_log_task(
        self,
        request: main_models.CreateSqlLogTaskRequest,
    ) -> main_models.CreateSqlLogTaskResponse:
        runtime = RuntimeOptions()
        return self.create_sql_log_task_with_options(request, runtime)

    async def create_sql_log_task_async(
        self,
        request: main_models.CreateSqlLogTaskRequest,
    ) -> main_models.CreateSqlLogTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_sql_log_task_with_options_async(request, runtime)

    def create_storage_analysis_task_with_options(
        self,
        request: main_models.CreateStorageAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStorageAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStorageAnalysisTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStorageAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_analysis_task_with_options_async(
        self,
        request: main_models.CreateStorageAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStorageAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStorageAnalysisTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStorageAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_analysis_task(
        self,
        request: main_models.CreateStorageAnalysisTaskRequest,
    ) -> main_models.CreateStorageAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.create_storage_analysis_task_with_options(request, runtime)

    async def create_storage_analysis_task_async(
        self,
        request: main_models.CreateStorageAnalysisTaskRequest,
    ) -> main_models.CreateStorageAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_storage_analysis_task_with_options_async(request, runtime)

    def delete_cloud_bench_task_with_options(
        self,
        request: main_models.DeleteCloudBenchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudBenchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudBenchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_bench_task_with_options_async(
        self,
        request: main_models.DeleteCloudBenchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudBenchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudBenchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudBenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_bench_task(
        self,
        request: main_models.DeleteCloudBenchTaskRequest,
    ) -> main_models.DeleteCloudBenchTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_bench_task_with_options(request, runtime)

    async def delete_cloud_bench_task_async(
        self,
        request: main_models.DeleteCloudBenchTaskRequest,
    ) -> main_models.DeleteCloudBenchTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_bench_task_with_options_async(request, runtime)

    def delete_security_ipgroup_with_options(
        self,
        request: main_models.DeleteSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_ipgroup_with_options_async(
        self,
        request: main_models.DeleteSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_ipgroup(
        self,
        request: main_models.DeleteSecurityIPGroupRequest,
    ) -> main_models.DeleteSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_security_ipgroup_with_options(request, runtime)

    async def delete_security_ipgroup_async(
        self,
        request: main_models.DeleteSecurityIPGroupRequest,
    ) -> main_models.DeleteSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_ipgroup_with_options_async(request, runtime)

    def delete_stop_gateway_with_options(
        self,
        request: main_models.DeleteStopGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStopGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStopGateway',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStopGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stop_gateway_with_options_async(
        self,
        request: main_models.DeleteStopGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStopGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStopGateway',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStopGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stop_gateway(
        self,
        request: main_models.DeleteStopGatewayRequest,
    ) -> main_models.DeleteStopGatewayResponse:
        runtime = RuntimeOptions()
        return self.delete_stop_gateway_with_options(request, runtime)

    async def delete_stop_gateway_async(
        self,
        request: main_models.DeleteStopGatewayRequest,
    ) -> main_models.DeleteStopGatewayResponse:
        runtime = RuntimeOptions()
        return await self.delete_stop_gateway_with_options_async(request, runtime)

    def describe_auto_scaling_config_with_options(
        self,
        request: main_models.DescribeAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoScalingConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_scaling_config_with_options_async(
        self,
        request: main_models.DescribeAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoScalingConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_scaling_config(
        self,
        request: main_models.DescribeAutoScalingConfigRequest,
    ) -> main_models.DescribeAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_scaling_config_with_options(request, runtime)

    async def describe_auto_scaling_config_async(
        self,
        request: main_models.DescribeAutoScalingConfigRequest,
    ) -> main_models.DescribeAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_scaling_config_with_options_async(request, runtime)

    def describe_auto_scaling_history_with_options(
        self,
        request: main_models.DescribeAutoScalingHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoScalingHistoryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoScalingHistory',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoScalingHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_scaling_history_with_options_async(
        self,
        request: main_models.DescribeAutoScalingHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoScalingHistoryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoScalingHistory',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoScalingHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_scaling_history(
        self,
        request: main_models.DescribeAutoScalingHistoryRequest,
    ) -> main_models.DescribeAutoScalingHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_scaling_history_with_options(request, runtime)

    async def describe_auto_scaling_history_async(
        self,
        request: main_models.DescribeAutoScalingHistoryRequest,
    ) -> main_models.DescribeAutoScalingHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_scaling_history_with_options_async(request, runtime)

    def describe_cache_analysis_job_with_options(
        self,
        request: main_models.DescribeCacheAnalysisJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCacheAnalysisJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCacheAnalysisJob',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCacheAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_job_with_options_async(
        self,
        request: main_models.DescribeCacheAnalysisJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCacheAnalysisJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCacheAnalysisJob',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCacheAnalysisJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cache_analysis_job(
        self,
        request: main_models.DescribeCacheAnalysisJobRequest,
    ) -> main_models.DescribeCacheAnalysisJobResponse:
        runtime = RuntimeOptions()
        return self.describe_cache_analysis_job_with_options(request, runtime)

    async def describe_cache_analysis_job_async(
        self,
        request: main_models.DescribeCacheAnalysisJobRequest,
    ) -> main_models.DescribeCacheAnalysisJobResponse:
        runtime = RuntimeOptions()
        return await self.describe_cache_analysis_job_with_options_async(request, runtime)

    def describe_cache_analysis_jobs_with_options(
        self,
        request: main_models.DescribeCacheAnalysisJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCacheAnalysisJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCacheAnalysisJobs',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCacheAnalysisJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cache_analysis_jobs_with_options_async(
        self,
        request: main_models.DescribeCacheAnalysisJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCacheAnalysisJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCacheAnalysisJobs',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCacheAnalysisJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cache_analysis_jobs(
        self,
        request: main_models.DescribeCacheAnalysisJobsRequest,
    ) -> main_models.DescribeCacheAnalysisJobsResponse:
        runtime = RuntimeOptions()
        return self.describe_cache_analysis_jobs_with_options(request, runtime)

    async def describe_cache_analysis_jobs_async(
        self,
        request: main_models.DescribeCacheAnalysisJobsRequest,
    ) -> main_models.DescribeCacheAnalysisJobsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cache_analysis_jobs_with_options_async(request, runtime)

    def describe_cloud_bench_tasks_with_options(
        self,
        request: main_models.DescribeCloudBenchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudBenchTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudBenchTasks',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudBenchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_bench_tasks_with_options_async(
        self,
        request: main_models.DescribeCloudBenchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudBenchTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudBenchTasks',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudBenchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_bench_tasks(
        self,
        request: main_models.DescribeCloudBenchTasksRequest,
    ) -> main_models.DescribeCloudBenchTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_bench_tasks_with_options(request, runtime)

    async def describe_cloud_bench_tasks_async(
        self,
        request: main_models.DescribeCloudBenchTasksRequest,
    ) -> main_models.DescribeCloudBenchTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_bench_tasks_with_options_async(request, runtime)

    def describe_cloudbench_task_with_options(
        self,
        request: main_models.DescribeCloudbenchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudbenchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudbenchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudbenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloudbench_task_with_options_async(
        self,
        request: main_models.DescribeCloudbenchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudbenchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudbenchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudbenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloudbench_task(
        self,
        request: main_models.DescribeCloudbenchTaskRequest,
    ) -> main_models.DescribeCloudbenchTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_cloudbench_task_with_options(request, runtime)

    async def describe_cloudbench_task_async(
        self,
        request: main_models.DescribeCloudbenchTaskRequest,
    ) -> main_models.DescribeCloudbenchTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloudbench_task_with_options_async(request, runtime)

    def describe_cloudbench_task_config_with_options(
        self,
        request: main_models.DescribeCloudbenchTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudbenchTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudbenchTaskConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudbenchTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloudbench_task_config_with_options_async(
        self,
        request: main_models.DescribeCloudbenchTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudbenchTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudbenchTaskConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudbenchTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloudbench_task_config(
        self,
        request: main_models.DescribeCloudbenchTaskConfigRequest,
    ) -> main_models.DescribeCloudbenchTaskConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_cloudbench_task_config_with_options(request, runtime)

    async def describe_cloudbench_task_config_async(
        self,
        request: main_models.DescribeCloudbenchTaskConfigRequest,
    ) -> main_models.DescribeCloudbenchTaskConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloudbench_task_config_with_options_async(request, runtime)

    def describe_diagnostic_report_list_with_options(
        self,
        request: main_models.DescribeDiagnosticReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosticReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosticReportList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosticReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: main_models.DescribeDiagnosticReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosticReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosticReportList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosticReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnostic_report_list(
        self,
        request: main_models.DescribeDiagnosticReportListRequest,
    ) -> main_models.DescribeDiagnosticReportListResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    async def describe_diagnostic_report_list_async(
        self,
        request: main_models.DescribeDiagnosticReportListRequest,
    ) -> main_models.DescribeDiagnosticReportListResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnostic_report_list_with_options_async(request, runtime)

    def describe_error_log_records_with_options(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeErrorLogRecords',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeErrorLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_error_log_records_with_options_async(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeErrorLogRecords',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeErrorLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_error_log_records(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_error_log_records_with_options(request, runtime)

    async def describe_error_log_records_async(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_error_log_records_with_options_async(request, runtime)

    def describe_hot_big_keys_with_options(
        self,
        request: main_models.DescribeHotBigKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHotBigKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHotBigKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHotBigKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hot_big_keys_with_options_async(
        self,
        request: main_models.DescribeHotBigKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHotBigKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHotBigKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHotBigKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hot_big_keys(
        self,
        request: main_models.DescribeHotBigKeysRequest,
    ) -> main_models.DescribeHotBigKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_hot_big_keys_with_options(request, runtime)

    async def describe_hot_big_keys_async(
        self,
        request: main_models.DescribeHotBigKeysRequest,
    ) -> main_models.DescribeHotBigKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_hot_big_keys_with_options_async(request, runtime)

    def describe_hot_keys_with_options(
        self,
        request: main_models.DescribeHotKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHotKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHotKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHotKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hot_keys_with_options_async(
        self,
        request: main_models.DescribeHotKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHotKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHotKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHotKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hot_keys(
        self,
        request: main_models.DescribeHotKeysRequest,
    ) -> main_models.DescribeHotKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_hot_keys_with_options(request, runtime)

    async def describe_hot_keys_async(
        self,
        request: main_models.DescribeHotKeysRequest,
    ) -> main_models.DescribeHotKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_hot_keys_with_options_async(request, runtime)

    def describe_instance_das_pro_with_options(
        self,
        request: main_models.DescribeInstanceDasProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDasProResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDasPro',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDasProResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_das_pro_with_options_async(
        self,
        request: main_models.DescribeInstanceDasProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDasProResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDasPro',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDasProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_das_pro(
        self,
        request: main_models.DescribeInstanceDasProRequest,
    ) -> main_models.DescribeInstanceDasProResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_das_pro_with_options(request, runtime)

    async def describe_instance_das_pro_async(
        self,
        request: main_models.DescribeInstanceDasProRequest,
    ) -> main_models.DescribeInstanceDasProResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_das_pro_with_options_async(request, runtime)

    def describe_query_explain_with_options(
        self,
        request: main_models.DescribeQueryExplainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryExplainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.schema):
            body['Schema'] = request.schema
        if not DaraCore.is_null(request.sql):
            body['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryExplain',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryExplainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_query_explain_with_options_async(
        self,
        request: main_models.DescribeQueryExplainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryExplainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.db_name):
            body['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.schema):
            body['Schema'] = request.schema
        if not DaraCore.is_null(request.sql):
            body['Sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryExplain',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryExplainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_query_explain(
        self,
        request: main_models.DescribeQueryExplainRequest,
    ) -> main_models.DescribeQueryExplainResponse:
        runtime = RuntimeOptions()
        return self.describe_query_explain_with_options(request, runtime)

    async def describe_query_explain_async(
        self,
        request: main_models.DescribeQueryExplainRequest,
    ) -> main_models.DescribeQueryExplainResponse:
        runtime = RuntimeOptions()
        return await self.describe_query_explain_with_options_async(request, runtime)

    def describe_security_ipgroup_with_options(
        self,
        request: main_models.DescribeSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ipgroup_with_options_async(
        self,
        request: main_models.DescribeSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ipgroup(
        self,
        request: main_models.DescribeSecurityIPGroupRequest,
    ) -> main_models.DescribeSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_security_ipgroup_with_options(request, runtime)

    async def describe_security_ipgroup_async(
        self,
        request: main_models.DescribeSecurityIPGroupRequest,
    ) -> main_models.DescribeSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_ipgroup_with_options_async(request, runtime)

    def describe_security_ipgroup_relation_with_options(
        self,
        request: main_models.DescribeSecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIPGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIPGroupRelation',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ipgroup_relation_with_options_async(
        self,
        request: main_models.DescribeSecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIPGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIPGroupRelation',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ipgroup_relation(
        self,
        request: main_models.DescribeSecurityIPGroupRelationRequest,
    ) -> main_models.DescribeSecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.describe_security_ipgroup_relation_with_options(request, runtime)

    async def describe_security_ipgroup_relation_async(
        self,
        request: main_models.DescribeSecurityIPGroupRelationRequest,
    ) -> main_models.DescribeSecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_ipgroup_relation_with_options_async(request, runtime)

    def describe_slow_log_histogram_async_with_options(
        self,
        request: main_models.DescribeSlowLogHistogramAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogHistogramAsyncResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogHistogramAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogHistogramAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_histogram_async_with_options_async(
        self,
        request: main_models.DescribeSlowLogHistogramAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogHistogramAsyncResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogHistogramAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogHistogramAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_histogram_async(
        self,
        request: main_models.DescribeSlowLogHistogramAsyncRequest,
    ) -> main_models.DescribeSlowLogHistogramAsyncResponse:
        runtime = RuntimeOptions()
        return self.describe_slow_log_histogram_async_with_options(request, runtime)

    async def describe_slow_log_histogram_async_async(
        self,
        request: main_models.DescribeSlowLogHistogramAsyncRequest,
    ) -> main_models.DescribeSlowLogHistogramAsyncResponse:
        runtime = RuntimeOptions()
        return await self.describe_slow_log_histogram_async_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_log_statistic_with_options(
        self,
        request: main_models.DescribeSlowLogStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogStatisticResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asc):
            body['Asc'] = request.asc
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_statistic_with_options_async(
        self,
        request: main_models.DescribeSlowLogStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogStatisticResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asc):
            body['Asc'] = request.asc
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_statistic(
        self,
        request: main_models.DescribeSlowLogStatisticRequest,
    ) -> main_models.DescribeSlowLogStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_slow_log_statistic_with_options(request, runtime)

    async def describe_slow_log_statistic_async(
        self,
        request: main_models.DescribeSlowLogStatisticRequest,
    ) -> main_models.DescribeSlowLogStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_slow_log_statistic_with_options_async(request, runtime)

    def describe_sql_log_config_with_options(
        self,
        request: main_models.DescribeSqlLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_log_config_with_options_async(
        self,
        request: main_models.DescribeSqlLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_log_config(
        self,
        request: main_models.DescribeSqlLogConfigRequest,
    ) -> main_models.DescribeSqlLogConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_log_config_with_options(request, runtime)

    async def describe_sql_log_config_async(
        self,
        request: main_models.DescribeSqlLogConfigRequest,
    ) -> main_models.DescribeSqlLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_log_config_with_options_async(request, runtime)

    def describe_sql_log_records_with_options(
        self,
        request: main_models.DescribeSqlLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogRecords',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_log_records_with_options_async(
        self,
        request: main_models.DescribeSqlLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogRecords',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_log_records(
        self,
        request: main_models.DescribeSqlLogRecordsRequest,
    ) -> main_models.DescribeSqlLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_log_records_with_options(request, runtime)

    async def describe_sql_log_records_async(
        self,
        request: main_models.DescribeSqlLogRecordsRequest,
    ) -> main_models.DescribeSqlLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_log_records_with_options_async(request, runtime)

    def describe_sql_log_statistic_with_options(
        self,
        request: main_models.DescribeSqlLogStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogStatisticResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_log_statistic_with_options_async(
        self,
        request: main_models.DescribeSqlLogStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogStatisticResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_log_statistic(
        self,
        request: main_models.DescribeSqlLogStatisticRequest,
    ) -> main_models.DescribeSqlLogStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_log_statistic_with_options(request, runtime)

    async def describe_sql_log_statistic_async(
        self,
        request: main_models.DescribeSqlLogStatisticRequest,
    ) -> main_models.DescribeSqlLogStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_log_statistic_with_options_async(request, runtime)

    def describe_sql_log_task_with_options(
        self,
        request: main_models.DescribeSqlLogTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_log_task_with_options_async(
        self,
        request: main_models.DescribeSqlLogTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_log_task(
        self,
        request: main_models.DescribeSqlLogTaskRequest,
    ) -> main_models.DescribeSqlLogTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_log_task_with_options(request, runtime)

    async def describe_sql_log_task_async(
        self,
        request: main_models.DescribeSqlLogTaskRequest,
    ) -> main_models.DescribeSqlLogTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_log_task_with_options_async(request, runtime)

    def describe_sql_log_tasks_with_options(
        self,
        request: main_models.DescribeSqlLogTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogTasks',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_log_tasks_with_options_async(
        self,
        request: main_models.DescribeSqlLogTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlLogTasksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlLogTasks',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlLogTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_log_tasks(
        self,
        request: main_models.DescribeSqlLogTasksRequest,
    ) -> main_models.DescribeSqlLogTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_log_tasks_with_options(request, runtime)

    async def describe_sql_log_tasks_async(
        self,
        request: main_models.DescribeSqlLogTasksRequest,
    ) -> main_models.DescribeSqlLogTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_log_tasks_with_options_async(request, runtime)

    def describe_top_big_keys_with_options(
        self,
        request: main_models.DescribeTopBigKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopBigKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTopBigKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopBigKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_big_keys_with_options_async(
        self,
        request: main_models.DescribeTopBigKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopBigKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTopBigKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopBigKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_big_keys(
        self,
        request: main_models.DescribeTopBigKeysRequest,
    ) -> main_models.DescribeTopBigKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_top_big_keys_with_options(request, runtime)

    async def describe_top_big_keys_async(
        self,
        request: main_models.DescribeTopBigKeysRequest,
    ) -> main_models.DescribeTopBigKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_top_big_keys_with_options_async(request, runtime)

    def describe_top_hot_keys_with_options(
        self,
        request: main_models.DescribeTopHotKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopHotKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTopHotKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopHotKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_hot_keys_with_options_async(
        self,
        request: main_models.DescribeTopHotKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTopHotKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTopHotKeys',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTopHotKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_hot_keys(
        self,
        request: main_models.DescribeTopHotKeysRequest,
    ) -> main_models.DescribeTopHotKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_top_hot_keys_with_options(request, runtime)

    async def describe_top_hot_keys_async(
        self,
        request: main_models.DescribeTopHotKeysRequest,
    ) -> main_models.DescribeTopHotKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_top_hot_keys_with_options_async(request, runtime)

    def disable_all_sql_concurrency_control_rules_with_options(
        self,
        request: main_models.DisableAllSqlConcurrencyControlRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAllSqlConcurrencyControlRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAllSqlConcurrencyControlRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAllSqlConcurrencyControlRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_all_sql_concurrency_control_rules_with_options_async(
        self,
        request: main_models.DisableAllSqlConcurrencyControlRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAllSqlConcurrencyControlRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAllSqlConcurrencyControlRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAllSqlConcurrencyControlRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_all_sql_concurrency_control_rules(
        self,
        request: main_models.DisableAllSqlConcurrencyControlRulesRequest,
    ) -> main_models.DisableAllSqlConcurrencyControlRulesResponse:
        runtime = RuntimeOptions()
        return self.disable_all_sql_concurrency_control_rules_with_options(request, runtime)

    async def disable_all_sql_concurrency_control_rules_async(
        self,
        request: main_models.DisableAllSqlConcurrencyControlRulesRequest,
    ) -> main_models.DisableAllSqlConcurrencyControlRulesResponse:
        runtime = RuntimeOptions()
        return await self.disable_all_sql_concurrency_control_rules_with_options_async(request, runtime)

    def disable_auto_resource_optimize_rules_with_options(
        self,
        request: main_models.DisableAutoResourceOptimizeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoResourceOptimizeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAutoResourceOptimizeRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoResourceOptimizeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_resource_optimize_rules_with_options_async(
        self,
        request: main_models.DisableAutoResourceOptimizeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoResourceOptimizeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAutoResourceOptimizeRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoResourceOptimizeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_resource_optimize_rules(
        self,
        request: main_models.DisableAutoResourceOptimizeRulesRequest,
    ) -> main_models.DisableAutoResourceOptimizeRulesResponse:
        runtime = RuntimeOptions()
        return self.disable_auto_resource_optimize_rules_with_options(request, runtime)

    async def disable_auto_resource_optimize_rules_async(
        self,
        request: main_models.DisableAutoResourceOptimizeRulesRequest,
    ) -> main_models.DisableAutoResourceOptimizeRulesResponse:
        runtime = RuntimeOptions()
        return await self.disable_auto_resource_optimize_rules_with_options_async(request, runtime)

    def disable_auto_throttle_rules_with_options(
        self,
        request: main_models.DisableAutoThrottleRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoThrottleRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAutoThrottleRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoThrottleRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_throttle_rules_with_options_async(
        self,
        request: main_models.DisableAutoThrottleRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoThrottleRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAutoThrottleRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoThrottleRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_throttle_rules(
        self,
        request: main_models.DisableAutoThrottleRulesRequest,
    ) -> main_models.DisableAutoThrottleRulesResponse:
        runtime = RuntimeOptions()
        return self.disable_auto_throttle_rules_with_options(request, runtime)

    async def disable_auto_throttle_rules_async(
        self,
        request: main_models.DisableAutoThrottleRulesRequest,
    ) -> main_models.DisableAutoThrottleRulesResponse:
        runtime = RuntimeOptions()
        return await self.disable_auto_throttle_rules_with_options_async(request, runtime)

    def disable_das_pro_with_options(
        self,
        request: main_models.DisableDasProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDasProResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDasPro',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDasProResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_das_pro_with_options_async(
        self,
        request: main_models.DisableDasProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDasProResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDasPro',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDasProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_das_pro(
        self,
        request: main_models.DisableDasProRequest,
    ) -> main_models.DisableDasProResponse:
        runtime = RuntimeOptions()
        return self.disable_das_pro_with_options(request, runtime)

    async def disable_das_pro_async(
        self,
        request: main_models.DisableDasProRequest,
    ) -> main_models.DisableDasProResponse:
        runtime = RuntimeOptions()
        return await self.disable_das_pro_with_options_async(request, runtime)

    def disable_instance_das_config_with_options(
        self,
        request: main_models.DisableInstanceDasConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstanceDasConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstanceDasConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstanceDasConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_instance_das_config_with_options_async(
        self,
        request: main_models.DisableInstanceDasConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstanceDasConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstanceDasConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstanceDasConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_instance_das_config(
        self,
        request: main_models.DisableInstanceDasConfigRequest,
    ) -> main_models.DisableInstanceDasConfigResponse:
        runtime = RuntimeOptions()
        return self.disable_instance_das_config_with_options(request, runtime)

    async def disable_instance_das_config_async(
        self,
        request: main_models.DisableInstanceDasConfigRequest,
    ) -> main_models.DisableInstanceDasConfigResponse:
        runtime = RuntimeOptions()
        return await self.disable_instance_das_config_with_options_async(request, runtime)

    def disable_sql_concurrency_control_with_options(
        self,
        request: main_models.DisableSqlConcurrencyControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSqlConcurrencyControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSqlConcurrencyControl',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSqlConcurrencyControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sql_concurrency_control_with_options_async(
        self,
        request: main_models.DisableSqlConcurrencyControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSqlConcurrencyControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id):
            query['ItemId'] = request.item_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSqlConcurrencyControl',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSqlConcurrencyControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_sql_concurrency_control(
        self,
        request: main_models.DisableSqlConcurrencyControlRequest,
    ) -> main_models.DisableSqlConcurrencyControlResponse:
        runtime = RuntimeOptions()
        return self.disable_sql_concurrency_control_with_options(request, runtime)

    async def disable_sql_concurrency_control_async(
        self,
        request: main_models.DisableSqlConcurrencyControlRequest,
    ) -> main_models.DisableSqlConcurrencyControlResponse:
        runtime = RuntimeOptions()
        return await self.disable_sql_concurrency_control_with_options_async(request, runtime)

    def enable_das_pro_with_options(
        self,
        request: main_models.EnableDasProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDasProResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_retention):
            query['SqlRetention'] = request.sql_retention
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDasPro',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDasProResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_das_pro_with_options_async(
        self,
        request: main_models.EnableDasProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDasProResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_retention):
            query['SqlRetention'] = request.sql_retention
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDasPro',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDasProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_das_pro(
        self,
        request: main_models.EnableDasProRequest,
    ) -> main_models.EnableDasProResponse:
        runtime = RuntimeOptions()
        return self.enable_das_pro_with_options(request, runtime)

    async def enable_das_pro_async(
        self,
        request: main_models.EnableDasProRequest,
    ) -> main_models.EnableDasProResponse:
        runtime = RuntimeOptions()
        return await self.enable_das_pro_with_options_async(request, runtime)

    def enable_sql_concurrency_control_with_options(
        self,
        request: main_models.EnableSqlConcurrencyControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSqlConcurrencyControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.concurrency_control_time):
            query['ConcurrencyControlTime'] = request.concurrency_control_time
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.sql_keywords):
            query['SqlKeywords'] = request.sql_keywords
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSqlConcurrencyControl',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSqlConcurrencyControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sql_concurrency_control_with_options_async(
        self,
        request: main_models.EnableSqlConcurrencyControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSqlConcurrencyControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.concurrency_control_time):
            query['ConcurrencyControlTime'] = request.concurrency_control_time
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not DaraCore.is_null(request.sql_keywords):
            query['SqlKeywords'] = request.sql_keywords
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSqlConcurrencyControl',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSqlConcurrencyControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sql_concurrency_control(
        self,
        request: main_models.EnableSqlConcurrencyControlRequest,
    ) -> main_models.EnableSqlConcurrencyControlResponse:
        runtime = RuntimeOptions()
        return self.enable_sql_concurrency_control_with_options(request, runtime)

    async def enable_sql_concurrency_control_async(
        self,
        request: main_models.EnableSqlConcurrencyControlRequest,
    ) -> main_models.EnableSqlConcurrencyControlResponse:
        runtime = RuntimeOptions()
        return await self.enable_sql_concurrency_control_with_options_async(request, runtime)

    def get_async_error_request_list_by_code_with_options(
        self,
        request: main_models.GetAsyncErrorRequestListByCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncErrorRequestListByCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.error_code):
            query['ErrorCode'] = request.error_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncErrorRequestListByCode',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncErrorRequestListByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_error_request_list_by_code_with_options_async(
        self,
        request: main_models.GetAsyncErrorRequestListByCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncErrorRequestListByCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.error_code):
            query['ErrorCode'] = request.error_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncErrorRequestListByCode',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncErrorRequestListByCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_error_request_list_by_code(
        self,
        request: main_models.GetAsyncErrorRequestListByCodeRequest,
    ) -> main_models.GetAsyncErrorRequestListByCodeResponse:
        runtime = RuntimeOptions()
        return self.get_async_error_request_list_by_code_with_options(request, runtime)

    async def get_async_error_request_list_by_code_async(
        self,
        request: main_models.GetAsyncErrorRequestListByCodeRequest,
    ) -> main_models.GetAsyncErrorRequestListByCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_async_error_request_list_by_code_with_options_async(request, runtime)

    def get_async_error_request_stat_by_code_with_options(
        self,
        request: main_models.GetAsyncErrorRequestStatByCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncErrorRequestStatByCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncErrorRequestStatByCode',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncErrorRequestStatByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_error_request_stat_by_code_with_options_async(
        self,
        request: main_models.GetAsyncErrorRequestStatByCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncErrorRequestStatByCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncErrorRequestStatByCode',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncErrorRequestStatByCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_error_request_stat_by_code(
        self,
        request: main_models.GetAsyncErrorRequestStatByCodeRequest,
    ) -> main_models.GetAsyncErrorRequestStatByCodeResponse:
        runtime = RuntimeOptions()
        return self.get_async_error_request_stat_by_code_with_options(request, runtime)

    async def get_async_error_request_stat_by_code_async(
        self,
        request: main_models.GetAsyncErrorRequestStatByCodeRequest,
    ) -> main_models.GetAsyncErrorRequestStatByCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_async_error_request_stat_by_code_with_options_async(request, runtime)

    def get_async_error_request_stat_result_with_options(
        self,
        request: main_models.GetAsyncErrorRequestStatResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncErrorRequestStatResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql_id_list):
            query['SqlIdList'] = request.sql_id_list
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncErrorRequestStatResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncErrorRequestStatResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_error_request_stat_result_with_options_async(
        self,
        request: main_models.GetAsyncErrorRequestStatResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncErrorRequestStatResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql_id_list):
            query['SqlIdList'] = request.sql_id_list
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncErrorRequestStatResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncErrorRequestStatResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_error_request_stat_result(
        self,
        request: main_models.GetAsyncErrorRequestStatResultRequest,
    ) -> main_models.GetAsyncErrorRequestStatResultResponse:
        runtime = RuntimeOptions()
        return self.get_async_error_request_stat_result_with_options(request, runtime)

    async def get_async_error_request_stat_result_async(
        self,
        request: main_models.GetAsyncErrorRequestStatResultRequest,
    ) -> main_models.GetAsyncErrorRequestStatResultResponse:
        runtime = RuntimeOptions()
        return await self.get_async_error_request_stat_result_with_options_async(request, runtime)

    def get_auto_increment_usage_statistic_with_options(
        self,
        request: main_models.GetAutoIncrementUsageStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoIncrementUsageStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_names):
            query['DbNames'] = request.db_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ratio_filter):
            query['RatioFilter'] = request.ratio_filter
        if not DaraCore.is_null(request.real_time):
            query['RealTime'] = request.real_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoIncrementUsageStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoIncrementUsageStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_increment_usage_statistic_with_options_async(
        self,
        request: main_models.GetAutoIncrementUsageStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoIncrementUsageStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_names):
            query['DbNames'] = request.db_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ratio_filter):
            query['RatioFilter'] = request.ratio_filter
        if not DaraCore.is_null(request.real_time):
            query['RealTime'] = request.real_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoIncrementUsageStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoIncrementUsageStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_increment_usage_statistic(
        self,
        request: main_models.GetAutoIncrementUsageStatisticRequest,
    ) -> main_models.GetAutoIncrementUsageStatisticResponse:
        runtime = RuntimeOptions()
        return self.get_auto_increment_usage_statistic_with_options(request, runtime)

    async def get_auto_increment_usage_statistic_async(
        self,
        request: main_models.GetAutoIncrementUsageStatisticRequest,
    ) -> main_models.GetAutoIncrementUsageStatisticResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_increment_usage_statistic_with_options_async(request, runtime)

    def get_auto_resource_optimize_rules_with_options(
        self,
        request: main_models.GetAutoResourceOptimizeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoResourceOptimizeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoResourceOptimizeRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoResourceOptimizeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_resource_optimize_rules_with_options_async(
        self,
        request: main_models.GetAutoResourceOptimizeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoResourceOptimizeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoResourceOptimizeRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoResourceOptimizeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_resource_optimize_rules(
        self,
        request: main_models.GetAutoResourceOptimizeRulesRequest,
    ) -> main_models.GetAutoResourceOptimizeRulesResponse:
        runtime = RuntimeOptions()
        return self.get_auto_resource_optimize_rules_with_options(request, runtime)

    async def get_auto_resource_optimize_rules_async(
        self,
        request: main_models.GetAutoResourceOptimizeRulesRequest,
    ) -> main_models.GetAutoResourceOptimizeRulesResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_resource_optimize_rules_with_options_async(request, runtime)

    def get_auto_throttle_rules_with_options(
        self,
        request: main_models.GetAutoThrottleRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoThrottleRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoThrottleRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoThrottleRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_throttle_rules_with_options_async(
        self,
        request: main_models.GetAutoThrottleRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoThrottleRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoThrottleRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoThrottleRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_throttle_rules(
        self,
        request: main_models.GetAutoThrottleRulesRequest,
    ) -> main_models.GetAutoThrottleRulesResponse:
        runtime = RuntimeOptions()
        return self.get_auto_throttle_rules_with_options(request, runtime)

    async def get_auto_throttle_rules_async(
        self,
        request: main_models.GetAutoThrottleRulesRequest,
    ) -> main_models.GetAutoThrottleRulesResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_throttle_rules_with_options_async(request, runtime)

    def get_autonomous_notify_event_content_with_options(
        self,
        request: main_models.GetAutonomousNotifyEventContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutonomousNotifyEventContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.span_id):
            query['SpanId'] = request.span_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutonomousNotifyEventContent',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutonomousNotifyEventContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_autonomous_notify_event_content_with_options_async(
        self,
        request: main_models.GetAutonomousNotifyEventContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutonomousNotifyEventContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.span_id):
            query['SpanId'] = request.span_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutonomousNotifyEventContent',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutonomousNotifyEventContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_autonomous_notify_event_content(
        self,
        request: main_models.GetAutonomousNotifyEventContentRequest,
    ) -> main_models.GetAutonomousNotifyEventContentResponse:
        runtime = RuntimeOptions()
        return self.get_autonomous_notify_event_content_with_options(request, runtime)

    async def get_autonomous_notify_event_content_async(
        self,
        request: main_models.GetAutonomousNotifyEventContentRequest,
    ) -> main_models.GetAutonomousNotifyEventContentResponse:
        runtime = RuntimeOptions()
        return await self.get_autonomous_notify_event_content_with_options_async(request, runtime)

    def get_autonomous_notify_events_in_range_with_options(
        self,
        request: main_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutonomousNotifyEventsInRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_context):
            query['EventContext'] = request.event_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.min_level):
            query['MinLevel'] = request.min_level
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_offset):
            query['PageOffset'] = request.page_offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutonomousNotifyEventsInRange',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutonomousNotifyEventsInRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_autonomous_notify_events_in_range_with_options_async(
        self,
        request: main_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutonomousNotifyEventsInRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_context):
            query['EventContext'] = request.event_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.min_level):
            query['MinLevel'] = request.min_level
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_offset):
            query['PageOffset'] = request.page_offset
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutonomousNotifyEventsInRange',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutonomousNotifyEventsInRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_autonomous_notify_events_in_range(
        self,
        request: main_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> main_models.GetAutonomousNotifyEventsInRangeResponse:
        runtime = RuntimeOptions()
        return self.get_autonomous_notify_events_in_range_with_options(request, runtime)

    async def get_autonomous_notify_events_in_range_async(
        self,
        request: main_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> main_models.GetAutonomousNotifyEventsInRangeResponse:
        runtime = RuntimeOptions()
        return await self.get_autonomous_notify_events_in_range_with_options_async(request, runtime)

    def get_blocking_detail_list_with_options(
        self,
        request: main_models.GetBlockingDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBlockingDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name_list):
            query['DbNameList'] = request.db_name_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_hash):
            query['QueryHash'] = request.query_hash
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBlockingDetailList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBlockingDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_blocking_detail_list_with_options_async(
        self,
        request: main_models.GetBlockingDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBlockingDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name_list):
            query['DbNameList'] = request.db_name_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_hash):
            query['QueryHash'] = request.query_hash
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBlockingDetailList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBlockingDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_blocking_detail_list(
        self,
        request: main_models.GetBlockingDetailListRequest,
    ) -> main_models.GetBlockingDetailListResponse:
        runtime = RuntimeOptions()
        return self.get_blocking_detail_list_with_options(request, runtime)

    async def get_blocking_detail_list_async(
        self,
        request: main_models.GetBlockingDetailListRequest,
    ) -> main_models.GetBlockingDetailListResponse:
        runtime = RuntimeOptions()
        return await self.get_blocking_detail_list_with_options_async(request, runtime)

    def get_dbinstance_connectivity_diagnosis_with_options(
        self,
        request: main_models.GetDBInstanceConnectivityDiagnosisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDBInstanceConnectivityDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDBInstanceConnectivityDiagnosis',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDBInstanceConnectivityDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dbinstance_connectivity_diagnosis_with_options_async(
        self,
        request: main_models.GetDBInstanceConnectivityDiagnosisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDBInstanceConnectivityDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDBInstanceConnectivityDiagnosis',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDBInstanceConnectivityDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dbinstance_connectivity_diagnosis(
        self,
        request: main_models.GetDBInstanceConnectivityDiagnosisRequest,
    ) -> main_models.GetDBInstanceConnectivityDiagnosisResponse:
        runtime = RuntimeOptions()
        return self.get_dbinstance_connectivity_diagnosis_with_options(request, runtime)

    async def get_dbinstance_connectivity_diagnosis_async(
        self,
        request: main_models.GetDBInstanceConnectivityDiagnosisRequest,
    ) -> main_models.GetDBInstanceConnectivityDiagnosisResponse:
        runtime = RuntimeOptions()
        return await self.get_dbinstance_connectivity_diagnosis_with_options_async(request, runtime)

    def get_das_agent_ssewith_sse(
        self,
        request: main_models.GetDasAgentSSERequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.GetDasAgentSSEResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDasAgentSSE',
            version = '2020-01-16',
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
                main_models.GetDasAgentSSEResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def get_das_agent_ssewith_sse_async(
        self,
        request: main_models.GetDasAgentSSERequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.GetDasAgentSSEResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDasAgentSSE',
            version = '2020-01-16',
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
                main_models.GetDasAgentSSEResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def get_das_agent_ssewith_options(
        self,
        request: main_models.GetDasAgentSSERequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDasAgentSSEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDasAgentSSE',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDasAgentSSEResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_das_agent_ssewith_options_async(
        self,
        request: main_models.GetDasAgentSSERequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDasAgentSSEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDasAgentSSE',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDasAgentSSEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_das_agent_sse(
        self,
        request: main_models.GetDasAgentSSERequest,
    ) -> main_models.GetDasAgentSSEResponse:
        runtime = RuntimeOptions()
        return self.get_das_agent_ssewith_options(request, runtime)

    async def get_das_agent_sse_async(
        self,
        request: main_models.GetDasAgentSSERequest,
    ) -> main_models.GetDasAgentSSEResponse:
        runtime = RuntimeOptions()
        return await self.get_das_agent_ssewith_options_async(request, runtime)

    def get_das_pro_service_usage_with_options(
        self,
        request: main_models.GetDasProServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDasProServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDasProServiceUsage',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDasProServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_das_pro_service_usage_with_options_async(
        self,
        request: main_models.GetDasProServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDasProServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDasProServiceUsage',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDasProServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_das_pro_service_usage(
        self,
        request: main_models.GetDasProServiceUsageRequest,
    ) -> main_models.GetDasProServiceUsageResponse:
        runtime = RuntimeOptions()
        return self.get_das_pro_service_usage_with_options(request, runtime)

    async def get_das_pro_service_usage_async(
        self,
        request: main_models.GetDasProServiceUsageRequest,
    ) -> main_models.GetDasProServiceUsageResponse:
        runtime = RuntimeOptions()
        return await self.get_das_pro_service_usage_with_options_async(request, runtime)

    def get_das_sqllog_hot_data_with_options(
        self,
        request: main_models.GetDasSQLLogHotDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDasSQLLogHotDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.child_dbinstance_ids):
            body['ChildDBInstanceIDs'] = request.child_dbinstance_ids
        if not DaraCore.is_null(request.dbname):
            body['DBName'] = request.dbname
        if not DaraCore.is_null(request.end):
            body['End'] = request.end
        if not DaraCore.is_null(request.fail):
            body['Fail'] = request.fail
        if not DaraCore.is_null(request.host_address):
            body['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logical_operator):
            body['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.max_latancy):
            body['MaxLatancy'] = request.max_latancy
        if not DaraCore.is_null(request.max_records_per_page):
            body['MaxRecordsPerPage'] = request.max_records_per_page
        if not DaraCore.is_null(request.max_rows):
            body['MaxRows'] = request.max_rows
        if not DaraCore.is_null(request.max_scan_rows):
            body['MaxScanRows'] = request.max_scan_rows
        if not DaraCore.is_null(request.max_spill_cnt):
            body['MaxSpillCnt'] = request.max_spill_cnt
        if not DaraCore.is_null(request.min_latancy):
            body['MinLatancy'] = request.min_latancy
        if not DaraCore.is_null(request.min_rows):
            body['MinRows'] = request.min_rows
        if not DaraCore.is_null(request.min_scan_rows):
            body['MinScanRows'] = request.min_scan_rows
        if not DaraCore.is_null(request.min_spill_cnt):
            body['MinSpillCnt'] = request.min_spill_cnt
        if not DaraCore.is_null(request.page_numbers):
            body['PageNumbers'] = request.page_numbers
        if not DaraCore.is_null(request.query_keyword):
            body['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.sort_key):
            body['SortKey'] = request.sort_key
        if not DaraCore.is_null(request.sort_method):
            body['SortMethod'] = request.sort_method
        if not DaraCore.is_null(request.sql_type):
            body['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        if not DaraCore.is_null(request.thread_id):
            body['ThreadID'] = request.thread_id
        if not DaraCore.is_null(request.trace_id):
            body['TraceId'] = request.trace_id
        if not DaraCore.is_null(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDasSQLLogHotData',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDasSQLLogHotDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_das_sqllog_hot_data_with_options_async(
        self,
        request: main_models.GetDasSQLLogHotDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDasSQLLogHotDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_name):
            body['AccountName'] = request.account_name
        if not DaraCore.is_null(request.child_dbinstance_ids):
            body['ChildDBInstanceIDs'] = request.child_dbinstance_ids
        if not DaraCore.is_null(request.dbname):
            body['DBName'] = request.dbname
        if not DaraCore.is_null(request.end):
            body['End'] = request.end
        if not DaraCore.is_null(request.fail):
            body['Fail'] = request.fail
        if not DaraCore.is_null(request.host_address):
            body['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logical_operator):
            body['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.max_latancy):
            body['MaxLatancy'] = request.max_latancy
        if not DaraCore.is_null(request.max_records_per_page):
            body['MaxRecordsPerPage'] = request.max_records_per_page
        if not DaraCore.is_null(request.max_rows):
            body['MaxRows'] = request.max_rows
        if not DaraCore.is_null(request.max_scan_rows):
            body['MaxScanRows'] = request.max_scan_rows
        if not DaraCore.is_null(request.max_spill_cnt):
            body['MaxSpillCnt'] = request.max_spill_cnt
        if not DaraCore.is_null(request.min_latancy):
            body['MinLatancy'] = request.min_latancy
        if not DaraCore.is_null(request.min_rows):
            body['MinRows'] = request.min_rows
        if not DaraCore.is_null(request.min_scan_rows):
            body['MinScanRows'] = request.min_scan_rows
        if not DaraCore.is_null(request.min_spill_cnt):
            body['MinSpillCnt'] = request.min_spill_cnt
        if not DaraCore.is_null(request.page_numbers):
            body['PageNumbers'] = request.page_numbers
        if not DaraCore.is_null(request.query_keyword):
            body['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.role):
            body['Role'] = request.role
        if not DaraCore.is_null(request.sort_key):
            body['SortKey'] = request.sort_key
        if not DaraCore.is_null(request.sort_method):
            body['SortMethod'] = request.sort_method
        if not DaraCore.is_null(request.sql_type):
            body['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        if not DaraCore.is_null(request.thread_id):
            body['ThreadID'] = request.thread_id
        if not DaraCore.is_null(request.trace_id):
            body['TraceId'] = request.trace_id
        if not DaraCore.is_null(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDasSQLLogHotData',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDasSQLLogHotDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_das_sqllog_hot_data(
        self,
        request: main_models.GetDasSQLLogHotDataRequest,
    ) -> main_models.GetDasSQLLogHotDataResponse:
        runtime = RuntimeOptions()
        return self.get_das_sqllog_hot_data_with_options(request, runtime)

    async def get_das_sqllog_hot_data_async(
        self,
        request: main_models.GetDasSQLLogHotDataRequest,
    ) -> main_models.GetDasSQLLogHotDataResponse:
        runtime = RuntimeOptions()
        return await self.get_das_sqllog_hot_data_with_options_async(request, runtime)

    def get_dead_lock_detail_with_options(
        self,
        request: main_models.GetDeadLockDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadLockDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.text_id):
            query['TextId'] = request.text_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadLockDetail',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadLockDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dead_lock_detail_with_options_async(
        self,
        request: main_models.GetDeadLockDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadLockDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.text_id):
            query['TextId'] = request.text_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadLockDetail',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadLockDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dead_lock_detail(
        self,
        request: main_models.GetDeadLockDetailRequest,
    ) -> main_models.GetDeadLockDetailResponse:
        runtime = RuntimeOptions()
        return self.get_dead_lock_detail_with_options(request, runtime)

    async def get_dead_lock_detail_async(
        self,
        request: main_models.GetDeadLockDetailRequest,
    ) -> main_models.GetDeadLockDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_dead_lock_detail_with_options_async(request, runtime)

    def get_dead_lock_detail_list_with_options(
        self,
        request: main_models.GetDeadLockDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadLockDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name_list):
            query['DbNameList'] = request.db_name_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadLockDetailList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadLockDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dead_lock_detail_list_with_options_async(
        self,
        request: main_models.GetDeadLockDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadLockDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name_list):
            query['DbNameList'] = request.db_name_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadLockDetailList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadLockDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dead_lock_detail_list(
        self,
        request: main_models.GetDeadLockDetailListRequest,
    ) -> main_models.GetDeadLockDetailListResponse:
        runtime = RuntimeOptions()
        return self.get_dead_lock_detail_list_with_options(request, runtime)

    async def get_dead_lock_detail_list_async(
        self,
        request: main_models.GetDeadLockDetailListRequest,
    ) -> main_models.GetDeadLockDetailListResponse:
        runtime = RuntimeOptions()
        return await self.get_dead_lock_detail_list_with_options_async(request, runtime)

    def get_dead_lock_history_with_options(
        self,
        request: main_models.GetDeadLockHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadLockHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadLockHistory',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadLockHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dead_lock_history_with_options_async(
        self,
        request: main_models.GetDeadLockHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadLockHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadLockHistory',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadLockHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dead_lock_history(
        self,
        request: main_models.GetDeadLockHistoryRequest,
    ) -> main_models.GetDeadLockHistoryResponse:
        runtime = RuntimeOptions()
        return self.get_dead_lock_history_with_options(request, runtime)

    async def get_dead_lock_history_async(
        self,
        request: main_models.GetDeadLockHistoryRequest,
    ) -> main_models.GetDeadLockHistoryResponse:
        runtime = RuntimeOptions()
        return await self.get_dead_lock_history_with_options_async(request, runtime)

    def get_deadlock_histogram_with_options(
        self,
        request: main_models.GetDeadlockHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadlockHistogramResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadlockHistogram',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadlockHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deadlock_histogram_with_options_async(
        self,
        request: main_models.GetDeadlockHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeadlockHistogramResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeadlockHistogram',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeadlockHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deadlock_histogram(
        self,
        request: main_models.GetDeadlockHistogramRequest,
    ) -> main_models.GetDeadlockHistogramResponse:
        runtime = RuntimeOptions()
        return self.get_deadlock_histogram_with_options(request, runtime)

    async def get_deadlock_histogram_async(
        self,
        request: main_models.GetDeadlockHistogramRequest,
    ) -> main_models.GetDeadlockHistogramResponse:
        runtime = RuntimeOptions()
        return await self.get_deadlock_histogram_with_options_async(request, runtime)

    def get_endpoint_switch_task_with_options(
        self,
        request: main_models.GetEndpointSwitchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEndpointSwitchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        if not DaraCore.is_null(request.access_key):
            query['accessKey'] = request.access_key
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not DaraCore.is_null(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEndpointSwitchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEndpointSwitchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_endpoint_switch_task_with_options_async(
        self,
        request: main_models.GetEndpointSwitchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEndpointSwitchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        if not DaraCore.is_null(request.access_key):
            query['accessKey'] = request.access_key
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not DaraCore.is_null(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEndpointSwitchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEndpointSwitchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_endpoint_switch_task(
        self,
        request: main_models.GetEndpointSwitchTaskRequest,
    ) -> main_models.GetEndpointSwitchTaskResponse:
        runtime = RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    async def get_endpoint_switch_task_async(
        self,
        request: main_models.GetEndpointSwitchTaskRequest,
    ) -> main_models.GetEndpointSwitchTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_endpoint_switch_task_with_options_async(request, runtime)

    def get_error_request_sample_with_options(
        self,
        request: main_models.GetErrorRequestSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorRequestSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetErrorRequestSample',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorRequestSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_error_request_sample_with_options_async(
        self,
        request: main_models.GetErrorRequestSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorRequestSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetErrorRequestSample',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorRequestSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_error_request_sample(
        self,
        request: main_models.GetErrorRequestSampleRequest,
    ) -> main_models.GetErrorRequestSampleResponse:
        runtime = RuntimeOptions()
        return self.get_error_request_sample_with_options(request, runtime)

    async def get_error_request_sample_async(
        self,
        request: main_models.GetErrorRequestSampleRequest,
    ) -> main_models.GetErrorRequestSampleResponse:
        runtime = RuntimeOptions()
        return await self.get_error_request_sample_with_options_async(request, runtime)

    def get_event_subscription_with_options(
        self,
        request: main_models.GetEventSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEventSubscription',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_subscription_with_options_async(
        self,
        request: main_models.GetEventSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEventSubscription',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_subscription(
        self,
        request: main_models.GetEventSubscriptionRequest,
    ) -> main_models.GetEventSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.get_event_subscription_with_options(request, runtime)

    async def get_event_subscription_async(
        self,
        request: main_models.GetEventSubscriptionRequest,
    ) -> main_models.GetEventSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.get_event_subscription_with_options_async(request, runtime)

    def get_full_request_origin_stat_by_instance_id_with_options(
        self,
        request: main_models.GetFullRequestOriginStatByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFullRequestOriginStatByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFullRequestOriginStatByInstanceId',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFullRequestOriginStatByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_full_request_origin_stat_by_instance_id_with_options_async(
        self,
        request: main_models.GetFullRequestOriginStatByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFullRequestOriginStatByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFullRequestOriginStatByInstanceId',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFullRequestOriginStatByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_full_request_origin_stat_by_instance_id(
        self,
        request: main_models.GetFullRequestOriginStatByInstanceIdRequest,
    ) -> main_models.GetFullRequestOriginStatByInstanceIdResponse:
        runtime = RuntimeOptions()
        return self.get_full_request_origin_stat_by_instance_id_with_options(request, runtime)

    async def get_full_request_origin_stat_by_instance_id_async(
        self,
        request: main_models.GetFullRequestOriginStatByInstanceIdRequest,
    ) -> main_models.GetFullRequestOriginStatByInstanceIdResponse:
        runtime = RuntimeOptions()
        return await self.get_full_request_origin_stat_by_instance_id_with_options_async(request, runtime)

    def get_full_request_sample_by_instance_id_with_options(
        self,
        request: main_models.GetFullRequestSampleByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFullRequestSampleByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        body = {}
        if not DaraCore.is_null(request.end):
            body['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_id):
            body['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFullRequestSampleByInstanceId',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFullRequestSampleByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_full_request_sample_by_instance_id_with_options_async(
        self,
        request: main_models.GetFullRequestSampleByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFullRequestSampleByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        body = {}
        if not DaraCore.is_null(request.end):
            body['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_id):
            body['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start):
            body['Start'] = request.start
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFullRequestSampleByInstanceId',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFullRequestSampleByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_full_request_sample_by_instance_id(
        self,
        request: main_models.GetFullRequestSampleByInstanceIdRequest,
    ) -> main_models.GetFullRequestSampleByInstanceIdResponse:
        runtime = RuntimeOptions()
        return self.get_full_request_sample_by_instance_id_with_options(request, runtime)

    async def get_full_request_sample_by_instance_id_async(
        self,
        request: main_models.GetFullRequestSampleByInstanceIdRequest,
    ) -> main_models.GetFullRequestSampleByInstanceIdResponse:
        runtime = RuntimeOptions()
        return await self.get_full_request_sample_by_instance_id_with_options_async(request, runtime)

    def get_full_request_stat_result_by_instance_id_with_options(
        self,
        request: main_models.GetFullRequestStatResultByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFullRequestStatResultByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.origin_host):
            query['OriginHost'] = request.origin_host
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFullRequestStatResultByInstanceId',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFullRequestStatResultByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_full_request_stat_result_by_instance_id_with_options_async(
        self,
        request: main_models.GetFullRequestStatResultByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFullRequestStatResultByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.origin_host):
            query['OriginHost'] = request.origin_host
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFullRequestStatResultByInstanceId',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFullRequestStatResultByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_full_request_stat_result_by_instance_id(
        self,
        request: main_models.GetFullRequestStatResultByInstanceIdRequest,
    ) -> main_models.GetFullRequestStatResultByInstanceIdResponse:
        runtime = RuntimeOptions()
        return self.get_full_request_stat_result_by_instance_id_with_options(request, runtime)

    async def get_full_request_stat_result_by_instance_id_async(
        self,
        request: main_models.GetFullRequestStatResultByInstanceIdRequest,
    ) -> main_models.GetFullRequestStatResultByInstanceIdResponse:
        runtime = RuntimeOptions()
        return await self.get_full_request_stat_result_by_instance_id_with_options_async(request, runtime)

    def get_hdmaliyun_resource_sync_result_with_options(
        self,
        request: main_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHDMAliyunResourceSyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        if not DaraCore.is_null(request.access_key):
            query['accessKey'] = request.access_key
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not DaraCore.is_null(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHDMAliyunResourceSyncResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHDMAliyunResourceSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hdmaliyun_resource_sync_result_with_options_async(
        self,
        request: main_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHDMAliyunResourceSyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        if not DaraCore.is_null(request.access_key):
            query['accessKey'] = request.access_key
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not DaraCore.is_null(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHDMAliyunResourceSyncResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHDMAliyunResourceSyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hdmaliyun_resource_sync_result(
        self,
        request: main_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> main_models.GetHDMAliyunResourceSyncResultResponse:
        runtime = RuntimeOptions()
        return self.get_hdmaliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmaliyun_resource_sync_result_async(
        self,
        request: main_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> main_models.GetHDMAliyunResourceSyncResultResponse:
        runtime = RuntimeOptions()
        return await self.get_hdmaliyun_resource_sync_result_with_options_async(request, runtime)

    def get_hdmlast_aliyun_resource_sync_result_with_options(
        self,
        request: main_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHDMLastAliyunResourceSyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        if not DaraCore.is_null(request.access_key):
            query['accessKey'] = request.access_key
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not DaraCore.is_null(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHDMLastAliyunResourceSyncResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHDMLastAliyunResourceSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hdmlast_aliyun_resource_sync_result_with_options_async(
        self,
        request: main_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHDMLastAliyunResourceSyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.context):
            query['__context'] = request.context
        if not DaraCore.is_null(request.access_key):
            query['accessKey'] = request.access_key
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.skip_auth):
            query['skipAuth'] = request.skip_auth
        if not DaraCore.is_null(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHDMLastAliyunResourceSyncResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHDMLastAliyunResourceSyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hdmlast_aliyun_resource_sync_result(
        self,
        request: main_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> main_models.GetHDMLastAliyunResourceSyncResultResponse:
        runtime = RuntimeOptions()
        return self.get_hdmlast_aliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmlast_aliyun_resource_sync_result_async(
        self,
        request: main_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> main_models.GetHDMLastAliyunResourceSyncResultResponse:
        runtime = RuntimeOptions()
        return await self.get_hdmlast_aliyun_resource_sync_result_with_options_async(request, runtime)

    def get_instance_group_inspect_report_detail_with_options(
        self,
        request: main_models.GetInstanceGroupInspectReportDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceGroupInspectReportDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        body = {}
        if not DaraCore.is_null(request.report_id):
            body['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceGroupInspectReportDetail',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceGroupInspectReportDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_group_inspect_report_detail_with_options_async(
        self,
        request: main_models.GetInstanceGroupInspectReportDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceGroupInspectReportDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        body = {}
        if not DaraCore.is_null(request.report_id):
            body['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceGroupInspectReportDetail',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceGroupInspectReportDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_group_inspect_report_detail(
        self,
        request: main_models.GetInstanceGroupInspectReportDetailRequest,
    ) -> main_models.GetInstanceGroupInspectReportDetailResponse:
        runtime = RuntimeOptions()
        return self.get_instance_group_inspect_report_detail_with_options(request, runtime)

    async def get_instance_group_inspect_report_detail_async(
        self,
        request: main_models.GetInstanceGroupInspectReportDetailRequest,
    ) -> main_models.GetInstanceGroupInspectReportDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_group_inspect_report_detail_with_options_async(request, runtime)

    def get_instance_group_inspect_report_list_with_options(
        self,
        request: main_models.GetInstanceGroupInspectReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceGroupInspectReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceGroupInspectReportList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceGroupInspectReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_group_inspect_report_list_with_options_async(
        self,
        request: main_models.GetInstanceGroupInspectReportListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceGroupInspectReportListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceGroupInspectReportList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceGroupInspectReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_group_inspect_report_list(
        self,
        request: main_models.GetInstanceGroupInspectReportListRequest,
    ) -> main_models.GetInstanceGroupInspectReportListResponse:
        runtime = RuntimeOptions()
        return self.get_instance_group_inspect_report_list_with_options(request, runtime)

    async def get_instance_group_inspect_report_list_async(
        self,
        request: main_models.GetInstanceGroupInspectReportListRequest,
    ) -> main_models.GetInstanceGroupInspectReportListResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_group_inspect_report_list_with_options_async(request, runtime)

    def get_instance_inspections_with_options(
        self,
        request: main_models.GetInstanceInspectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceInspectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_map):
            query['SearchMap'] = request.search_map
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceInspections',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceInspectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_inspections_with_options_async(
        self,
        request: main_models.GetInstanceInspectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceInspectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_area):
            query['InstanceArea'] = request.instance_area
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_map):
            query['SearchMap'] = request.search_map
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceInspections',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceInspectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_inspections(
        self,
        request: main_models.GetInstanceInspectionsRequest,
    ) -> main_models.GetInstanceInspectionsResponse:
        runtime = RuntimeOptions()
        return self.get_instance_inspections_with_options(request, runtime)

    async def get_instance_inspections_async(
        self,
        request: main_models.GetInstanceInspectionsRequest,
    ) -> main_models.GetInstanceInspectionsResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_inspections_with_options_async(request, runtime)

    def get_instance_missing_index_list_with_options(
        self,
        request: main_models.GetInstanceMissingIndexListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceMissingIndexListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avg_total_user_cost):
            query['AvgTotalUserCost'] = request.avg_total_user_cost
        if not DaraCore.is_null(request.avg_user_impact):
            query['AvgUserImpact'] = request.avg_user_impact
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.index_count):
            query['IndexCount'] = request.index_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_name):
            query['ObjectName'] = request.object_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reserved_pages):
            query['ReservedPages'] = request.reserved_pages
        if not DaraCore.is_null(request.reserved_size):
            query['ReservedSize'] = request.reserved_size
        if not DaraCore.is_null(request.row_count):
            query['RowCount'] = request.row_count
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.unique_compiles):
            query['UniqueCompiles'] = request.unique_compiles
        if not DaraCore.is_null(request.user_scans):
            query['UserScans'] = request.user_scans
        if not DaraCore.is_null(request.user_seeks):
            query['UserSeeks'] = request.user_seeks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceMissingIndexList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceMissingIndexListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_missing_index_list_with_options_async(
        self,
        request: main_models.GetInstanceMissingIndexListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceMissingIndexListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avg_total_user_cost):
            query['AvgTotalUserCost'] = request.avg_total_user_cost
        if not DaraCore.is_null(request.avg_user_impact):
            query['AvgUserImpact'] = request.avg_user_impact
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.index_count):
            query['IndexCount'] = request.index_count
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_name):
            query['ObjectName'] = request.object_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reserved_pages):
            query['ReservedPages'] = request.reserved_pages
        if not DaraCore.is_null(request.reserved_size):
            query['ReservedSize'] = request.reserved_size
        if not DaraCore.is_null(request.row_count):
            query['RowCount'] = request.row_count
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.unique_compiles):
            query['UniqueCompiles'] = request.unique_compiles
        if not DaraCore.is_null(request.user_scans):
            query['UserScans'] = request.user_scans
        if not DaraCore.is_null(request.user_seeks):
            query['UserSeeks'] = request.user_seeks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceMissingIndexList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceMissingIndexListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_missing_index_list(
        self,
        request: main_models.GetInstanceMissingIndexListRequest,
    ) -> main_models.GetInstanceMissingIndexListResponse:
        runtime = RuntimeOptions()
        return self.get_instance_missing_index_list_with_options(request, runtime)

    async def get_instance_missing_index_list_async(
        self,
        request: main_models.GetInstanceMissingIndexListRequest,
    ) -> main_models.GetInstanceMissingIndexListResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_missing_index_list_with_options_async(request, runtime)

    def get_instance_sql_optimize_statistic_with_options(
        self,
        request: main_models.GetInstanceSqlOptimizeStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSqlOptimizeStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter_enable):
            query['FilterEnable'] = request.filter_enable
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.use_merging):
            query['UseMerging'] = request.use_merging
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSqlOptimizeStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSqlOptimizeStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_sql_optimize_statistic_with_options_async(
        self,
        request: main_models.GetInstanceSqlOptimizeStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceSqlOptimizeStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter_enable):
            query['FilterEnable'] = request.filter_enable
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.use_merging):
            query['UseMerging'] = request.use_merging
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceSqlOptimizeStatistic',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceSqlOptimizeStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_sql_optimize_statistic(
        self,
        request: main_models.GetInstanceSqlOptimizeStatisticRequest,
    ) -> main_models.GetInstanceSqlOptimizeStatisticResponse:
        runtime = RuntimeOptions()
        return self.get_instance_sql_optimize_statistic_with_options(request, runtime)

    async def get_instance_sql_optimize_statistic_async(
        self,
        request: main_models.GetInstanceSqlOptimizeStatisticRequest,
    ) -> main_models.GetInstanceSqlOptimizeStatisticResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_sql_optimize_statistic_with_options_async(request, runtime)

    def get_kill_instance_session_task_result_with_options(
        self,
        request: main_models.GetKillInstanceSessionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKillInstanceSessionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKillInstanceSessionTaskResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKillInstanceSessionTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kill_instance_session_task_result_with_options_async(
        self,
        request: main_models.GetKillInstanceSessionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKillInstanceSessionTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKillInstanceSessionTaskResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKillInstanceSessionTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kill_instance_session_task_result(
        self,
        request: main_models.GetKillInstanceSessionTaskResultRequest,
    ) -> main_models.GetKillInstanceSessionTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_kill_instance_session_task_result_with_options(request, runtime)

    async def get_kill_instance_session_task_result_async(
        self,
        request: main_models.GetKillInstanceSessionTaskResultRequest,
    ) -> main_models.GetKillInstanceSessionTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_kill_instance_session_task_result_with_options_async(request, runtime)

    def get_mongo_dbcurrent_op_with_options(
        self,
        request: main_models.GetMongoDBCurrentOpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMongoDBCurrentOpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_doc):
            query['FilterDoc'] = request.filter_doc
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMongoDBCurrentOp',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMongoDBCurrentOpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mongo_dbcurrent_op_with_options_async(
        self,
        request: main_models.GetMongoDBCurrentOpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMongoDBCurrentOpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_doc):
            query['FilterDoc'] = request.filter_doc
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMongoDBCurrentOp',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMongoDBCurrentOpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mongo_dbcurrent_op(
        self,
        request: main_models.GetMongoDBCurrentOpRequest,
    ) -> main_models.GetMongoDBCurrentOpResponse:
        runtime = RuntimeOptions()
        return self.get_mongo_dbcurrent_op_with_options(request, runtime)

    async def get_mongo_dbcurrent_op_async(
        self,
        request: main_models.GetMongoDBCurrentOpRequest,
    ) -> main_models.GetMongoDBCurrentOpResponse:
        runtime = RuntimeOptions()
        return await self.get_mongo_dbcurrent_op_with_options_async(request, runtime)

    def get_my_sqlall_session_async_with_options(
        self,
        request: main_models.GetMySQLAllSessionAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMySQLAllSessionAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMySQLAllSessionAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMySQLAllSessionAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_sqlall_session_async_with_options_async(
        self,
        request: main_models.GetMySQLAllSessionAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMySQLAllSessionAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMySQLAllSessionAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMySQLAllSessionAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_sqlall_session_async(
        self,
        request: main_models.GetMySQLAllSessionAsyncRequest,
    ) -> main_models.GetMySQLAllSessionAsyncResponse:
        runtime = RuntimeOptions()
        return self.get_my_sqlall_session_async_with_options(request, runtime)

    async def get_my_sqlall_session_async_async(
        self,
        request: main_models.GetMySQLAllSessionAsyncRequest,
    ) -> main_models.GetMySQLAllSessionAsyncResponse:
        runtime = RuntimeOptions()
        return await self.get_my_sqlall_session_async_with_options_async(request, runtime)

    def get_partitions_heatmap_with_options(
        self,
        request: main_models.GetPartitionsHeatmapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPartitionsHeatmapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPartitionsHeatmap',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPartitionsHeatmapResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_partitions_heatmap_with_options_async(
        self,
        request: main_models.GetPartitionsHeatmapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPartitionsHeatmapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPartitionsHeatmap',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPartitionsHeatmapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_partitions_heatmap(
        self,
        request: main_models.GetPartitionsHeatmapRequest,
    ) -> main_models.GetPartitionsHeatmapResponse:
        runtime = RuntimeOptions()
        return self.get_partitions_heatmap_with_options(request, runtime)

    async def get_partitions_heatmap_async(
        self,
        request: main_models.GetPartitionsHeatmapRequest,
    ) -> main_models.GetPartitionsHeatmapResponse:
        runtime = RuntimeOptions()
        return await self.get_partitions_heatmap_with_options_async(request, runtime)

    def get_pfs_metric_trends_with_options(
        self,
        request: main_models.GetPfsMetricTrendsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPfsMetricTrendsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric):
            body['Metric'] = request.metric
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPfsMetricTrends',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPfsMetricTrendsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pfs_metric_trends_with_options_async(
        self,
        request: main_models.GetPfsMetricTrendsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPfsMetricTrendsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric):
            body['Metric'] = request.metric
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPfsMetricTrends',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPfsMetricTrendsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pfs_metric_trends(
        self,
        request: main_models.GetPfsMetricTrendsRequest,
    ) -> main_models.GetPfsMetricTrendsResponse:
        runtime = RuntimeOptions()
        return self.get_pfs_metric_trends_with_options(request, runtime)

    async def get_pfs_metric_trends_async(
        self,
        request: main_models.GetPfsMetricTrendsRequest,
    ) -> main_models.GetPfsMetricTrendsResponse:
        runtime = RuntimeOptions()
        return await self.get_pfs_metric_trends_with_options_async(request, runtime)

    def get_pfs_sql_sample_with_options(
        self,
        request: main_models.GetPfsSqlSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPfsSqlSampleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql_id):
            body['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPfsSqlSample',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPfsSqlSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pfs_sql_sample_with_options_async(
        self,
        request: main_models.GetPfsSqlSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPfsSqlSampleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.sql_id):
            body['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPfsSqlSample',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPfsSqlSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pfs_sql_sample(
        self,
        request: main_models.GetPfsSqlSampleRequest,
    ) -> main_models.GetPfsSqlSampleResponse:
        runtime = RuntimeOptions()
        return self.get_pfs_sql_sample_with_options(request, runtime)

    async def get_pfs_sql_sample_async(
        self,
        request: main_models.GetPfsSqlSampleRequest,
    ) -> main_models.GetPfsSqlSampleResponse:
        runtime = RuntimeOptions()
        return await self.get_pfs_sql_sample_with_options_async(request, runtime)

    def get_pfs_sql_summaries_with_options(
        self,
        request: main_models.GetPfsSqlSummariesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPfsSqlSummariesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asc):
            body['Asc'] = request.asc
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sql_id):
            body['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPfsSqlSummaries',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPfsSqlSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pfs_sql_summaries_with_options_async(
        self,
        request: main_models.GetPfsSqlSummariesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPfsSqlSummariesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.asc):
            body['Asc'] = request.asc
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            body['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sql_id):
            body['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPfsSqlSummaries',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPfsSqlSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pfs_sql_summaries(
        self,
        request: main_models.GetPfsSqlSummariesRequest,
    ) -> main_models.GetPfsSqlSummariesResponse:
        runtime = RuntimeOptions()
        return self.get_pfs_sql_summaries_with_options(request, runtime)

    async def get_pfs_sql_summaries_async(
        self,
        request: main_models.GetPfsSqlSummariesRequest,
    ) -> main_models.GetPfsSqlSummariesResponse:
        runtime = RuntimeOptions()
        return await self.get_pfs_sql_summaries_with_options_async(request, runtime)

    def get_query_optimize_data_stats_with_options(
        self,
        request: main_models.GetQueryOptimizeDataStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeDataStatsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeDataStats',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeDataStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_data_stats_with_options_async(
        self,
        request: main_models.GetQueryOptimizeDataStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeDataStatsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeDataStats',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeDataStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_data_stats(
        self,
        request: main_models.GetQueryOptimizeDataStatsRequest,
    ) -> main_models.GetQueryOptimizeDataStatsResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_data_stats_with_options(request, runtime)

    async def get_query_optimize_data_stats_async(
        self,
        request: main_models.GetQueryOptimizeDataStatsRequest,
    ) -> main_models.GetQueryOptimizeDataStatsResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_data_stats_with_options_async(request, runtime)

    def get_query_optimize_data_top_with_options(
        self,
        request: main_models.GetQueryOptimizeDataTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeDataTopResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeDataTop',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeDataTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_data_top_with_options_async(
        self,
        request: main_models.GetQueryOptimizeDataTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeDataTopResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeDataTop',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeDataTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_data_top(
        self,
        request: main_models.GetQueryOptimizeDataTopRequest,
    ) -> main_models.GetQueryOptimizeDataTopResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_data_top_with_options(request, runtime)

    async def get_query_optimize_data_top_async(
        self,
        request: main_models.GetQueryOptimizeDataTopRequest,
    ) -> main_models.GetQueryOptimizeDataTopResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_data_top_with_options_async(request, runtime)

    def get_query_optimize_data_trend_with_options(
        self,
        request: main_models.GetQueryOptimizeDataTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeDataTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeDataTrend',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeDataTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_data_trend_with_options_async(
        self,
        request: main_models.GetQueryOptimizeDataTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeDataTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeDataTrend',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeDataTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_data_trend(
        self,
        request: main_models.GetQueryOptimizeDataTrendRequest,
    ) -> main_models.GetQueryOptimizeDataTrendResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_data_trend_with_options(request, runtime)

    async def get_query_optimize_data_trend_async(
        self,
        request: main_models.GetQueryOptimizeDataTrendRequest,
    ) -> main_models.GetQueryOptimizeDataTrendResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_data_trend_with_options_async(request, runtime)

    def get_query_optimize_exec_error_sample_with_options(
        self,
        request: main_models.GetQueryOptimizeExecErrorSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeExecErrorSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeExecErrorSample',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeExecErrorSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_exec_error_sample_with_options_async(
        self,
        request: main_models.GetQueryOptimizeExecErrorSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeExecErrorSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeExecErrorSample',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeExecErrorSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_exec_error_sample(
        self,
        request: main_models.GetQueryOptimizeExecErrorSampleRequest,
    ) -> main_models.GetQueryOptimizeExecErrorSampleResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_exec_error_sample_with_options(request, runtime)

    async def get_query_optimize_exec_error_sample_async(
        self,
        request: main_models.GetQueryOptimizeExecErrorSampleRequest,
    ) -> main_models.GetQueryOptimizeExecErrorSampleResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_exec_error_sample_with_options_async(request, runtime)

    def get_query_optimize_exec_error_stats_with_options(
        self,
        request: main_models.GetQueryOptimizeExecErrorStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeExecErrorStatsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeExecErrorStats',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeExecErrorStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_exec_error_stats_with_options_async(
        self,
        request: main_models.GetQueryOptimizeExecErrorStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeExecErrorStatsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeExecErrorStats',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeExecErrorStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_exec_error_stats(
        self,
        request: main_models.GetQueryOptimizeExecErrorStatsRequest,
    ) -> main_models.GetQueryOptimizeExecErrorStatsResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_exec_error_stats_with_options(request, runtime)

    async def get_query_optimize_exec_error_stats_async(
        self,
        request: main_models.GetQueryOptimizeExecErrorStatsRequest,
    ) -> main_models.GetQueryOptimizeExecErrorStatsResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_exec_error_stats_with_options_async(request, runtime)

    def get_query_optimize_rule_list_with_options(
        self,
        request: main_models.GetQueryOptimizeRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeRuleListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeRuleList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_rule_list_with_options_async(
        self,
        request: main_models.GetQueryOptimizeRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeRuleListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeRuleList',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_rule_list(
        self,
        request: main_models.GetQueryOptimizeRuleListRequest,
    ) -> main_models.GetQueryOptimizeRuleListResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_rule_list_with_options(request, runtime)

    async def get_query_optimize_rule_list_async(
        self,
        request: main_models.GetQueryOptimizeRuleListRequest,
    ) -> main_models.GetQueryOptimizeRuleListResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_rule_list_with_options_async(request, runtime)

    def get_query_optimize_share_url_with_options(
        self,
        request: main_models.GetQueryOptimizeShareUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeShareUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.db_names):
            query['DbNames'] = request.db_names
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.only_optimized_sql):
            query['OnlyOptimizedSql'] = request.only_optimized_sql
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.sql_ids):
            query['SqlIds'] = request.sql_ids
        if not DaraCore.is_null(request.tag_names):
            query['TagNames'] = request.tag_names
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeShareUrl',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeShareUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_share_url_with_options_async(
        self,
        request: main_models.GetQueryOptimizeShareUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeShareUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc):
            query['Asc'] = request.asc
        if not DaraCore.is_null(request.db_names):
            query['DbNames'] = request.db_names
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.keywords):
            query['Keywords'] = request.keywords
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.only_optimized_sql):
            query['OnlyOptimizedSql'] = request.only_optimized_sql
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.sql_ids):
            query['SqlIds'] = request.sql_ids
        if not DaraCore.is_null(request.tag_names):
            query['TagNames'] = request.tag_names
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeShareUrl',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeShareUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_share_url(
        self,
        request: main_models.GetQueryOptimizeShareUrlRequest,
    ) -> main_models.GetQueryOptimizeShareUrlResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_share_url_with_options(request, runtime)

    async def get_query_optimize_share_url_async(
        self,
        request: main_models.GetQueryOptimizeShareUrlRequest,
    ) -> main_models.GetQueryOptimizeShareUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_share_url_with_options_async(request, runtime)

    def get_query_optimize_solution_with_options(
        self,
        request: main_models.GetQueryOptimizeSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeSolution',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_solution_with_options_async(
        self,
        request: main_models.GetQueryOptimizeSolutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeSolutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeSolution',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_solution(
        self,
        request: main_models.GetQueryOptimizeSolutionRequest,
    ) -> main_models.GetQueryOptimizeSolutionResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_solution_with_options(request, runtime)

    async def get_query_optimize_solution_async(
        self,
        request: main_models.GetQueryOptimizeSolutionRequest,
    ) -> main_models.GetQueryOptimizeSolutionResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_solution_with_options_async(request, runtime)

    def get_query_optimize_tag_with_options(
        self,
        request: main_models.GetQueryOptimizeTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeTag',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_tag_with_options_async(
        self,
        request: main_models.GetQueryOptimizeTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryOptimizeTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryOptimizeTag',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryOptimizeTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_tag(
        self,
        request: main_models.GetQueryOptimizeTagRequest,
    ) -> main_models.GetQueryOptimizeTagResponse:
        runtime = RuntimeOptions()
        return self.get_query_optimize_tag_with_options(request, runtime)

    async def get_query_optimize_tag_async(
        self,
        request: main_models.GetQueryOptimizeTagRequest,
    ) -> main_models.GetQueryOptimizeTagResponse:
        runtime = RuntimeOptions()
        return await self.get_query_optimize_tag_with_options_async(request, runtime)

    def get_redis_all_session_with_options(
        self,
        request: main_models.GetRedisAllSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRedisAllSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRedisAllSession',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRedisAllSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_redis_all_session_with_options_async(
        self,
        request: main_models.GetRedisAllSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRedisAllSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRedisAllSession',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRedisAllSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_redis_all_session(
        self,
        request: main_models.GetRedisAllSessionRequest,
    ) -> main_models.GetRedisAllSessionResponse:
        runtime = RuntimeOptions()
        return self.get_redis_all_session_with_options(request, runtime)

    async def get_redis_all_session_async(
        self,
        request: main_models.GetRedisAllSessionRequest,
    ) -> main_models.GetRedisAllSessionResponse:
        runtime = RuntimeOptions()
        return await self.get_redis_all_session_with_options_async(request, runtime)

    def get_request_diagnosis_page_with_options(
        self,
        request: main_models.GetRequestDiagnosisPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRequestDiagnosisPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRequestDiagnosisPage',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRequestDiagnosisPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_request_diagnosis_page_with_options_async(
        self,
        request: main_models.GetRequestDiagnosisPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRequestDiagnosisPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRequestDiagnosisPage',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRequestDiagnosisPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_request_diagnosis_page(
        self,
        request: main_models.GetRequestDiagnosisPageRequest,
    ) -> main_models.GetRequestDiagnosisPageResponse:
        runtime = RuntimeOptions()
        return self.get_request_diagnosis_page_with_options(request, runtime)

    async def get_request_diagnosis_page_async(
        self,
        request: main_models.GetRequestDiagnosisPageRequest,
    ) -> main_models.GetRequestDiagnosisPageResponse:
        runtime = RuntimeOptions()
        return await self.get_request_diagnosis_page_with_options_async(request, runtime)

    def get_request_diagnosis_result_with_options(
        self,
        request: main_models.GetRequestDiagnosisResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRequestDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRequestDiagnosisResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRequestDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_request_diagnosis_result_with_options_async(
        self,
        request: main_models.GetRequestDiagnosisResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRequestDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_id):
            query['MessageId'] = request.message_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRequestDiagnosisResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRequestDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_request_diagnosis_result(
        self,
        request: main_models.GetRequestDiagnosisResultRequest,
    ) -> main_models.GetRequestDiagnosisResultResponse:
        runtime = RuntimeOptions()
        return self.get_request_diagnosis_result_with_options(request, runtime)

    async def get_request_diagnosis_result_async(
        self,
        request: main_models.GetRequestDiagnosisResultRequest,
    ) -> main_models.GetRequestDiagnosisResultResponse:
        runtime = RuntimeOptions()
        return await self.get_request_diagnosis_result_with_options_async(request, runtime)

    def get_running_sql_concurrency_control_rules_with_options(
        self,
        request: main_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRunningSqlConcurrencyControlRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRunningSqlConcurrencyControlRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunningSqlConcurrencyControlRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_running_sql_concurrency_control_rules_with_options_async(
        self,
        request: main_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRunningSqlConcurrencyControlRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRunningSqlConcurrencyControlRules',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunningSqlConcurrencyControlRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_running_sql_concurrency_control_rules(
        self,
        request: main_models.GetRunningSqlConcurrencyControlRulesRequest,
    ) -> main_models.GetRunningSqlConcurrencyControlRulesResponse:
        runtime = RuntimeOptions()
        return self.get_running_sql_concurrency_control_rules_with_options(request, runtime)

    async def get_running_sql_concurrency_control_rules_async(
        self,
        request: main_models.GetRunningSqlConcurrencyControlRulesRequest,
    ) -> main_models.GetRunningSqlConcurrencyControlRulesResponse:
        runtime = RuntimeOptions()
        return await self.get_running_sql_concurrency_control_rules_with_options_async(request, runtime)

    def get_sql_concurrency_control_keywords_from_sql_text_with_options(
        self,
        request: main_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_text):
            query['SqlText'] = request.sql_text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConcurrencyControlKeywordsFromSqlText',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_concurrency_control_keywords_from_sql_text_with_options_async(
        self,
        request: main_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sql_text):
            query['SqlText'] = request.sql_text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConcurrencyControlKeywordsFromSqlText',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_concurrency_control_keywords_from_sql_text(
        self,
        request: main_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
    ) -> main_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        runtime = RuntimeOptions()
        return self.get_sql_concurrency_control_keywords_from_sql_text_with_options(request, runtime)

    async def get_sql_concurrency_control_keywords_from_sql_text_async(
        self,
        request: main_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
    ) -> main_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        runtime = RuntimeOptions()
        return await self.get_sql_concurrency_control_keywords_from_sql_text_with_options_async(request, runtime)

    def get_sql_concurrency_control_rules_history_with_options(
        self,
        request: main_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConcurrencyControlRulesHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConcurrencyControlRulesHistory',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_concurrency_control_rules_history_with_options_async(
        self,
        request: main_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConcurrencyControlRulesHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConcurrencyControlRulesHistory',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConcurrencyControlRulesHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_concurrency_control_rules_history(
        self,
        request: main_models.GetSqlConcurrencyControlRulesHistoryRequest,
    ) -> main_models.GetSqlConcurrencyControlRulesHistoryResponse:
        runtime = RuntimeOptions()
        return self.get_sql_concurrency_control_rules_history_with_options(request, runtime)

    async def get_sql_concurrency_control_rules_history_async(
        self,
        request: main_models.GetSqlConcurrencyControlRulesHistoryRequest,
    ) -> main_models.GetSqlConcurrencyControlRulesHistoryResponse:
        runtime = RuntimeOptions()
        return await self.get_sql_concurrency_control_rules_history_with_options_async(request, runtime)

    def get_sql_optimize_advice_with_options(
        self,
        request: main_models.GetSqlOptimizeAdviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlOptimizeAdviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.end_dt):
            query['EndDt'] = request.end_dt
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_dt):
            query['StartDt'] = request.start_dt
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlOptimizeAdvice',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlOptimizeAdviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_optimize_advice_with_options_async(
        self,
        request: main_models.GetSqlOptimizeAdviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlOptimizeAdviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.end_dt):
            query['EndDt'] = request.end_dt
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_dt):
            query['StartDt'] = request.start_dt
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlOptimizeAdvice',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlOptimizeAdviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_optimize_advice(
        self,
        request: main_models.GetSqlOptimizeAdviceRequest,
    ) -> main_models.GetSqlOptimizeAdviceResponse:
        runtime = RuntimeOptions()
        return self.get_sql_optimize_advice_with_options(request, runtime)

    async def get_sql_optimize_advice_async(
        self,
        request: main_models.GetSqlOptimizeAdviceRequest,
    ) -> main_models.GetSqlOptimizeAdviceResponse:
        runtime = RuntimeOptions()
        return await self.get_sql_optimize_advice_with_options_async(request, runtime)

    def get_storage_analysis_result_with_options(
        self,
        request: main_models.GetStorageAnalysisResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageAnalysisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageAnalysisResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageAnalysisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_analysis_result_with_options_async(
        self,
        request: main_models.GetStorageAnalysisResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageAnalysisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageAnalysisResult',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageAnalysisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_analysis_result(
        self,
        request: main_models.GetStorageAnalysisResultRequest,
    ) -> main_models.GetStorageAnalysisResultResponse:
        runtime = RuntimeOptions()
        return self.get_storage_analysis_result_with_options(request, runtime)

    async def get_storage_analysis_result_async(
        self,
        request: main_models.GetStorageAnalysisResultRequest,
    ) -> main_models.GetStorageAnalysisResultResponse:
        runtime = RuntimeOptions()
        return await self.get_storage_analysis_result_with_options_async(request, runtime)

    def kill_instance_all_session_with_options(
        self,
        request: main_models.KillInstanceAllSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillInstanceAllSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillInstanceAllSession',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillInstanceAllSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_instance_all_session_with_options_async(
        self,
        request: main_models.KillInstanceAllSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillInstanceAllSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillInstanceAllSession',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillInstanceAllSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_instance_all_session(
        self,
        request: main_models.KillInstanceAllSessionRequest,
    ) -> main_models.KillInstanceAllSessionResponse:
        runtime = RuntimeOptions()
        return self.kill_instance_all_session_with_options(request, runtime)

    async def kill_instance_all_session_async(
        self,
        request: main_models.KillInstanceAllSessionRequest,
    ) -> main_models.KillInstanceAllSessionResponse:
        runtime = RuntimeOptions()
        return await self.kill_instance_all_session_with_options_async(request, runtime)

    def modify_auto_scaling_config_with_options(
        self,
        request: main_models.ModifyAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.shard):
            query['Shard'] = request.shard
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoScalingConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_scaling_config_with_options_async(
        self,
        request: main_models.ModifyAutoScalingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.shard):
            query['Shard'] = request.shard
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoScalingConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_scaling_config(
        self,
        request: main_models.ModifyAutoScalingConfigRequest,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_auto_scaling_config_with_options(request, runtime)

    async def modify_auto_scaling_config_async(
        self,
        request: main_models.ModifyAutoScalingConfigRequest,
    ) -> main_models.ModifyAutoScalingConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_auto_scaling_config_with_options_async(request, runtime)

    def modify_security_ipgroup_with_options(
        self,
        request: main_models.ModifySecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ipgroup_with_options_async(
        self,
        request: main_models.ModifySecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIPGroup',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ipgroup(
        self,
        request: main_models.ModifySecurityIPGroupRequest,
    ) -> main_models.ModifySecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_security_ipgroup_with_options(request, runtime)

    async def modify_security_ipgroup_async(
        self,
        request: main_models.ModifySecurityIPGroupRequest,
    ) -> main_models.ModifySecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_security_ipgroup_with_options_async(request, runtime)

    def modify_security_ipgroup_relation_with_options(
        self,
        request: main_models.ModifySecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIPGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIPGroupRelation',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ipgroup_relation_with_options_async(
        self,
        request: main_models.ModifySecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIPGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIPGroupRelation',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ipgroup_relation(
        self,
        request: main_models.ModifySecurityIPGroupRelationRequest,
    ) -> main_models.ModifySecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.modify_security_ipgroup_relation_with_options(request, runtime)

    async def modify_security_ipgroup_relation_async(
        self,
        request: main_models.ModifySecurityIPGroupRelationRequest,
    ) -> main_models.ModifySecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.modify_security_ipgroup_relation_with_options_async(request, runtime)

    def modify_sql_log_config_with_options(
        self,
        request: main_models.ModifySqlLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySqlLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_audit):
            query['EnableAudit'] = request.enable_audit
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        body = {}
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.hot_retention):
            body['HotRetention'] = request.hot_retention
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_enable):
            body['RequestEnable'] = request.request_enable
        if not DaraCore.is_null(request.retention):
            body['Retention'] = request.retention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySqlLogConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySqlLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sql_log_config_with_options_async(
        self,
        request: main_models.ModifySqlLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySqlLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_audit):
            query['EnableAudit'] = request.enable_audit
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        body = {}
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.hot_retention):
            body['HotRetention'] = request.hot_retention
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.request_enable):
            body['RequestEnable'] = request.request_enable
        if not DaraCore.is_null(request.retention):
            body['Retention'] = request.retention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySqlLogConfig',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySqlLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sql_log_config(
        self,
        request: main_models.ModifySqlLogConfigRequest,
    ) -> main_models.ModifySqlLogConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_sql_log_config_with_options(request, runtime)

    async def modify_sql_log_config_async(
        self,
        request: main_models.ModifySqlLogConfigRequest,
    ) -> main_models.ModifySqlLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_sql_log_config_with_options_async(request, runtime)

    def run_cloud_bench_task_with_options(
        self,
        request: main_models.RunCloudBenchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCloudBenchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunCloudBenchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCloudBenchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cloud_bench_task_with_options_async(
        self,
        request: main_models.RunCloudBenchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCloudBenchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunCloudBenchTask',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCloudBenchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_cloud_bench_task(
        self,
        request: main_models.RunCloudBenchTaskRequest,
    ) -> main_models.RunCloudBenchTaskResponse:
        runtime = RuntimeOptions()
        return self.run_cloud_bench_task_with_options(request, runtime)

    async def run_cloud_bench_task_async(
        self,
        request: main_models.RunCloudBenchTaskRequest,
    ) -> main_models.RunCloudBenchTaskResponse:
        runtime = RuntimeOptions()
        return await self.run_cloud_bench_task_with_options_async(request, runtime)

    def set_event_subscription_with_options(
        self,
        request: main_models.SetEventSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetEventSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not DaraCore.is_null(request.event_context):
            query['EventContext'] = request.event_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.min_interval):
            query['MinInterval'] = request.min_interval
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetEventSubscription',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetEventSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_event_subscription_with_options_async(
        self,
        request: main_models.SetEventSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetEventSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not DaraCore.is_null(request.event_context):
            query['EventContext'] = request.event_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.min_interval):
            query['MinInterval'] = request.min_interval
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetEventSubscription',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetEventSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_event_subscription(
        self,
        request: main_models.SetEventSubscriptionRequest,
    ) -> main_models.SetEventSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.set_event_subscription_with_options(request, runtime)

    async def set_event_subscription_async(
        self,
        request: main_models.SetEventSubscriptionRequest,
    ) -> main_models.SetEventSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.set_event_subscription_with_options_async(request, runtime)

    def update_auto_resource_optimize_rules_async_with_options(
        self,
        request: main_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.result_id):
            query['ResultId'] = request.result_id
        if not DaraCore.is_null(request.table_fragmentation_ratio):
            query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        if not DaraCore.is_null(request.table_space_size):
            query['TableSpaceSize'] = request.table_space_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoResourceOptimizeRulesAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_resource_optimize_rules_async_with_options_async(
        self,
        request: main_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.result_id):
            query['ResultId'] = request.result_id
        if not DaraCore.is_null(request.table_fragmentation_ratio):
            query['TableFragmentationRatio'] = request.table_fragmentation_ratio
        if not DaraCore.is_null(request.table_space_size):
            query['TableSpaceSize'] = request.table_space_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoResourceOptimizeRulesAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_resource_optimize_rules_async(
        self,
        request: main_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
    ) -> main_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        runtime = RuntimeOptions()
        return self.update_auto_resource_optimize_rules_async_with_options(request, runtime)

    async def update_auto_resource_optimize_rules_async_async(
        self,
        request: main_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
    ) -> main_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        runtime = RuntimeOptions()
        return await self.update_auto_resource_optimize_rules_async_with_options_async(request, runtime)

    def update_auto_sql_optimize_status_with_options(
        self,
        request: main_models.UpdateAutoSqlOptimizeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoSqlOptimizeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoSqlOptimizeStatus',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoSqlOptimizeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_sql_optimize_status_with_options_async(
        self,
        request: main_models.UpdateAutoSqlOptimizeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoSqlOptimizeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoSqlOptimizeStatus',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoSqlOptimizeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_sql_optimize_status(
        self,
        request: main_models.UpdateAutoSqlOptimizeStatusRequest,
    ) -> main_models.UpdateAutoSqlOptimizeStatusResponse:
        runtime = RuntimeOptions()
        return self.update_auto_sql_optimize_status_with_options(request, runtime)

    async def update_auto_sql_optimize_status_async(
        self,
        request: main_models.UpdateAutoSqlOptimizeStatusRequest,
    ) -> main_models.UpdateAutoSqlOptimizeStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_auto_sql_optimize_status_with_options_async(request, runtime)

    def update_auto_throttle_rules_async_with_options(
        self,
        request: main_models.UpdateAutoThrottleRulesAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoThrottleRulesAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_duration):
            query['AbnormalDuration'] = request.abnormal_duration
        if not DaraCore.is_null(request.active_sessions):
            query['ActiveSessions'] = request.active_sessions
        if not DaraCore.is_null(request.allow_throttle_end_time):
            query['AllowThrottleEndTime'] = request.allow_throttle_end_time
        if not DaraCore.is_null(request.allow_throttle_start_time):
            query['AllowThrottleStartTime'] = request.allow_throttle_start_time
        if not DaraCore.is_null(request.auto_kill_session):
            query['AutoKillSession'] = request.auto_kill_session
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.cpu_session_relation):
            query['CpuSessionRelation'] = request.cpu_session_relation
        if not DaraCore.is_null(request.cpu_usage):
            query['CpuUsage'] = request.cpu_usage
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.max_throttle_time):
            query['MaxThrottleTime'] = request.max_throttle_time
        if not DaraCore.is_null(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoThrottleRulesAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoThrottleRulesAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_throttle_rules_async_with_options_async(
        self,
        request: main_models.UpdateAutoThrottleRulesAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoThrottleRulesAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_duration):
            query['AbnormalDuration'] = request.abnormal_duration
        if not DaraCore.is_null(request.active_sessions):
            query['ActiveSessions'] = request.active_sessions
        if not DaraCore.is_null(request.allow_throttle_end_time):
            query['AllowThrottleEndTime'] = request.allow_throttle_end_time
        if not DaraCore.is_null(request.allow_throttle_start_time):
            query['AllowThrottleStartTime'] = request.allow_throttle_start_time
        if not DaraCore.is_null(request.auto_kill_session):
            query['AutoKillSession'] = request.auto_kill_session
        if not DaraCore.is_null(request.console_context):
            query['ConsoleContext'] = request.console_context
        if not DaraCore.is_null(request.cpu_session_relation):
            query['CpuSessionRelation'] = request.cpu_session_relation
        if not DaraCore.is_null(request.cpu_usage):
            query['CpuUsage'] = request.cpu_usage
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.max_throttle_time):
            query['MaxThrottleTime'] = request.max_throttle_time
        if not DaraCore.is_null(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoThrottleRulesAsync',
            version = '2020-01-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoThrottleRulesAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_throttle_rules_async(
        self,
        request: main_models.UpdateAutoThrottleRulesAsyncRequest,
    ) -> main_models.UpdateAutoThrottleRulesAsyncResponse:
        runtime = RuntimeOptions()
        return self.update_auto_throttle_rules_async_with_options(request, runtime)

    async def update_auto_throttle_rules_async_async(
        self,
        request: main_models.UpdateAutoThrottleRulesAsyncRequest,
    ) -> main_models.UpdateAutoThrottleRulesAsyncResponse:
        runtime = RuntimeOptions()
        return await self.update_auto_throttle_rules_async_with_options_async(request, runtime)
