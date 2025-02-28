# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adb_inc20211201 import models as adb_inc_20211201_models
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
        self._endpoint = self.get_endpoint('adb-inc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_cluster_vpc_connection_with_options(
        self,
        request: adb_inc_20211201_models.AllocateClusterVpcConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.AllocateClusterVpcConnectionResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: AllocateClusterVpcConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateClusterVpcConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterVpcConnection',
            version='2021-12-01',
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
                adb_inc_20211201_models.AllocateClusterVpcConnectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.AllocateClusterVpcConnectionResponse(),
                self.execute(params, req, runtime)
            )

    async def allocate_cluster_vpc_connection_with_options_async(
        self,
        request: adb_inc_20211201_models.AllocateClusterVpcConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.AllocateClusterVpcConnectionResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: AllocateClusterVpcConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateClusterVpcConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterVpcConnection',
            version='2021-12-01',
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
                adb_inc_20211201_models.AllocateClusterVpcConnectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.AllocateClusterVpcConnectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def allocate_cluster_vpc_connection(
        self,
        request: adb_inc_20211201_models.AllocateClusterVpcConnectionRequest,
    ) -> adb_inc_20211201_models.AllocateClusterVpcConnectionResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: AllocateClusterVpcConnectionRequest
        @return: AllocateClusterVpcConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_vpc_connection_with_options(request, runtime)

    async def allocate_cluster_vpc_connection_async(
        self,
        request: adb_inc_20211201_models.AllocateClusterVpcConnectionRequest,
    ) -> adb_inc_20211201_models.AllocateClusterVpcConnectionResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: AllocateClusterVpcConnectionRequest
        @return: AllocateClusterVpcConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cluster_vpc_connection_with_options_async(request, runtime)

    def authorize_instance_egress_with_options(
        self,
        request: adb_inc_20211201_models.AuthorizeInstanceEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.AuthorizeInstanceEgressResponse:
        """
        @param request: AuthorizeInstanceEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeInstanceEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeInstanceEgress',
            version='2021-12-01',
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
                adb_inc_20211201_models.AuthorizeInstanceEgressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.AuthorizeInstanceEgressResponse(),
                self.execute(params, req, runtime)
            )

    async def authorize_instance_egress_with_options_async(
        self,
        request: adb_inc_20211201_models.AuthorizeInstanceEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.AuthorizeInstanceEgressResponse:
        """
        @param request: AuthorizeInstanceEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeInstanceEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeInstanceEgress',
            version='2021-12-01',
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
                adb_inc_20211201_models.AuthorizeInstanceEgressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.AuthorizeInstanceEgressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def authorize_instance_egress(
        self,
        request: adb_inc_20211201_models.AuthorizeInstanceEgressRequest,
    ) -> adb_inc_20211201_models.AuthorizeInstanceEgressResponse:
        """
        @param request: AuthorizeInstanceEgressRequest
        @return: AuthorizeInstanceEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_instance_egress_with_options(request, runtime)

    async def authorize_instance_egress_async(
        self,
        request: adb_inc_20211201_models.AuthorizeInstanceEgressRequest,
    ) -> adb_inc_20211201_models.AuthorizeInstanceEgressResponse:
        """
        @param request: AuthorizeInstanceEgressRequest
        @return: AuthorizeInstanceEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_instance_egress_with_options_async(request, runtime)

    def check_oss_object_content_consistency_with_options(
        self,
        request: adb_inc_20211201_models.CheckOssObjectContentConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse:
        """
        @summary 检查OSS的两个文件或文件前缀下的文件内容是否一致
        
        @param request: CheckOssObjectContentConsistencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckOssObjectContentConsistencyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_bucket_name):
            query['SourceBucketName'] = request.source_bucket_name
        if not UtilClient.is_unset(request.source_db_cluster_id):
            query['SourceDbClusterId'] = request.source_db_cluster_id
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        if not UtilClient.is_unset(request.target_bucket_name):
            query['TargetBucketName'] = request.target_bucket_name
        if not UtilClient.is_unset(request.target_endpoint):
            query['TargetEndpoint'] = request.target_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckOssObjectContentConsistency',
            version='2021-12-01',
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
                adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse(),
                self.execute(params, req, runtime)
            )

    async def check_oss_object_content_consistency_with_options_async(
        self,
        request: adb_inc_20211201_models.CheckOssObjectContentConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse:
        """
        @summary 检查OSS的两个文件或文件前缀下的文件内容是否一致
        
        @param request: CheckOssObjectContentConsistencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckOssObjectContentConsistencyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_bucket_name):
            query['SourceBucketName'] = request.source_bucket_name
        if not UtilClient.is_unset(request.source_db_cluster_id):
            query['SourceDbClusterId'] = request.source_db_cluster_id
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        if not UtilClient.is_unset(request.target_bucket_name):
            query['TargetBucketName'] = request.target_bucket_name
        if not UtilClient.is_unset(request.target_endpoint):
            query['TargetEndpoint'] = request.target_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckOssObjectContentConsistency',
            version='2021-12-01',
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
                adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def check_oss_object_content_consistency(
        self,
        request: adb_inc_20211201_models.CheckOssObjectContentConsistencyRequest,
    ) -> adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse:
        """
        @summary 检查OSS的两个文件或文件前缀下的文件内容是否一致
        
        @param request: CheckOssObjectContentConsistencyRequest
        @return: CheckOssObjectContentConsistencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_oss_object_content_consistency_with_options(request, runtime)

    async def check_oss_object_content_consistency_async(
        self,
        request: adb_inc_20211201_models.CheckOssObjectContentConsistencyRequest,
    ) -> adb_inc_20211201_models.CheckOssObjectContentConsistencyResponse:
        """
        @summary 检查OSS的两个文件或文件前缀下的文件内容是否一致
        
        @param request: CheckOssObjectContentConsistencyRequest
        @return: CheckOssObjectContentConsistencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_oss_object_content_consistency_with_options_async(request, runtime)

    def create_major_customer_with_options(
        self,
        request: adb_inc_20211201_models.CreateMajorCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.CreateMajorCustomerResponse:
        """
        @summary 新增重点客户
        
        @param request: CreateMajorCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMajorCustomerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.pd):
            query['Pd'] = request.pd
        if not UtilClient.is_unset(request.pdsa):
            query['Pdsa'] = request.pdsa
        if not UtilClient.is_unset(request.ranking):
            query['Ranking'] = request.ranking
        if not UtilClient.is_unset(request.rd):
            query['Rd'] = request.rd
        if not UtilClient.is_unset(request.sa):
            query['Sa'] = request.sa
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMajorCustomer',
            version='2021-12-01',
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
                adb_inc_20211201_models.CreateMajorCustomerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.CreateMajorCustomerResponse(),
                self.execute(params, req, runtime)
            )

    async def create_major_customer_with_options_async(
        self,
        request: adb_inc_20211201_models.CreateMajorCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.CreateMajorCustomerResponse:
        """
        @summary 新增重点客户
        
        @param request: CreateMajorCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMajorCustomerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.pd):
            query['Pd'] = request.pd
        if not UtilClient.is_unset(request.pdsa):
            query['Pdsa'] = request.pdsa
        if not UtilClient.is_unset(request.ranking):
            query['Ranking'] = request.ranking
        if not UtilClient.is_unset(request.rd):
            query['Rd'] = request.rd
        if not UtilClient.is_unset(request.sa):
            query['Sa'] = request.sa
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMajorCustomer',
            version='2021-12-01',
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
                adb_inc_20211201_models.CreateMajorCustomerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.CreateMajorCustomerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_major_customer(
        self,
        request: adb_inc_20211201_models.CreateMajorCustomerRequest,
    ) -> adb_inc_20211201_models.CreateMajorCustomerResponse:
        """
        @summary 新增重点客户
        
        @param request: CreateMajorCustomerRequest
        @return: CreateMajorCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_major_customer_with_options(request, runtime)

    async def create_major_customer_async(
        self,
        request: adb_inc_20211201_models.CreateMajorCustomerRequest,
    ) -> adb_inc_20211201_models.CreateMajorCustomerResponse:
        """
        @summary 新增重点客户
        
        @param request: CreateMajorCustomerRequest
        @return: CreateMajorCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_major_customer_with_options_async(request, runtime)

    def delete_bucket_replication_with_options(
        self,
        request: adb_inc_20211201_models.DeleteBucketReplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DeleteBucketReplicationResponse:
        """
        @summary 删除OSS跨区域复制任务
        
        @param request: DeleteBucketReplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBucketReplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_bucket_name):
            query['SourceBucketName'] = request.source_bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucketReplication',
            version='2021-12-01',
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
                adb_inc_20211201_models.DeleteBucketReplicationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DeleteBucketReplicationResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_bucket_replication_with_options_async(
        self,
        request: adb_inc_20211201_models.DeleteBucketReplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DeleteBucketReplicationResponse:
        """
        @summary 删除OSS跨区域复制任务
        
        @param request: DeleteBucketReplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBucketReplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_bucket_name):
            query['SourceBucketName'] = request.source_bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucketReplication',
            version='2021-12-01',
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
                adb_inc_20211201_models.DeleteBucketReplicationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DeleteBucketReplicationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_bucket_replication(
        self,
        request: adb_inc_20211201_models.DeleteBucketReplicationRequest,
    ) -> adb_inc_20211201_models.DeleteBucketReplicationResponse:
        """
        @summary 删除OSS跨区域复制任务
        
        @param request: DeleteBucketReplicationRequest
        @return: DeleteBucketReplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_bucket_replication_with_options(request, runtime)

    async def delete_bucket_replication_async(
        self,
        request: adb_inc_20211201_models.DeleteBucketReplicationRequest,
    ) -> adb_inc_20211201_models.DeleteBucketReplicationResponse:
        """
        @summary 删除OSS跨区域复制任务
        
        @param request: DeleteBucketReplicationRequest
        @return: DeleteBucketReplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_bucket_replication_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: adb_inc_20211201_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DeleteDBClusterResponse:
        """
        @summary 删除集群
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.DeleteDBClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DeleteDBClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_dbcluster_with_options_async(
        self,
        request: adb_inc_20211201_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DeleteDBClusterResponse:
        """
        @summary 删除集群
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.DeleteDBClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DeleteDBClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_dbcluster(
        self,
        request: adb_inc_20211201_models.DeleteDBClusterRequest,
    ) -> adb_inc_20211201_models.DeleteDBClusterResponse:
        """
        @summary 删除集群
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: adb_inc_20211201_models.DeleteDBClusterRequest,
    ) -> adb_inc_20211201_models.DeleteDBClusterResponse:
        """
        @summary 删除集群
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_major_customer_with_options(
        self,
        request: adb_inc_20211201_models.DeleteMajorCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DeleteMajorCustomerResponse:
        """
        @summary 删除重点客户
        
        @param request: DeleteMajorCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMajorCustomerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMajorCustomer',
            version='2021-12-01',
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
                adb_inc_20211201_models.DeleteMajorCustomerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DeleteMajorCustomerResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_major_customer_with_options_async(
        self,
        request: adb_inc_20211201_models.DeleteMajorCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DeleteMajorCustomerResponse:
        """
        @summary 删除重点客户
        
        @param request: DeleteMajorCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMajorCustomerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMajorCustomer',
            version='2021-12-01',
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
                adb_inc_20211201_models.DeleteMajorCustomerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DeleteMajorCustomerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_major_customer(
        self,
        request: adb_inc_20211201_models.DeleteMajorCustomerRequest,
    ) -> adb_inc_20211201_models.DeleteMajorCustomerResponse:
        """
        @summary 删除重点客户
        
        @param request: DeleteMajorCustomerRequest
        @return: DeleteMajorCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_major_customer_with_options(request, runtime)

    async def delete_major_customer_async(
        self,
        request: adb_inc_20211201_models.DeleteMajorCustomerRequest,
    ) -> adb_inc_20211201_models.DeleteMajorCustomerResponse:
        """
        @summary 删除重点客户
        
        @param request: DeleteMajorCustomerRequest
        @return: DeleteMajorCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_major_customer_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: adb_inc_20211201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeAccountsResponse:
        """
        @summary 查询帐号列表
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeAccountsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeAccountsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_accounts_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeAccountsResponse:
        """
        @summary 查询帐号列表
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeAccountsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeAccountsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_accounts(
        self,
        request: adb_inc_20211201_models.DescribeAccountsRequest,
    ) -> adb_inc_20211201_models.DescribeAccountsResponse:
        """
        @summary 查询帐号列表
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: adb_inc_20211201_models.DescribeAccountsRequest,
    ) -> adb_inc_20211201_models.DescribeAccountsResponse:
        """
        @summary 查询帐号列表
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_adb_duty_rule_with_options(
        self,
        request: adb_inc_20211201_models.DescribeAdbDutyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeAdbDutyRuleResponse:
        """
        @summary 获取ADB值班人员信息
        
        @param request: DescribeAdbDutyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbDutyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbDutyRule',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeAdbDutyRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeAdbDutyRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_adb_duty_rule_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeAdbDutyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeAdbDutyRuleResponse:
        """
        @summary 获取ADB值班人员信息
        
        @param request: DescribeAdbDutyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdbDutyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbDutyRule',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeAdbDutyRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeAdbDutyRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_adb_duty_rule(
        self,
        request: adb_inc_20211201_models.DescribeAdbDutyRuleRequest,
    ) -> adb_inc_20211201_models.DescribeAdbDutyRuleResponse:
        """
        @summary 获取ADB值班人员信息
        
        @param request: DescribeAdbDutyRuleRequest
        @return: DescribeAdbDutyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_adb_duty_rule_with_options(request, runtime)

    async def describe_adb_duty_rule_async(
        self,
        request: adb_inc_20211201_models.DescribeAdbDutyRuleRequest,
    ) -> adb_inc_20211201_models.DescribeAdbDutyRuleResponse:
        """
        @summary 获取ADB值班人员信息
        
        @param request: DescribeAdbDutyRuleRequest
        @return: DescribeAdbDutyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_adb_duty_rule_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: adb_inc_20211201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeBackupPolicyResponse:
        """
        @summary 获取实例的备份策略
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeBackupPolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeBackupPolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_backup_policy_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeBackupPolicyResponse:
        """
        @summary 获取实例的备份策略
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeBackupPolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeBackupPolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_backup_policy(
        self,
        request: adb_inc_20211201_models.DescribeBackupPolicyRequest,
    ) -> adb_inc_20211201_models.DescribeBackupPolicyResponse:
        """
        @summary 获取实例的备份策略
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: adb_inc_20211201_models.DescribeBackupPolicyRequest,
    ) -> adb_inc_20211201_models.DescribeBackupPolicyResponse:
        """
        @summary 获取实例的备份策略
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: adb_inc_20211201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeBackupsResponse:
        """
        @summary 获取实例的备份详细信息
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.backup_id):
            query['BackupID'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeBackupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeBackupsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_backups_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeBackupsResponse:
        """
        @summary 获取实例的备份详细信息
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.backup_id):
            query['BackupID'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeBackupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeBackupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_backups(
        self,
        request: adb_inc_20211201_models.DescribeBackupsRequest,
    ) -> adb_inc_20211201_models.DescribeBackupsResponse:
        """
        @summary 获取实例的备份详细信息
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: adb_inc_20211201_models.DescribeBackupsRequest,
    ) -> adb_inc_20211201_models.DescribeBackupsResponse:
        """
        @summary 获取实例的备份详细信息
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cluster_instance_with_options(
        self,
        request: adb_inc_20211201_models.DescribeClusterInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeClusterInstanceResponse:
        """
        @summary 获取集群的实例信息
        
        @param request: DescribeClusterInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterInstance',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeClusterInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeClusterInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_instance_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeClusterInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeClusterInstanceResponse:
        """
        @summary 获取集群的实例信息
        
        @param request: DescribeClusterInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterInstance',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeClusterInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeClusterInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_instance(
        self,
        request: adb_inc_20211201_models.DescribeClusterInstanceRequest,
    ) -> adb_inc_20211201_models.DescribeClusterInstanceResponse:
        """
        @summary 获取集群的实例信息
        
        @param request: DescribeClusterInstanceRequest
        @return: DescribeClusterInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_instance_with_options(request, runtime)

    async def describe_cluster_instance_async(
        self,
        request: adb_inc_20211201_models.DescribeClusterInstanceRequest,
    ) -> adb_inc_20211201_models.DescribeClusterInstanceResponse:
        """
        @summary 获取集群的实例信息
        
        @param request: DescribeClusterInstanceRequest
        @return: DescribeClusterInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_instance_with_options_async(request, runtime)

    def describe_cluster_net_info_with_options(
        self,
        request: adb_inc_20211201_models.DescribeClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary 描述集群网络信息
        
        @param request: DescribeClusterNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNetInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeClusterNetInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeClusterNetInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cluster_net_info_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary 描述集群网络信息
        
        @param request: DescribeClusterNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNetInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeClusterNetInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeClusterNetInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cluster_net_info(
        self,
        request: adb_inc_20211201_models.DescribeClusterNetInfoRequest,
    ) -> adb_inc_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary 描述集群网络信息
        
        @param request: DescribeClusterNetInfoRequest
        @return: DescribeClusterNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_net_info_with_options(request, runtime)

    async def describe_cluster_net_info_async(
        self,
        request: adb_inc_20211201_models.DescribeClusterNetInfoRequest,
    ) -> adb_inc_20211201_models.DescribeClusterNetInfoResponse:
        """
        @summary 描述集群网络信息
        
        @param request: DescribeClusterNetInfoRequest
        @return: DescribeClusterNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_net_info_with_options_async(request, runtime)

    def describe_customers_with_options(
        self,
        request: adb_inc_20211201_models.DescribeCustomersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeCustomersResponse:
        """
        @summary 查看客户信息
        
        @param request: DescribeCustomersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomers',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeCustomersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeCustomersResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_customers_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeCustomersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeCustomersResponse:
        """
        @summary 查看客户信息
        
        @param request: DescribeCustomersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomers',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeCustomersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeCustomersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_customers(
        self,
        request: adb_inc_20211201_models.DescribeCustomersRequest,
    ) -> adb_inc_20211201_models.DescribeCustomersResponse:
        """
        @summary 查看客户信息
        
        @param request: DescribeCustomersRequest
        @return: DescribeCustomersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_customers_with_options(request, runtime)

    async def describe_customers_async(
        self,
        request: adb_inc_20211201_models.DescribeCustomersRequest,
    ) -> adb_inc_20211201_models.DescribeCustomersResponse:
        """
        @summary 查看客户信息
        
        @param request: DescribeCustomersRequest
        @return: DescribeCustomersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_customers_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: adb_inc_20211201_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary 性能指标查询接口
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDBClusterPerformanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDBClusterPerformanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary 性能指标查询接口
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDBClusterPerformanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDBClusterPerformanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dbcluster_performance(
        self,
        request: adb_inc_20211201_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_inc_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary 性能指标查询接口
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: adb_inc_20211201_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_inc_20211201_models.DescribeDBClusterPerformanceResponse:
        """
        @summary 性能指标查询接口
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbresource_group_with_options(
        self,
        request: adb_inc_20211201_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary 查询资源组
        
        @param request: DescribeDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.exclude_ainode):
            query['ExcludeAINode'] = request.exclude_ainode
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDBResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDBResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_dbresource_group_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary 查询资源组
        
        @param request: DescribeDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.exclude_ainode):
            query['ExcludeAINode'] = request.exclude_ainode
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDBResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDBResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_dbresource_group(
        self,
        request: adb_inc_20211201_models.DescribeDBResourceGroupRequest,
    ) -> adb_inc_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary 查询资源组
        
        @param request: DescribeDBResourceGroupRequest
        @return: DescribeDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_group_with_options(request, runtime)

    async def describe_dbresource_group_async(
        self,
        request: adb_inc_20211201_models.DescribeDBResourceGroupRequest,
    ) -> adb_inc_20211201_models.DescribeDBResourceGroupResponse:
        """
        @summary 查询资源组
        
        @param request: DescribeDBResourceGroupRequest
        @return: DescribeDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbresource_group_with_options_async(request, runtime)

    def describe_db_cluster_with_options(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDbClusterResponse:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDbClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDbClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_db_cluster_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDbClusterResponse:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDbClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDbClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_db_cluster(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterRequest,
    ) -> adb_inc_20211201_models.DescribeDbClusterResponse:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterRequest
        @return: DescribeDbClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_db_cluster_with_options(request, runtime)

    async def describe_db_cluster_async(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterRequest,
    ) -> adb_inc_20211201_models.DescribeDbClusterResponse:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterRequest
        @return: DescribeDbClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_cluster_with_options_async(request, runtime)

    def describe_db_cluster_param_with_options(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDbClusterParamResponse:
        """
        @summary 获取实例的参数信息
        
        @param request: DescribeDbClusterParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbClusterParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.param_name):
            query['ParamName'] = request.param_name
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbClusterParam',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDbClusterParamResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDbClusterParamResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_db_cluster_param_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDbClusterParamResponse:
        """
        @summary 获取实例的参数信息
        
        @param request: DescribeDbClusterParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbClusterParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.param_name):
            query['ParamName'] = request.param_name
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbClusterParam',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDbClusterParamResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDbClusterParamResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_db_cluster_param(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterParamRequest,
    ) -> adb_inc_20211201_models.DescribeDbClusterParamResponse:
        """
        @summary 获取实例的参数信息
        
        @param request: DescribeDbClusterParamRequest
        @return: DescribeDbClusterParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_db_cluster_param_with_options(request, runtime)

    async def describe_db_cluster_param_async(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterParamRequest,
    ) -> adb_inc_20211201_models.DescribeDbClusterParamResponse:
        """
        @summary 获取实例的参数信息
        
        @param request: DescribeDbClusterParamRequest
        @return: DescribeDbClusterParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_cluster_param_with_options_async(request, runtime)

    def describe_db_cluster_v5with_options(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterV5Request,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDbClusterV5Response:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterV5Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbClusterV5Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbClusterV5',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDbClusterV5Response(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDbClusterV5Response(),
                self.execute(params, req, runtime)
            )

    async def describe_db_cluster_v5with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterV5Request,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeDbClusterV5Response:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterV5Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDbClusterV5Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbClusterV5',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeDbClusterV5Response(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeDbClusterV5Response(),
                await self.execute_async(params, req, runtime)
            )

    def describe_db_cluster_v5(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterV5Request,
    ) -> adb_inc_20211201_models.DescribeDbClusterV5Response:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterV5Request
        @return: DescribeDbClusterV5Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_db_cluster_v5with_options(request, runtime)

    async def describe_db_cluster_v5_async(
        self,
        request: adb_inc_20211201_models.DescribeDbClusterV5Request,
    ) -> adb_inc_20211201_models.DescribeDbClusterV5Response:
        """
        @summary 查询实例信息
        
        @param request: DescribeDbClusterV5Request
        @return: DescribeDbClusterV5Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_cluster_v5with_options_async(request, runtime)

    def describe_instance_release_with_options(
        self,
        request: adb_inc_20211201_models.DescribeInstanceReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeInstanceReleaseResponse:
        """
        @summary 获取实例的版本信息
        
        @param request: DescribeInstanceReleaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceReleaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRelease',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeInstanceReleaseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeInstanceReleaseResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_release_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeInstanceReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeInstanceReleaseResponse:
        """
        @summary 获取实例的版本信息
        
        @param request: DescribeInstanceReleaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceReleaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRelease',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeInstanceReleaseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeInstanceReleaseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_release(
        self,
        request: adb_inc_20211201_models.DescribeInstanceReleaseRequest,
    ) -> adb_inc_20211201_models.DescribeInstanceReleaseResponse:
        """
        @summary 获取实例的版本信息
        
        @param request: DescribeInstanceReleaseRequest
        @return: DescribeInstanceReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_release_with_options(request, runtime)

    async def describe_instance_release_async(
        self,
        request: adb_inc_20211201_models.DescribeInstanceReleaseRequest,
    ) -> adb_inc_20211201_models.DescribeInstanceReleaseResponse:
        """
        @summary 获取实例的版本信息
        
        @param request: DescribeInstanceReleaseRequest
        @return: DescribeInstanceReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_release_with_options_async(request, runtime)

    def describe_major_customer_instances_with_options(
        self,
        request: adb_inc_20211201_models.DescribeMajorCustomerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse:
        """
        @summary 查看重点客户实例列表
        
        @param request: DescribeMajorCustomerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMajorCustomerInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_ids):
            query['CustomerIds'] = request.customer_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMajorCustomerInstances',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_major_customer_instances_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeMajorCustomerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse:
        """
        @summary 查看重点客户实例列表
        
        @param request: DescribeMajorCustomerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMajorCustomerInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_ids):
            query['CustomerIds'] = request.customer_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMajorCustomerInstances',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_major_customer_instances(
        self,
        request: adb_inc_20211201_models.DescribeMajorCustomerInstancesRequest,
    ) -> adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse:
        """
        @summary 查看重点客户实例列表
        
        @param request: DescribeMajorCustomerInstancesRequest
        @return: DescribeMajorCustomerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_major_customer_instances_with_options(request, runtime)

    async def describe_major_customer_instances_async(
        self,
        request: adb_inc_20211201_models.DescribeMajorCustomerInstancesRequest,
    ) -> adb_inc_20211201_models.DescribeMajorCustomerInstancesResponse:
        """
        @summary 查看重点客户实例列表
        
        @param request: DescribeMajorCustomerInstancesRequest
        @return: DescribeMajorCustomerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_major_customer_instances_with_options_async(request, runtime)

    def describe_major_customers_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeMajorCustomersResponse:
        """
        @summary 查看重点客户信息
        
        @param request: DescribeMajorCustomersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMajorCustomersResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMajorCustomers',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeMajorCustomersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeMajorCustomersResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_major_customers_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeMajorCustomersResponse:
        """
        @summary 查看重点客户信息
        
        @param request: DescribeMajorCustomersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMajorCustomersResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMajorCustomers',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeMajorCustomersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeMajorCustomersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_major_customers(self) -> adb_inc_20211201_models.DescribeMajorCustomersResponse:
        """
        @summary 查看重点客户信息
        
        @return: DescribeMajorCustomersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_major_customers_with_options(runtime)

    async def describe_major_customers_async(self) -> adb_inc_20211201_models.DescribeMajorCustomersResponse:
        """
        @summary 查看重点客户信息
        
        @return: DescribeMajorCustomersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_major_customers_with_options_async(runtime)

    def describe_oss_bucket_replication_progress_with_options(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssBucketReplicationProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBucketReplicationProgress',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oss_bucket_replication_progress_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssBucketReplicationProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBucketReplicationProgress',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oss_bucket_replication_progress(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationProgressRequest,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationProgressRequest
        @return: DescribeOssBucketReplicationProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_bucket_replication_progress_with_options(request, runtime)

    async def describe_oss_bucket_replication_progress_async(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationProgressRequest,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationProgressResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationProgressRequest
        @return: DescribeOssBucketReplicationProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_bucket_replication_progress_with_options_async(request, runtime)

    def describe_oss_bucket_replication_rules_with_options(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssBucketReplicationRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBucketReplicationRules',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oss_bucket_replication_rules_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssBucketReplicationRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssBucketReplicationRules',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oss_bucket_replication_rules(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationRulesRequest,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationRulesRequest
        @return: DescribeOssBucketReplicationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_bucket_replication_rules_with_options(request, runtime)

    async def describe_oss_bucket_replication_rules_async(
        self,
        request: adb_inc_20211201_models.DescribeOssBucketReplicationRulesRequest,
    ) -> adb_inc_20211201_models.DescribeOssBucketReplicationRulesResponse:
        """
        @summary 获取OSS跨区域复制任务进度
        
        @param request: DescribeOssBucketReplicationRulesRequest
        @return: DescribeOssBucketReplicationRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_bucket_replication_rules_with_options_async(request, runtime)

    def describe_oss_info_with_options(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssInfoResponse:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oss_info_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssInfoResponse:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oss_info(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoRequest,
    ) -> adb_inc_20211201_models.DescribeOssInfoResponse:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoRequest
        @return: DescribeOssInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_info_with_options(request, runtime)

    async def describe_oss_info_async(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoRequest,
    ) -> adb_inc_20211201_models.DescribeOssInfoResponse:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoRequest
        @return: DescribeOssInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_info_with_options_async(request, runtime)

    def describe_oss_info_v2with_options(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssInfoV2Response:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssInfoV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssInfoV2',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssInfoV2Response(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssInfoV2Response(),
                self.execute(params, req, runtime)
            )

    async def describe_oss_info_v2with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeOssInfoV2Response:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssInfoV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ali_uid):
            query['aliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssInfoV2',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeOssInfoV2Response(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeOssInfoV2Response(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oss_info_v2(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoV2Request,
    ) -> adb_inc_20211201_models.DescribeOssInfoV2Response:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoV2Request
        @return: DescribeOssInfoV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_info_v2with_options(request, runtime)

    async def describe_oss_info_v2_async(
        self,
        request: adb_inc_20211201_models.DescribeOssInfoV2Request,
    ) -> adb_inc_20211201_models.DescribeOssInfoV2Response:
        """
        @summary 获取实例的OSS信息
        
        @param request: DescribeOssInfoV2Request
        @return: DescribeOssInfoV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_info_v2with_options_async(request, runtime)

    def describe_task_status_with_options(
        self,
        request: adb_inc_20211201_models.DescribeTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeTaskStatusResponse:
        """
        @summary 查询异步任务状态
        
        @param request: DescribeTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskStatus',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeTaskStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeTaskStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_task_status_with_options_async(
        self,
        request: adb_inc_20211201_models.DescribeTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.DescribeTaskStatusResponse:
        """
        @summary 查询异步任务状态
        
        @param request: DescribeTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskStatus',
            version='2021-12-01',
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
                adb_inc_20211201_models.DescribeTaskStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.DescribeTaskStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_task_status(
        self,
        request: adb_inc_20211201_models.DescribeTaskStatusRequest,
    ) -> adb_inc_20211201_models.DescribeTaskStatusResponse:
        """
        @summary 查询异步任务状态
        
        @param request: DescribeTaskStatusRequest
        @return: DescribeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_task_status_with_options(request, runtime)

    async def describe_task_status_async(
        self,
        request: adb_inc_20211201_models.DescribeTaskStatusRequest,
    ) -> adb_inc_20211201_models.DescribeTaskStatusResponse:
        """
        @summary 查询异步任务状态
        
        @param request: DescribeTaskStatusRequest
        @return: DescribeTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_status_with_options_async(request, runtime)

    def generate_zero_etl_token_with_options(
        self,
        request: adb_inc_20211201_models.GenerateZeroEtlTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GenerateZeroEtlTokenResponse:
        """
        @summary 弹性导入生成鉴权token接口。
        
        @param request: GenerateZeroEtlTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateZeroEtlTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.polar_dbinstance_id):
            body['PolarDBInstanceId'] = request.polar_dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            body['UID'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateZeroEtlToken',
            version='2021-12-01',
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
                adb_inc_20211201_models.GenerateZeroEtlTokenResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GenerateZeroEtlTokenResponse(),
                self.execute(params, req, runtime)
            )

    async def generate_zero_etl_token_with_options_async(
        self,
        request: adb_inc_20211201_models.GenerateZeroEtlTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GenerateZeroEtlTokenResponse:
        """
        @summary 弹性导入生成鉴权token接口。
        
        @param request: GenerateZeroEtlTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateZeroEtlTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.polar_dbinstance_id):
            body['PolarDBInstanceId'] = request.polar_dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            body['UID'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateZeroEtlToken',
            version='2021-12-01',
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
                adb_inc_20211201_models.GenerateZeroEtlTokenResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GenerateZeroEtlTokenResponse(),
                await self.execute_async(params, req, runtime)
            )

    def generate_zero_etl_token(
        self,
        request: adb_inc_20211201_models.GenerateZeroEtlTokenRequest,
    ) -> adb_inc_20211201_models.GenerateZeroEtlTokenResponse:
        """
        @summary 弹性导入生成鉴权token接口。
        
        @param request: GenerateZeroEtlTokenRequest
        @return: GenerateZeroEtlTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_zero_etl_token_with_options(request, runtime)

    async def generate_zero_etl_token_async(
        self,
        request: adb_inc_20211201_models.GenerateZeroEtlTokenRequest,
    ) -> adb_inc_20211201_models.GenerateZeroEtlTokenResponse:
        """
        @summary 弹性导入生成鉴权token接口。
        
        @param request: GenerateZeroEtlTokenRequest
        @return: GenerateZeroEtlTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_zero_etl_token_with_options_async(request, runtime)

    def get_aatoss_info_for_adbwith_options(
        self,
        request: adb_inc_20211201_models.GetAATOssInfoForADBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetAATOssInfoForADBResponse:
        """
        @summary 获取aat表oss信息。
        
        @param request: GetAATOssInfoForADBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAATOssInfoForADBResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.polar_dbinstance_id):
            body['PolarDBInstanceId'] = request.polar_dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAATOssInfoForADB',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetAATOssInfoForADBResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetAATOssInfoForADBResponse(),
                self.execute(params, req, runtime)
            )

    async def get_aatoss_info_for_adbwith_options_async(
        self,
        request: adb_inc_20211201_models.GetAATOssInfoForADBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetAATOssInfoForADBResponse:
        """
        @summary 获取aat表oss信息。
        
        @param request: GetAATOssInfoForADBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAATOssInfoForADBResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.polar_dbinstance_id):
            body['PolarDBInstanceId'] = request.polar_dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAATOssInfoForADB',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetAATOssInfoForADBResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetAATOssInfoForADBResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_aatoss_info_for_adb(
        self,
        request: adb_inc_20211201_models.GetAATOssInfoForADBRequest,
    ) -> adb_inc_20211201_models.GetAATOssInfoForADBResponse:
        """
        @summary 获取aat表oss信息。
        
        @param request: GetAATOssInfoForADBRequest
        @return: GetAATOssInfoForADBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aatoss_info_for_adbwith_options(request, runtime)

    async def get_aatoss_info_for_adb_async(
        self,
        request: adb_inc_20211201_models.GetAATOssInfoForADBRequest,
    ) -> adb_inc_20211201_models.GetAATOssInfoForADBResponse:
        """
        @summary 获取aat表oss信息。
        
        @param request: GetAATOssInfoForADBRequest
        @return: GetAATOssInfoForADBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_aatoss_info_for_adbwith_options_async(request, runtime)

    def get_bucket_transfer_acceleration_with_options(
        self,
        request: adb_inc_20211201_models.GetBucketTransferAccelerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetBucketTransferAccelerationResponse:
        """
        @summary 查询OSS Bucket传输加速功能
        
        @param request: GetBucketTransferAccelerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBucketTransferAccelerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketTransferAcceleration',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetBucketTransferAccelerationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetBucketTransferAccelerationResponse(),
                self.execute(params, req, runtime)
            )

    async def get_bucket_transfer_acceleration_with_options_async(
        self,
        request: adb_inc_20211201_models.GetBucketTransferAccelerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetBucketTransferAccelerationResponse:
        """
        @summary 查询OSS Bucket传输加速功能
        
        @param request: GetBucketTransferAccelerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBucketTransferAccelerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketTransferAcceleration',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetBucketTransferAccelerationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetBucketTransferAccelerationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_bucket_transfer_acceleration(
        self,
        request: adb_inc_20211201_models.GetBucketTransferAccelerationRequest,
    ) -> adb_inc_20211201_models.GetBucketTransferAccelerationResponse:
        """
        @summary 查询OSS Bucket传输加速功能
        
        @param request: GetBucketTransferAccelerationRequest
        @return: GetBucketTransferAccelerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_bucket_transfer_acceleration_with_options(request, runtime)

    async def get_bucket_transfer_acceleration_async(
        self,
        request: adb_inc_20211201_models.GetBucketTransferAccelerationRequest,
    ) -> adb_inc_20211201_models.GetBucketTransferAccelerationResponse:
        """
        @summary 查询OSS Bucket传输加速功能
        
        @param request: GetBucketTransferAccelerationRequest
        @return: GetBucketTransferAccelerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_bucket_transfer_acceleration_with_options_async(request, runtime)

    def get_dbresource_group_with_options(
        self,
        request: adb_inc_20211201_models.GetDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetDBResourceGroupResponse:
        """
        @summary 获取实例资源组
        
        @param request: GetDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBResourceGroup',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetDBResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetDBResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def get_dbresource_group_with_options_async(
        self,
        request: adb_inc_20211201_models.GetDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetDBResourceGroupResponse:
        """
        @summary 获取实例资源组
        
        @param request: GetDBResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDBResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBResourceGroup',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetDBResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetDBResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_dbresource_group(
        self,
        request: adb_inc_20211201_models.GetDBResourceGroupRequest,
    ) -> adb_inc_20211201_models.GetDBResourceGroupResponse:
        """
        @summary 获取实例资源组
        
        @param request: GetDBResourceGroupRequest
        @return: GetDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dbresource_group_with_options(request, runtime)

    async def get_dbresource_group_async(
        self,
        request: adb_inc_20211201_models.GetDBResourceGroupRequest,
    ) -> adb_inc_20211201_models.GetDBResourceGroupResponse:
        """
        @summary 获取实例资源组
        
        @param request: GetDBResourceGroupRequest
        @return: GetDBResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dbresource_group_with_options_async(request, runtime)

    def get_init_dms_aiservice_k8s_env_info_with_options(
        self,
        request: adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse:
        """
        @summary 获取打通DMS AI Service的pvl并初始化K8s环境任务的结果
        
        @param request: GetInitDmsAIServiceK8sEnvInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInitDmsAIServiceK8sEnvInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInitDmsAIServiceK8sEnvInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def get_init_dms_aiservice_k8s_env_info_with_options_async(
        self,
        request: adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse:
        """
        @summary 获取打通DMS AI Service的pvl并初始化K8s环境任务的结果
        
        @param request: GetInitDmsAIServiceK8sEnvInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInitDmsAIServiceK8sEnvInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInitDmsAIServiceK8sEnvInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_init_dms_aiservice_k8s_env_info(
        self,
        request: adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoRequest,
    ) -> adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse:
        """
        @summary 获取打通DMS AI Service的pvl并初始化K8s环境任务的结果
        
        @param request: GetInitDmsAIServiceK8sEnvInfoRequest
        @return: GetInitDmsAIServiceK8sEnvInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_init_dms_aiservice_k8s_env_info_with_options(request, runtime)

    async def get_init_dms_aiservice_k8s_env_info_async(
        self,
        request: adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoRequest,
    ) -> adb_inc_20211201_models.GetInitDmsAIServiceK8sEnvInfoResponse:
        """
        @summary 获取打通DMS AI Service的pvl并初始化K8s环境任务的结果
        
        @param request: GetInitDmsAIServiceK8sEnvInfoRequest
        @return: GetInitDmsAIServiceK8sEnvInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_init_dms_aiservice_k8s_env_info_with_options_async(request, runtime)

    def get_spark_app_metrics_with_options(
        self,
        request: adb_inc_20211201_models.GetSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary 获取Spark应用指标信息
        
        @param request: GetSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppMetrics',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetSparkAppMetricsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetSparkAppMetricsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_spark_app_metrics_with_options_async(
        self,
        request: adb_inc_20211201_models.GetSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary 获取Spark应用指标信息
        
        @param request: GetSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppMetrics',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetSparkAppMetricsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetSparkAppMetricsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_spark_app_metrics(
        self,
        request: adb_inc_20211201_models.GetSparkAppMetricsRequest,
    ) -> adb_inc_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary 获取Spark应用指标信息
        
        @param request: GetSparkAppMetricsRequest
        @return: GetSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_metrics_with_options(request, runtime)

    async def get_spark_app_metrics_async(
        self,
        request: adb_inc_20211201_models.GetSparkAppMetricsRequest,
    ) -> adb_inc_20211201_models.GetSparkAppMetricsResponse:
        """
        @summary 获取Spark应用指标信息
        
        @param request: GetSparkAppMetricsRequest
        @return: GetSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_metrics_with_options_async(request, runtime)

    def get_spark_submit_info_with_options(
        self,
        request: adb_inc_20211201_models.GetSparkSubmitInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetSparkSubmitInfoResponse:
        """
        @summary 获取提交Spark需要的必要信息
        
        @param request: GetSparkSubmitInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkSubmitInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conf):
            body['Conf'] = request.conf
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSubmitInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetSparkSubmitInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetSparkSubmitInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def get_spark_submit_info_with_options_async(
        self,
        request: adb_inc_20211201_models.GetSparkSubmitInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.GetSparkSubmitInfoResponse:
        """
        @summary 获取提交Spark需要的必要信息
        
        @param request: GetSparkSubmitInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkSubmitInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conf):
            body['Conf'] = request.conf
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSubmitInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.GetSparkSubmitInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.GetSparkSubmitInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_spark_submit_info(
        self,
        request: adb_inc_20211201_models.GetSparkSubmitInfoRequest,
    ) -> adb_inc_20211201_models.GetSparkSubmitInfoResponse:
        """
        @summary 获取提交Spark需要的必要信息
        
        @param request: GetSparkSubmitInfoRequest
        @return: GetSparkSubmitInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_submit_info_with_options(request, runtime)

    async def get_spark_submit_info_async(
        self,
        request: adb_inc_20211201_models.GetSparkSubmitInfoRequest,
    ) -> adb_inc_20211201_models.GetSparkSubmitInfoResponse:
        """
        @summary 获取提交Spark需要的必要信息
        
        @param request: GetSparkSubmitInfoRequest
        @return: GetSparkSubmitInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_submit_info_with_options_async(request, runtime)

    def init_dms_aiservice_k8s_env_with_options(
        self,
        request: adb_inc_20211201_models.InitDmsAIServiceK8sEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse:
        """
        @summary 打通DMS AI Service的pvl并初始化K8s环境
        
        @param request: InitDmsAIServiceK8sEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitDmsAIServiceK8sEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitDmsAIServiceK8sEnv',
            version='2021-12-01',
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
                adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse(),
                self.execute(params, req, runtime)
            )

    async def init_dms_aiservice_k8s_env_with_options_async(
        self,
        request: adb_inc_20211201_models.InitDmsAIServiceK8sEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse:
        """
        @summary 打通DMS AI Service的pvl并初始化K8s环境
        
        @param request: InitDmsAIServiceK8sEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitDmsAIServiceK8sEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitDmsAIServiceK8sEnv',
            version='2021-12-01',
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
                adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse(),
                await self.execute_async(params, req, runtime)
            )

    def init_dms_aiservice_k8s_env(
        self,
        request: adb_inc_20211201_models.InitDmsAIServiceK8sEnvRequest,
    ) -> adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse:
        """
        @summary 打通DMS AI Service的pvl并初始化K8s环境
        
        @param request: InitDmsAIServiceK8sEnvRequest
        @return: InitDmsAIServiceK8sEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_dms_aiservice_k8s_env_with_options(request, runtime)

    async def init_dms_aiservice_k8s_env_async(
        self,
        request: adb_inc_20211201_models.InitDmsAIServiceK8sEnvRequest,
    ) -> adb_inc_20211201_models.InitDmsAIServiceK8sEnvResponse:
        """
        @summary 打通DMS AI Service的pvl并初始化K8s环境
        
        @param request: InitDmsAIServiceK8sEnvRequest
        @return: InitDmsAIServiceK8sEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_dms_aiservice_k8s_env_with_options_async(request, runtime)

    def inner_get_spark_app_info_with_options(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppInfoResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def inner_get_spark_app_info_with_options_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppInfoResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppInfo',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inner_get_spark_app_info(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppInfoRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppInfoResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppInfoRequest
        @return: InnerGetSparkAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_get_spark_app_info_with_options(request, runtime)

    async def inner_get_spark_app_info_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppInfoRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppInfoResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppInfoRequest
        @return: InnerGetSparkAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_get_spark_app_info_with_options_async(request, runtime)

    def inner_get_spark_app_log_with_options(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppLogResponse:
        """
        @summary 获取Spark App的部分日志
        
        @param request: InnerGetSparkAppLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppLog',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppLogResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppLogResponse(),
                self.execute(params, req, runtime)
            )

    async def inner_get_spark_app_log_with_options_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppLogResponse:
        """
        @summary 获取Spark App的部分日志
        
        @param request: InnerGetSparkAppLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppLog',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppLogResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppLogResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inner_get_spark_app_log(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppLogRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppLogResponse:
        """
        @summary 获取Spark App的部分日志
        
        @param request: InnerGetSparkAppLogRequest
        @return: InnerGetSparkAppLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_get_spark_app_log_with_options(request, runtime)

    async def inner_get_spark_app_log_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppLogRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppLogResponse:
        """
        @summary 获取Spark App的部分日志
        
        @param request: InnerGetSparkAppLogRequest
        @return: InnerGetSparkAppLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_get_spark_app_log_with_options_async(request, runtime)

    def inner_get_spark_app_state_with_options(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppStateResponse:
        """
        @summary 获取Spark应用的状态
        
        @param request: InnerGetSparkAppStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppState',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppStateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppStateResponse(),
                self.execute(params, req, runtime)
            )

    async def inner_get_spark_app_state_with_options_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppStateResponse:
        """
        @summary 获取Spark应用的状态
        
        @param request: InnerGetSparkAppStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppState',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppStateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppStateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inner_get_spark_app_state(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppStateRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppStateResponse:
        """
        @summary 获取Spark应用的状态
        
        @param request: InnerGetSparkAppStateRequest
        @return: InnerGetSparkAppStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_get_spark_app_state_with_options(request, runtime)

    async def inner_get_spark_app_state_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppStateRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppStateResponse:
        """
        @summary 获取Spark应用的状态
        
        @param request: InnerGetSparkAppStateRequest
        @return: InnerGetSparkAppStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_get_spark_app_state_with_options_async(request, runtime)

    def inner_get_spark_app_web_ui_address_with_options(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppWebUiAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppWebUiAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppWebUiAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppWebUiAddress',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse(),
                self.execute(params, req, runtime)
            )

    async def inner_get_spark_app_web_ui_address_with_options_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppWebUiAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppWebUiAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerGetSparkAppWebUiAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerGetSparkAppWebUiAddress',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inner_get_spark_app_web_ui_address(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppWebUiAddressRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppWebUiAddressRequest
        @return: InnerGetSparkAppWebUiAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_get_spark_app_web_ui_address_with_options(request, runtime)

    async def inner_get_spark_app_web_ui_address_async(
        self,
        request: adb_inc_20211201_models.InnerGetSparkAppWebUiAddressRequest,
    ) -> adb_inc_20211201_models.InnerGetSparkAppWebUiAddressResponse:
        """
        @summary 获取Spark应用的详细信息
        
        @param request: InnerGetSparkAppWebUiAddressRequest
        @return: InnerGetSparkAppWebUiAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_get_spark_app_web_ui_address_with_options_async(request, runtime)

    def inner_kill_spark_app_with_options(
        self,
        request: adb_inc_20211201_models.InnerKillSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerKillSparkAppResponse:
        """
        @summary 终止一个Spark Application的运行
        
        @param request: InnerKillSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerKillSparkAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerKillSparkApp',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerKillSparkAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerKillSparkAppResponse(),
                self.execute(params, req, runtime)
            )

    async def inner_kill_spark_app_with_options_async(
        self,
        request: adb_inc_20211201_models.InnerKillSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerKillSparkAppResponse:
        """
        @summary 终止一个Spark Application的运行
        
        @param request: InnerKillSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerKillSparkAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerKillSparkApp',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerKillSparkAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerKillSparkAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inner_kill_spark_app(
        self,
        request: adb_inc_20211201_models.InnerKillSparkAppRequest,
    ) -> adb_inc_20211201_models.InnerKillSparkAppResponse:
        """
        @summary 终止一个Spark Application的运行
        
        @param request: InnerKillSparkAppRequest
        @return: InnerKillSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_kill_spark_app_with_options(request, runtime)

    async def inner_kill_spark_app_async(
        self,
        request: adb_inc_20211201_models.InnerKillSparkAppRequest,
    ) -> adb_inc_20211201_models.InnerKillSparkAppResponse:
        """
        @summary 终止一个Spark Application的运行
        
        @param request: InnerKillSparkAppRequest
        @return: InnerKillSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_kill_spark_app_with_options_async(request, runtime)

    def inner_submit_spark_app_with_options(
        self,
        request: adb_inc_20211201_models.InnerSubmitSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerSubmitSparkAppResponse:
        """
        @summary 内部用提交一个Spark Application
        
        @param request: InnerSubmitSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerSubmitSparkAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not UtilClient.is_unset(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerSubmitSparkApp',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerSubmitSparkAppResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerSubmitSparkAppResponse(),
                self.execute(params, req, runtime)
            )

    async def inner_submit_spark_app_with_options_async(
        self,
        request: adb_inc_20211201_models.InnerSubmitSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.InnerSubmitSparkAppResponse:
        """
        @summary 内部用提交一个Spark Application
        
        @param request: InnerSubmitSparkAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InnerSubmitSparkAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not UtilClient.is_unset(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        if not UtilClient.is_unset(request.trusted_caller_parent_id):
            body['TrustedCallerParentId'] = request.trusted_caller_parent_id
        if not UtilClient.is_unset(request.trusted_caller_type):
            body['TrustedCallerType'] = request.trusted_caller_type
        if not UtilClient.is_unset(request.trusted_caller_uid):
            body['TrustedCallerUid'] = request.trusted_caller_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InnerSubmitSparkApp',
            version='2021-12-01',
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
                adb_inc_20211201_models.InnerSubmitSparkAppResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.InnerSubmitSparkAppResponse(),
                await self.execute_async(params, req, runtime)
            )

    def inner_submit_spark_app(
        self,
        request: adb_inc_20211201_models.InnerSubmitSparkAppRequest,
    ) -> adb_inc_20211201_models.InnerSubmitSparkAppResponse:
        """
        @summary 内部用提交一个Spark Application
        
        @param request: InnerSubmitSparkAppRequest
        @return: InnerSubmitSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inner_submit_spark_app_with_options(request, runtime)

    async def inner_submit_spark_app_async(
        self,
        request: adb_inc_20211201_models.InnerSubmitSparkAppRequest,
    ) -> adb_inc_20211201_models.InnerSubmitSparkAppResponse:
        """
        @summary 内部用提交一个Spark Application
        
        @param request: InnerSubmitSparkAppRequest
        @return: InnerSubmitSparkAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inner_submit_spark_app_with_options_async(request, runtime)

    def list_service_quotas_with_options(
        self,
        request: adb_inc_20211201_models.ListServiceQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ListServiceQuotasResponse:
        """
        @summary 查询API配额信息
        
        @param request: ListServiceQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceQuotasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.category_enum):
            body['CategoryEnum'] = request.category_enum
        if not UtilClient.is_unset(request.dimension_group_key):
            body['DimensionGroupKey'] = request.dimension_group_key
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.use_cache):
            body['UseCache'] = request.use_cache
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceQuotas',
            version='2021-12-01',
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
                adb_inc_20211201_models.ListServiceQuotasResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ListServiceQuotasResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_quotas_with_options_async(
        self,
        request: adb_inc_20211201_models.ListServiceQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ListServiceQuotasResponse:
        """
        @summary 查询API配额信息
        
        @param request: ListServiceQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceQuotasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            body['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.category_enum):
            body['CategoryEnum'] = request.category_enum
        if not UtilClient.is_unset(request.dimension_group_key):
            body['DimensionGroupKey'] = request.dimension_group_key
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.use_cache):
            body['UseCache'] = request.use_cache
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceQuotas',
            version='2021-12-01',
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
                adb_inc_20211201_models.ListServiceQuotasResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ListServiceQuotasResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_quotas(
        self,
        request: adb_inc_20211201_models.ListServiceQuotasRequest,
    ) -> adb_inc_20211201_models.ListServiceQuotasResponse:
        """
        @summary 查询API配额信息
        
        @param request: ListServiceQuotasRequest
        @return: ListServiceQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_quotas_with_options(request, runtime)

    async def list_service_quotas_async(
        self,
        request: adb_inc_20211201_models.ListServiceQuotasRequest,
    ) -> adb_inc_20211201_models.ListServiceQuotasResponse:
        """
        @summary 查询API配额信息
        
        @param request: ListServiceQuotasRequest
        @return: ListServiceQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_quotas_with_options_async(request, runtime)

    def migrate_dbcluster_with_options(
        self,
        request: adb_inc_20211201_models.MigrateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.MigrateDBClusterResponse:
        """
        @summary 迁移集群
        
        @param request: MigrateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.link_switch_mode):
            query['LinkSwitchMode'] = request.link_switch_mode
        if not UtilClient.is_unset(request.new_shard_number):
            query['NewShardNumber'] = request.new_shard_number
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDBCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.MigrateDBClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.MigrateDBClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def migrate_dbcluster_with_options_async(
        self,
        request: adb_inc_20211201_models.MigrateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.MigrateDBClusterResponse:
        """
        @summary 迁移集群
        
        @param request: MigrateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.link_switch_mode):
            query['LinkSwitchMode'] = request.link_switch_mode
        if not UtilClient.is_unset(request.new_shard_number):
            query['NewShardNumber'] = request.new_shard_number
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDBCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.MigrateDBClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.MigrateDBClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def migrate_dbcluster(
        self,
        request: adb_inc_20211201_models.MigrateDBClusterRequest,
    ) -> adb_inc_20211201_models.MigrateDBClusterResponse:
        """
        @summary 迁移集群
        
        @param request: MigrateDBClusterRequest
        @return: MigrateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbcluster_with_options(request, runtime)

    async def migrate_dbcluster_async(
        self,
        request: adb_inc_20211201_models.MigrateDBClusterRequest,
    ) -> adb_inc_20211201_models.MigrateDBClusterResponse:
        """
        @summary 迁移集群
        
        @param request: MigrateDBClusterRequest
        @return: MigrateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.migrate_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_config_with_options(
        self,
        tmp_req: adb_inc_20211201_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ModifyDBClusterConfigResponse:
        """
        @summary 修改实例配置
        
        @param tmp_req: ModifyDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_inc_20211201_models.ModifyDBClusterConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        query = {}
        if not UtilClient.is_unset(request.configs_shrink):
            query['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2021-12-01',
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
                adb_inc_20211201_models.ModifyDBClusterConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ModifyDBClusterConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_dbcluster_config_with_options_async(
        self,
        tmp_req: adb_inc_20211201_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ModifyDBClusterConfigResponse:
        """
        @summary 修改实例配置
        
        @param tmp_req: ModifyDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_inc_20211201_models.ModifyDBClusterConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        query = {}
        if not UtilClient.is_unset(request.configs_shrink):
            query['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2021-12-01',
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
                adb_inc_20211201_models.ModifyDBClusterConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ModifyDBClusterConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_dbcluster_config(
        self,
        request: adb_inc_20211201_models.ModifyDBClusterConfigRequest,
    ) -> adb_inc_20211201_models.ModifyDBClusterConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyDBClusterConfigRequest
        @return: ModifyDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    async def modify_dbcluster_config_async(
        self,
        request: adb_inc_20211201_models.ModifyDBClusterConfigRequest,
    ) -> adb_inc_20211201_models.ModifyDBClusterConfigResponse:
        """
        @summary 修改实例配置
        
        @param request: ModifyDBClusterConfigRequest
        @return: ModifyDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_config_with_options_async(request, runtime)

    def modify_major_customer_with_options(
        self,
        request: adb_inc_20211201_models.ModifyMajorCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ModifyMajorCustomerResponse:
        """
        @summary 修改重点客户信息
        
        @param request: ModifyMajorCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMajorCustomerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.pd):
            query['Pd'] = request.pd
        if not UtilClient.is_unset(request.pdsa):
            query['Pdsa'] = request.pdsa
        if not UtilClient.is_unset(request.ranking):
            query['Ranking'] = request.ranking
        if not UtilClient.is_unset(request.rd):
            query['Rd'] = request.rd
        if not UtilClient.is_unset(request.sa):
            query['Sa'] = request.sa
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMajorCustomer',
            version='2021-12-01',
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
                adb_inc_20211201_models.ModifyMajorCustomerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ModifyMajorCustomerResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_major_customer_with_options_async(
        self,
        request: adb_inc_20211201_models.ModifyMajorCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ModifyMajorCustomerResponse:
        """
        @summary 修改重点客户信息
        
        @param request: ModifyMajorCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMajorCustomerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.pd):
            query['Pd'] = request.pd
        if not UtilClient.is_unset(request.pdsa):
            query['Pdsa'] = request.pdsa
        if not UtilClient.is_unset(request.ranking):
            query['Ranking'] = request.ranking
        if not UtilClient.is_unset(request.rd):
            query['Rd'] = request.rd
        if not UtilClient.is_unset(request.sa):
            query['Sa'] = request.sa
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMajorCustomer',
            version='2021-12-01',
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
                adb_inc_20211201_models.ModifyMajorCustomerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ModifyMajorCustomerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_major_customer(
        self,
        request: adb_inc_20211201_models.ModifyMajorCustomerRequest,
    ) -> adb_inc_20211201_models.ModifyMajorCustomerResponse:
        """
        @summary 修改重点客户信息
        
        @param request: ModifyMajorCustomerRequest
        @return: ModifyMajorCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_major_customer_with_options(request, runtime)

    async def modify_major_customer_async(
        self,
        request: adb_inc_20211201_models.ModifyMajorCustomerRequest,
    ) -> adb_inc_20211201_models.ModifyMajorCustomerResponse:
        """
        @summary 修改重点客户信息
        
        @param request: ModifyMajorCustomerRequest
        @return: ModifyMajorCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_major_customer_with_options_async(request, runtime)

    def modify_service_quota_with_options(
        self,
        tmp_req: adb_inc_20211201_models.ModifyServiceQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ModifyServiceQuotaResponse:
        """
        @summary 用户申请审批通过后通知云产品调整quota
        
        @param tmp_req: ModifyServiceQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceQuotaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_inc_20211201_models.ModifyServiceQuotaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            query['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            query['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyServiceQuota',
            version='2021-12-01',
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
                adb_inc_20211201_models.ModifyServiceQuotaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ModifyServiceQuotaResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_service_quota_with_options_async(
        self,
        tmp_req: adb_inc_20211201_models.ModifyServiceQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ModifyServiceQuotaResponse:
        """
        @summary 用户申请审批通过后通知云产品调整quota
        
        @param tmp_req: ModifyServiceQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceQuotaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_inc_20211201_models.ModifyServiceQuotaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            query['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            query['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyServiceQuota',
            version='2021-12-01',
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
                adb_inc_20211201_models.ModifyServiceQuotaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ModifyServiceQuotaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_service_quota(
        self,
        request: adb_inc_20211201_models.ModifyServiceQuotaRequest,
    ) -> adb_inc_20211201_models.ModifyServiceQuotaResponse:
        """
        @summary 用户申请审批通过后通知云产品调整quota
        
        @param request: ModifyServiceQuotaRequest
        @return: ModifyServiceQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_service_quota_with_options(request, runtime)

    async def modify_service_quota_async(
        self,
        request: adb_inc_20211201_models.ModifyServiceQuotaRequest,
    ) -> adb_inc_20211201_models.ModifyServiceQuotaResponse:
        """
        @summary 用户申请审批通过后通知云产品调整quota
        
        @param request: ModifyServiceQuotaRequest
        @return: ModifyServiceQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_quota_with_options_async(request, runtime)

    def preload_spark_app_metrics_with_options(
        self,
        request: adb_inc_20211201_models.PreloadSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary 预加载Spark应用指标信息
        
        @param request: PreloadSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreloadSparkAppMetrics',
            version='2021-12-01',
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
                adb_inc_20211201_models.PreloadSparkAppMetricsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.PreloadSparkAppMetricsResponse(),
                self.execute(params, req, runtime)
            )

    async def preload_spark_app_metrics_with_options_async(
        self,
        request: adb_inc_20211201_models.PreloadSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary 预加载Spark应用指标信息
        
        @param request: PreloadSparkAppMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadSparkAppMetricsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreloadSparkAppMetrics',
            version='2021-12-01',
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
                adb_inc_20211201_models.PreloadSparkAppMetricsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.PreloadSparkAppMetricsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def preload_spark_app_metrics(
        self,
        request: adb_inc_20211201_models.PreloadSparkAppMetricsRequest,
    ) -> adb_inc_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary 预加载Spark应用指标信息
        
        @param request: PreloadSparkAppMetricsRequest
        @return: PreloadSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preload_spark_app_metrics_with_options(request, runtime)

    async def preload_spark_app_metrics_async(
        self,
        request: adb_inc_20211201_models.PreloadSparkAppMetricsRequest,
    ) -> adb_inc_20211201_models.PreloadSparkAppMetricsResponse:
        """
        @summary 预加载Spark应用指标信息
        
        @param request: PreloadSparkAppMetricsRequest
        @return: PreloadSparkAppMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.preload_spark_app_metrics_with_options_async(request, runtime)

    def release_cluster_vpc_connection_with_options(
        self,
        request: adb_inc_20211201_models.ReleaseClusterVpcConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse:
        """
        @param request: ReleaseClusterVpcConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterVpcConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterVpcConnection',
            version='2021-12-01',
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
                adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse(),
                self.execute(params, req, runtime)
            )

    async def release_cluster_vpc_connection_with_options_async(
        self,
        request: adb_inc_20211201_models.ReleaseClusterVpcConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse:
        """
        @param request: ReleaseClusterVpcConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterVpcConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterVpcConnection',
            version='2021-12-01',
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
                adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def release_cluster_vpc_connection(
        self,
        request: adb_inc_20211201_models.ReleaseClusterVpcConnectionRequest,
    ) -> adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse:
        """
        @param request: ReleaseClusterVpcConnectionRequest
        @return: ReleaseClusterVpcConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_vpc_connection_with_options(request, runtime)

    async def release_cluster_vpc_connection_async(
        self,
        request: adb_inc_20211201_models.ReleaseClusterVpcConnectionRequest,
    ) -> adb_inc_20211201_models.ReleaseClusterVpcConnectionResponse:
        """
        @param request: ReleaseClusterVpcConnectionRequest
        @return: ReleaseClusterVpcConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_vpc_connection_with_options_async(request, runtime)

    def restart_dbcluster_with_options(
        self,
        request: adb_inc_20211201_models.RestartDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.RestartDBClusterResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: RestartDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.RestartDBClusterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.RestartDBClusterResponse(),
                self.execute(params, req, runtime)
            )

    async def restart_dbcluster_with_options_async(
        self,
        request: adb_inc_20211201_models.RestartDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.RestartDBClusterResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: RestartDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBCluster',
            version='2021-12-01',
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
                adb_inc_20211201_models.RestartDBClusterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.RestartDBClusterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def restart_dbcluster(
        self,
        request: adb_inc_20211201_models.RestartDBClusterRequest,
    ) -> adb_inc_20211201_models.RestartDBClusterResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: RestartDBClusterRequest
        @return: RestartDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbcluster_with_options(request, runtime)

    async def restart_dbcluster_async(
        self,
        request: adb_inc_20211201_models.RestartDBClusterRequest,
    ) -> adb_inc_20211201_models.RestartDBClusterResponse:
        """
        @summary 给实例开启VPC连接
        
        @param request: RestartDBClusterRequest
        @return: RestartDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbcluster_with_options_async(request, runtime)

    def revoke_instance_egress_with_options(
        self,
        request: adb_inc_20211201_models.RevokeInstanceEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.RevokeInstanceEgressResponse:
        """
        @param request: RevokeInstanceEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeInstanceEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceEgress',
            version='2021-12-01',
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
                adb_inc_20211201_models.RevokeInstanceEgressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.RevokeInstanceEgressResponse(),
                self.execute(params, req, runtime)
            )

    async def revoke_instance_egress_with_options_async(
        self,
        request: adb_inc_20211201_models.RevokeInstanceEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.RevokeInstanceEgressResponse:
        """
        @param request: RevokeInstanceEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeInstanceEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.ins_type):
            query['InsType'] = request.ins_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceEgress',
            version='2021-12-01',
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
                adb_inc_20211201_models.RevokeInstanceEgressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.RevokeInstanceEgressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def revoke_instance_egress(
        self,
        request: adb_inc_20211201_models.RevokeInstanceEgressRequest,
    ) -> adb_inc_20211201_models.RevokeInstanceEgressResponse:
        """
        @param request: RevokeInstanceEgressRequest
        @return: RevokeInstanceEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_egress_with_options(request, runtime)

    async def revoke_instance_egress_async(
        self,
        request: adb_inc_20211201_models.RevokeInstanceEgressRequest,
    ) -> adb_inc_20211201_models.RevokeInstanceEgressResponse:
        """
        @param request: RevokeInstanceEgressRequest
        @return: RevokeInstanceEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_instance_egress_with_options_async(request, runtime)

    def set_bucket_transfer_acceleration_with_options(
        self,
        request: adb_inc_20211201_models.SetBucketTransferAccelerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.SetBucketTransferAccelerationResponse:
        """
        @summary 开启/关闭指定OSSBucket的传输加速功能
        
        @param request: SetBucketTransferAccelerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetBucketTransferAccelerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acceleration_enabled):
            query['AccelerationEnabled'] = request.acceleration_enabled
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBucketTransferAcceleration',
            version='2021-12-01',
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
                adb_inc_20211201_models.SetBucketTransferAccelerationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.SetBucketTransferAccelerationResponse(),
                self.execute(params, req, runtime)
            )

    async def set_bucket_transfer_acceleration_with_options_async(
        self,
        request: adb_inc_20211201_models.SetBucketTransferAccelerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.SetBucketTransferAccelerationResponse:
        """
        @summary 开启/关闭指定OSSBucket的传输加速功能
        
        @param request: SetBucketTransferAccelerationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetBucketTransferAccelerationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acceleration_enabled):
            query['AccelerationEnabled'] = request.acceleration_enabled
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBucketTransferAcceleration',
            version='2021-12-01',
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
                adb_inc_20211201_models.SetBucketTransferAccelerationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.SetBucketTransferAccelerationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_bucket_transfer_acceleration(
        self,
        request: adb_inc_20211201_models.SetBucketTransferAccelerationRequest,
    ) -> adb_inc_20211201_models.SetBucketTransferAccelerationResponse:
        """
        @summary 开启/关闭指定OSSBucket的传输加速功能
        
        @param request: SetBucketTransferAccelerationRequest
        @return: SetBucketTransferAccelerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_bucket_transfer_acceleration_with_options(request, runtime)

    async def set_bucket_transfer_acceleration_async(
        self,
        request: adb_inc_20211201_models.SetBucketTransferAccelerationRequest,
    ) -> adb_inc_20211201_models.SetBucketTransferAccelerationResponse:
        """
        @summary 开启/关闭指定OSSBucket的传输加速功能
        
        @param request: SetBucketTransferAccelerationRequest
        @return: SetBucketTransferAccelerationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_bucket_transfer_acceleration_with_options_async(request, runtime)

    def start_oss_bucket_replication_with_options(
        self,
        tmp_req: adb_inc_20211201_models.StartOssBucketReplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.StartOssBucketReplicationResponse:
        """
        @summary 创建并执行OSS跨区域复制任务
        
        @param tmp_req: StartOssBucketReplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartOssBucketReplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_inc_20211201_models.StartOssBucketReplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.prefix_list):
            request.prefix_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prefix_list, 'PrefixList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.prefix_list_shrink):
            query['PrefixList'] = request.prefix_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_kms_key_id):
            query['ReplicaKmsKeyId'] = request.replica_kms_key_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.source_bucket_name):
            query['SourceBucketName'] = request.source_bucket_name
        if not UtilClient.is_unset(request.sse_kms_encrypted_objects_status):
            query['SseKmsEncryptedObjectsStatus'] = request.sse_kms_encrypted_objects_status
        if not UtilClient.is_unset(request.target_bucket_name):
            query['TargetBucketName'] = request.target_bucket_name
        if not UtilClient.is_unset(request.target_region_code):
            query['TargetRegionCode'] = request.target_region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartOssBucketReplication',
            version='2021-12-01',
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
                adb_inc_20211201_models.StartOssBucketReplicationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.StartOssBucketReplicationResponse(),
                self.execute(params, req, runtime)
            )

    async def start_oss_bucket_replication_with_options_async(
        self,
        tmp_req: adb_inc_20211201_models.StartOssBucketReplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_inc_20211201_models.StartOssBucketReplicationResponse:
        """
        @summary 创建并执行OSS跨区域复制任务
        
        @param tmp_req: StartOssBucketReplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartOssBucketReplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adb_inc_20211201_models.StartOssBucketReplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.prefix_list):
            request.prefix_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prefix_list, 'PrefixList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ak):
            query['Ak'] = request.ak
        if not UtilClient.is_unset(request.encrypted_sk):
            query['EncryptedSk'] = request.encrypted_sk
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.prefix_list_shrink):
            query['PrefixList'] = request.prefix_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_kms_key_id):
            query['ReplicaKmsKeyId'] = request.replica_kms_key_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.source_bucket_name):
            query['SourceBucketName'] = request.source_bucket_name
        if not UtilClient.is_unset(request.sse_kms_encrypted_objects_status):
            query['SseKmsEncryptedObjectsStatus'] = request.sse_kms_encrypted_objects_status
        if not UtilClient.is_unset(request.target_bucket_name):
            query['TargetBucketName'] = request.target_bucket_name
        if not UtilClient.is_unset(request.target_region_code):
            query['TargetRegionCode'] = request.target_region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartOssBucketReplication',
            version='2021-12-01',
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
                adb_inc_20211201_models.StartOssBucketReplicationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                adb_inc_20211201_models.StartOssBucketReplicationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_oss_bucket_replication(
        self,
        request: adb_inc_20211201_models.StartOssBucketReplicationRequest,
    ) -> adb_inc_20211201_models.StartOssBucketReplicationResponse:
        """
        @summary 创建并执行OSS跨区域复制任务
        
        @param request: StartOssBucketReplicationRequest
        @return: StartOssBucketReplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_oss_bucket_replication_with_options(request, runtime)

    async def start_oss_bucket_replication_async(
        self,
        request: adb_inc_20211201_models.StartOssBucketReplicationRequest,
    ) -> adb_inc_20211201_models.StartOssBucketReplicationResponse:
        """
        @summary 创建并执行OSS跨区域复制任务
        
        @param request: StartOssBucketReplicationRequest
        @return: StartOssBucketReplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_oss_bucket_replication_with_options_async(request, runtime)
