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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: AddHDMInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddHDMInstanceResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: AddHDMInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddHDMInstanceResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: AddHDMInstanceRequest
        @return: AddHDMInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_hdminstance_with_options(request, runtime)

    async def add_hdminstance_async(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
    ) -> das20200116_models.AddHDMInstanceResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: AddHDMInstanceRequest
        @return: AddHDMInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_hdminstance_with_options_async(request, runtime)

    def create_adam_bench_task_with_options(
        self,
        request: das20200116_models.CreateAdamBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateAdamBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. You use an ADAM stress testing task to check whether you need to scale up or scale out your database instance to handle workloads during peak hours. For more information, see [Intelligent Stress Testing](~~155068~~).
        Make sure that your database instances meet the following requirements:
        *   The source instance supports the following database engines: ApsaraDB RDS for MySQL on High-availability Edition or Enterprise Edition, and PolarDB for MySQL on Cluster Edition or X-Engine.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The database instance is connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is activated for the source and destination database instances. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateAdamBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdamBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. You use an ADAM stress testing task to check whether you need to scale up or scale out your database instance to handle workloads during peak hours. For more information, see [Intelligent Stress Testing](~~155068~~).
        Make sure that your database instances meet the following requirements:
        *   The source instance supports the following database engines: ApsaraDB RDS for MySQL on High-availability Edition or Enterprise Edition, and PolarDB for MySQL on Cluster Edition or X-Engine.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The database instance is connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is activated for the source and destination database instances. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateAdamBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdamBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. You use an ADAM stress testing task to check whether you need to scale up or scale out your database instance to handle workloads during peak hours. For more information, see [Intelligent Stress Testing](~~155068~~).
        Make sure that your database instances meet the following requirements:
        *   The source instance supports the following database engines: ApsaraDB RDS for MySQL on High-availability Edition or Enterprise Edition, and PolarDB for MySQL on Cluster Edition or X-Engine.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The database instance is connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is activated for the source and destination database instances. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateAdamBenchTaskRequest
        @return: CreateAdamBenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_adam_bench_task_with_options(request, runtime)

    async def create_adam_bench_task_async(
        self,
        request: das20200116_models.CreateAdamBenchTaskRequest,
    ) -> das20200116_models.CreateAdamBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. You use an ADAM stress testing task to check whether you need to scale up or scale out your database instance to handle workloads during peak hours. For more information, see [Intelligent Stress Testing](~~155068~~).
        Make sure that your database instances meet the following requirements:
        *   The source instance supports the following database engines: ApsaraDB RDS for MySQL on High-availability Edition or Enterprise Edition, and PolarDB for MySQL on Cluster Edition or X-Engine.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The database instance is connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is activated for the source and destination database instances. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateAdamBenchTaskRequest
        @return: CreateAdamBenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_adam_bench_task_with_options_async(request, runtime)

    def create_cache_analysis_job_with_options(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis Community Edition instances and performance-enhanced instances of the ApsaraDB for Redis Enhanced Edition (Tair).
        >  Redis 7.0 is not supported. You are not allowed to use custom modules.
        
        @param request: CreateCacheAnalysisJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCacheAnalysisJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.separators):
            query['Separators'] = request.separators
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis Community Edition instances and performance-enhanced instances of the ApsaraDB for Redis Enhanced Edition (Tair).
        >  Redis 7.0 is not supported. You are not allowed to use custom modules.
        
        @param request: CreateCacheAnalysisJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCacheAnalysisJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.separators):
            query['Separators'] = request.separators
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis Community Edition instances and performance-enhanced instances of the ApsaraDB for Redis Enhanced Edition (Tair).
        >  Redis 7.0 is not supported. You are not allowed to use custom modules.
        
        @param request: CreateCacheAnalysisJobRequest
        @return: CreateCacheAnalysisJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_job_with_options(request, runtime)

    async def create_cache_analysis_job_async(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis Community Edition instances and performance-enhanced instances of the ApsaraDB for Redis Enhanced Edition (Tair).
        >  Redis 7.0 is not supported. You are not allowed to use custom modules.
        
        @param request: CreateCacheAnalysisJobRequest
        @return: CreateCacheAnalysisJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cache_analysis_job_with_options_async(request, runtime)

    def create_cloud_bench_tasks_with_options(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~). Before you call this API operation, make sure that your database instances meet the following requirements:
        *   The source database instance must be an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition or X-Engine Edition instance.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The source instance and the destination instance are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is enabled for the source instance and the destination instance. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateCloudBenchTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudBenchTasksResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~). Before you call this API operation, make sure that your database instances meet the following requirements:
        *   The source database instance must be an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition or X-Engine Edition instance.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The source instance and the destination instance are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is enabled for the source instance and the destination instance. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateCloudBenchTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudBenchTasksResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~). Before you call this API operation, make sure that your database instances meet the following requirements:
        *   The source database instance must be an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition or X-Engine Edition instance.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The source instance and the destination instance are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is enabled for the source instance and the destination instance. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateCloudBenchTasksRequest
        @return: CreateCloudBenchTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_bench_tasks_with_options(request, runtime)

    async def create_cloud_bench_tasks_async(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~). Before you call this API operation, make sure that your database instances meet the following requirements:
        *   The source database instance must be an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition or X-Engine Edition instance.
        *   The destination instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        *   The source instance and the destination instance are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](~~65405~~).
        *   DAS Professional Edition is enabled for the source instance and the destination instance. For more information, see [DAS Professional Edition](~~190912~~).
        
        @param request: CreateCloudBenchTasksRequest
        @return: CreateCloudBenchTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_bench_tasks_with_options_async(request, runtime)

    def create_diagnostic_report_with_options(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   RDS MySQL
        *   PolarDB for MySQL
        *   Redis
        
        @param request: CreateDiagnosticReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiagnosticReportResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   RDS MySQL
        *   PolarDB for MySQL
        *   Redis
        
        @param request: CreateDiagnosticReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiagnosticReportResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   RDS MySQL
        *   PolarDB for MySQL
        *   Redis
        
        @param request: CreateDiagnosticReportRequest
        @return: CreateDiagnosticReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   RDS MySQL
        *   PolarDB for MySQL
        *   Redis
        
        @param request: CreateDiagnosticReportRequest
        @return: CreateDiagnosticReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def create_kill_instance_session_task_with_options(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: CreateKillInstanceSessionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKillInstanceSessionTaskResponse
        """
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
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: CreateKillInstanceSessionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKillInstanceSessionTaskResponse
        """
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
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: CreateKillInstanceSessionTaskRequest
        @return: CreateKillInstanceSessionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_kill_instance_session_task_with_options(request, runtime)

    async def create_kill_instance_session_task_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: CreateKillInstanceSessionTaskRequest
        @return: CreateKillInstanceSessionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_kill_instance_session_task_with_options_async(request, runtime)

    def create_kill_instance_session_task_with_maintain_user_with_options(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='CreateKillInstanceSessionTaskWithMaintainUser',
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
            das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kill_instance_session_task_with_maintain_user_with_options_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='CreateKillInstanceSessionTaskWithMaintainUser',
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
            das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kill_instance_session_task_with_maintain_user(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_kill_instance_session_task_with_maintain_user_with_options(request, runtime)

    async def create_kill_instance_session_task_with_maintain_user_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_kill_instance_session_task_with_maintain_user_with_options_async(request, runtime)

    def create_query_optimize_tag_with_options(
        self,
        request: das20200116_models.CreateQueryOptimizeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: CreateQueryOptimizeTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueryOptimizeTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_ids):
            query['SqlIds'] = request.sql_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueryOptimizeTag',
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
            das20200116_models.CreateQueryOptimizeTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_query_optimize_tag_with_options_async(
        self,
        request: das20200116_models.CreateQueryOptimizeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: CreateQueryOptimizeTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueryOptimizeTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_ids):
            query['SqlIds'] = request.sql_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueryOptimizeTag',
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
            das20200116_models.CreateQueryOptimizeTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_query_optimize_tag(
        self,
        request: das20200116_models.CreateQueryOptimizeTagRequest,
    ) -> das20200116_models.CreateQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: CreateQueryOptimizeTagRequest
        @return: CreateQueryOptimizeTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_query_optimize_tag_with_options(request, runtime)

    async def create_query_optimize_tag_async(
        self,
        request: das20200116_models.CreateQueryOptimizeTagRequest,
    ) -> das20200116_models.CreateQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: CreateQueryOptimizeTagRequest
        @return: CreateQueryOptimizeTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_query_optimize_tag_with_options_async(request, runtime)

    def create_request_diagnosis_with_options(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: CreateRequestDiagnosisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRequestDiagnosisResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: CreateRequestDiagnosisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRequestDiagnosisResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: CreateRequestDiagnosisRequest
        @return: CreateRequestDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_request_diagnosis_with_options(request, runtime)

    async def create_request_diagnosis_async(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: CreateRequestDiagnosisRequest
        @return: CreateRequestDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_request_diagnosis_with_options_async(request, runtime)

    def create_storage_analysis_task_with_options(
        self,
        request: das20200116_models.CreateStorageAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateStorageAnalysisTaskResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: CreateStorageAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStorageAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStorageAnalysisTask',
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
            das20200116_models.CreateStorageAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_analysis_task_with_options_async(
        self,
        request: das20200116_models.CreateStorageAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateStorageAnalysisTaskResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: CreateStorageAnalysisTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStorageAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStorageAnalysisTask',
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
            das20200116_models.CreateStorageAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_analysis_task(
        self,
        request: das20200116_models.CreateStorageAnalysisTaskRequest,
    ) -> das20200116_models.CreateStorageAnalysisTaskResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: CreateStorageAnalysisTaskRequest
        @return: CreateStorageAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_storage_analysis_task_with_options(request, runtime)

    async def create_storage_analysis_task_async(
        self,
        request: das20200116_models.CreateStorageAnalysisTaskRequest,
    ) -> das20200116_models.CreateStorageAnalysisTaskResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: CreateStorageAnalysisTaskRequest
        @return: CreateStorageAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_storage_analysis_task_with_options_async(request, runtime)

    def delete_cloud_bench_task_with_options(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DeleteCloudBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DeleteCloudBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DeleteCloudBenchTaskRequest
        @return: DeleteCloudBenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_bench_task_with_options(request, runtime)

    async def delete_cloud_bench_task_async(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DeleteCloudBenchTaskRequest
        @return: DeleteCloudBenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_bench_task_with_options_async(request, runtime)

    def delete_stop_gateway_with_options(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        """
        This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](~~230665~~) operation.
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  If the heartbeat is lost between a DBGateway and the access point for more than 20 seconds, the DBGateway is considered stopped.
        
        @param request: DeleteStopGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStopGatewayResponse
        """
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
        """
        This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](~~230665~~) operation.
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  If the heartbeat is lost between a DBGateway and the access point for more than 20 seconds, the DBGateway is considered stopped.
        
        @param request: DeleteStopGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStopGatewayResponse
        """
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
        """
        This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](~~230665~~) operation.
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  If the heartbeat is lost between a DBGateway and the access point for more than 20 seconds, the DBGateway is considered stopped.
        
        @param request: DeleteStopGatewayRequest
        @return: DeleteStopGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_stop_gateway_with_options(request, runtime)

    async def delete_stop_gateway_async(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        """
        This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](~~230665~~) operation.
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  If the heartbeat is lost between a DBGateway and the access point for more than 20 seconds, the DBGateway is considered stopped.
        
        @param request: DeleteStopGatewayRequest
        @return: DeleteStopGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_stop_gateway_with_options_async(request, runtime)

    def describe_auto_scaling_config_with_options(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoScalingConfigResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoScalingConfigResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeAutoScalingConfigRequest
        @return: DescribeAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scaling_config_with_options(request, runtime)

    async def describe_auto_scaling_config_async(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeAutoScalingConfigRequest
        @return: DescribeAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_scaling_config_with_options_async(request, runtime)

    def describe_auto_scaling_history_with_options(
        self,
        request: das20200116_models.DescribeAutoScalingHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeAutoScalingHistoryResponse:
        """
        You can query only the history of automatic performance scaling of ApsaraDB RDS for MySQL instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: DescribeAutoScalingHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoScalingHistoryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoScalingHistory',
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
            das20200116_models.DescribeAutoScalingHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_scaling_history_with_options_async(
        self,
        request: das20200116_models.DescribeAutoScalingHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeAutoScalingHistoryResponse:
        """
        You can query only the history of automatic performance scaling of ApsaraDB RDS for MySQL instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: DescribeAutoScalingHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoScalingHistoryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoScalingHistory',
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
            das20200116_models.DescribeAutoScalingHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_scaling_history(
        self,
        request: das20200116_models.DescribeAutoScalingHistoryRequest,
    ) -> das20200116_models.DescribeAutoScalingHistoryResponse:
        """
        You can query only the history of automatic performance scaling of ApsaraDB RDS for MySQL instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: DescribeAutoScalingHistoryRequest
        @return: DescribeAutoScalingHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scaling_history_with_options(request, runtime)

    async def describe_auto_scaling_history_async(
        self,
        request: das20200116_models.DescribeAutoScalingHistoryRequest,
    ) -> das20200116_models.DescribeAutoScalingHistoryResponse:
        """
        You can query only the history of automatic performance scaling of ApsaraDB RDS for MySQL instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: DescribeAutoScalingHistoryRequest
        @return: DescribeAutoScalingHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_scaling_history_with_options_async(request, runtime)

    def describe_cache_analysis_job_with_options(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisJobResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisJobResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobRequest
        @return: DescribeCacheAnalysisJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_job_with_options(request, runtime)

    async def describe_cache_analysis_job_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobRequest
        @return: DescribeCacheAnalysisJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_job_with_options_async(request, runtime)

    def describe_cache_analysis_jobs_with_options(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisJobsResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCacheAnalysisJobsResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobsRequest
        @return: DescribeCacheAnalysisJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_jobs_with_options(request, runtime)

    async def describe_cache_analysis_jobs_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis.
        
        @param request: DescribeCacheAnalysisJobsRequest
        @return: DescribeCacheAnalysisJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_jobs_with_options_async(request, runtime)

    def describe_cloud_bench_tasks_with_options(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudBenchTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudBenchTasksResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudBenchTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudBenchTasksResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudBenchTasksRequest
        @return: DescribeCloudBenchTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_bench_tasks_with_options(request, runtime)

    async def describe_cloud_bench_tasks_async(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudBenchTasksRequest
        @return: DescribeCloudBenchTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_bench_tasks_with_options_async(request, runtime)

    def describe_cloudbench_task_with_options(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudbenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudbenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskRequest
        @return: DescribeCloudbenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_with_options(request, runtime)

    async def describe_cloudbench_task_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskRequest
        @return: DescribeCloudbenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloudbench_task_with_options_async(request, runtime)

    def describe_cloudbench_task_config_with_options(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudbenchTaskConfigResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudbenchTaskConfigResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskConfigRequest
        @return: DescribeCloudbenchTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloudbench_task_config_with_options(request, runtime)

    async def describe_cloudbench_task_config_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: DescribeCloudbenchTaskConfigRequest
        @return: DescribeCloudbenchTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloudbench_task_config_with_options_async(request, runtime)

    def describe_diagnostic_report_list_with_options(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB for Redis
        
        @param request: DescribeDiagnosticReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosticReportListResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB for Redis
        
        @param request: DescribeDiagnosticReportListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosticReportListResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB for Redis
        
        @param request: DescribeDiagnosticReportListRequest
        @return: DescribeDiagnosticReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    async def describe_diagnostic_report_list_async(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB for Redis
        
        @param request: DescribeDiagnosticReportListRequest
        @return: DescribeDiagnosticReportListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_report_list_with_options_async(request, runtime)

    def describe_hot_big_keys_with_options(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        """
        This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        *   The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotBigKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHotBigKeysResponse
        """
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
        """
        This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        *   The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotBigKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHotBigKeysResponse
        """
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
        """
        This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        *   The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotBigKeysRequest
        @return: DescribeHotBigKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_big_keys_with_options(request, runtime)

    async def describe_hot_big_keys_async(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        """
        This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        *   The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotBigKeysRequest
        @return: DescribeHotBigKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hot_big_keys_with_options_async(request, runtime)

    def describe_hot_keys_with_options(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotKeysResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        *   The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For more information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHotKeysResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        *   The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For more information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHotKeysResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        *   The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For more information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotKeysRequest
        @return: DescribeHotKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_keys_with_options(request, runtime)

    async def describe_hot_keys_async(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
    ) -> das20200116_models.DescribeHotKeysResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        *   The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For more information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeHotKeysRequest
        @return: DescribeHotKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hot_keys_with_options_async(request, runtime)

    def describe_instance_das_pro_with_options(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeInstanceDasProRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDasProResponse
        """
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
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeInstanceDasProRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceDasProResponse
        """
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
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeInstanceDasProRequest
        @return: DescribeInstanceDasProResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_das_pro_with_options(request, runtime)

    async def describe_instance_das_pro_async(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeInstanceDasProRequest
        @return: DescribeInstanceDasProResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_das_pro_with_options_async(request, runtime)

    def describe_top_big_keys_with_options(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        """
        The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeTopBigKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopBigKeysResponse
        """
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
        """
        The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeTopBigKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopBigKeysResponse
        """
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
        """
        The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeTopBigKeysRequest
        @return: DescribeTopBigKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_top_big_keys_with_options(request, runtime)

    async def describe_top_big_keys_async(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        """
        The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [ModifyInstanceMinorVersion](~~129381~~) and [DescribeEngineVersion](~~95268~~).
        
        @param request: DescribeTopBigKeysRequest
        @return: DescribeTopBigKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_big_keys_with_options_async(request, runtime)

    def describe_top_hot_keys_with_options(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        """
        If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [DescribeEngineVersion](~~95268~~) and [ModifyInstanceMinorVersion](~~129381~~).
        
        @param request: DescribeTopHotKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopHotKeysResponse
        """
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
        """
        If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [DescribeEngineVersion](~~95268~~) and [ModifyInstanceMinorVersion](~~129381~~).
        
        @param request: DescribeTopHotKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopHotKeysResponse
        """
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
        """
        If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [DescribeEngineVersion](~~95268~~) and [ModifyInstanceMinorVersion](~~129381~~).
        
        @param request: DescribeTopHotKeysRequest
        @return: DescribeTopHotKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_top_hot_keys_with_options(request, runtime)

    async def describe_top_hot_keys_async(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        """
        If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        *   The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        *   The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        *   The ApsaraDB for Redis instance is updated to the latest minor version.
        >  For information about how to query and update the minor version of an instance, see [DescribeEngineVersion](~~95268~~) and [ModifyInstanceMinorVersion](~~129381~~).
        
        @param request: DescribeTopHotKeysRequest
        @return: DescribeTopHotKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_hot_keys_with_options_async(request, runtime)

    def disable_all_sql_concurrency_control_rules_with_options(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableAllSqlConcurrencyControlRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAllSqlConcurrencyControlRulesResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableAllSqlConcurrencyControlRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAllSqlConcurrencyControlRulesResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableAllSqlConcurrencyControlRulesRequest
        @return: DisableAllSqlConcurrencyControlRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_all_sql_concurrency_control_rules_with_options(request, runtime)

    async def disable_all_sql_concurrency_control_rules_async(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableAllSqlConcurrencyControlRulesRequest
        @return: DisableAllSqlConcurrencyControlRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_all_sql_concurrency_control_rules_with_options_async(request, runtime)

    def disable_auto_resource_optimize_rules_with_options(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        """
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoResourceOptimizeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoResourceOptimizeRulesResponse
        """
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
        """
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoResourceOptimizeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoResourceOptimizeRulesResponse
        """
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
        """
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoResourceOptimizeRulesRequest
        @return: DisableAutoResourceOptimizeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_resource_optimize_rules_with_options(request, runtime)

    async def disable_auto_resource_optimize_rules_async(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        """
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoResourceOptimizeRulesRequest
        @return: DisableAutoResourceOptimizeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_resource_optimize_rules_with_options_async(request, runtime)

    def disable_auto_throttle_rules_with_options(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        """
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoThrottleRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoThrottleRulesResponse
        """
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
        """
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoThrottleRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoThrottleRulesResponse
        """
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
        """
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoThrottleRulesRequest
        @return: DisableAutoThrottleRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_throttle_rules_with_options(request, runtime)

    async def disable_auto_throttle_rules_async(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        """
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: DisableAutoThrottleRulesRequest
        @return: DisableAutoThrottleRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_throttle_rules_with_options_async(request, runtime)

    def disable_das_pro_with_options(
        self,
        request: das20200116_models.DisableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableDasProResponse:
        """
        For information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DisableDasProRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDasProResponse
        """
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
        """
        For information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DisableDasProRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDasProResponse
        """
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
        """
        For information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DisableDasProRequest
        @return: DisableDasProResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_das_pro_with_options(request, runtime)

    async def disable_das_pro_async(
        self,
        request: das20200116_models.DisableDasProRequest,
    ) -> das20200116_models.DisableDasProResponse:
        """
        For information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DisableDasProRequest
        @return: DisableDasProResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_das_pro_with_options_async(request, runtime)

    def disable_instance_das_config_with_options(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances.
        
        @param request: DisableInstanceDasConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInstanceDasConfigResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances.
        
        @param request: DisableInstanceDasConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInstanceDasConfigResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances.
        
        @param request: DisableInstanceDasConfigRequest
        @return: DisableInstanceDasConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_das_config_with_options(request, runtime)

    async def disable_instance_das_config_async(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation is applicable only to ApsaraDB for Redis instances.
        
        @param request: DisableInstanceDasConfigRequest
        @return: DisableInstanceDasConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_das_config_with_options_async(request, runtime)

    def disable_sql_concurrency_control_with_options(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        """
        This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableSqlConcurrencyControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSqlConcurrencyControlResponse
        """
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
        """
        This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableSqlConcurrencyControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSqlConcurrencyControlResponse
        """
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
        """
        This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableSqlConcurrencyControlRequest
        @return: DisableSqlConcurrencyControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_concurrency_control_with_options(request, runtime)

    async def disable_sql_concurrency_control_async(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        """
        This operation is applicable to the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: DisableSqlConcurrencyControlRequest
        @return: DisableSqlConcurrencyControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_sql_concurrency_control_with_options_async(request, runtime)

    def enable_das_pro_with_options(
        self,
        request: das20200116_models.EnableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableDasProResponse:
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: EnableDasProRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDasProResponse
        """
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
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: EnableDasProRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDasProResponse
        """
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
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: EnableDasProRequest
        @return: EnableDasProResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_das_pro_with_options(request, runtime)

    async def enable_das_pro_async(
        self,
        request: das20200116_models.EnableDasProRequest,
    ) -> das20200116_models.EnableDasProResponse:
        """
        For more information about database instances that support DAS Professional Edition, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: EnableDasProRequest
        @return: EnableDasProResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_das_pro_with_options_async(request, runtime)

    def enable_sql_concurrency_control_with_options(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: EnableSqlConcurrencyControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSqlConcurrencyControlResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: EnableSqlConcurrencyControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSqlConcurrencyControlResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: EnableSqlConcurrencyControlRequest
        @return: EnableSqlConcurrencyControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_concurrency_control_with_options(request, runtime)

    async def enable_sql_concurrency_control_async(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: EnableSqlConcurrencyControlRequest
        @return: EnableSqlConcurrencyControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_sql_concurrency_control_with_options_async(request, runtime)

    def get_async_error_request_list_by_code_with_options(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        """
        >  When an asynchronous call is made, the complete query results are not immediately returned. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which DAS Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestListByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncErrorRequestListByCodeResponse
        """
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
        """
        >  When an asynchronous call is made, the complete query results are not immediately returned. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which DAS Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestListByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncErrorRequestListByCodeResponse
        """
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
        """
        >  When an asynchronous call is made, the complete query results are not immediately returned. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which DAS Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestListByCodeRequest
        @return: GetAsyncErrorRequestListByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_list_by_code_with_options(request, runtime)

    async def get_async_error_request_list_by_code_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        """
        >  When an asynchronous call is made, the complete query results are not immediately returned. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which DAS Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestListByCodeRequest
        @return: GetAsyncErrorRequestListByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_error_request_list_by_code_with_options_async(request, runtime)

    def get_async_error_request_stat_by_code_with_options(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncErrorRequestStatByCodeResponse
        """
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
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncErrorRequestStatByCodeResponse
        """
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
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatByCodeRequest
        @return: GetAsyncErrorRequestStatByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_stat_by_code_with_options(request, runtime)

    async def get_async_error_request_stat_by_code_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatByCodeRequest
        @return: GetAsyncErrorRequestStatByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_error_request_stat_by_code_with_options_async(request, runtime)

    def get_async_error_request_stat_result_with_options(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncErrorRequestStatResultResponse
        """
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
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncErrorRequestStatResultResponse
        """
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
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatResultRequest
        @return: GetAsyncErrorRequestStatResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_error_request_stat_result_with_options(request, runtime)

    async def get_async_error_request_stat_result_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        """
        >  When an asynchronous call is made, the complete query results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. The complete query results are returned until the value of **isFinish** is **true**.
        *   This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetAsyncErrorRequestStatResultRequest
        @return: GetAsyncErrorRequestStatResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_error_request_stat_result_with_options_async(request, runtime)

    def get_auto_increment_usage_statistic_with_options(
        self,
        request: das20200116_models.GetAutoIncrementUsageStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoIncrementUsageStatisticResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: GetAutoIncrementUsageStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoIncrementUsageStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_names):
            query['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ratio_filter):
            query['RatioFilter'] = request.ratio_filter
        if not UtilClient.is_unset(request.real_time):
            query['RealTime'] = request.real_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoIncrementUsageStatistic',
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
            das20200116_models.GetAutoIncrementUsageStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_increment_usage_statistic_with_options_async(
        self,
        request: das20200116_models.GetAutoIncrementUsageStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoIncrementUsageStatisticResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: GetAutoIncrementUsageStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoIncrementUsageStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_names):
            query['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ratio_filter):
            query['RatioFilter'] = request.ratio_filter
        if not UtilClient.is_unset(request.real_time):
            query['RealTime'] = request.real_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoIncrementUsageStatistic',
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
            das20200116_models.GetAutoIncrementUsageStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_increment_usage_statistic(
        self,
        request: das20200116_models.GetAutoIncrementUsageStatisticRequest,
    ) -> das20200116_models.GetAutoIncrementUsageStatisticResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: GetAutoIncrementUsageStatisticRequest
        @return: GetAutoIncrementUsageStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_increment_usage_statistic_with_options(request, runtime)

    async def get_auto_increment_usage_statistic_async(
        self,
        request: das20200116_models.GetAutoIncrementUsageStatisticRequest,
    ) -> das20200116_models.GetAutoIncrementUsageStatisticResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: GetAutoIncrementUsageStatisticRequest
        @return: GetAutoIncrementUsageStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_increment_usage_statistic_with_options_async(request, runtime)

    def get_auto_resource_optimize_rules_with_options(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: GetAutoResourceOptimizeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoResourceOptimizeRulesResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: GetAutoResourceOptimizeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoResourceOptimizeRulesResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: GetAutoResourceOptimizeRulesRequest
        @return: GetAutoResourceOptimizeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_resource_optimize_rules_with_options(request, runtime)

    async def get_auto_resource_optimize_rules_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: GetAutoResourceOptimizeRulesRequest
        @return: GetAutoResourceOptimizeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_resource_optimize_rules_with_options_async(request, runtime)

    def get_auto_throttle_rules_with_options(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0.
        *   PolarDB for MySQL Cluster Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, or PolarDB for MySQL X-Engine Edition instance that runs MySQL 8.0.
        
        @param request: GetAutoThrottleRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoThrottleRulesResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0.
        *   PolarDB for MySQL Cluster Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, or PolarDB for MySQL X-Engine Edition instance that runs MySQL 8.0.
        
        @param request: GetAutoThrottleRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoThrottleRulesResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0.
        *   PolarDB for MySQL Cluster Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, or PolarDB for MySQL X-Engine Edition instance that runs MySQL 8.0.
        
        @param request: GetAutoThrottleRulesRequest
        @return: GetAutoThrottleRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_throttle_rules_with_options(request, runtime)

    async def get_auto_throttle_rules_async(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0.
        *   PolarDB for MySQL Cluster Edition instance that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, or PolarDB for MySQL X-Engine Edition instance that runs MySQL 8.0.
        
        @param request: GetAutoThrottleRulesRequest
        @return: GetAutoThrottleRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_throttle_rules_with_options_async(request, runtime)

    def get_autonomous_notify_event_content_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutonomousNotifyEventContentResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutonomousNotifyEventContentResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventContentRequest
        @return: GetAutonomousNotifyEventContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_event_content_with_options(request, runtime)

    async def get_autonomous_notify_event_content_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventContentRequest
        @return: GetAutonomousNotifyEventContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_event_content_with_options_async(request, runtime)

    def get_autonomous_notify_events_in_range_with_options(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventsInRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutonomousNotifyEventsInRangeResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventsInRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutonomousNotifyEventsInRangeResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventsInRangeRequest
        @return: GetAutonomousNotifyEventsInRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_autonomous_notify_events_in_range_with_options(request, runtime)

    async def get_autonomous_notify_events_in_range_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](~~152139~~).
        
        @param request: GetAutonomousNotifyEventsInRangeRequest
        @return: GetAutonomousNotifyEventsInRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_autonomous_notify_events_in_range_with_options_async(request, runtime)

    def get_blocking_detail_list_with_options(
        self,
        request: das20200116_models.GetBlockingDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetBlockingDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetBlockingDetailListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBlockingDetailListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name_list):
            query['DbNameList'] = request.db_name_list
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_hash):
            query['QueryHash'] = request.query_hash
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBlockingDetailList',
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
            das20200116_models.GetBlockingDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_blocking_detail_list_with_options_async(
        self,
        request: das20200116_models.GetBlockingDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetBlockingDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetBlockingDetailListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBlockingDetailListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name_list):
            query['DbNameList'] = request.db_name_list
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_hash):
            query['QueryHash'] = request.query_hash
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBlockingDetailList',
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
            das20200116_models.GetBlockingDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_blocking_detail_list(
        self,
        request: das20200116_models.GetBlockingDetailListRequest,
    ) -> das20200116_models.GetBlockingDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetBlockingDetailListRequest
        @return: GetBlockingDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_blocking_detail_list_with_options(request, runtime)

    async def get_blocking_detail_list_async(
        self,
        request: das20200116_models.GetBlockingDetailListRequest,
    ) -> das20200116_models.GetBlockingDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetBlockingDetailListRequest
        @return: GetBlockingDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_blocking_detail_list_with_options_async(request, runtime)

    def get_dbinstance_connectivity_diagnosis_with_options(
        self,
        request: das20200116_models.GetDBInstanceConnectivityDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDBInstanceConnectivityDiagnosisResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetDBInstanceConnectivityDiagnosisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDBInstanceConnectivityDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBInstanceConnectivityDiagnosis',
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
            das20200116_models.GetDBInstanceConnectivityDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dbinstance_connectivity_diagnosis_with_options_async(
        self,
        request: das20200116_models.GetDBInstanceConnectivityDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDBInstanceConnectivityDiagnosisResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetDBInstanceConnectivityDiagnosisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDBInstanceConnectivityDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBInstanceConnectivityDiagnosis',
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
            das20200116_models.GetDBInstanceConnectivityDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dbinstance_connectivity_diagnosis(
        self,
        request: das20200116_models.GetDBInstanceConnectivityDiagnosisRequest,
    ) -> das20200116_models.GetDBInstanceConnectivityDiagnosisResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetDBInstanceConnectivityDiagnosisRequest
        @return: GetDBInstanceConnectivityDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dbinstance_connectivity_diagnosis_with_options(request, runtime)

    async def get_dbinstance_connectivity_diagnosis_async(
        self,
        request: das20200116_models.GetDBInstanceConnectivityDiagnosisRequest,
    ) -> das20200116_models.GetDBInstanceConnectivityDiagnosisResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetDBInstanceConnectivityDiagnosisRequest
        @return: GetDBInstanceConnectivityDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dbinstance_connectivity_diagnosis_with_options_async(request, runtime)

    def get_das_pro_service_usage_with_options(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        """
        For information about databases that are supported, see [Overview](~~190912~~).
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDasProServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDasProServiceUsageResponse
        """
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
        """
        For information about databases that are supported, see [Overview](~~190912~~).
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDasProServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDasProServiceUsageResponse
        """
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
        """
        For information about databases that are supported, see [Overview](~~190912~~).
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDasProServiceUsageRequest
        @return: GetDasProServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_das_pro_service_usage_with_options(request, runtime)

    async def get_das_pro_service_usage_async(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        """
        For information about databases that are supported, see [Overview](~~190912~~).
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDasProServiceUsageRequest
        @return: GetDasProServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_das_pro_service_usage_with_options_async(request, runtime)

    def get_das_sqllog_hot_data_with_options(
        self,
        request: das20200116_models.GetDasSQLLogHotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDasSQLLogHotDataResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL database or a PolarDB for MySQL database in the China (Shanghai) region is connected to DAS.
        *   The new SQL Explorer and Audit feature is enabled for the database instance. For more information, see the [Enable the SQL Explorer and Audit feature](~~92561~~) section of the "Overview" topic.
        >  You can query only the data that is generated after the new SQL Explorer and Audit feature is enabled. The start time can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed 24 hours.
        
        @param request: GetDasSQLLogHotDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDasSQLLogHotDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.child_dbinstance_ids):
            body['ChildDBInstanceIDs'] = request.child_dbinstance_ids
        if not UtilClient.is_unset(request.dbname):
            body['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.fail):
            body['Fail'] = request.fail
        if not UtilClient.is_unset(request.host_address):
            body['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logical_operator):
            body['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.max_latancy):
            body['MaxLatancy'] = request.max_latancy
        if not UtilClient.is_unset(request.max_records_per_page):
            body['MaxRecordsPerPage'] = request.max_records_per_page
        if not UtilClient.is_unset(request.max_rows):
            body['MaxRows'] = request.max_rows
        if not UtilClient.is_unset(request.max_scan_rows):
            body['MaxScanRows'] = request.max_scan_rows
        if not UtilClient.is_unset(request.max_spill_cnt):
            body['MaxSpillCnt'] = request.max_spill_cnt
        if not UtilClient.is_unset(request.min_latancy):
            body['MinLatancy'] = request.min_latancy
        if not UtilClient.is_unset(request.min_rows):
            body['MinRows'] = request.min_rows
        if not UtilClient.is_unset(request.min_scan_rows):
            body['MinScanRows'] = request.min_scan_rows
        if not UtilClient.is_unset(request.min_spill_cnt):
            body['MinSpillCnt'] = request.min_spill_cnt
        if not UtilClient.is_unset(request.page_numbers):
            body['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.query_keyword):
            body['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.sort_key):
            body['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_method):
            body['SortMethod'] = request.sort_method
        if not UtilClient.is_unset(request.sql_type):
            body['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.state):
            body['State'] = request.state
        if not UtilClient.is_unset(request.thread_id):
            body['ThreadID'] = request.thread_id
        if not UtilClient.is_unset(request.trace_id):
            body['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDasSQLLogHotData',
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
            das20200116_models.GetDasSQLLogHotDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_das_sqllog_hot_data_with_options_async(
        self,
        request: das20200116_models.GetDasSQLLogHotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDasSQLLogHotDataResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL database or a PolarDB for MySQL database in the China (Shanghai) region is connected to DAS.
        *   The new SQL Explorer and Audit feature is enabled for the database instance. For more information, see the [Enable the SQL Explorer and Audit feature](~~92561~~) section of the "Overview" topic.
        >  You can query only the data that is generated after the new SQL Explorer and Audit feature is enabled. The start time can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed 24 hours.
        
        @param request: GetDasSQLLogHotDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDasSQLLogHotDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.child_dbinstance_ids):
            body['ChildDBInstanceIDs'] = request.child_dbinstance_ids
        if not UtilClient.is_unset(request.dbname):
            body['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.fail):
            body['Fail'] = request.fail
        if not UtilClient.is_unset(request.host_address):
            body['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logical_operator):
            body['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.max_latancy):
            body['MaxLatancy'] = request.max_latancy
        if not UtilClient.is_unset(request.max_records_per_page):
            body['MaxRecordsPerPage'] = request.max_records_per_page
        if not UtilClient.is_unset(request.max_rows):
            body['MaxRows'] = request.max_rows
        if not UtilClient.is_unset(request.max_scan_rows):
            body['MaxScanRows'] = request.max_scan_rows
        if not UtilClient.is_unset(request.max_spill_cnt):
            body['MaxSpillCnt'] = request.max_spill_cnt
        if not UtilClient.is_unset(request.min_latancy):
            body['MinLatancy'] = request.min_latancy
        if not UtilClient.is_unset(request.min_rows):
            body['MinRows'] = request.min_rows
        if not UtilClient.is_unset(request.min_scan_rows):
            body['MinScanRows'] = request.min_scan_rows
        if not UtilClient.is_unset(request.min_spill_cnt):
            body['MinSpillCnt'] = request.min_spill_cnt
        if not UtilClient.is_unset(request.page_numbers):
            body['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.query_keyword):
            body['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.sort_key):
            body['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_method):
            body['SortMethod'] = request.sort_method
        if not UtilClient.is_unset(request.sql_type):
            body['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.state):
            body['State'] = request.state
        if not UtilClient.is_unset(request.thread_id):
            body['ThreadID'] = request.thread_id
        if not UtilClient.is_unset(request.trace_id):
            body['TraceId'] = request.trace_id
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDasSQLLogHotData',
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
            das20200116_models.GetDasSQLLogHotDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_das_sqllog_hot_data(
        self,
        request: das20200116_models.GetDasSQLLogHotDataRequest,
    ) -> das20200116_models.GetDasSQLLogHotDataResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL database or a PolarDB for MySQL database in the China (Shanghai) region is connected to DAS.
        *   The new SQL Explorer and Audit feature is enabled for the database instance. For more information, see the [Enable the SQL Explorer and Audit feature](~~92561~~) section of the "Overview" topic.
        >  You can query only the data that is generated after the new SQL Explorer and Audit feature is enabled. The start time can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed 24 hours.
        
        @param request: GetDasSQLLogHotDataRequest
        @return: GetDasSQLLogHotDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_das_sqllog_hot_data_with_options(request, runtime)

    async def get_das_sqllog_hot_data_async(
        self,
        request: das20200116_models.GetDasSQLLogHotDataRequest,
    ) -> das20200116_models.GetDasSQLLogHotDataResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL database or a PolarDB for MySQL database in the China (Shanghai) region is connected to DAS.
        *   The new SQL Explorer and Audit feature is enabled for the database instance. For more information, see the [Enable the SQL Explorer and Audit feature](~~92561~~) section of the "Overview" topic.
        >  You can query only the data that is generated after the new SQL Explorer and Audit feature is enabled. The start time can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed 24 hours.
        
        @param request: GetDasSQLLogHotDataRequest
        @return: GetDasSQLLogHotDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_das_sqllog_hot_data_with_options_async(request, runtime)

    def get_dead_lock_detail_list_with_options(
        self,
        request: das20200116_models.GetDeadLockDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDeadLockDetailListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadLockDetailListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name_list):
            query['DbNameList'] = request.db_name_list
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
            action='GetDeadLockDetailList',
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
            das20200116_models.GetDeadLockDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dead_lock_detail_list_with_options_async(
        self,
        request: das20200116_models.GetDeadLockDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDeadLockDetailListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadLockDetailListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name_list):
            query['DbNameList'] = request.db_name_list
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
            action='GetDeadLockDetailList',
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
            das20200116_models.GetDeadLockDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dead_lock_detail_list(
        self,
        request: das20200116_models.GetDeadLockDetailListRequest,
    ) -> das20200116_models.GetDeadLockDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDeadLockDetailListRequest
        @return: GetDeadLockDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dead_lock_detail_list_with_options(request, runtime)

    async def get_dead_lock_detail_list_async(
        self,
        request: das20200116_models.GetDeadLockDetailListRequest,
    ) -> das20200116_models.GetDeadLockDetailListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDeadLockDetailListRequest
        @return: GetDeadLockDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dead_lock_detail_list_with_options_async(request, runtime)

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
        """
        >  The complete query results are not immediately returned after an asynchronous request is sent. If the value of *isFinish** is **false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetErrorRequestSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorRequestSampleResponse
        """
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
        """
        >  The complete query results are not immediately returned after an asynchronous request is sent. If the value of *isFinish** is **false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetErrorRequestSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorRequestSampleResponse
        """
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
        """
        >  The complete query results are not immediately returned after an asynchronous request is sent. If the value of *isFinish** is **false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetErrorRequestSampleRequest
        @return: GetErrorRequestSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_error_request_sample_with_options(request, runtime)

    async def get_error_request_sample_async(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        """
        >  The complete query results are not immediately returned after an asynchronous request is sent. If the value of *isFinish** is **false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of **isFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Professional Edition is enabled. For more information, see [Purchase DAS Professional Edition](~~163298~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetErrorRequestSampleRequest
        @return: GetErrorRequestSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_error_request_sample_with_options_async(request, runtime)

    def get_event_subscription_with_options(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetEventSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventSubscriptionResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetEventSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventSubscriptionResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetEventSubscriptionRequest
        @return: GetEventSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_event_subscription_with_options(request, runtime)

    async def get_event_subscription_async(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: GetEventSubscriptionRequest
        @return: GetEventSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_event_subscription_with_options_async(request, runtime)

    def get_full_request_origin_stat_by_instance_id_with_options(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestOriginStatByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFullRequestOriginStatByInstanceIdResponse
        """
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
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestOriginStatByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFullRequestOriginStatByInstanceIdResponse
        """
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
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestOriginStatByInstanceIdRequest
        @return: GetFullRequestOriginStatByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_full_request_origin_stat_by_instance_id_with_options(request, runtime)

    async def get_full_request_origin_stat_by_instance_id_async(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestOriginStatByInstanceIdRequest
        @return: GetFullRequestOriginStatByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_full_request_origin_stat_by_instance_id_with_options_async(request, runtime)

    def get_full_request_sample_by_instance_id_with_options(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about the database engines that support SQL Explorer, see [SQL Explorer](~~204096~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestSampleByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFullRequestSampleByInstanceIdResponse
        """
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
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about the database engines that support SQL Explorer, see [SQL Explorer](~~204096~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestSampleByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFullRequestSampleByInstanceIdResponse
        """
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
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about the database engines that support SQL Explorer, see [SQL Explorer](~~204096~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestSampleByInstanceIdRequest
        @return: GetFullRequestSampleByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_full_request_sample_by_instance_id_with_options(request, runtime)

    async def get_full_request_sample_by_instance_id_async(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        """
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about the database engines that support SQL Explorer, see [SQL Explorer](~~204096~~).
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestSampleByInstanceIdRequest
        @return: GetFullRequestSampleByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_full_request_sample_by_instance_id_with_options_async(request, runtime)

    def get_full_request_stat_result_by_instance_id_with_options(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        """
        >  The complete query results are not returned immediately after an asynchronous request is sent. If the value of isFinish is *false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of isFinish is **true**.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestStatResultByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFullRequestStatResultByInstanceIdResponse
        """
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
        """
        >  The complete query results are not returned immediately after an asynchronous request is sent. If the value of isFinish is *false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of isFinish is **true**.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestStatResultByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFullRequestStatResultByInstanceIdResponse
        """
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
        """
        >  The complete query results are not returned immediately after an asynchronous request is sent. If the value of isFinish is *false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of isFinish is **true**.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestStatResultByInstanceIdRequest
        @return: GetFullRequestStatResultByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_full_request_stat_result_by_instance_id_with_options(request, runtime)

    async def get_full_request_stat_result_by_instance_id_async(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        """
        >  The complete query results are not returned immediately after an asynchronous request is sent. If the value of isFinish is *false** in the response, wait for 1 second and send the request again. The complete query results are returned until the value of isFinish is **true**.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](~~204096~~).
        *   For more information about database instances that support SQL Explorer, see [Overview](~~190912~~).
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
        @param request: GetFullRequestStatResultByInstanceIdRequest
        @return: GetFullRequestStatResultByInstanceIdResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](~~205659~~).
        Before you call this operation, take note of the following items:
        *   This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of DAS SDK must be V1.0.3 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceInspectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceInspectionsResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](~~205659~~).
        Before you call this operation, take note of the following items:
        *   This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of DAS SDK must be V1.0.3 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceInspectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceInspectionsResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](~~205659~~).
        Before you call this operation, take note of the following items:
        *   This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of DAS SDK must be V1.0.3 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceInspectionsRequest
        @return: GetInstanceInspectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_inspections_with_options(request, runtime)

    async def get_instance_inspections_async(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        """
        Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](~~205659~~).
        Before you call this operation, take note of the following items:
        *   This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        *   If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of DAS SDK must be V1.0.3 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceInspectionsRequest
        @return: GetInstanceInspectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_inspections_with_options_async(request, runtime)

    def get_instance_missing_index_list_with_options(
        self,
        request: das20200116_models.GetInstanceMissingIndexListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceMissingIndexListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceMissingIndexListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceMissingIndexListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avg_total_user_cost):
            query['AvgTotalUserCost'] = request.avg_total_user_cost
        if not UtilClient.is_unset(request.avg_user_impact):
            query['AvgUserImpact'] = request.avg_user_impact
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.index_count):
            query['IndexCount'] = request.index_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_name):
            query['ObjectName'] = request.object_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reserved_pages):
            query['ReservedPages'] = request.reserved_pages
        if not UtilClient.is_unset(request.reserved_size):
            query['ReservedSize'] = request.reserved_size
        if not UtilClient.is_unset(request.row_count):
            query['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.unique_compiles):
            query['UniqueCompiles'] = request.unique_compiles
        if not UtilClient.is_unset(request.user_scans):
            query['UserScans'] = request.user_scans
        if not UtilClient.is_unset(request.user_seeks):
            query['UserSeeks'] = request.user_seeks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceMissingIndexList',
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
            das20200116_models.GetInstanceMissingIndexListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_missing_index_list_with_options_async(
        self,
        request: das20200116_models.GetInstanceMissingIndexListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceMissingIndexListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceMissingIndexListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceMissingIndexListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avg_total_user_cost):
            query['AvgTotalUserCost'] = request.avg_total_user_cost
        if not UtilClient.is_unset(request.avg_user_impact):
            query['AvgUserImpact'] = request.avg_user_impact
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.index_count):
            query['IndexCount'] = request.index_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.object_name):
            query['ObjectName'] = request.object_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reserved_pages):
            query['ReservedPages'] = request.reserved_pages
        if not UtilClient.is_unset(request.reserved_size):
            query['ReservedSize'] = request.reserved_size
        if not UtilClient.is_unset(request.row_count):
            query['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.unique_compiles):
            query['UniqueCompiles'] = request.unique_compiles
        if not UtilClient.is_unset(request.user_scans):
            query['UserScans'] = request.user_scans
        if not UtilClient.is_unset(request.user_seeks):
            query['UserSeeks'] = request.user_seeks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceMissingIndexList',
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
            das20200116_models.GetInstanceMissingIndexListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_missing_index_list(
        self,
        request: das20200116_models.GetInstanceMissingIndexListRequest,
    ) -> das20200116_models.GetInstanceMissingIndexListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceMissingIndexListRequest
        @return: GetInstanceMissingIndexListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_missing_index_list_with_options(request, runtime)

    async def get_instance_missing_index_list_async(
        self,
        request: das20200116_models.GetInstanceMissingIndexListRequest,
    ) -> das20200116_models.GetInstanceMissingIndexListResponse:
        """
        This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetInstanceMissingIndexListRequest
        @return: GetInstanceMissingIndexListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_missing_index_list_with_options_async(request, runtime)

    def get_instance_sql_optimize_statistic_with_options(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
        @param request: GetInstanceSqlOptimizeStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceSqlOptimizeStatisticResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
        @param request: GetInstanceSqlOptimizeStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceSqlOptimizeStatisticResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
        @param request: GetInstanceSqlOptimizeStatisticRequest
        @return: GetInstanceSqlOptimizeStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_sql_optimize_statistic_with_options(request, runtime)

    async def get_instance_sql_optimize_statistic_async(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
        @param request: GetInstanceSqlOptimizeStatisticRequest
        @return: GetInstanceSqlOptimizeStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_sql_optimize_statistic_with_options_async(request, runtime)

    def get_kill_instance_session_task_result_with_options(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetKillInstanceSessionTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKillInstanceSessionTaskResultResponse
        """
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
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetKillInstanceSessionTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKillInstanceSessionTaskResultResponse
        """
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
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetKillInstanceSessionTaskResultRequest
        @return: GetKillInstanceSessionTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_kill_instance_session_task_result_with_options(request, runtime)

    async def get_kill_instance_session_task_result_async(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetKillInstanceSessionTaskResultRequest
        @return: GetKillInstanceSessionTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_kill_instance_session_task_result_with_options_async(request, runtime)

    def get_mongo_dbcurrent_op_with_options(
        self,
        request: das20200116_models.GetMongoDBCurrentOpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetMongoDBCurrentOpResponse:
        """
        This operation is applicable only to MongoDB instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: GetMongoDBCurrentOpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMongoDBCurrentOpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_doc):
            query['FilterDoc'] = request.filter_doc
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMongoDBCurrentOp',
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
            das20200116_models.GetMongoDBCurrentOpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mongo_dbcurrent_op_with_options_async(
        self,
        request: das20200116_models.GetMongoDBCurrentOpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetMongoDBCurrentOpResponse:
        """
        This operation is applicable only to MongoDB instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: GetMongoDBCurrentOpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMongoDBCurrentOpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_doc):
            query['FilterDoc'] = request.filter_doc
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMongoDBCurrentOp',
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
            das20200116_models.GetMongoDBCurrentOpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mongo_dbcurrent_op(
        self,
        request: das20200116_models.GetMongoDBCurrentOpRequest,
    ) -> das20200116_models.GetMongoDBCurrentOpResponse:
        """
        This operation is applicable only to MongoDB instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: GetMongoDBCurrentOpRequest
        @return: GetMongoDBCurrentOpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mongo_dbcurrent_op_with_options(request, runtime)

    async def get_mongo_dbcurrent_op_async(
        self,
        request: das20200116_models.GetMongoDBCurrentOpRequest,
    ) -> das20200116_models.GetMongoDBCurrentOpResponse:
        """
        This operation is applicable only to MongoDB instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
        @param request: GetMongoDBCurrentOpRequest
        @return: GetMongoDBCurrentOpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mongo_dbcurrent_op_with_options_async(request, runtime)

    def get_my_sqlall_session_async_with_options(
        self,
        request: das20200116_models.GetMySQLAllSessionAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetMySQLAllSessionAsyncResponse:
        """
        >  Asynchronous calls do not immediately return the complete results. You must use the value of *ResultId** returned in the response to re-initiate the call. The complete results are returned only if the value of **IsFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL, PolarDB for MySQL, and PolarDB-X 2.0 instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetMySQLAllSessionAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMySQLAllSessionAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMySQLAllSessionAsync',
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
            das20200116_models.GetMySQLAllSessionAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_sqlall_session_async_with_options_async(
        self,
        request: das20200116_models.GetMySQLAllSessionAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetMySQLAllSessionAsyncResponse:
        """
        >  Asynchronous calls do not immediately return the complete results. You must use the value of *ResultId** returned in the response to re-initiate the call. The complete results are returned only if the value of **IsFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL, PolarDB for MySQL, and PolarDB-X 2.0 instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetMySQLAllSessionAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMySQLAllSessionAsyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.result_id):
            query['ResultId'] = request.result_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMySQLAllSessionAsync',
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
            das20200116_models.GetMySQLAllSessionAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_sqlall_session_async(
        self,
        request: das20200116_models.GetMySQLAllSessionAsyncRequest,
    ) -> das20200116_models.GetMySQLAllSessionAsyncResponse:
        """
        >  Asynchronous calls do not immediately return the complete results. You must use the value of *ResultId** returned in the response to re-initiate the call. The complete results are returned only if the value of **IsFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL, PolarDB for MySQL, and PolarDB-X 2.0 instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetMySQLAllSessionAsyncRequest
        @return: GetMySQLAllSessionAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_my_sqlall_session_async_with_options(request, runtime)

    async def get_my_sqlall_session_async_async(
        self,
        request: das20200116_models.GetMySQLAllSessionAsyncRequest,
    ) -> das20200116_models.GetMySQLAllSessionAsyncResponse:
        """
        >  Asynchronous calls do not immediately return the complete results. You must use the value of *ResultId** returned in the response to re-initiate the call. The complete results are returned only if the value of **IsFinish** is **true**.
        *   This operation is applicable only to ApsaraDB RDS for MySQL, PolarDB for MySQL, and PolarDB-X 2.0 instances.
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetMySQLAllSessionAsyncRequest
        @return: GetMySQLAllSessionAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_my_sqlall_session_async_with_options_async(request, runtime)

    def get_partitions_heatmap_with_options(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        """
        We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](~~470302~~) feature of Database Autonomy Service (DAS) to query the data.
        
        @param request: GetPartitionsHeatmapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPartitionsHeatmapResponse
        """
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
        """
        We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](~~470302~~) feature of Database Autonomy Service (DAS) to query the data.
        
        @param request: GetPartitionsHeatmapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPartitionsHeatmapResponse
        """
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
        """
        We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](~~470302~~) feature of Database Autonomy Service (DAS) to query the data.
        
        @param request: GetPartitionsHeatmapRequest
        @return: GetPartitionsHeatmapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_partitions_heatmap_with_options(request, runtime)

    async def get_partitions_heatmap_async(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        """
        We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](~~470302~~) feature of Database Autonomy Service (DAS) to query the data.
        
        @param request: GetPartitionsHeatmapRequest
        @return: GetPartitionsHeatmapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_partitions_heatmap_with_options_async(request, runtime)

    def get_pfs_metric_trends_with_options(
        self,
        request: das20200116_models.GetPfsMetricTrendsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsMetricTrendsResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsMetricTrendsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPfsMetricTrendsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPfsMetricTrends',
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
            das20200116_models.GetPfsMetricTrendsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pfs_metric_trends_with_options_async(
        self,
        request: das20200116_models.GetPfsMetricTrendsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsMetricTrendsResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsMetricTrendsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPfsMetricTrendsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPfsMetricTrends',
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
            das20200116_models.GetPfsMetricTrendsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pfs_metric_trends(
        self,
        request: das20200116_models.GetPfsMetricTrendsRequest,
    ) -> das20200116_models.GetPfsMetricTrendsResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsMetricTrendsRequest
        @return: GetPfsMetricTrendsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pfs_metric_trends_with_options(request, runtime)

    async def get_pfs_metric_trends_async(
        self,
        request: das20200116_models.GetPfsMetricTrendsRequest,
    ) -> das20200116_models.GetPfsMetricTrendsResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsMetricTrendsRequest
        @return: GetPfsMetricTrendsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pfs_metric_trends_with_options_async(request, runtime)

    def get_pfs_sql_sample_with_options(
        self,
        request: das20200116_models.GetPfsSqlSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsSqlSampleResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPfsSqlSampleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPfsSqlSample',
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
            das20200116_models.GetPfsSqlSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pfs_sql_sample_with_options_async(
        self,
        request: das20200116_models.GetPfsSqlSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsSqlSampleResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPfsSqlSampleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPfsSqlSample',
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
            das20200116_models.GetPfsSqlSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pfs_sql_sample(
        self,
        request: das20200116_models.GetPfsSqlSampleRequest,
    ) -> das20200116_models.GetPfsSqlSampleResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSampleRequest
        @return: GetPfsSqlSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pfs_sql_sample_with_options(request, runtime)

    async def get_pfs_sql_sample_async(
        self,
        request: das20200116_models.GetPfsSqlSampleRequest,
    ) -> das20200116_models.GetPfsSqlSampleResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSampleRequest
        @return: GetPfsSqlSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pfs_sql_sample_with_options_async(request, runtime)

    def get_pfs_sql_summaries_with_options(
        self,
        request: das20200116_models.GetPfsSqlSummariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsSqlSummariesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSummariesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPfsSqlSummariesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asc):
            body['Asc'] = request.asc
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPfsSqlSummaries',
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
            das20200116_models.GetPfsSqlSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pfs_sql_summaries_with_options_async(
        self,
        request: das20200116_models.GetPfsSqlSummariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsSqlSummariesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSummariesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPfsSqlSummariesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asc):
            body['Asc'] = request.asc
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPfsSqlSummaries',
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
            das20200116_models.GetPfsSqlSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pfs_sql_summaries(
        self,
        request: das20200116_models.GetPfsSqlSummariesRequest,
    ) -> das20200116_models.GetPfsSqlSummariesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSummariesRequest
        @return: GetPfsSqlSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pfs_sql_summaries_with_options(request, runtime)

    async def get_pfs_sql_summaries_async(
        self,
        request: das20200116_models.GetPfsSqlSummariesRequest,
    ) -> das20200116_models.GetPfsSqlSummariesResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        *   The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](~~469117~~).
        
        @param request: GetPfsSqlSummariesRequest
        @return: GetPfsSqlSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pfs_sql_summaries_with_options_async(request, runtime)

    def get_query_optimize_data_stats_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeDataStatsResponse
        """
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
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeDataStatsResponse
        """
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
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataStatsRequest
        @return: GetQueryOptimizeDataStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_stats_with_options(request, runtime)

    async def get_query_optimize_data_stats_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataStatsRequest
        @return: GetQueryOptimizeDataStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_data_stats_with_options_async(request, runtime)

    def get_query_optimize_data_top_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeDataTopResponse
        """
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
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTopRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeDataTopResponse
        """
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
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTopRequest
        @return: GetQueryOptimizeDataTopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_top_with_options(request, runtime)

    async def get_query_optimize_data_top_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        """
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTopRequest
        @return: GetQueryOptimizeDataTopResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_data_top_with_options_async(request, runtime)

    def get_query_optimize_data_trend_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeDataTrendResponse
        """
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
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeDataTrendResponse
        """
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
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTrendRequest
        @return: GetQueryOptimizeDataTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_data_trend_with_options(request, runtime)

    async def get_query_optimize_data_trend_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeDataTrendRequest
        @return: GetQueryOptimizeDataTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_data_trend_with_options_async(request, runtime)

    def get_query_optimize_exec_error_sample_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeExecErrorSampleResponse
        """
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
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeExecErrorSampleResponse
        """
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
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorSampleRequest
        @return: GetQueryOptimizeExecErrorSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_exec_error_sample_with_options(request, runtime)

    async def get_query_optimize_exec_error_sample_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorSampleRequest
        @return: GetQueryOptimizeExecErrorSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_exec_error_sample_with_options_async(request, runtime)

    def get_query_optimize_exec_error_stats_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeExecErrorStatsResponse
        """
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
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeExecErrorStatsResponse
        """
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
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorStatsRequest
        @return: GetQueryOptimizeExecErrorStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_exec_error_stats_with_options(request, runtime)

    async def get_query_optimize_exec_error_stats_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeExecErrorStatsRequest
        @return: GetQueryOptimizeExecErrorStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_exec_error_stats_with_options_async(request, runtime)

    def get_query_optimize_rule_list_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeRuleListResponse
        """
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
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeRuleListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeRuleListResponse
        """
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
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeRuleListRequest
        @return: GetQueryOptimizeRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_rule_list_with_options(request, runtime)

    async def get_query_optimize_rule_list_async(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        """
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeRuleListRequest
        @return: GetQueryOptimizeRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_rule_list_with_options_async(request, runtime)

    def get_query_optimize_share_url_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeShareUrlResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeShareUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeShareUrlResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeShareUrl',
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
            das20200116_models.GetQueryOptimizeShareUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_share_url_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeShareUrlResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeShareUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeShareUrlResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeShareUrl',
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
            das20200116_models.GetQueryOptimizeShareUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_share_url(
        self,
        request: das20200116_models.GetQueryOptimizeShareUrlRequest,
    ) -> das20200116_models.GetQueryOptimizeShareUrlResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeShareUrlRequest
        @return: GetQueryOptimizeShareUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_share_url_with_options(request, runtime)

    async def get_query_optimize_share_url_async(
        self,
        request: das20200116_models.GetQueryOptimizeShareUrlRequest,
    ) -> das20200116_models.GetQueryOptimizeShareUrlResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeShareUrlRequest
        @return: GetQueryOptimizeShareUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_share_url_with_options_async(request, runtime)

    def get_query_optimize_solution_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        """
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeSolutionResponse
        """
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
        """
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeSolutionResponse
        """
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
        """
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeSolutionRequest
        @return: GetQueryOptimizeSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_solution_with_options(request, runtime)

    async def get_query_optimize_solution_async(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        """
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeSolutionRequest
        @return: GetQueryOptimizeSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_solution_with_options_async(request, runtime)

    def get_query_optimize_tag_with_options(
        self,
        request: das20200116_models.GetQueryOptimizeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeTagResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeTag',
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
            das20200116_models.GetQueryOptimizeTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_optimize_tag_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueryOptimizeTagResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryOptimizeTag',
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
            das20200116_models.GetQueryOptimizeTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_optimize_tag(
        self,
        request: das20200116_models.GetQueryOptimizeTagRequest,
    ) -> das20200116_models.GetQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeTagRequest
        @return: GetQueryOptimizeTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_query_optimize_tag_with_options(request, runtime)

    async def get_query_optimize_tag_async(
        self,
        request: das20200116_models.GetQueryOptimizeTagRequest,
    ) -> das20200116_models.GetQueryOptimizeTagResponse:
        """
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        *   ApsaraDB RDS for PostgreSQL
        
        @param request: GetQueryOptimizeTagRequest
        @return: GetQueryOptimizeTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_query_optimize_tag_with_options_async(request, runtime)

    def get_redis_all_session_with_options(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        """
        This operation is applicable only to ApsaraDB for Redis instances.
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  This operation cannot be used to query sessions generated in direct connection mode on ApsaraDB for Redis cluster instances.
        
        @param request: GetRedisAllSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRedisAllSessionResponse
        """
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
        """
        This operation is applicable only to ApsaraDB for Redis instances.
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  This operation cannot be used to query sessions generated in direct connection mode on ApsaraDB for Redis cluster instances.
        
        @param request: GetRedisAllSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRedisAllSessionResponse
        """
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
        """
        This operation is applicable only to ApsaraDB for Redis instances.
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  This operation cannot be used to query sessions generated in direct connection mode on ApsaraDB for Redis cluster instances.
        
        @param request: GetRedisAllSessionRequest
        @return: GetRedisAllSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_redis_all_session_with_options(request, runtime)

    async def get_redis_all_session_async(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        """
        This operation is applicable only to ApsaraDB for Redis instances.
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        >  This operation cannot be used to query sessions generated in direct connection mode on ApsaraDB for Redis cluster instances.
        
        @param request: GetRedisAllSessionRequest
        @return: GetRedisAllSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_redis_all_session_with_options_async(request, runtime)

    def get_request_diagnosis_page_with_options(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (Compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestDiagnosisPageResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (Compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestDiagnosisPageResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (Compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisPageRequest
        @return: GetRequestDiagnosisPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_page_with_options(request, runtime)

    async def get_request_diagnosis_page_async(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (Compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisPageRequest
        @return: GetRequestDiagnosisPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_request_diagnosis_page_with_options_async(request, runtime)

    def get_request_diagnosis_result_with_options(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestDiagnosisResultResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRequestDiagnosisResultResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisResultRequest
        @return: GetRequestDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_request_diagnosis_result_with_options(request, runtime)

    async def get_request_diagnosis_result_async(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   ApsaraDB RDS for PostgreSQL
        *   ApsaraDB RDS for SQL Server
        *   PolarDB for MySQL
        *   PolarDB for PostgreSQL (compatible with Oracle)
        *   ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~).
        
        @param request: GetRequestDiagnosisResultRequest
        @return: GetRequestDiagnosisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_request_diagnosis_result_with_options_async(request, runtime)

    def get_running_sql_concurrency_control_rules_with_options(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetRunningSqlConcurrencyControlRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunningSqlConcurrencyControlRulesResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetRunningSqlConcurrencyControlRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunningSqlConcurrencyControlRulesResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetRunningSqlConcurrencyControlRulesRequest
        @return: GetRunningSqlConcurrencyControlRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_running_sql_concurrency_control_rules_with_options(request, runtime)

    async def get_running_sql_concurrency_control_rules_async(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetRunningSqlConcurrencyControlRulesRequest
        @return: GetRunningSqlConcurrencyControlRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_running_sql_concurrency_control_rules_with_options_async(request, runtime)

    def get_sql_concurrency_control_keywords_from_sql_text_with_options(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlKeywordsFromSqlTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlConcurrencyControlKeywordsFromSqlTextResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlKeywordsFromSqlTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlConcurrencyControlKeywordsFromSqlTextResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlKeywordsFromSqlTextRequest
        @return: GetSqlConcurrencyControlKeywordsFromSqlTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sql_concurrency_control_keywords_from_sql_text_with_options(request, runtime)

    async def get_sql_concurrency_control_keywords_from_sql_text_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlKeywordsFromSqlTextRequest
        @return: GetSqlConcurrencyControlKeywordsFromSqlTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sql_concurrency_control_keywords_from_sql_text_with_options_async(request, runtime)

    def get_sql_concurrency_control_rules_history_with_options(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlRulesHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlConcurrencyControlRulesHistoryResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlRulesHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlConcurrencyControlRulesHistoryResponse
        """
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
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlRulesHistoryRequest
        @return: GetSqlConcurrencyControlRulesHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sql_concurrency_control_rules_history_with_options(request, runtime)

    async def get_sql_concurrency_control_rules_history_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        """
        This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL
        *   PolarDB for MySQL
        
        @param request: GetSqlConcurrencyControlRulesHistoryRequest
        @return: GetSqlConcurrencyControlRulesHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sql_concurrency_control_rules_history_with_options_async(request, runtime)

    def get_sql_optimize_advice_with_options(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        """
        The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](~~167895~~).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        *   This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetSqlOptimizeAdviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlOptimizeAdviceResponse
        """
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
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
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
        """
        The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](~~167895~~).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        *   This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetSqlOptimizeAdviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlOptimizeAdviceResponse
        """
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
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
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
        """
        The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](~~167895~~).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        *   This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetSqlOptimizeAdviceRequest
        @return: GetSqlOptimizeAdviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sql_optimize_advice_with_options(request, runtime)

    async def get_sql_optimize_advice_async(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        """
        The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](~~167895~~).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        *   This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetSqlOptimizeAdviceRequest
        @return: GetSqlOptimizeAdviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sql_optimize_advice_with_options_async(request, runtime)

    def get_storage_analysis_result_with_options(
        self,
        request: das20200116_models.GetStorageAnalysisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetStorageAnalysisResultResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from information_schema.tables. Due to the asynchronicity of the statistics update mechanism in MySQL, statistics and analysis results may not be perfectly accurate. You can execute the ANALYZE TABLE statement on related tables during off-peak hours to obtain the latest information.
        
        @param request: GetStorageAnalysisResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageAnalysisResultResponse
        """
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
            action='GetStorageAnalysisResult',
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
            das20200116_models.GetStorageAnalysisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_analysis_result_with_options_async(
        self,
        request: das20200116_models.GetStorageAnalysisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetStorageAnalysisResultResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from information_schema.tables. Due to the asynchronicity of the statistics update mechanism in MySQL, statistics and analysis results may not be perfectly accurate. You can execute the ANALYZE TABLE statement on related tables during off-peak hours to obtain the latest information.
        
        @param request: GetStorageAnalysisResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageAnalysisResultResponse
        """
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
            action='GetStorageAnalysisResult',
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
            das20200116_models.GetStorageAnalysisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_analysis_result(
        self,
        request: das20200116_models.GetStorageAnalysisResultRequest,
    ) -> das20200116_models.GetStorageAnalysisResultResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from information_schema.tables. Due to the asynchronicity of the statistics update mechanism in MySQL, statistics and analysis results may not be perfectly accurate. You can execute the ANALYZE TABLE statement on related tables during off-peak hours to obtain the latest information.
        
        @param request: GetStorageAnalysisResultRequest
        @return: GetStorageAnalysisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_storage_analysis_result_with_options(request, runtime)

    async def get_storage_analysis_result_async(
        self,
        request: das20200116_models.GetStorageAnalysisResultRequest,
    ) -> das20200116_models.GetStorageAnalysisResultResponse:
        """
        This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        *   The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from information_schema.tables. Due to the asynchronicity of the statistics update mechanism in MySQL, statistics and analysis results may not be perfectly accurate. You can execute the ANALYZE TABLE statement on related tables during off-peak hours to obtain the latest information.
        
        @param request: GetStorageAnalysisResultRequest
        @return: GetStorageAnalysisResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_storage_analysis_result_with_options_async(request, runtime)

    def kill_instance_all_session_with_options(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        """
        This operation is applicable only to ApsaraDB for Redis.
        *   If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: KillInstanceAllSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillInstanceAllSessionResponse
        """
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
        """
        This operation is applicable only to ApsaraDB for Redis.
        *   If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: KillInstanceAllSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillInstanceAllSessionResponse
        """
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
        """
        This operation is applicable only to ApsaraDB for Redis.
        *   If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: KillInstanceAllSessionRequest
        @return: KillInstanceAllSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_instance_all_session_with_options(request, runtime)

    async def kill_instance_all_session_async(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        """
        This operation is applicable only to ApsaraDB for Redis.
        *   If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        *   The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: KillInstanceAllSessionRequest
        @return: KillInstanceAllSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_instance_all_session_with_options_async(request, runtime)

    def modify_auto_scaling_config_with_options(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        """
        You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        *   You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        *   PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](~~173345~~).
        *   You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        *   ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](~~216312~~).
        *   You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        *   General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: ModifyAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoScalingConfigResponse
        """
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
        """
        You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        *   You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        *   PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](~~173345~~).
        *   You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        *   ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](~~216312~~).
        *   You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        *   General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: ModifyAutoScalingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoScalingConfigResponse
        """
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
        """
        You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        *   You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        *   PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](~~173345~~).
        *   You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        *   ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](~~216312~~).
        *   You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        *   General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: ModifyAutoScalingConfigRequest
        @return: ModifyAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_scaling_config_with_options(request, runtime)

    async def modify_auto_scaling_config_async(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        """
        You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        *   You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        *   PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        *   ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](~~173345~~).
        *   You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        *   ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](~~216312~~).
        *   You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        *   General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](~~169686~~).
        *   If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: ModifyAutoScalingConfigRequest
        @return: ModifyAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_scaling_config_with_options_async(request, runtime)

    def run_cloud_bench_task_with_options(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: RunCloudBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCloudBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: RunCloudBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCloudBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: RunCloudBenchTaskRequest
        @return: RunCloudBenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_bench_task_with_options(request, runtime)

    async def run_cloud_bench_task_async(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: RunCloudBenchTaskRequest
        @return: RunCloudBenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_cloud_bench_task_with_options_async(request, runtime)

    def set_event_subscription_with_options(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: SetEventSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetEventSubscriptionResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: SetEventSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetEventSubscriptionResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: SetEventSubscriptionRequest
        @return: SetEventSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_event_subscription_with_options(request, runtime)

    async def set_event_subscription_async(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        *   If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        *   The database instance that you want to manage is connected to DAS.
        
        @param request: SetEventSubscriptionRequest
        @return: SetEventSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_event_subscription_with_options_async(request, runtime)

    def stop_cloud_bench_task_with_options(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: StopCloudBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCloudBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: StopCloudBenchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCloudBenchTaskResponse
        """
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
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: StopCloudBenchTaskRequest
        @return: StopCloudBenchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_cloud_bench_task_with_options(request, runtime)

    async def stop_cloud_bench_task_async(
        self,
        request: das20200116_models.StopCloudBenchTaskRequest,
    ) -> das20200116_models.StopCloudBenchTaskResponse:
        """
        Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](~~155068~~).
        
        @param request: StopCloudBenchTaskRequest
        @return: StopCloudBenchTaskResponse
        """
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
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   DAS Professional Edition is enabled for the database instance. You can call the [DescribeInstanceDasPro](~~413866~~) operation to check whether DAS Professional Edition is enabled for a database instance.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: UpdateAutoResourceOptimizeRulesAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoResourceOptimizeRulesAsyncResponse
        """
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
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   DAS Professional Edition is enabled for the database instance. You can call the [DescribeInstanceDasPro](~~413866~~) operation to check whether DAS Professional Edition is enabled for a database instance.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: UpdateAutoResourceOptimizeRulesAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoResourceOptimizeRulesAsyncResponse
        """
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
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   DAS Professional Edition is enabled for the database instance. You can call the [DescribeInstanceDasPro](~~413866~~) operation to check whether DAS Professional Edition is enabled for a database instance.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: UpdateAutoResourceOptimizeRulesAsyncRequest
        @return: UpdateAutoResourceOptimizeRulesAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_auto_resource_optimize_rules_async_with_options(request, runtime)

    async def update_auto_resource_optimize_rules_async_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        *   DAS Professional Edition is enabled for the database instance. You can call the [DescribeInstanceDasPro](~~413866~~) operation to check whether DAS Professional Edition is enabled for a database instance.
        *   The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
        @param request: UpdateAutoResourceOptimizeRulesAsyncRequest
        @return: UpdateAutoResourceOptimizeRulesAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_resource_optimize_rules_async_with_options_async(request, runtime)

    def update_auto_sql_optimize_status_with_options(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   DAS Professional Edition is enabled for the database instance that you want to manage. To enable DAS Professional Edition for a database instance, you can call the [EnableDasPro](~~411645~~) operation.
        *   The autonomy service is enabled for the database instance. For more information, see [Autonomy center](~~152139~~).
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL High-availability Edition and Enterprise Edition
        *   PolarDB for MySQL Cluster Edition and X-Engine Edition
        
        @param request: UpdateAutoSqlOptimizeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoSqlOptimizeStatusResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   DAS Professional Edition is enabled for the database instance that you want to manage. To enable DAS Professional Edition for a database instance, you can call the [EnableDasPro](~~411645~~) operation.
        *   The autonomy service is enabled for the database instance. For more information, see [Autonomy center](~~152139~~).
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL High-availability Edition and Enterprise Edition
        *   PolarDB for MySQL Cluster Edition and X-Engine Edition
        
        @param request: UpdateAutoSqlOptimizeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoSqlOptimizeStatusResponse
        """
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
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   DAS Professional Edition is enabled for the database instance that you want to manage. To enable DAS Professional Edition for a database instance, you can call the [EnableDasPro](~~411645~~) operation.
        *   The autonomy service is enabled for the database instance. For more information, see [Autonomy center](~~152139~~).
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL High-availability Edition and Enterprise Edition
        *   PolarDB for MySQL Cluster Edition and X-Engine Edition
        
        @param request: UpdateAutoSqlOptimizeStatusRequest
        @return: UpdateAutoSqlOptimizeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_auto_sql_optimize_status_with_options(request, runtime)

    async def update_auto_sql_optimize_status_async(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        """
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   DAS Professional Edition is enabled for the database instance that you want to manage. To enable DAS Professional Edition for a database instance, you can call the [EnableDasPro](~~411645~~) operation.
        *   The autonomy service is enabled for the database instance. For more information, see [Autonomy center](~~152139~~).
        *   This operation supports the following database engines:
        *   ApsaraDB RDS for MySQL High-availability Edition and Enterprise Edition
        *   PolarDB for MySQL Cluster Edition and X-Engine Edition
        
        @param request: UpdateAutoSqlOptimizeStatusRequest
        @return: UpdateAutoSqlOptimizeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_sql_optimize_status_with_options_async(request, runtime)

    def update_auto_throttle_rules_async_with_options(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](~~152139~~).
        *   The database instance that you want to manage must be of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        *   PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, and PolarDB for MySQL X-Engine Edition that runs MySQL 8.0
        
        @param request: UpdateAutoThrottleRulesAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoThrottleRulesAsyncResponse
        """
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
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](~~152139~~).
        *   The database instance that you want to manage must be of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        *   PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, and PolarDB for MySQL X-Engine Edition that runs MySQL 8.0
        
        @param request: UpdateAutoThrottleRulesAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoThrottleRulesAsyncResponse
        """
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
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](~~152139~~).
        *   The database instance that you want to manage must be of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        *   PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, and PolarDB for MySQL X-Engine Edition that runs MySQL 8.0
        
        @param request: UpdateAutoThrottleRulesAsyncRequest
        @return: UpdateAutoThrottleRulesAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_auto_throttle_rules_async_with_options(request, runtime)

    async def update_auto_throttle_rules_async_async(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        """
        >  An asynchronous call does not immediately return complete results. If the value of *isFinish** is **false** in the response, wait for 1 second and then re-initiate the call. If the value of **isFinish** is **true**, the complete results are returned.
        Before you call this operation, take note of the following items:
        *   If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        *   The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](~~152139~~).
        *   The database instance that you want to manage must be of one of the following types:
        *   ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        *   PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0, and PolarDB for MySQL X-Engine Edition that runs MySQL 8.0
        
        @param request: UpdateAutoThrottleRulesAsyncRequest
        @return: UpdateAutoThrottleRulesAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_throttle_rules_async_with_options_async(request, runtime)
