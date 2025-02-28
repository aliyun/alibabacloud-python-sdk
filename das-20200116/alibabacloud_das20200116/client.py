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
        @summary Adds a database instance to Database Autonomy Service (DAS).
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.AddHDMInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.AddHDMInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def add_hdminstance_with_options_async(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.AddHDMInstanceResponse:
        """
        @summary Adds a database instance to Database Autonomy Service (DAS).
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.AddHDMInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.AddHDMInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_hdminstance(
        self,
        request: das20200116_models.AddHDMInstanceRequest,
    ) -> das20200116_models.AddHDMInstanceResponse:
        """
        @summary Adds a database instance to Database Autonomy Service (DAS).
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
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
        @summary Adds a database instance to Database Autonomy Service (DAS).
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
        @param request: AddHDMInstanceRequest
        @return: AddHDMInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_hdminstance_with_options_async(request, runtime)

    def create_cache_analysis_job_with_options(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        """
        @summary Creates a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        You can call this operation to analyze the data structures of ApsaraDB for Redis and the following self-developed data structures of Tair: TairString, TairHash, TairGIS, TairBloom, TairDoc, TairCpc, and TairZset. Other self-developed Tair data structures are not supported.
        If the specifications of the database instance that you want to analyze are changed, the backup file generated before the specification change cannot be analyzed.
        Tair ESSD/SSD-based instances are not supported.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateCacheAnalysisJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateCacheAnalysisJobResponse(),
                self.execute(params, req, runtime)
            )

    async def create_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        """
        @summary Creates a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        You can call this operation to analyze the data structures of ApsaraDB for Redis and the following self-developed data structures of Tair: TairString, TairHash, TairGIS, TairBloom, TairDoc, TairCpc, and TairZset. Other self-developed Tair data structures are not supported.
        If the specifications of the database instance that you want to analyze are changed, the backup file generated before the specification change cannot be analyzed.
        Tair ESSD/SSD-based instances are not supported.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateCacheAnalysisJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateCacheAnalysisJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_cache_analysis_job(
        self,
        request: das20200116_models.CreateCacheAnalysisJobRequest,
    ) -> das20200116_models.CreateCacheAnalysisJobResponse:
        """
        @summary Creates a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        You can call this operation to analyze the data structures of ApsaraDB for Redis and the following self-developed data structures of Tair: TairString, TairHash, TairGIS, TairBloom, TairDoc, TairCpc, and TairZset. Other self-developed Tair data structures are not supported.
        If the specifications of the database instance that you want to analyze are changed, the backup file generated before the specification change cannot be analyzed.
        Tair ESSD/SSD-based instances are not supported.
        
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
        @summary Creates a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        You can call this operation to analyze the data structures of ApsaraDB for Redis and the following self-developed data structures of Tair: TairString, TairHash, TairGIS, TairBloom, TairDoc, TairCpc, and TairZset. Other self-developed Tair data structures are not supported.
        If the specifications of the database instance that you want to analyze are changed, the backup file generated before the specification change cannot be analyzed.
        Tair ESSD/SSD-based instances are not supported.
        
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
        @summary Creates stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html). Before you call this API operation, make sure that your database instances meet the following requirements:
        The source database instance is an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition cluster.
        The destination database instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        The source and destination database instances are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](https://help.aliyun.com/document_detail/65405.html).
        DAS Enterprise Edition is enabled for the source and destination database instances. For more information, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateCloudBenchTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateCloudBenchTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def create_cloud_bench_tasks_with_options_async(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        """
        @summary Creates stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html). Before you call this API operation, make sure that your database instances meet the following requirements:
        The source database instance is an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition cluster.
        The destination database instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        The source and destination database instances are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](https://help.aliyun.com/document_detail/65405.html).
        DAS Enterprise Edition is enabled for the source and destination database instances. For more information, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateCloudBenchTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateCloudBenchTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_cloud_bench_tasks(
        self,
        request: das20200116_models.CreateCloudBenchTasksRequest,
    ) -> das20200116_models.CreateCloudBenchTasksResponse:
        """
        @summary Creates stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html). Before you call this API operation, make sure that your database instances meet the following requirements:
        The source database instance is an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition cluster.
        The destination database instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        The source and destination database instances are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](https://help.aliyun.com/document_detail/65405.html).
        DAS Enterprise Edition is enabled for the source and destination database instances. For more information, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        
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
        @summary Creates stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html). Before you call this API operation, make sure that your database instances meet the following requirements:
        The source database instance is an ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition instance, or a PolarDB for MySQL Cluster Edition cluster.
        The destination database instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        The source and destination database instances are connected to DAS. For information about how to connect database instances to DAS, see [Connect an Alibaba Cloud database instance to DAS](https://help.aliyun.com/document_detail/65405.html).
        DAS Enterprise Edition is enabled for the source and destination database instances. For more information, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        
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
        @summary Creates a diagnostic report.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        This operation supports the following database engines:
        RDS MySQL
        PolarDB for MySQL
        Redis
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateDiagnosticReportResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateDiagnosticReportResponse(),
                self.execute(params, req, runtime)
            )

    async def create_diagnostic_report_with_options_async(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        """
        @summary Creates a diagnostic report.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        This operation supports the following database engines:
        RDS MySQL
        PolarDB for MySQL
        Redis
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateDiagnosticReportResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateDiagnosticReportResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_diagnostic_report(
        self,
        request: das20200116_models.CreateDiagnosticReportRequest,
    ) -> das20200116_models.CreateDiagnosticReportResponse:
        """
        @summary Creates a diagnostic report.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        This operation supports the following database engines:
        RDS MySQL
        PolarDB for MySQL
        Redis
        
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
        @summary Creates a diagnostic report.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.3 or later.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        This operation supports the following database engines:
        RDS MySQL
        PolarDB for MySQL
        Redis
        
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
        @summary Creates a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def create_kill_instance_session_task_with_options_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        """
        @summary Creates a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_kill_instance_session_task(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskResponse:
        """
        @summary Creates a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Creates a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        """
        @summary 创建结束会话的任务
        
        @param request: CreateKillInstanceSessionTaskWithMaintainUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKillInstanceSessionTaskWithMaintainUserResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
                self.execute(params, req, runtime)
            )

    async def create_kill_instance_session_task_with_maintain_user_with_options_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        """
        @summary 创建结束会话的任务
        
        @param request: CreateKillInstanceSessionTaskWithMaintainUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKillInstanceSessionTaskWithMaintainUserResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_kill_instance_session_task_with_maintain_user(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        """
        @summary 创建结束会话的任务
        
        @param request: CreateKillInstanceSessionTaskWithMaintainUserRequest
        @return: CreateKillInstanceSessionTaskWithMaintainUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_kill_instance_session_task_with_maintain_user_with_options(request, runtime)

    async def create_kill_instance_session_task_with_maintain_user_async(
        self,
        request: das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserRequest,
    ) -> das20200116_models.CreateKillInstanceSessionTaskWithMaintainUserResponse:
        """
        @summary 创建结束会话的任务
        
        @param request: CreateKillInstanceSessionTaskWithMaintainUserRequest
        @return: CreateKillInstanceSessionTaskWithMaintainUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_kill_instance_session_task_with_maintain_user_with_options_async(request, runtime)

    def create_latest_dead_lock_analysis_with_options(
        self,
        request: das20200116_models.CreateLatestDeadLockAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateLatestDeadLockAnalysisResponse:
        """
        @summary 创建最近死锁分析任务
        
        @param request: CreateLatestDeadLockAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLatestDeadLockAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLatestDeadLockAnalysis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateLatestDeadLockAnalysisResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateLatestDeadLockAnalysisResponse(),
                self.execute(params, req, runtime)
            )

    async def create_latest_dead_lock_analysis_with_options_async(
        self,
        request: das20200116_models.CreateLatestDeadLockAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateLatestDeadLockAnalysisResponse:
        """
        @summary 创建最近死锁分析任务
        
        @param request: CreateLatestDeadLockAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLatestDeadLockAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLatestDeadLockAnalysis',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateLatestDeadLockAnalysisResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateLatestDeadLockAnalysisResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_latest_dead_lock_analysis(
        self,
        request: das20200116_models.CreateLatestDeadLockAnalysisRequest,
    ) -> das20200116_models.CreateLatestDeadLockAnalysisResponse:
        """
        @summary 创建最近死锁分析任务
        
        @param request: CreateLatestDeadLockAnalysisRequest
        @return: CreateLatestDeadLockAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_latest_dead_lock_analysis_with_options(request, runtime)

    async def create_latest_dead_lock_analysis_async(
        self,
        request: das20200116_models.CreateLatestDeadLockAnalysisRequest,
    ) -> das20200116_models.CreateLatestDeadLockAnalysisResponse:
        """
        @summary 创建最近死锁分析任务
        
        @param request: CreateLatestDeadLockAnalysisRequest
        @return: CreateLatestDeadLockAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_latest_dead_lock_analysis_with_options_async(request, runtime)

    def create_query_optimize_tag_with_options(
        self,
        request: das20200116_models.CreateQueryOptimizeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateQueryOptimizeTagResponse:
        """
        @summary Adds a tag to a SQL template.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateQueryOptimizeTagResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateQueryOptimizeTagResponse(),
                self.execute(params, req, runtime)
            )

    async def create_query_optimize_tag_with_options_async(
        self,
        request: das20200116_models.CreateQueryOptimizeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateQueryOptimizeTagResponse:
        """
        @summary Adds a tag to a SQL template.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateQueryOptimizeTagResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateQueryOptimizeTagResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_query_optimize_tag(
        self,
        request: das20200116_models.CreateQueryOptimizeTagRequest,
    ) -> das20200116_models.CreateQueryOptimizeTagResponse:
        """
        @summary Adds a tag to a SQL template.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Adds a tag to a SQL template.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Initiates an SQL statement diagnostics request.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateRequestDiagnosisResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateRequestDiagnosisResponse(),
                self.execute(params, req, runtime)
            )

    async def create_request_diagnosis_with_options_async(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        """
        @summary Initiates an SQL statement diagnostics request.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateRequestDiagnosisResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateRequestDiagnosisResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_request_diagnosis(
        self,
        request: das20200116_models.CreateRequestDiagnosisRequest,
    ) -> das20200116_models.CreateRequestDiagnosisResponse:
        """
        @summary Initiates an SQL statement diagnostics request.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        @summary Initiates an SQL statement diagnostics request.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call Database Autonomy Service (DAS), you must set the region to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of ApsaraDB RDS for PostgreSQL instances must be 20221230 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
        @param request: CreateRequestDiagnosisRequest
        @return: CreateRequestDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_request_diagnosis_with_options_async(request, runtime)

    def create_sql_log_task_with_options(
        self,
        request: das20200116_models.CreateSqlLogTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateSqlLogTaskResponse:
        """
        @summary Creates an offline task for Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        You can create an offline task only for database instances for which DAS Enterprise Edition V2 or V3 is enabled. For more information about the databases and regions that are supported by various versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: CreateSqlLogTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlLogTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlLogTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateSqlLogTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateSqlLogTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def create_sql_log_task_with_options_async(
        self,
        request: das20200116_models.CreateSqlLogTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateSqlLogTaskResponse:
        """
        @summary Creates an offline task for Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        You can create an offline task only for database instances for which DAS Enterprise Edition V2 or V3 is enabled. For more information about the databases and regions that are supported by various versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: CreateSqlLogTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlLogTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlLogTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateSqlLogTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateSqlLogTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_sql_log_task(
        self,
        request: das20200116_models.CreateSqlLogTaskRequest,
    ) -> das20200116_models.CreateSqlLogTaskResponse:
        """
        @summary Creates an offline task for Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        You can create an offline task only for database instances for which DAS Enterprise Edition V2 or V3 is enabled. For more information about the databases and regions that are supported by various versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: CreateSqlLogTaskRequest
        @return: CreateSqlLogTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sql_log_task_with_options(request, runtime)

    async def create_sql_log_task_async(
        self,
        request: das20200116_models.CreateSqlLogTaskRequest,
    ) -> das20200116_models.CreateSqlLogTaskResponse:
        """
        @summary Creates an offline task for Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        You can create an offline task only for database instances for which DAS Enterprise Edition V2 or V3 is enabled. For more information about the databases and regions that are supported by various versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: CreateSqlLogTaskRequest
        @return: CreateSqlLogTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sql_log_task_with_options_async(request, runtime)

    def create_storage_analysis_task_with_options(
        self,
        request: das20200116_models.CreateStorageAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateStorageAnalysisTaskResponse:
        """
        @summary Creates a storage analysis task to query the usage details of one or more databases and tables.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateStorageAnalysisTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateStorageAnalysisTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def create_storage_analysis_task_with_options_async(
        self,
        request: das20200116_models.CreateStorageAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.CreateStorageAnalysisTaskResponse:
        """
        @summary Creates a storage analysis task to query the usage details of one or more databases and tables.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.CreateStorageAnalysisTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.CreateStorageAnalysisTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_storage_analysis_task(
        self,
        request: das20200116_models.CreateStorageAnalysisTaskRequest,
    ) -> das20200116_models.CreateStorageAnalysisTaskResponse:
        """
        @summary Creates a storage analysis task to query the usage details of one or more databases and tables.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Creates a storage analysis task to query the usage details of one or more databases and tables.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Deletes a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DeleteCloudBenchTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DeleteCloudBenchTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_cloud_bench_task_with_options_async(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        """
        @summary Deletes a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DeleteCloudBenchTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DeleteCloudBenchTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_cloud_bench_task(
        self,
        request: das20200116_models.DeleteCloudBenchTaskRequest,
    ) -> das20200116_models.DeleteCloudBenchTaskResponse:
        """
        @summary Deletes a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Deletes a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to handle traffic spikes in an effective manner. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Deletes the metadata of a stopped DBGateway.
        
        @description    This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](https://help.aliyun.com/document_detail/230665.html) operation.
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DeleteStopGatewayResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DeleteStopGatewayResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_stop_gateway_with_options_async(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        """
        @summary Deletes the metadata of a stopped DBGateway.
        
        @description    This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](https://help.aliyun.com/document_detail/230665.html) operation.
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DeleteStopGatewayResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DeleteStopGatewayResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_stop_gateway(
        self,
        request: das20200116_models.DeleteStopGatewayRequest,
    ) -> das20200116_models.DeleteStopGatewayResponse:
        """
        @summary Deletes the metadata of a stopped DBGateway.
        
        @description    This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](https://help.aliyun.com/document_detail/230665.html) operation.
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        @summary Deletes the metadata of a stopped DBGateway.
        
        @description    This operation is used to delete the metadata of a DBGateway that is released in a stress testing task created by calling the [CreateCloudBenchTasks](https://help.aliyun.com/document_detail/230665.html) operation.
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        @summary Queries the configurations of the auto scaling feature for an instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_auto_scaling_config_with_options_async(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        """
        @summary Queries the configurations of the auto scaling feature for an instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_auto_scaling_config(
        self,
        request: das20200116_models.DescribeAutoScalingConfigRequest,
    ) -> das20200116_models.DescribeAutoScalingConfigResponse:
        """
        @summary Queries the configurations of the auto scaling feature for an instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the configurations of the auto scaling feature for an instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the auto scaling history of an instance.
        
        @description    You can call this operation to query the history information about the automatic performance scaling only of ApsaraDB RDS for MySQL High-availability Edition instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingHistoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingHistoryResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_auto_scaling_history_with_options_async(
        self,
        request: das20200116_models.DescribeAutoScalingHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeAutoScalingHistoryResponse:
        """
        @summary Queries the auto scaling history of an instance.
        
        @description    You can call this operation to query the history information about the automatic performance scaling only of ApsaraDB RDS for MySQL High-availability Edition instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingHistoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeAutoScalingHistoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_auto_scaling_history(
        self,
        request: das20200116_models.DescribeAutoScalingHistoryRequest,
    ) -> das20200116_models.DescribeAutoScalingHistoryResponse:
        """
        @summary Queries the auto scaling history of an instance.
        
        @description    You can call this operation to query the history information about the automatic performance scaling only of ApsaraDB RDS for MySQL High-availability Edition instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the auto scaling history of an instance.
        
        @description    You can call this operation to query the history information about the automatic performance scaling only of ApsaraDB RDS for MySQL High-availability Edition instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the details of a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        >  You can call this operation to query the top 500 keys in a cache analysis task.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cache_analysis_job_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        """
        @summary Queries the details of a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        >  You can call this operation to query the top 500 keys in a cache analysis task.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cache_analysis_job(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobResponse:
        """
        @summary Queries the details of a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        >  You can call this operation to query the top 500 keys in a cache analysis task.
        
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
        @summary Queries the details of a cache analysis task.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        >  You can call this operation to query the top 500 keys in a cache analysis task.
        
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
        @summary Queries a list of cache analysis tasks.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cache_analysis_jobs_with_options_async(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        """
        @summary Queries a list of cache analysis tasks.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCacheAnalysisJobsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cache_analysis_jobs(
        self,
        request: das20200116_models.DescribeCacheAnalysisJobsRequest,
    ) -> das20200116_models.DescribeCacheAnalysisJobsResponse:
        """
        @summary Queries a list of cache analysis tasks.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        
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
        @summary Queries a list of cache analysis tasks.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis.
        
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
        @summary Queries stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCloudBenchTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCloudBenchTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cloud_bench_tasks_with_options_async(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        """
        @summary Queries stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCloudBenchTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCloudBenchTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cloud_bench_tasks(
        self,
        request: das20200116_models.DescribeCloudBenchTasksRequest,
    ) -> das20200116_models.DescribeCloudBenchTasksResponse:
        """
        @summary Queries stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Queries stress testing tasks.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Queries a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cloudbench_task_with_options_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        """
        @summary Queries a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cloudbench_task(
        self,
        request: das20200116_models.DescribeCloudbenchTaskRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskResponse:
        """
        @summary Queries a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Queries a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether you need to scale up your database instance to handle workloads during peak hours. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Queries the configurations of a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cloudbench_task_config_with_options_async(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        """
        @summary Queries the configurations of a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeCloudbenchTaskConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cloudbench_task_config(
        self,
        request: das20200116_models.DescribeCloudbenchTaskConfigRequest,
    ) -> das20200116_models.DescribeCloudbenchTaskConfigResponse:
        """
        @summary Queries the configurations of a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Queries the configurations of a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Queries diagnostics reports.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB for Redis
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeDiagnosticReportListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeDiagnosticReportListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        """
        @summary Queries diagnostics reports.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB for Redis
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeDiagnosticReportListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeDiagnosticReportListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_diagnostic_report_list(
        self,
        request: das20200116_models.DescribeDiagnosticReportListRequest,
    ) -> das20200116_models.DescribeDiagnosticReportListResponse:
        """
        @summary Queries diagnostics reports.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB for Redis
        
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
        @summary Queries diagnostics reports.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB for Redis
        
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
        @summary Queries the hot keys and the large keys in the memory in real time.
        
        @description This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeHotBigKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeHotBigKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_hot_big_keys_with_options_async(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        """
        @summary Queries the hot keys and the large keys in the memory in real time.
        
        @description This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeHotBigKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeHotBigKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_hot_big_keys(
        self,
        request: das20200116_models.DescribeHotBigKeysRequest,
    ) -> das20200116_models.DescribeHotBigKeysResponse:
        """
        @summary Queries the hot keys and the large keys in the memory in real time.
        
        @description This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Queries the hot keys and the large keys in the memory in real time.
        
        @description This operation sorts list, hash, set, and zset keys based on the number of elements contained in these keys. The top three keys that contain the most elements are considered large keys. If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for ApsaraDB for Redis instances that meet the following requirements:
        The instance is a Community Edition instance that uses a major version of 5.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Queries the hot keys of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeHotKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeHotKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_hot_keys_with_options_async(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeHotKeysResponse:
        """
        @summary Queries the hot keys of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeHotKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeHotKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_hot_keys(
        self,
        request: das20200116_models.DescribeHotKeysRequest,
    ) -> das20200116_models.DescribeHotKeysResponse:
        """
        @summary Queries the hot keys of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Queries the hot keys of an ApsaraDB for Redis instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances that meet the following requirements:
        The ApsaraDB for Redis instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Queries whether Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled for a database instance.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogConfig](https://help.aliyun.com/document_detail/2778837.html) operation to query the DAS Enterprise Edition configurations of a database instance.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeInstanceDasProResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeInstanceDasProResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_das_pro_with_options_async(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        """
        @summary Queries whether Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled for a database instance.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogConfig](https://help.aliyun.com/document_detail/2778837.html) operation to query the DAS Enterprise Edition configurations of a database instance.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeInstanceDasProResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeInstanceDasProResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_das_pro(
        self,
        request: das20200116_models.DescribeInstanceDasProRequest,
    ) -> das20200116_models.DescribeInstanceDasProResponse:
        """
        @summary Queries whether Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled for a database instance.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogConfig](https://help.aliyun.com/document_detail/2778837.html) operation to query the DAS Enterprise Edition configurations of a database instance.
        
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
        @summary Queries whether Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled for a database instance.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogConfig](https://help.aliyun.com/document_detail/2778837.html) operation to query the DAS Enterprise Edition configurations of a database instance.
        
        @param request: DescribeInstanceDasProRequest
        @return: DescribeInstanceDasProResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_das_pro_with_options_async(request, runtime)

    def describe_slow_log_histogram_async_with_options(
        self,
        request: das20200116_models.DescribeSlowLogHistogramAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSlowLogHistogramAsyncResponse:
        """
        @summary DescribeSlowLogHistogramAsync
        
        @param request: DescribeSlowLogHistogramAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogHistogramAsyncResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogHistogramAsync',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogHistogramAsyncResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogHistogramAsyncResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_slow_log_histogram_async_with_options_async(
        self,
        request: das20200116_models.DescribeSlowLogHistogramAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSlowLogHistogramAsyncResponse:
        """
        @summary DescribeSlowLogHistogramAsync
        
        @param request: DescribeSlowLogHistogramAsyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogHistogramAsyncResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogHistogramAsync',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogHistogramAsyncResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogHistogramAsyncResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_slow_log_histogram_async(
        self,
        request: das20200116_models.DescribeSlowLogHistogramAsyncRequest,
    ) -> das20200116_models.DescribeSlowLogHistogramAsyncResponse:
        """
        @summary DescribeSlowLogHistogramAsync
        
        @param request: DescribeSlowLogHistogramAsyncRequest
        @return: DescribeSlowLogHistogramAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_histogram_async_with_options(request, runtime)

    async def describe_slow_log_histogram_async_async(
        self,
        request: das20200116_models.DescribeSlowLogHistogramAsyncRequest,
    ) -> das20200116_models.DescribeSlowLogHistogramAsyncResponse:
        """
        @summary DescribeSlowLogHistogramAsync
        
        @param request: DescribeSlowLogHistogramAsyncRequest
        @return: DescribeSlowLogHistogramAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_histogram_async_with_options_async(request, runtime)

    def describe_slow_log_statistic_with_options(
        self,
        request: das20200116_models.DescribeSlowLogStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSlowLogStatisticResponse:
        """
        @summary 慢日志统计信息
        
        @param request: DescribeSlowLogStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogStatisticResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asc):
            body['Asc'] = request.asc
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogStatistic',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogStatisticResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogStatisticResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_slow_log_statistic_with_options_async(
        self,
        request: das20200116_models.DescribeSlowLogStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSlowLogStatisticResponse:
        """
        @summary 慢日志统计信息
        
        @param request: DescribeSlowLogStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogStatisticResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asc):
            body['Asc'] = request.asc
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogStatistic',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogStatisticResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSlowLogStatisticResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_slow_log_statistic(
        self,
        request: das20200116_models.DescribeSlowLogStatisticRequest,
    ) -> das20200116_models.DescribeSlowLogStatisticResponse:
        """
        @summary 慢日志统计信息
        
        @param request: DescribeSlowLogStatisticRequest
        @return: DescribeSlowLogStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_statistic_with_options(request, runtime)

    async def describe_slow_log_statistic_async(
        self,
        request: das20200116_models.DescribeSlowLogStatisticRequest,
    ) -> das20200116_models.DescribeSlowLogStatisticResponse:
        """
        @summary 慢日志统计信息
        
        @param request: DescribeSlowLogStatisticRequest
        @return: DescribeSlowLogStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_statistic_with_options_async(request, runtime)

    def describe_sql_log_config_with_options(
        self,
        request: das20200116_models.DescribeSqlLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogConfigResponse:
        """
        @summary Queries the configurations of Database Autonomy Service (DAS) Enterprise Edition that is enabled for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sql_log_config_with_options_async(
        self,
        request: das20200116_models.DescribeSqlLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogConfigResponse:
        """
        @summary Queries the configurations of Database Autonomy Service (DAS) Enterprise Edition that is enabled for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sql_log_config(
        self,
        request: das20200116_models.DescribeSqlLogConfigRequest,
    ) -> das20200116_models.DescribeSqlLogConfigResponse:
        """
        @summary Queries the configurations of Database Autonomy Service (DAS) Enterprise Edition that is enabled for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogConfigRequest
        @return: DescribeSqlLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_log_config_with_options(request, runtime)

    async def describe_sql_log_config_async(
        self,
        request: das20200116_models.DescribeSqlLogConfigRequest,
    ) -> das20200116_models.DescribeSqlLogConfigResponse:
        """
        @summary Queries the configurations of Database Autonomy Service (DAS) Enterprise Edition that is enabled for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogConfigRequest
        @return: DescribeSqlLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_log_config_with_options_async(request, runtime)

    def describe_sql_log_records_with_options(
        self,
        request: das20200116_models.DescribeSqlLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogRecordsResponse:
        """
        @summary Queries the log details of a database instance for which Database Autonomy Service (DAS) Enterprise Edition is enabled.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogRecords',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogRecordsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogRecordsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sql_log_records_with_options_async(
        self,
        request: das20200116_models.DescribeSqlLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogRecordsResponse:
        """
        @summary Queries the log details of a database instance for which Database Autonomy Service (DAS) Enterprise Edition is enabled.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogRecords',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogRecordsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogRecordsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sql_log_records(
        self,
        request: das20200116_models.DescribeSqlLogRecordsRequest,
    ) -> das20200116_models.DescribeSqlLogRecordsResponse:
        """
        @summary Queries the log details of a database instance for which Database Autonomy Service (DAS) Enterprise Edition is enabled.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogRecordsRequest
        @return: DescribeSqlLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_log_records_with_options(request, runtime)

    async def describe_sql_log_records_async(
        self,
        request: das20200116_models.DescribeSqlLogRecordsRequest,
    ) -> das20200116_models.DescribeSqlLogRecordsResponse:
        """
        @summary Queries the log details of a database instance for which Database Autonomy Service (DAS) Enterprise Edition is enabled.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogRecordsRequest
        @return: DescribeSqlLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_log_records_with_options_async(request, runtime)

    def describe_sql_log_statistic_with_options(
        self,
        request: das20200116_models.DescribeSqlLogStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogStatisticResponse:
        """
        @summary Queries the statistics of Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogStatisticResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogStatistic',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogStatisticResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogStatisticResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sql_log_statistic_with_options_async(
        self,
        request: das20200116_models.DescribeSqlLogStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogStatisticResponse:
        """
        @summary Queries the statistics of Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogStatisticResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogStatistic',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogStatisticResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogStatisticResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sql_log_statistic(
        self,
        request: das20200116_models.DescribeSqlLogStatisticRequest,
    ) -> das20200116_models.DescribeSqlLogStatisticResponse:
        """
        @summary Queries the statistics of Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogStatisticRequest
        @return: DescribeSqlLogStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_log_statistic_with_options(request, runtime)

    async def describe_sql_log_statistic_async(
        self,
        request: das20200116_models.DescribeSqlLogStatisticRequest,
    ) -> das20200116_models.DescribeSqlLogStatisticResponse:
        """
        @summary Queries the statistics of Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogStatisticRequest
        @return: DescribeSqlLogStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_log_statistic_with_options_async(request, runtime)

    def describe_sql_log_task_with_options(
        self,
        request: das20200116_models.DescribeSqlLogTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogTaskResponse:
        """
        @summary Queries the details of an offline task in Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sql_log_task_with_options_async(
        self,
        request: das20200116_models.DescribeSqlLogTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogTaskResponse:
        """
        @summary Queries the details of an offline task in Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogTask',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sql_log_task(
        self,
        request: das20200116_models.DescribeSqlLogTaskRequest,
    ) -> das20200116_models.DescribeSqlLogTaskResponse:
        """
        @summary Queries the details of an offline task in Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTaskRequest
        @return: DescribeSqlLogTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_log_task_with_options(request, runtime)

    async def describe_sql_log_task_async(
        self,
        request: das20200116_models.DescribeSqlLogTaskRequest,
    ) -> das20200116_models.DescribeSqlLogTaskResponse:
        """
        @summary Queries the details of an offline task in Database Autonomy Service (DAS) Enterprise Edition.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTaskRequest
        @return: DescribeSqlLogTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_log_task_with_options_async(request, runtime)

    def describe_sql_log_tasks_with_options(
        self,
        request: das20200116_models.DescribeSqlLogTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogTasksResponse:
        """
        @summary Queries the audit log tasks of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sql_log_tasks_with_options_async(
        self,
        request: das20200116_models.DescribeSqlLogTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeSqlLogTasksResponse:
        """
        @summary Queries the audit log tasks of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSqlLogTasksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSqlLogTasks',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeSqlLogTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sql_log_tasks(
        self,
        request: das20200116_models.DescribeSqlLogTasksRequest,
    ) -> das20200116_models.DescribeSqlLogTasksResponse:
        """
        @summary Queries the audit log tasks of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTasksRequest
        @return: DescribeSqlLogTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_log_tasks_with_options(request, runtime)

    async def describe_sql_log_tasks_async(
        self,
        request: das20200116_models.DescribeSqlLogTasksRequest,
    ) -> das20200116_models.DescribeSqlLogTasksResponse:
        """
        @summary Queries the audit log tasks of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: DescribeSqlLogTasksRequest
        @return: DescribeSqlLogTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_log_tasks_with_options_async(request, runtime)

    def describe_top_big_keys_with_options(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        """
        @summary Queries the top 100 large keys over a period of time.
        
        @description The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeTopBigKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeTopBigKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_top_big_keys_with_options_async(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        """
        @summary Queries the top 100 large keys over a period of time.
        
        @description The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeTopBigKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeTopBigKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_top_big_keys(
        self,
        request: das20200116_models.DescribeTopBigKeysRequest,
    ) -> das20200116_models.DescribeTopBigKeysResponse:
        """
        @summary Queries the top 100 large keys over a period of time.
        
        @description The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Queries the top 100 large keys over a period of time.
        
        @description The list, hash, set, and zset keys are sorted based on the number of elements in these keys. The top three keys that have the most elements are considered large keys.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is ApsaraDB for Redis Community Edition instances that use a major version of 5.0 or later or a performance-enhanced instance of the ApsaraDB for Redis Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Queries the top 100 hotkeys over a period of time.
        
        @description If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeTopHotKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeTopHotKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_top_hot_keys_with_options_async(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        """
        @summary Queries the top 100 hotkeys over a period of time.
        
        @description If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DescribeTopHotKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DescribeTopHotKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_top_hot_keys(
        self,
        request: das20200116_models.DescribeTopHotKeysRequest,
    ) -> das20200116_models.DescribeTopHotKeysResponse:
        """
        @summary Queries the top 100 hotkeys over a period of time.
        
        @description If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Queries the top 100 hotkeys over a period of time.
        
        @description If the number of queries per second (QPS) of a key is greater than 3,000, the key is considered a hot key.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than 4.3.3. We recommend that you use the latest version.
        The version of Database Autonomy Service (DAS) SDK must be 1.0.2 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is available only for an ApsaraDB for Redis instance of one of the following versions:
        The instance is a Community Edition instance that uses a major version of 4.0 or later or a performance-enhanced instance of the Enhanced Edition (Tair).
        The ApsaraDB for Redis instance is updated to the latest minor version.
        
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
        @summary Disables all throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_all_sql_concurrency_control_rules_with_options_async(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        """
        @summary Disables all throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableAllSqlConcurrencyControlRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_all_sql_concurrency_control_rules(
        self,
        request: das20200116_models.DisableAllSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.DisableAllSqlConcurrencyControlRulesResponse:
        """
        @summary Disables all throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Disables all throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Disables the automatic tablespace fragment recycling feature for database instances at a time.
        
        @description If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableAutoResourceOptimizeRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableAutoResourceOptimizeRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_auto_resource_optimize_rules_with_options_async(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        """
        @summary Disables the automatic tablespace fragment recycling feature for database instances at a time.
        
        @description If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableAutoResourceOptimizeRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableAutoResourceOptimizeRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_auto_resource_optimize_rules(
        self,
        request: das20200116_models.DisableAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.DisableAutoResourceOptimizeRulesResponse:
        """
        @summary Disables the automatic tablespace fragment recycling feature for database instances at a time.
        
        @description If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        @summary Disables the automatic tablespace fragment recycling feature for database instances at a time.
        
        @description If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        @summary Disables the automatic SQL throttling feature for multiple database instances at a time.
        
        @description If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableAutoThrottleRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableAutoThrottleRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_auto_throttle_rules_with_options_async(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        """
        @summary Disables the automatic SQL throttling feature for multiple database instances at a time.
        
        @description If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableAutoThrottleRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableAutoThrottleRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_auto_throttle_rules(
        self,
        request: das20200116_models.DisableAutoThrottleRulesRequest,
    ) -> das20200116_models.DisableAutoThrottleRulesResponse:
        """
        @summary Disables the automatic SQL throttling feature for multiple database instances at a time.
        
        @description If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        @summary Disables the automatic SQL throttling feature for multiple database instances at a time.
        
        @description If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        @summary Deactivates Database Autonomy Service (DAS) Professional Edition.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to enable or disable DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableDasProResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableDasProResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_das_pro_with_options_async(
        self,
        request: das20200116_models.DisableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableDasProResponse:
        """
        @summary Deactivates Database Autonomy Service (DAS) Professional Edition.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to enable or disable DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableDasProResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableDasProResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_das_pro(
        self,
        request: das20200116_models.DisableDasProRequest,
    ) -> das20200116_models.DisableDasProResponse:
        """
        @summary Deactivates Database Autonomy Service (DAS) Professional Edition.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to enable or disable DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        @summary Deactivates Database Autonomy Service (DAS) Professional Edition.
        
        @description    For more information about the database instances that support DAS Enterprise Edition, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to enable or disable DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        @summary Disables the auto scaling feature for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableInstanceDasConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableInstanceDasConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_instance_das_config_with_options_async(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        """
        @summary Disables the auto scaling feature for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableInstanceDasConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableInstanceDasConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_instance_das_config(
        self,
        request: das20200116_models.DisableInstanceDasConfigRequest,
    ) -> das20200116_models.DisableInstanceDasConfigResponse:
        """
        @summary Disables the auto scaling feature for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances.
        
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
        @summary Disables the auto scaling feature for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to ApsaraDB for Redis instances.
        
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
        @summary Disables a throttling rule.
        
        @description This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableSqlConcurrencyControlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableSqlConcurrencyControlResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_sql_concurrency_control_with_options_async(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        """
        @summary Disables a throttling rule.
        
        @description This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.DisableSqlConcurrencyControlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.DisableSqlConcurrencyControlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_sql_concurrency_control(
        self,
        request: das20200116_models.DisableSqlConcurrencyControlRequest,
    ) -> das20200116_models.DisableSqlConcurrencyControlResponse:
        """
        @summary Disables a throttling rule.
        
        @description This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Disables a throttling rule.
        
        @description This operation is applicable to the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Activates Database Autonomy Service (DAS) Professional Edition.
        
        @description    If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to activate or deactivate DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [DAS editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.EnableDasProResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.EnableDasProResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_das_pro_with_options_async(
        self,
        request: das20200116_models.EnableDasProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableDasProResponse:
        """
        @summary Activates Database Autonomy Service (DAS) Professional Edition.
        
        @description    If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to activate or deactivate DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [DAS editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.EnableDasProResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.EnableDasProResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_das_pro(
        self,
        request: das20200116_models.EnableDasProRequest,
    ) -> das20200116_models.EnableDasProResponse:
        """
        @summary Activates Database Autonomy Service (DAS) Professional Edition.
        
        @description    If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to activate or deactivate DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [DAS editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        @summary Activates Database Autonomy Service (DAS) Professional Edition.
        
        @description    If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1.
        >  We recommend that you call the [ModifySqlLogConfig](https://help.aliyun.com/document_detail/2778835.html) operation to activate or deactivate DAS Enterprise Edition for a database instance. For more information about the databases and regions supported by each version of DAS Enterprise Edition, see [DAS editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
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
        @summary Enables SQL throttling to control the numbers of database access requests and concurrent SQL statements.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.EnableSqlConcurrencyControlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.EnableSqlConcurrencyControlResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_sql_concurrency_control_with_options_async(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        """
        @summary Enables SQL throttling to control the numbers of database access requests and concurrent SQL statements.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.EnableSqlConcurrencyControlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.EnableSqlConcurrencyControlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_sql_concurrency_control(
        self,
        request: das20200116_models.EnableSqlConcurrencyControlRequest,
    ) -> das20200116_models.EnableSqlConcurrencyControlResponse:
        """
        @summary Enables SQL throttling to control the numbers of database access requests and concurrent SQL statements.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Enables SQL throttling to control the numbers of database access requests and concurrent SQL statements.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Asynchronously queries the IDs of SQL statements that generate a MySQL error code in the SQL Explorer results of a database instance.
        
        @description >  GetAsyncErrorRequestListByCode is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the *isFinish** parameter is **false** in the response, wait for 1 second and then send a request again. If the value of the **isFinish** parameter is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Enable and manage DAS Economy Edition and DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestListByCodeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestListByCodeResponse(),
                self.execute(params, req, runtime)
            )

    async def get_async_error_request_list_by_code_with_options_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        """
        @summary Asynchronously queries the IDs of SQL statements that generate a MySQL error code in the SQL Explorer results of a database instance.
        
        @description >  GetAsyncErrorRequestListByCode is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the *isFinish** parameter is **false** in the response, wait for 1 second and then send a request again. If the value of the **isFinish** parameter is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Enable and manage DAS Economy Edition and DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestListByCodeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestListByCodeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_async_error_request_list_by_code(
        self,
        request: das20200116_models.GetAsyncErrorRequestListByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestListByCodeResponse:
        """
        @summary Asynchronously queries the IDs of SQL statements that generate a MySQL error code in the SQL Explorer results of a database instance.
        
        @description >  GetAsyncErrorRequestListByCode is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the *isFinish** parameter is **false** in the response, wait for 1 second and then send a request again. If the value of the **isFinish** parameter is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Enable and manage DAS Economy Edition and DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        @summary Asynchronously queries the IDs of SQL statements that generate a MySQL error code in the SQL Explorer results of a database instance.
        
        @description >  GetAsyncErrorRequestListByCode is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the *isFinish** parameter is **false** in the response, wait for 1 second and then send a request again. If the value of the **isFinish** parameter is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Enable and manage DAS Economy Edition and DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        @summary Asynchronously queries the MySQL error codes in SQL Explorer data and the number of SQL queries corresponding to each error code.
        
        @description >  GetAsyncErrorRequestStatByCode is an asynchronous operation After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatByCodeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatByCodeResponse(),
                self.execute(params, req, runtime)
            )

    async def get_async_error_request_stat_by_code_with_options_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        """
        @summary Asynchronously queries the MySQL error codes in SQL Explorer data and the number of SQL queries corresponding to each error code.
        
        @description >  GetAsyncErrorRequestStatByCode is an asynchronous operation After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatByCodeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatByCodeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_async_error_request_stat_by_code(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatByCodeRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatByCodeResponse:
        """
        @summary Asynchronously queries the MySQL error codes in SQL Explorer data and the number of SQL queries corresponding to each error code.
        
        @description >  GetAsyncErrorRequestStatByCode is an asynchronous operation After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Asynchronously queries the MySQL error codes in SQL Explorer data and the number of SQL queries corresponding to each error code.
        
        @description >  GetAsyncErrorRequestStatByCode is an asynchronous operation After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Asynchronously obtains the number of failed executions of SQL templates based on SQL Explorer data.
        
        @description >  GetAsyncErrorRequestStatResult is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_async_error_request_stat_result_with_options_async(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        """
        @summary Asynchronously obtains the number of failed executions of SQL templates based on SQL Explorer data.
        
        @description >  GetAsyncErrorRequestStatResult is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAsyncErrorRequestStatResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_async_error_request_stat_result(
        self,
        request: das20200116_models.GetAsyncErrorRequestStatResultRequest,
    ) -> das20200116_models.GetAsyncErrorRequestStatResultResponse:
        """
        @summary Asynchronously obtains the number of failed executions of SQL templates based on SQL Explorer data.
        
        @description >  GetAsyncErrorRequestStatResult is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Asynchronously obtains the number of failed executions of SQL templates based on SQL Explorer data.
        
        @description >  GetAsyncErrorRequestStatResult is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the usage of auto-increment table IDs.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutoIncrementUsageStatisticResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutoIncrementUsageStatisticResponse(),
                self.execute(params, req, runtime)
            )

    async def get_auto_increment_usage_statistic_with_options_async(
        self,
        request: das20200116_models.GetAutoIncrementUsageStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoIncrementUsageStatisticResponse:
        """
        @summary Queries the usage of auto-increment table IDs.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutoIncrementUsageStatisticResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutoIncrementUsageStatisticResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_auto_increment_usage_statistic(
        self,
        request: das20200116_models.GetAutoIncrementUsageStatisticRequest,
    ) -> das20200116_models.GetAutoIncrementUsageStatisticResponse:
        """
        @summary Queries the usage of auto-increment table IDs.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
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
        @summary Queries the usage of auto-increment table IDs.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call DAS, you must set the region to cn-shanghai.
        
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
        @summary Queries the automatic fragment recycling rules of database instances.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutoResourceOptimizeRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutoResourceOptimizeRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_auto_resource_optimize_rules_with_options_async(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        """
        @summary Queries the automatic fragment recycling rules of database instances.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutoResourceOptimizeRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutoResourceOptimizeRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_auto_resource_optimize_rules(
        self,
        request: das20200116_models.GetAutoResourceOptimizeRulesRequest,
    ) -> das20200116_models.GetAutoResourceOptimizeRulesResponse:
        """
        @summary Queries the automatic fragment recycling rules of database instances.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
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
        @summary Queries the automatic fragment recycling rules of database instances.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance is an ApsaraDB RDS for MySQL instance of High-availability Edition.
        The database instance has four or more cores, and **innodb_file_per_table** is set to **ON**.
        
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
        @summary Queries the automatic SQL throttling rules of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutoThrottleRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutoThrottleRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_auto_throttle_rules_with_options_async(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        """
        @summary Queries the automatic SQL throttling rules of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutoThrottleRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutoThrottleRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_auto_throttle_rules(
        self,
        request: das20200116_models.GetAutoThrottleRulesRequest,
    ) -> das20200116_models.GetAutoThrottleRulesResponse:
        """
        @summary Queries the automatic SQL throttling rules of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
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
        @summary Queries the automatic SQL throttling rules of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
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
        @summary Queries the details of notification events of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventContentResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventContentResponse(),
                self.execute(params, req, runtime)
            )

    async def get_autonomous_notify_event_content_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        """
        @summary Queries the details of notification events of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventContentResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventContentResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_autonomous_notify_event_content(
        self,
        request: das20200116_models.GetAutonomousNotifyEventContentRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventContentResponse:
        """
        @summary Queries the details of notification events of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        @summary Queries the details of notification events of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        @summary Queries the notification events of one or more urgency levels within a period.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
                self.execute(params, req, runtime)
            )

    async def get_autonomous_notify_events_in_range_with_options_async(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        """
        @summary Queries the notification events of one or more urgency levels within a period.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetAutonomousNotifyEventsInRangeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_autonomous_notify_events_in_range(
        self,
        request: das20200116_models.GetAutonomousNotifyEventsInRangeRequest,
    ) -> das20200116_models.GetAutonomousNotifyEventsInRangeResponse:
        """
        @summary Queries the notification events of one or more urgency levels within a period.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        @summary Queries the notification events of one or more urgency levels within a period.
        
        @description Before you call this operation, take note of the following items:
        If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        After your instance is connected to DAS, notification events such as snapshot capture are triggered if DAS detects changes to database monitoring metrics during anomaly detection.
        >  You can query the details of notification events only if the autonomy center is enabled. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        
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
        @summary Queries the blocking data of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetBlockingDetailListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetBlockingDetailListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_blocking_detail_list_with_options_async(
        self,
        request: das20200116_models.GetBlockingDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetBlockingDetailListResponse:
        """
        @summary Queries the blocking data of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetBlockingDetailListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetBlockingDetailListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_blocking_detail_list(
        self,
        request: das20200116_models.GetBlockingDetailListRequest,
    ) -> das20200116_models.GetBlockingDetailListResponse:
        """
        @summary Queries the blocking data of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the blocking data of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the diagnosis of network connectivity when a user accesses a specific database instance by specifying an IP address.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDBInstanceConnectivityDiagnosisResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDBInstanceConnectivityDiagnosisResponse(),
                self.execute(params, req, runtime)
            )

    async def get_dbinstance_connectivity_diagnosis_with_options_async(
        self,
        request: das20200116_models.GetDBInstanceConnectivityDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDBInstanceConnectivityDiagnosisResponse:
        """
        @summary Queries the diagnosis of network connectivity when a user accesses a specific database instance by specifying an IP address.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDBInstanceConnectivityDiagnosisResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDBInstanceConnectivityDiagnosisResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_dbinstance_connectivity_diagnosis(
        self,
        request: das20200116_models.GetDBInstanceConnectivityDiagnosisRequest,
    ) -> das20200116_models.GetDBInstanceConnectivityDiagnosisResponse:
        """
        @summary Queries the diagnosis of network connectivity when a user accesses a specific database instance by specifying an IP address.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        @summary Queries the diagnosis of network connectivity when a user accesses a specific database instance by specifying an IP address.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        @summary Queries the storage usage of a database instance for which Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled.
        
        @description    For information about the database instances that support this operation, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogStatistic](https://help.aliyun.com/document_detail/2778836.html) operation to query the data statistics of a database instance for which DAS Enterprise Edition is enabled.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDasProServiceUsageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDasProServiceUsageResponse(),
                self.execute(params, req, runtime)
            )

    async def get_das_pro_service_usage_with_options_async(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        """
        @summary Queries the storage usage of a database instance for which Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled.
        
        @description    For information about the database instances that support this operation, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogStatistic](https://help.aliyun.com/document_detail/2778836.html) operation to query the data statistics of a database instance for which DAS Enterprise Edition is enabled.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDasProServiceUsageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDasProServiceUsageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_das_pro_service_usage(
        self,
        request: das20200116_models.GetDasProServiceUsageRequest,
    ) -> das20200116_models.GetDasProServiceUsageResponse:
        """
        @summary Queries the storage usage of a database instance for which Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled.
        
        @description    For information about the database instances that support this operation, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogStatistic](https://help.aliyun.com/document_detail/2778836.html) operation to query the data statistics of a database instance for which DAS Enterprise Edition is enabled.
        
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
        @summary Queries the storage usage of a database instance for which Database Autonomy Service (DAS) Enterprise Edition V1 or V2 is enabled.
        
        @description    For information about the database instances that support this operation, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable only to DAS Enterprise Edition V1 and V2.
        >  We recommend that you call the [DescribeSqlLogStatistic](https://help.aliyun.com/document_detail/2778836.html) operation to query the data statistics of a database instance for which DAS Enterprise Edition is enabled.
        
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
        @summary Queries the hot data of audit logs.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to PolarDB for MySQL, ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and ApsaraDB RDS for SQL Server.
        >  The beginning of the time range to query can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed one day. This operation can return a maximum of 10,000 entries.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDasSQLLogHotDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDasSQLLogHotDataResponse(),
                self.execute(params, req, runtime)
            )

    async def get_das_sqllog_hot_data_with_options_async(
        self,
        request: das20200116_models.GetDasSQLLogHotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDasSQLLogHotDataResponse:
        """
        @summary Queries the hot data of audit logs.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to PolarDB for MySQL, ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and ApsaraDB RDS for SQL Server.
        >  The beginning of the time range to query can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed one day. This operation can return a maximum of 10,000 entries.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDasSQLLogHotDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDasSQLLogHotDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_das_sqllog_hot_data(
        self,
        request: das20200116_models.GetDasSQLLogHotDataRequest,
    ) -> das20200116_models.GetDasSQLLogHotDataResponse:
        """
        @summary Queries the hot data of audit logs.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to PolarDB for MySQL, ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and ApsaraDB RDS for SQL Server.
        >  The beginning of the time range to query can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed one day. This operation can return a maximum of 10,000 entries.
        
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
        @summary Queries the hot data of audit logs.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation is applicable to PolarDB for MySQL, ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and ApsaraDB RDS for SQL Server.
        >  The beginning of the time range to query can be up to seven days earlier than the current time. The interval between the start time and the end time cannot exceed one day. This operation can return a maximum of 10,000 entries.
        
        @param request: GetDasSQLLogHotDataRequest
        @return: GetDasSQLLogHotDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_das_sqllog_hot_data_with_options_async(request, runtime)

    def get_dead_lock_detail_with_options(
        self,
        request: das20200116_models.GetDeadLockDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockDetailResponse:
        """
        @summary 查询单个死锁详情
        
        @param request: GetDeadLockDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadLockDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.text_id):
            query['TextId'] = request.text_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeadLockDetail',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailResponse(),
                self.execute(params, req, runtime)
            )

    async def get_dead_lock_detail_with_options_async(
        self,
        request: das20200116_models.GetDeadLockDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockDetailResponse:
        """
        @summary 查询单个死锁详情
        
        @param request: GetDeadLockDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadLockDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.text_id):
            query['TextId'] = request.text_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeadLockDetail',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_dead_lock_detail(
        self,
        request: das20200116_models.GetDeadLockDetailRequest,
    ) -> das20200116_models.GetDeadLockDetailResponse:
        """
        @summary 查询单个死锁详情
        
        @param request: GetDeadLockDetailRequest
        @return: GetDeadLockDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dead_lock_detail_with_options(request, runtime)

    async def get_dead_lock_detail_async(
        self,
        request: das20200116_models.GetDeadLockDetailRequest,
    ) -> das20200116_models.GetDeadLockDetailResponse:
        """
        @summary 查询单个死锁详情
        
        @param request: GetDeadLockDetailRequest
        @return: GetDeadLockDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dead_lock_detail_with_options_async(request, runtime)

    def get_dead_lock_detail_list_with_options(
        self,
        request: das20200116_models.GetDeadLockDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockDetailListResponse:
        """
        @summary Queries the deadlock details of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_dead_lock_detail_list_with_options_async(
        self,
        request: das20200116_models.GetDeadLockDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockDetailListResponse:
        """
        @summary Queries the deadlock details of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadLockDetailListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_dead_lock_detail_list(
        self,
        request: das20200116_models.GetDeadLockDetailListRequest,
    ) -> das20200116_models.GetDeadLockDetailListResponse:
        """
        @summary Queries the deadlock details of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the deadlock details of an ApsaraDB RDS for SQL Server instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: GetDeadLockDetailListRequest
        @return: GetDeadLockDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dead_lock_detail_list_with_options_async(request, runtime)

    def get_dead_lock_history_with_options(
        self,
        request: das20200116_models.GetDeadLockHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockHistoryResponse:
        """
        @summary 获取历史死锁记录
        
        @param request: GetDeadLockHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadLockHistoryResponse
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
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeadLockHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadLockHistoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadLockHistoryResponse(),
                self.execute(params, req, runtime)
            )

    async def get_dead_lock_history_with_options_async(
        self,
        request: das20200116_models.GetDeadLockHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadLockHistoryResponse:
        """
        @summary 获取历史死锁记录
        
        @param request: GetDeadLockHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadLockHistoryResponse
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
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeadLockHistory',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadLockHistoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadLockHistoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_dead_lock_history(
        self,
        request: das20200116_models.GetDeadLockHistoryRequest,
    ) -> das20200116_models.GetDeadLockHistoryResponse:
        """
        @summary 获取历史死锁记录
        
        @param request: GetDeadLockHistoryRequest
        @return: GetDeadLockHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dead_lock_history_with_options(request, runtime)

    async def get_dead_lock_history_async(
        self,
        request: das20200116_models.GetDeadLockHistoryRequest,
    ) -> das20200116_models.GetDeadLockHistoryResponse:
        """
        @summary 获取历史死锁记录
        
        @param request: GetDeadLockHistoryRequest
        @return: GetDeadLockHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dead_lock_history_with_options_async(request, runtime)

    def get_deadlock_histogram_with_options(
        self,
        request: das20200116_models.GetDeadlockHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadlockHistogramResponse:
        """
        @summary 查询时间范围内基于错误日志分析的死锁数量
        
        @param request: GetDeadlockHistogramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadlockHistogramResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeadlockHistogram',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadlockHistogramResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadlockHistogramResponse(),
                self.execute(params, req, runtime)
            )

    async def get_deadlock_histogram_with_options_async(
        self,
        request: das20200116_models.GetDeadlockHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetDeadlockHistogramResponse:
        """
        @summary 查询时间范围内基于错误日志分析的死锁数量
        
        @param request: GetDeadlockHistogramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeadlockHistogramResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeadlockHistogram',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetDeadlockHistogramResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetDeadlockHistogramResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_deadlock_histogram(
        self,
        request: das20200116_models.GetDeadlockHistogramRequest,
    ) -> das20200116_models.GetDeadlockHistogramResponse:
        """
        @summary 查询时间范围内基于错误日志分析的死锁数量
        
        @param request: GetDeadlockHistogramRequest
        @return: GetDeadlockHistogramResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_deadlock_histogram_with_options(request, runtime)

    async def get_deadlock_histogram_async(
        self,
        request: das20200116_models.GetDeadlockHistogramRequest,
    ) -> das20200116_models.GetDeadlockHistogramResponse:
        """
        @summary 查询时间范围内基于错误日志分析的死锁数量
        
        @param request: GetDeadlockHistogramRequest
        @return: GetDeadlockHistogramResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_deadlock_histogram_with_options_async(request, runtime)

    def get_endpoint_switch_task_with_options(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        """
        @param request: GetEndpointSwitchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEndpointSwitchTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetEndpointSwitchTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetEndpointSwitchTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def get_endpoint_switch_task_with_options_async(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        """
        @param request: GetEndpointSwitchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEndpointSwitchTaskResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetEndpointSwitchTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetEndpointSwitchTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_endpoint_switch_task(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        """
        @param request: GetEndpointSwitchTaskRequest
        @return: GetEndpointSwitchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_switch_task_with_options(request, runtime)

    async def get_endpoint_switch_task_async(
        self,
        request: das20200116_models.GetEndpointSwitchTaskRequest,
    ) -> das20200116_models.GetEndpointSwitchTaskResponse:
        """
        @param request: GetEndpointSwitchTaskRequest
        @return: GetEndpointSwitchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_endpoint_switch_task_with_options_async(request, runtime)

    def get_error_request_sample_with_options(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        """
        @summary Asynchronously queries information about failed SQL queries in SQL Explorer data. You can query up to 20 failed SQL queries within the specific time range.
        
        @description >  GetErrorRequestSample is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetErrorRequestSampleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetErrorRequestSampleResponse(),
                self.execute(params, req, runtime)
            )

    async def get_error_request_sample_with_options_async(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        """
        @summary Asynchronously queries information about failed SQL queries in SQL Explorer data. You can query up to 20 failed SQL queries within the specific time range.
        
        @description >  GetErrorRequestSample is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetErrorRequestSampleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetErrorRequestSampleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_error_request_sample(
        self,
        request: das20200116_models.GetErrorRequestSampleRequest,
    ) -> das20200116_models.GetErrorRequestSampleResponse:
        """
        @summary Asynchronously queries information about failed SQL queries in SQL Explorer data. You can query up to 20 failed SQL queries within the specific time range.
        
        @description >  GetErrorRequestSample is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Asynchronously queries information about failed SQL queries in SQL Explorer data. You can query up to 20 failed SQL queries within the specific time range.
        
        @description >  GetErrorRequestSample is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of *isFinish** is **false** in the response, wait for 1 second and then send a request again. If the value of **isFinish** is **true**, the complete results are returned.
        This API operation supports only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters for which Database Autonomy Service (DAS) Enterprise Edition is enabled. For more information, see [Purchase DAS Enterprise Edition](https://help.aliyun.com/document_detail/163298.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the event subscription settings of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetEventSubscriptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetEventSubscriptionResponse(),
                self.execute(params, req, runtime)
            )

    async def get_event_subscription_with_options_async(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        """
        @summary Queries the event subscription settings of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetEventSubscriptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetEventSubscriptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_event_subscription(
        self,
        request: das20200116_models.GetEventSubscriptionRequest,
    ) -> das20200116_models.GetEventSubscriptionResponse:
        """
        @summary Queries the event subscription settings of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        @summary Queries the event subscription settings of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        The database instance that you want to manage is connected to DAS.
        
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
        @summary Collects the full request statistics in the SQL Explorer results of a database instance by access source.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetFullRequestOriginStatByInstanceIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetFullRequestOriginStatByInstanceIdResponse(),
                self.execute(params, req, runtime)
            )

    async def get_full_request_origin_stat_by_instance_id_with_options_async(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        """
        @summary Collects the full request statistics in the SQL Explorer results of a database instance by access source.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetFullRequestOriginStatByInstanceIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetFullRequestOriginStatByInstanceIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_full_request_origin_stat_by_instance_id(
        self,
        request: das20200116_models.GetFullRequestOriginStatByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestOriginStatByInstanceIdResponse:
        """
        @summary Collects the full request statistics in the SQL Explorer results of a database instance by access source.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        @summary Collects the full request statistics in the SQL Explorer results of a database instance by access source.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        
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
        @summary Queries sample SQL statements in the SQL Explorer data of a database instance by SQL ID. You can query up to 20 sample SQL statements.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about the database engines that support SQL Explorer, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetFullRequestSampleByInstanceIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetFullRequestSampleByInstanceIdResponse(),
                self.execute(params, req, runtime)
            )

    async def get_full_request_sample_by_instance_id_with_options_async(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        """
        @summary Queries sample SQL statements in the SQL Explorer data of a database instance by SQL ID. You can query up to 20 sample SQL statements.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about the database engines that support SQL Explorer, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetFullRequestSampleByInstanceIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetFullRequestSampleByInstanceIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_full_request_sample_by_instance_id(
        self,
        request: das20200116_models.GetFullRequestSampleByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestSampleByInstanceIdResponse:
        """
        @summary Queries sample SQL statements in the SQL Explorer data of a database instance by SQL ID. You can query up to 20 sample SQL statements.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about the database engines that support SQL Explorer, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries sample SQL statements in the SQL Explorer data of a database instance by SQL ID. You can query up to 20 sample SQL statements.
        
        @description The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about the database engines that support SQL Explorer, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Asynchronously collects the full request statistics in the SQL Explorer results of a database instance by SQL ID.
        
        @description >  GetFullRequestStatResultByInstanceId is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the isFinish parameter is *false** in the response, wait for 1 second and then send a request again. If the value of the isFinish parameter is **true**, the complete results are returned.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetFullRequestStatResultByInstanceIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetFullRequestStatResultByInstanceIdResponse(),
                self.execute(params, req, runtime)
            )

    async def get_full_request_stat_result_by_instance_id_with_options_async(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        """
        @summary Asynchronously collects the full request statistics in the SQL Explorer results of a database instance by SQL ID.
        
        @description >  GetFullRequestStatResultByInstanceId is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the isFinish parameter is *false** in the response, wait for 1 second and then send a request again. If the value of the isFinish parameter is **true**, the complete results are returned.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetFullRequestStatResultByInstanceIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetFullRequestStatResultByInstanceIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_full_request_stat_result_by_instance_id(
        self,
        request: das20200116_models.GetFullRequestStatResultByInstanceIdRequest,
    ) -> das20200116_models.GetFullRequestStatResultByInstanceIdResponse:
        """
        @summary Asynchronously collects the full request statistics in the SQL Explorer results of a database instance by SQL ID.
        
        @description >  GetFullRequestStatResultByInstanceId is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the isFinish parameter is *false** in the response, wait for 1 second and then send a request again. If the value of the isFinish parameter is **true**, the complete results are returned.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        @summary Asynchronously collects the full request statistics in the SQL Explorer results of a database instance by SQL ID.
        
        @description >  GetFullRequestStatResultByInstanceId is an asynchronous operation. After a request is sent, the complete results are not returned immediately. If the value of the isFinish parameter is *false** in the response, wait for 1 second and then send a request again. If the value of the isFinish parameter is **true**, the complete results are returned.
        The SQL Explorer feature allows you to check the health status of SQL statements and troubleshoot performance issues. For more information, see [SQL Explorer](https://help.aliyun.com/document_detail/204096.html).
        For more information about database instances that support this feature, see [Overview of DAS Enterprise Edition](https://help.aliyun.com/document_detail/190912.html).
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        When you call this operation, the value of the SqlId parameter changes due to the optimization of the SQL template algorithm starting from September 1, 2024. For more information, see [[Notice\\] Optimization of the SQL template algorithm](~~2845725~~).
        
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
        """
        @param request: GetHDMAliyunResourceSyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHDMAliyunResourceSyncResultResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hdmaliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        """
        @param request: GetHDMAliyunResourceSyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHDMAliyunResourceSyncResultResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetHDMAliyunResourceSyncResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hdmaliyun_resource_sync_result(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        """
        @param request: GetHDMAliyunResourceSyncResultRequest
        @return: GetHDMAliyunResourceSyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hdmaliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmaliyun_resource_sync_result_async(
        self,
        request: das20200116_models.GetHDMAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMAliyunResourceSyncResultResponse:
        """
        @param request: GetHDMAliyunResourceSyncResultRequest
        @return: GetHDMAliyunResourceSyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hdmaliyun_resource_sync_result_with_options_async(request, runtime)

    def get_hdmlast_aliyun_resource_sync_result_with_options(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        """
        @param request: GetHDMLastAliyunResourceSyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHDMLastAliyunResourceSyncResultResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_hdmlast_aliyun_resource_sync_result_with_options_async(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        """
        @param request: GetHDMLastAliyunResourceSyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHDMLastAliyunResourceSyncResultResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetHDMLastAliyunResourceSyncResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_hdmlast_aliyun_resource_sync_result(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        """
        @param request: GetHDMLastAliyunResourceSyncResultRequest
        @return: GetHDMLastAliyunResourceSyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_hdmlast_aliyun_resource_sync_result_with_options(request, runtime)

    async def get_hdmlast_aliyun_resource_sync_result_async(
        self,
        request: das20200116_models.GetHDMLastAliyunResourceSyncResultRequest,
    ) -> das20200116_models.GetHDMLastAliyunResourceSyncResultResponse:
        """
        @param request: GetHDMLastAliyunResourceSyncResultRequest
        @return: GetHDMLastAliyunResourceSyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_hdmlast_aliyun_resource_sync_result_with_options_async(request, runtime)

    def get_instance_inspections_with_options(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        """
        @summary Queries the result of an inspection that is performed on a database instance by using the inspection and scoring feature.
        
        @description Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](https://help.aliyun.com/document_detail/205659.html).
        Before you call this operation, take note of the following items:
        This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of DAS SDK must be V1.0.3 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetInstanceInspectionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetInstanceInspectionsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_instance_inspections_with_options_async(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        """
        @summary Queries the result of an inspection that is performed on a database instance by using the inspection and scoring feature.
        
        @description Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](https://help.aliyun.com/document_detail/205659.html).
        Before you call this operation, take note of the following items:
        This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of DAS SDK must be V1.0.3 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetInstanceInspectionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetInstanceInspectionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_instance_inspections(
        self,
        request: das20200116_models.GetInstanceInspectionsRequest,
    ) -> das20200116_models.GetInstanceInspectionsResponse:
        """
        @summary Queries the result of an inspection that is performed on a database instance by using the inspection and scoring feature.
        
        @description Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](https://help.aliyun.com/document_detail/205659.html).
        Before you call this operation, take note of the following items:
        This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of DAS SDK must be V1.0.3 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the result of an inspection that is performed on a database instance by using the inspection and scoring feature.
        
        @description Database Autonomy Service (DAS) provides the inspection and scoring feature. This feature allows you to inspect and score the health status of your instance on a regular basis. This helps you obtain information about the status of your databases. For more information, see [Inspection and scoring](https://help.aliyun.com/document_detail/205659.html).
        Before you call this operation, take note of the following items:
        This operation is applicable only to ApsaraDB RDS for MySQL databases, self-managed MySQL databases hosted on Elastic Compute Service (ECS) instances, self-managed MySQL databases in data centers, ApsaraDB for Redis databases, and PolarDB for MySQL databases.
        If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of DAS SDK must be V1.0.3 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the details of all missing indexes of an instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetInstanceMissingIndexListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetInstanceMissingIndexListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_instance_missing_index_list_with_options_async(
        self,
        request: das20200116_models.GetInstanceMissingIndexListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceMissingIndexListResponse:
        """
        @summary Queries the details of all missing indexes of an instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetInstanceMissingIndexListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetInstanceMissingIndexListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_instance_missing_index_list(
        self,
        request: das20200116_models.GetInstanceMissingIndexListRequest,
    ) -> das20200116_models.GetInstanceMissingIndexListResponse:
        """
        @summary Queries the details of all missing indexes of an instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the details of all missing indexes of an instance.
        
        @description    This operation is applicable only to ApsaraDB RDS for SQL Server instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries statistics on automatic SQL optimization events within a period of time, such as the total number of optimization events and the maximum improvement.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetInstanceSqlOptimizeStatisticResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetInstanceSqlOptimizeStatisticResponse(),
                self.execute(params, req, runtime)
            )

    async def get_instance_sql_optimize_statistic_with_options_async(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        """
        @summary Queries statistics on automatic SQL optimization events within a period of time, such as the total number of optimization events and the maximum improvement.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetInstanceSqlOptimizeStatisticResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetInstanceSqlOptimizeStatisticResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_instance_sql_optimize_statistic(
        self,
        request: das20200116_models.GetInstanceSqlOptimizeStatisticRequest,
    ) -> das20200116_models.GetInstanceSqlOptimizeStatisticResponse:
        """
        @summary Queries statistics on automatic SQL optimization events within a period of time, such as the total number of optimization events and the maximum improvement.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
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
        @summary Queries statistics on automatic SQL optimization events within a period of time, such as the total number of optimization events and the maximum improvement.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        The database engine is ApsaraDB RDS for MySQL or PolarDB for MySQL.
        
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
        @summary Queries the results of a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetKillInstanceSessionTaskResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetKillInstanceSessionTaskResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_kill_instance_session_task_result_with_options_async(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        """
        @summary Queries the results of a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetKillInstanceSessionTaskResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetKillInstanceSessionTaskResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_kill_instance_session_task_result(
        self,
        request: das20200116_models.GetKillInstanceSessionTaskResultRequest,
    ) -> das20200116_models.GetKillInstanceSessionTaskResultResponse:
        """
        @summary Queries the results of a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the results of a task that terminates sessions.
        
        @description    This operation is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the current sessions of an ApsaraDB for MongoDB (MongoDB) instance.
        
        @description    This operation is applicable only to MongoDB instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetMongoDBCurrentOpResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetMongoDBCurrentOpResponse(),
                self.execute(params, req, runtime)
            )

    async def get_mongo_dbcurrent_op_with_options_async(
        self,
        request: das20200116_models.GetMongoDBCurrentOpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetMongoDBCurrentOpResponse:
        """
        @summary Queries the current sessions of an ApsaraDB for MongoDB (MongoDB) instance.
        
        @description    This operation is applicable only to MongoDB instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetMongoDBCurrentOpResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetMongoDBCurrentOpResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_mongo_dbcurrent_op(
        self,
        request: das20200116_models.GetMongoDBCurrentOpRequest,
    ) -> das20200116_models.GetMongoDBCurrentOpResponse:
        """
        @summary Queries the current sessions of an ApsaraDB for MongoDB (MongoDB) instance.
        
        @description    This operation is applicable only to MongoDB instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
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
        @summary Queries the current sessions of an ApsaraDB for MongoDB (MongoDB) instance.
        
        @description    This operation is applicable only to MongoDB instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region to cn-shanghai.
        
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
        @summary Asynchronously queries the sessions of an instance and collects statistics on the sessions based on dimensions.
        
        @description >  GetMySQLAllSessionAsync is an asynchronous operation. After a request is sent, the system does not return complete results but returns a request ID. You need to use the request ID to initiate requests until the value of the *isFinish** field in the returned results is **true**, the complete results are returned. This indicates that to obtain complete data, you must call this operation at least twice.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and PolarDB-X 2.0 instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetMySQLAllSessionAsyncResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetMySQLAllSessionAsyncResponse(),
                self.execute(params, req, runtime)
            )

    async def get_my_sqlall_session_async_with_options_async(
        self,
        request: das20200116_models.GetMySQLAllSessionAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetMySQLAllSessionAsyncResponse:
        """
        @summary Asynchronously queries the sessions of an instance and collects statistics on the sessions based on dimensions.
        
        @description >  GetMySQLAllSessionAsync is an asynchronous operation. After a request is sent, the system does not return complete results but returns a request ID. You need to use the request ID to initiate requests until the value of the *isFinish** field in the returned results is **true**, the complete results are returned. This indicates that to obtain complete data, you must call this operation at least twice.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and PolarDB-X 2.0 instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetMySQLAllSessionAsyncResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetMySQLAllSessionAsyncResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_my_sqlall_session_async(
        self,
        request: das20200116_models.GetMySQLAllSessionAsyncRequest,
    ) -> das20200116_models.GetMySQLAllSessionAsyncResponse:
        """
        @summary Asynchronously queries the sessions of an instance and collects statistics on the sessions based on dimensions.
        
        @description >  GetMySQLAllSessionAsync is an asynchronous operation. After a request is sent, the system does not return complete results but returns a request ID. You need to use the request ID to initiate requests until the value of the *isFinish** field in the returned results is **true**, the complete results are returned. This indicates that to obtain complete data, you must call this operation at least twice.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and PolarDB-X 2.0 instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Asynchronously queries the sessions of an instance and collects statistics on the sessions based on dimensions.
        
        @description >  GetMySQLAllSessionAsync is an asynchronous operation. After a request is sent, the system does not return complete results but returns a request ID. You need to use the request ID to initiate requests until the value of the *isFinish** field in the returned results is **true**, the complete results are returned. This indicates that to obtain complete data, you must call this operation at least twice.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and PolarDB-X 2.0 instances.
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries access frequency statistics and hot data on partitions of a PolarDB-X 2.0 instance.
        
        @description We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](https://help.aliyun.com/document_detail/470302.html) feature of Database Autonomy Service (DAS) to query the data.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPartitionsHeatmapResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPartitionsHeatmapResponse(),
                self.execute(params, req, runtime)
            )

    async def get_partitions_heatmap_with_options_async(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        """
        @summary Queries access frequency statistics and hot data on partitions of a PolarDB-X 2.0 instance.
        
        @description We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](https://help.aliyun.com/document_detail/470302.html) feature of Database Autonomy Service (DAS) to query the data.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPartitionsHeatmapResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPartitionsHeatmapResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_partitions_heatmap(
        self,
        request: das20200116_models.GetPartitionsHeatmapRequest,
    ) -> das20200116_models.GetPartitionsHeatmapResponse:
        """
        @summary Queries access frequency statistics and hot data on partitions of a PolarDB-X 2.0 instance.
        
        @description We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](https://help.aliyun.com/document_detail/470302.html) feature of Database Autonomy Service (DAS) to query the data.
        
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
        @summary Queries access frequency statistics and hot data on partitions of a PolarDB-X 2.0 instance.
        
        @description We recommend that you do not call this operation. The data is returned in a special format and is complex to parse. You can use the [heatmap](https://help.aliyun.com/document_detail/470302.html) feature of Database Autonomy Service (DAS) to query the data.
        
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
        @summary Queries the trend of a metric for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPfsMetricTrendsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPfsMetricTrendsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_pfs_metric_trends_with_options_async(
        self,
        request: das20200116_models.GetPfsMetricTrendsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsMetricTrendsResponse:
        """
        @summary Queries the trend of a metric for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPfsMetricTrendsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPfsMetricTrendsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_pfs_metric_trends(
        self,
        request: das20200116_models.GetPfsMetricTrendsRequest,
    ) -> das20200116_models.GetPfsMetricTrendsResponse:
        """
        @summary Queries the trend of a metric for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        @summary Queries the trend of a metric for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        @summary Queries the SQL sample data for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSampleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSampleResponse(),
                self.execute(params, req, runtime)
            )

    async def get_pfs_sql_sample_with_options_async(
        self,
        request: das20200116_models.GetPfsSqlSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsSqlSampleResponse:
        """
        @summary Queries the SQL sample data for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSampleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSampleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_pfs_sql_sample(
        self,
        request: das20200116_models.GetPfsSqlSampleRequest,
    ) -> das20200116_models.GetPfsSqlSampleResponse:
        """
        @summary Queries the SQL sample data for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        @summary Queries the SQL sample data for the new version of the performance insight feature of a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        @summary Queries the full request data generated by the new version of the performance insight feature of a database instance based on the SQL ID.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSummariesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSummariesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_pfs_sql_summaries_with_options_async(
        self,
        request: das20200116_models.GetPfsSqlSummariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetPfsSqlSummariesResponse:
        """
        @summary Queries the full request data generated by the new version of the performance insight feature of a database instance based on the SQL ID.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSummariesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetPfsSqlSummariesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_pfs_sql_summaries(
        self,
        request: das20200116_models.GetPfsSqlSummariesRequest,
    ) -> das20200116_models.GetPfsSqlSummariesResponse:
        """
        @summary Queries the full request data generated by the new version of the performance insight feature of a database instance based on the SQL ID.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        @summary Queries the full request data generated by the new version of the performance insight feature of a database instance based on the SQL ID.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this API operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        An ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster is connected to DAS.
        The new version of the performance insight feature is enabled for the database instance. For more information, see [Performance insight (new version)](https://help.aliyun.com/document_detail/469117.html).
        
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
        @summary Queries information about SQL templates based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataStatsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataStatsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_data_stats_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        """
        @summary Queries information about SQL templates based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataStatsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataStatsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_data_stats(
        self,
        request: das20200116_models.GetQueryOptimizeDataStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeDataStatsResponse:
        """
        @summary Queries information about SQL templates based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries information about SQL templates based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries information about the best-performing and worst-performing instances based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTopResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTopResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_data_top_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        """
        @summary Queries information about the best-performing and worst-performing instances based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTopResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTopResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_data_top(
        self,
        request: das20200116_models.GetQueryOptimizeDataTopRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTopResponse:
        """
        @summary Queries information about the best-performing and worst-performing instances based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries information about the best-performing and worst-performing instances based on query governance data.
        
        @description    If you use an Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries query governance trend data.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTrendResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTrendResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_data_trend_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        """
        @summary Queries query governance trend data.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTrendResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeDataTrendResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_data_trend(
        self,
        request: das20200116_models.GetQueryOptimizeDataTrendRequest,
    ) -> das20200116_models.GetQueryOptimizeDataTrendResponse:
        """
        @summary Queries query governance trend data.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries query governance trend data.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries the failed SQL statements under a SQL template.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorSampleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorSampleResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_exec_error_sample_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        """
        @summary Queries the failed SQL statements under a SQL template.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorSampleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorSampleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_exec_error_sample(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorSampleRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorSampleResponse:
        """
        @summary Queries the failed SQL statements under a SQL template.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries the failed SQL statements under a SQL template.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries SQL templates that failed to be executed.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorStatsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorStatsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_exec_error_stats_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        """
        @summary Queries SQL templates that failed to be executed.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorStatsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeExecErrorStatsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_exec_error_stats(
        self,
        request: das20200116_models.GetQueryOptimizeExecErrorStatsRequest,
    ) -> das20200116_models.GetQueryOptimizeExecErrorStatsResponse:
        """
        @summary Queries SQL templates that failed to be executed.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries SQL templates that failed to be executed.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries the tags added by the query governance feature to specified database instances.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeRuleListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeRuleListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_rule_list_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        """
        @summary Queries the tags added by the query governance feature to specified database instances.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeRuleListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeRuleListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_rule_list(
        self,
        request: das20200116_models.GetQueryOptimizeRuleListRequest,
    ) -> das20200116_models.GetQueryOptimizeRuleListResponse:
        """
        @summary Queries the tags added by the query governance feature to specified database instances.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries the tags added by the query governance feature to specified database instances.
        
        @description    If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V2.1.8. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V2.1.8 or later.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries a share URL provided by the query governance feature.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeShareUrlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeShareUrlResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_share_url_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeShareUrlResponse:
        """
        @summary Queries a share URL provided by the query governance feature.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeShareUrlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeShareUrlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_share_url(
        self,
        request: das20200116_models.GetQueryOptimizeShareUrlRequest,
    ) -> das20200116_models.GetQueryOptimizeShareUrlResponse:
        """
        @summary Queries a share URL provided by the query governance feature.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries a share URL provided by the query governance feature.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call API operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries suggestions provided by query governance for optimizing an SQL template.
        
        @description    If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeSolutionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeSolutionResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_solution_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        """
        @summary Queries suggestions provided by query governance for optimizing an SQL template.
        
        @description    If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeSolutionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeSolutionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_solution(
        self,
        request: das20200116_models.GetQueryOptimizeSolutionRequest,
    ) -> das20200116_models.GetQueryOptimizeSolutionResponse:
        """
        @summary Queries suggestions provided by query governance for optimizing an SQL template.
        
        @description    If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries suggestions provided by query governance for optimizing an SQL template.
        
        @description    If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries the tags of a SQL statement.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeTagResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeTagResponse(),
                self.execute(params, req, runtime)
            )

    async def get_query_optimize_tag_with_options_async(
        self,
        request: das20200116_models.GetQueryOptimizeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetQueryOptimizeTagResponse:
        """
        @summary Queries the tags of a SQL statement.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeTagResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetQueryOptimizeTagResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_query_optimize_tag(
        self,
        request: das20200116_models.GetQueryOptimizeTagRequest,
    ) -> das20200116_models.GetQueryOptimizeTagResponse:
        """
        @summary Queries the tags of a SQL statement.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries the tags of a SQL statement.
        
        @description    If you use Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        ApsaraDB RDS for PostgreSQL
        
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
        @summary Queries the current session on an ApsaraDB for Redis instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis instances.
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRedisAllSessionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRedisAllSessionResponse(),
                self.execute(params, req, runtime)
            )

    async def get_redis_all_session_with_options_async(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        """
        @summary Queries the current session on an ApsaraDB for Redis instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis instances.
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRedisAllSessionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRedisAllSessionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_redis_all_session(
        self,
        request: das20200116_models.GetRedisAllSessionRequest,
    ) -> das20200116_models.GetRedisAllSessionResponse:
        """
        @summary Queries the current session on an ApsaraDB for Redis instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis instances.
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        @summary Queries the current session on an ApsaraDB for Redis instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis instances.
        If you use an SDK to call operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
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
        @summary Queries SQL diagnostics records by pages.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisPageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisPageResponse(),
                self.execute(params, req, runtime)
            )

    async def get_request_diagnosis_page_with_options_async(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        """
        @summary Queries SQL diagnostics records by pages.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisPageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisPageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_request_diagnosis_page(
        self,
        request: das20200116_models.GetRequestDiagnosisPageRequest,
    ) -> das20200116_models.GetRequestDiagnosisPageResponse:
        """
        @summary Queries SQL diagnostics records by pages.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        @summary Queries SQL diagnostics records by pages.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        ApsaraDB RDS for PostgreSQL
        ApsaraDB RDS for SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  The minor engine version of the Apsara RDS for PostgreSQL instance must be 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        @summary Queries the results of an SQL diagnostics task.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        You cannot call this operation to query the diagnostic result of the automatic SQL optimization feature.
        This operation is applicable to the following database engines:
        RDS MySQL
        RDS PostgreSQL
        RDS SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  If your instance is an ApsaraDB RDS for PostgreSQL instance, make sure that the minor engine version of your instance is 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_request_diagnosis_result_with_options_async(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        """
        @summary Queries the results of an SQL diagnostics task.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        You cannot call this operation to query the diagnostic result of the automatic SQL optimization feature.
        This operation is applicable to the following database engines:
        RDS MySQL
        RDS PostgreSQL
        RDS SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  If your instance is an ApsaraDB RDS for PostgreSQL instance, make sure that the minor engine version of your instance is 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRequestDiagnosisResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_request_diagnosis_result(
        self,
        request: das20200116_models.GetRequestDiagnosisResultRequest,
    ) -> das20200116_models.GetRequestDiagnosisResultResponse:
        """
        @summary Queries the results of an SQL diagnostics task.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        You cannot call this operation to query the diagnostic result of the automatic SQL optimization feature.
        This operation is applicable to the following database engines:
        RDS MySQL
        RDS PostgreSQL
        RDS SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  If your instance is an ApsaraDB RDS for PostgreSQL instance, make sure that the minor engine version of your instance is 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        @summary Queries the results of an SQL diagnostics task.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        You cannot call this operation to query the diagnostic result of the automatic SQL optimization feature.
        This operation is applicable to the following database engines:
        RDS MySQL
        RDS PostgreSQL
        RDS SQL Server
        PolarDB for MySQL
        PolarDB for PostgreSQL (Compatible with Oracle)
        ApsaraDB for MongoDB
        >  If your instance is an ApsaraDB RDS for PostgreSQL instance, make sure that the minor engine version of your instance is 20220130 or later. For more information about how to check and update the minor engine version of an ApsaraDB RDS for PostgreSQL instance, see [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/146895.html).
        
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
        @summary Queries the throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_running_sql_concurrency_control_rules_with_options_async(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        """
        @summary Queries the throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetRunningSqlConcurrencyControlRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_running_sql_concurrency_control_rules(
        self,
        request: das20200116_models.GetRunningSqlConcurrencyControlRulesRequest,
    ) -> das20200116_models.GetRunningSqlConcurrencyControlRulesResponse:
        """
        @summary Queries the throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Queries the throttling rules that are in effect.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Generates a throttling keyword string based on an SQL statement.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
                self.execute(params, req, runtime)
            )

    async def get_sql_concurrency_control_keywords_from_sql_text_with_options_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        """
        @summary Generates a throttling keyword string based on an SQL statement.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_sql_concurrency_control_keywords_from_sql_text(
        self,
        request: das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlKeywordsFromSqlTextResponse:
        """
        @summary Generates a throttling keyword string based on an SQL statement.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Generates a throttling keyword string based on an SQL statement.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Queries the throttling rules that are being executed or have been triggered.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
                self.execute(params, req, runtime)
            )

    async def get_sql_concurrency_control_rules_history_with_options_async(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        """
        @summary Queries the throttling rules that are being executed or have been triggered.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_sql_concurrency_control_rules_history(
        self,
        request: das20200116_models.GetSqlConcurrencyControlRulesHistoryRequest,
    ) -> das20200116_models.GetSqlConcurrencyControlRulesHistoryResponse:
        """
        @summary Queries the throttling rules that are being executed or have been triggered.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Queries the throttling rules that are being executed or have been triggered.
        
        @description This operation supports the following database engines:
        ApsaraDB RDS for MySQL
        PolarDB for MySQL
        
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
        @summary Queries optimization suggestions that are generated by the SQL diagnostics feature of Database Autonomy Service (DAS).
        
        @description The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](https://help.aliyun.com/document_detail/167895.html).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetSqlOptimizeAdviceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetSqlOptimizeAdviceResponse(),
                self.execute(params, req, runtime)
            )

    async def get_sql_optimize_advice_with_options_async(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        """
        @summary Queries optimization suggestions that are generated by the SQL diagnostics feature of Database Autonomy Service (DAS).
        
        @description The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](https://help.aliyun.com/document_detail/167895.html).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetSqlOptimizeAdviceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetSqlOptimizeAdviceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_sql_optimize_advice(
        self,
        request: das20200116_models.GetSqlOptimizeAdviceRequest,
    ) -> das20200116_models.GetSqlOptimizeAdviceResponse:
        """
        @summary Queries optimization suggestions that are generated by the SQL diagnostics feature of Database Autonomy Service (DAS).
        
        @description The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](https://help.aliyun.com/document_detail/167895.html).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries optimization suggestions that are generated by the SQL diagnostics feature of Database Autonomy Service (DAS).
        
        @description The SQL diagnostics feature provides optimization suggestions for instances based on diagnostics results. You can use the optimization suggestions to optimize instance indexes. For more information, see [Automatic SQL optimization](https://help.aliyun.com/document_detail/167895.html).
        >  You can call this operation to query only the optimization suggestions that are automatically generated by the SQL diagnostics feature.
        Before you call this operation, take note of the following items:
        This operation is applicable to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the status and results of a storage analysis task.
        
        @description >  The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from `information_schema.tables`. Statistics in MySQL are not updated in real time. Therefore, the statistics may be different from the physical file sizes. If you want to obtain the latest data, you can execute the `ANALYZE TABLE` statement on the relevant tables during off-peak hours.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetStorageAnalysisResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetStorageAnalysisResultResponse(),
                self.execute(params, req, runtime)
            )

    async def get_storage_analysis_result_with_options_async(
        self,
        request: das20200116_models.GetStorageAnalysisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.GetStorageAnalysisResultResponse:
        """
        @summary Queries the status and results of a storage analysis task.
        
        @description >  The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from `information_schema.tables`. Statistics in MySQL are not updated in real time. Therefore, the statistics may be different from the physical file sizes. If you want to obtain the latest data, you can execute the `ANALYZE TABLE` statement on the relevant tables during off-peak hours.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.GetStorageAnalysisResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.GetStorageAnalysisResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_storage_analysis_result(
        self,
        request: das20200116_models.GetStorageAnalysisResultRequest,
    ) -> das20200116_models.GetStorageAnalysisResultResponse:
        """
        @summary Queries the status and results of a storage analysis task.
        
        @description >  The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from `information_schema.tables`. Statistics in MySQL are not updated in real time. Therefore, the statistics may be different from the physical file sizes. If you want to obtain the latest data, you can execute the `ANALYZE TABLE` statement on the relevant tables during off-peak hours.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Queries the status and results of a storage analysis task.
        
        @description >  The physical file size indicates the actual size of an obtained file. Only specific deployment modes of database instances support the display of physical file sizes. The statistics on tables are obtained from `information_schema.tables`. Statistics in MySQL are not updated in real time. Therefore, the statistics may be different from the physical file sizes. If you want to obtain the latest data, you can execute the `ANALYZE TABLE` statement on the relevant tables during off-peak hours.
        This operation is applicable only to ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and ApsaraDB for MongoDB instances.
        For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this operation works the same as the storage analysis feature of the previous version. Tasks generated by this operation cannot be viewed on the Storage Analysis page of the new version in the Database Autonomy Service (DAS) console. If you want to view the tasks and results, call the related API operation to obtain data and save data to your computer.
        If you use an Alibaba Cloud SDK or DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Terminates all sessions on an instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis.
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.KillInstanceAllSessionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.KillInstanceAllSessionResponse(),
                self.execute(params, req, runtime)
            )

    async def kill_instance_all_session_with_options_async(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        """
        @summary Terminates all sessions on an instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis.
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.KillInstanceAllSessionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.KillInstanceAllSessionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def kill_instance_all_session(
        self,
        request: das20200116_models.KillInstanceAllSessionRequest,
    ) -> das20200116_models.KillInstanceAllSessionResponse:
        """
        @summary Terminates all sessions on an instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis.
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Terminates all sessions on an instance.
        
        @description    This operation is applicable only to ApsaraDB for Redis.
        If you use Alibaba Cloud SDK, make sure that the aliyun-sdk-core version is later than V4.3.3. We recommend that you use the latest version.
        The version of your Database Autonomy Service (DAS) SDK must be V1.0.2 or later.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Modifies the auto scaling configurations of an instance.
        
        @description You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](https://help.aliyun.com/document_detail/173345.html).
        You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](https://help.aliyun.com/document_detail/216312.html).
        You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.ModifyAutoScalingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.ModifyAutoScalingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_auto_scaling_config_with_options_async(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        """
        @summary Modifies the auto scaling configurations of an instance.
        
        @description You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](https://help.aliyun.com/document_detail/173345.html).
        You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](https://help.aliyun.com/document_detail/216312.html).
        You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.ModifyAutoScalingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.ModifyAutoScalingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_auto_scaling_config(
        self,
        request: das20200116_models.ModifyAutoScalingConfigRequest,
    ) -> das20200116_models.ModifyAutoScalingConfigResponse:
        """
        @summary Modifies the auto scaling configurations of an instance.
        
        @description You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](https://help.aliyun.com/document_detail/173345.html).
        You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](https://help.aliyun.com/document_detail/216312.html).
        You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
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
        @summary Modifies the auto scaling configurations of an instance.
        
        @description You can call this operation to modify the following auto scaling configurations of an instance: *auto scaling for specifications**, **automatic storage expansion**, **automatic bandwidth adjustment**, and **auto scaling for resources**.
        You can modify the configurations of the **auto scaling feature for specifications** for the following types of database instances:
        PolarDB for MySQL Cluster Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or enhanced SSDs (ESSDs). For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        You can modify the configurations of the **automatic storage expansion** feature for the following types of database instances:
        ApsaraDB RDS for MySQL High-availability Edition instances that use standard SSDs or ESSDs. For more information about the feature and the billing rules, see [Automatic space expansion](https://help.aliyun.com/document_detail/173345.html).
        You can modify the configurations of the **automatic bandwidth adjustment** feature for the following types of database instances:
        ApsaraDB for Redis Classic (Local Disk-based) Edition instances. For more information about the feature and the billing rules, see [Automatic bandwidth adjustment](https://help.aliyun.com/document_detail/216312.html).
        You can modify the configurations of the **auto scaling feature for resources** for the following types of database instances:
        General-purpose ApsaraDB RDS for MySQL Enterprise Edition instances. For more information about the feature and the billing rules, see [Automatic performance scaling](https://help.aliyun.com/document_detail/169686.html).
        If you use an Alibaba Cloud SDK or Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        
        @param request: ModifyAutoScalingConfigRequest
        @return: ModifyAutoScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_scaling_config_with_options_async(request, runtime)

    def modify_sql_log_config_with_options(
        self,
        request: das20200116_models.ModifySqlLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.ModifySqlLogConfigResponse:
        """
        @summary Enables or configures Database Autonomy Service (DAS) Enterprise Edition for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        By default, the latest version of DAS Enterprise Edition that supports the database instance is enabled. For information about the databases and regions that are supported by different versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: ModifySqlLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySqlLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_audit):
            query['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.hot_retention):
            body['HotRetention'] = request.hot_retention
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_enable):
            body['RequestEnable'] = request.request_enable
        if not UtilClient.is_unset(request.retention):
            body['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySqlLogConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.ModifySqlLogConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.ModifySqlLogConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_sql_log_config_with_options_async(
        self,
        request: das20200116_models.ModifySqlLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.ModifySqlLogConfigResponse:
        """
        @summary Enables or configures Database Autonomy Service (DAS) Enterprise Edition for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        By default, the latest version of DAS Enterprise Edition that supports the database instance is enabled. For information about the databases and regions that are supported by different versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: ModifySqlLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySqlLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_audit):
            query['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.hot_retention):
            body['HotRetention'] = request.hot_retention
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_enable):
            body['RequestEnable'] = request.request_enable
        if not UtilClient.is_unset(request.retention):
            body['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySqlLogConfig',
            version='2020-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.ModifySqlLogConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.ModifySqlLogConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_sql_log_config(
        self,
        request: das20200116_models.ModifySqlLogConfigRequest,
    ) -> das20200116_models.ModifySqlLogConfigResponse:
        """
        @summary Enables or configures Database Autonomy Service (DAS) Enterprise Edition for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        By default, the latest version of DAS Enterprise Edition that supports the database instance is enabled. For information about the databases and regions that are supported by different versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: ModifySqlLogConfigRequest
        @return: ModifySqlLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sql_log_config_with_options(request, runtime)

    async def modify_sql_log_config_async(
        self,
        request: das20200116_models.ModifySqlLogConfigRequest,
    ) -> das20200116_models.ModifySqlLogConfigResponse:
        """
        @summary Enables or configures Database Autonomy Service (DAS) Enterprise Edition for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a DAS SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call operations of DAS, you must set the region ID to cn-shanghai.
        By default, the latest version of DAS Enterprise Edition that supports the database instance is enabled. For information about the databases and regions that are supported by different versions of DAS Enterprise Edition, see [Editions and supported features](https://help.aliyun.com/document_detail/156204.html).
        
        @param request: ModifySqlLogConfigRequest
        @return: ModifySqlLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_sql_log_config_with_options_async(request, runtime)

    def run_cloud_bench_task_with_options(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        """
        @summary Runs a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.RunCloudBenchTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.RunCloudBenchTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def run_cloud_bench_task_with_options_async(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        """
        @summary Runs a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.RunCloudBenchTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.RunCloudBenchTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_cloud_bench_task(
        self,
        request: das20200116_models.RunCloudBenchTaskRequest,
    ) -> das20200116_models.RunCloudBenchTaskResponse:
        """
        @summary Runs a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Runs a stress testing task.
        
        @description Database Autonomy Service (DAS) provides the intelligent stress testing feature. This feature helps you check whether your instance needs to be scaled up to effectively handle traffic spikes. For more information, see [Intelligent stress testing](https://help.aliyun.com/document_detail/155068.html).
        
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
        @summary Configures the event subscription settings for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        Make sure that the database instance that you want to manage is connected to DAS.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.SetEventSubscriptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.SetEventSubscriptionResponse(),
                self.execute(params, req, runtime)
            )

    async def set_event_subscription_with_options_async(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        """
        @summary Configures the event subscription settings for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        Make sure that the database instance that you want to manage is connected to DAS.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.SetEventSubscriptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.SetEventSubscriptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_event_subscription(
        self,
        request: das20200116_models.SetEventSubscriptionRequest,
    ) -> das20200116_models.SetEventSubscriptionResponse:
        """
        @summary Configures the event subscription settings for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        Make sure that the database instance that you want to manage is connected to DAS.
        
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
        @summary Configures the event subscription settings for a database instance.
        
        @description Before you call this operation, take note of the following items:
        If you use an Alibaba Cloud SDK or a Database Autonomy Service (DAS) SDK to call this operation, we recommend that you use the latest version of the SDK.
        If you use an SDK to call the API operations of DAS, you must set the region ID to cn-shanghai.
        Make sure that the database instance that you want to manage is connected to DAS.
        
        @param request: SetEventSubscriptionRequest
        @return: SetEventSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_event_subscription_with_options_async(request, runtime)

    def update_auto_resource_optimize_rules_async_with_options(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        """
        @summary Asynchronously configures parameters related to the automatic fragment recycling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instances must be an ApsaraDB RDS for MySQL High-availability Edition instance.
        DAS Enterprise Edition must be enabled for the database instance. You can call the call [DescribeInstanceDasPro](https://help.aliyun.com/document_detail/413866.html) operation to query whether DAS Enterprise Edition is enabled.
        The database instance has four or more CPU cores, and **innodb_file_per_table** is set to **ON**.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
                self.execute(params, req, runtime)
            )

    async def update_auto_resource_optimize_rules_async_with_options_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        """
        @summary Asynchronously configures parameters related to the automatic fragment recycling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instances must be an ApsaraDB RDS for MySQL High-availability Edition instance.
        DAS Enterprise Edition must be enabled for the database instance. You can call the call [DescribeInstanceDasPro](https://help.aliyun.com/document_detail/413866.html) operation to query whether DAS Enterprise Edition is enabled.
        The database instance has four or more CPU cores, and **innodb_file_per_table** is set to **ON**.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_auto_resource_optimize_rules_async(
        self,
        request: das20200116_models.UpdateAutoResourceOptimizeRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoResourceOptimizeRulesAsyncResponse:
        """
        @summary Asynchronously configures parameters related to the automatic fragment recycling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instances must be an ApsaraDB RDS for MySQL High-availability Edition instance.
        DAS Enterprise Edition must be enabled for the database instance. You can call the call [DescribeInstanceDasPro](https://help.aliyun.com/document_detail/413866.html) operation to query whether DAS Enterprise Edition is enabled.
        The database instance has four or more CPU cores, and **innodb_file_per_table** is set to **ON**.
        
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
        @summary Asynchronously configures parameters related to the automatic fragment recycling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call the API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The database instances must be an ApsaraDB RDS for MySQL High-availability Edition instance.
        DAS Enterprise Edition must be enabled for the database instance. You can call the call [DescribeInstanceDasPro](https://help.aliyun.com/document_detail/413866.html) operation to query whether DAS Enterprise Edition is enabled.
        The database instance has four or more CPU cores, and **innodb_file_per_table** is set to **ON**.
        
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
        @summary Enables, modifies, or disables the automatic SQL optimization feature for multiple database instances at a time.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        DAS Enterprise Edition must be enabled for the database instance that you want to manage. To enable DAS Enterprise Edition for a database instance, you can call the [EnableDasPro](https://help.aliyun.com/document_detail/411645.html) operation.
        The autonomy service must be enabled for the database instance. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition
        PolarDB for MySQL Cluster Edition
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.UpdateAutoSqlOptimizeStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.UpdateAutoSqlOptimizeStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def update_auto_sql_optimize_status_with_options_async(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        """
        @summary Enables, modifies, or disables the automatic SQL optimization feature for multiple database instances at a time.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        DAS Enterprise Edition must be enabled for the database instance that you want to manage. To enable DAS Enterprise Edition for a database instance, you can call the [EnableDasPro](https://help.aliyun.com/document_detail/411645.html) operation.
        The autonomy service must be enabled for the database instance. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition
        PolarDB for MySQL Cluster Edition
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.UpdateAutoSqlOptimizeStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.UpdateAutoSqlOptimizeStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_auto_sql_optimize_status(
        self,
        request: das20200116_models.UpdateAutoSqlOptimizeStatusRequest,
    ) -> das20200116_models.UpdateAutoSqlOptimizeStatusResponse:
        """
        @summary Enables, modifies, or disables the automatic SQL optimization feature for multiple database instances at a time.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        DAS Enterprise Edition must be enabled for the database instance that you want to manage. To enable DAS Enterprise Edition for a database instance, you can call the [EnableDasPro](https://help.aliyun.com/document_detail/411645.html) operation.
        The autonomy service must be enabled for the database instance. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition
        PolarDB for MySQL Cluster Edition
        
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
        @summary Enables, modifies, or disables the automatic SQL optimization feature for multiple database instances at a time.
        
        @description Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        DAS Enterprise Edition must be enabled for the database instance that you want to manage. To enable DAS Enterprise Edition for a database instance, you can call the [EnableDasPro](https://help.aliyun.com/document_detail/411645.html) operation.
        The autonomy service must be enabled for the database instance. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        This operation supports the following database engines:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition
        PolarDB for MySQL Cluster Edition
        
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
        @summary Asynchronously configures parameters related to the automatic SQL throttling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.UpdateAutoThrottleRulesAsyncResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.UpdateAutoThrottleRulesAsyncResponse(),
                self.execute(params, req, runtime)
            )

    async def update_auto_throttle_rules_async_with_options_async(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        """
        @summary Asynchronously configures parameters related to the automatic SQL throttling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                das20200116_models.UpdateAutoThrottleRulesAsyncResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                das20200116_models.UpdateAutoThrottleRulesAsyncResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_auto_throttle_rules_async(
        self,
        request: das20200116_models.UpdateAutoThrottleRulesAsyncRequest,
    ) -> das20200116_models.UpdateAutoThrottleRulesAsyncResponse:
        """
        @summary Asynchronously configures parameters related to the automatic SQL throttling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
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
        @summary Asynchronously configures parameters related to the automatic SQL throttling feature for multiple database instances at a time.
        
        @description >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of *ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        Before you call this operation, take note of the following items:
        If you use an SDK to call API operations of Database Autonomy Service (DAS), you must set the region ID to cn-shanghai.
        The autonomy service must be enabled for the database instance that you want to manage. For more information, see [Autonomy center](https://help.aliyun.com/document_detail/152139.html).
        The database instance that you want to manage must be of one of the following types:
        ApsaraDB RDS for MySQL High-availability Edition or Enterprise Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        PolarDB for MySQL Cluster Edition that runs MySQL 5.6, MySQL 5.7, or MySQL 8.0
        
        @param request: UpdateAutoThrottleRulesAsyncRequest
        @return: UpdateAutoThrottleRulesAsyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_throttle_rules_async_with_options_async(request, runtime)
