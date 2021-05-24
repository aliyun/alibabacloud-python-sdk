# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_r_kvstore20150101 import models as r_kvstore_20150101_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'r-kvstore.aliyuncs.com',
            'cn-beijing': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou': 'r-kvstore.aliyuncs.com',
            'cn-shanghai': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen': 'r-kvstore.aliyuncs.com',
            'cn-heyuan': 'r-kvstore.aliyuncs.com',
            'ap-southeast-1': 'r-kvstore.aliyuncs.com',
            'us-west-1': 'r-kvstore.aliyuncs.com',
            'us-east-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-finance': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-north-2-gov-1': 'r-kvstore.aliyuncs.com',
            'ap-northeast-2-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-beijing-gov-1': 'r-kvstore.aliyuncs.com',
            'cn-beijing-nu16-b01': 'r-kvstore.aliyuncs.com',
            'cn-edge-1': 'r-kvstore.aliyuncs.com',
            'cn-fujian': 'r-kvstore.aliyuncs.com',
            'cn-haidian-cm12-c01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'r-kvstore.aliyuncs.com',
            'cn-hangzhou-test-306': 'r-kvstore.aliyuncs.com',
            'cn-hongkong-finance-pop': 'r-kvstore.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'r-kvstore.aliyuncs.com',
            'cn-qingdao-nebula': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et15-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-et2-b01': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-inner': 'r-kvstore.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-inner': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'r-kvstore.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'r-kvstore.aliyuncs.com',
            'cn-wuhan': 'r-kvstore.aliyuncs.com',
            'cn-wulanchabu': 'r-kvstore.aliyuncs.com',
            'cn-yushanfang': 'r-kvstore.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'r-kvstore.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'r-kvstore.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'r-kvstore.aliyuncs.com',
            'eu-west-1-oxs': 'r-kvstore.aliyuncs.com',
            'rus-west-1-pop': 'r-kvstore.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('r-kvstore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_sharding_node_with_options(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AddShardingNodeResponse(),
            self.do_rpcrequest('AddShardingNode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_sharding_node_with_options_async(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AddShardingNodeResponse(),
            await self.do_rpcrequest_async('AddShardingNode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sharding_node(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sharding_node_with_options(request, runtime)

    async def add_sharding_node_async(
        self,
        request: r_kvstore_20150101_models.AddShardingNodeRequest,
    ) -> r_kvstore_20150101_models.AddShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sharding_node_with_options_async(request, runtime)

    def allocate_direct_connection_with_options(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateDirectConnectionResponse(),
            self.do_rpcrequest('AllocateDirectConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_direct_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateDirectConnectionResponse(),
            await self.do_rpcrequest_async('AllocateDirectConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_direct_connection(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_direct_connection_with_options(request, runtime)

    async def allocate_direct_connection_async(
        self,
        request: r_kvstore_20150101_models.AllocateDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_direct_connection_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse(),
            self.do_rpcrequest('AllocateInstancePublicConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse(),
            await self.do_rpcrequest_async('AllocateInstancePublicConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: r_kvstore_20150101_models.AllocateInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateAccountResponse(),
            await self.do_rpcrequest_async('CreateAccount', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: r_kvstore_20150101_models.CreateAccountRequest,
    ) -> r_kvstore_20150101_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateBackupResponse(),
            self.do_rpcrequest('CreateBackup', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateBackupResponse(),
            await self.do_rpcrequest_async('CreateBackup', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: r_kvstore_20150101_models.CreateBackupRequest,
    ) -> r_kvstore_20150101_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_cache_analysis_task_with_options(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse(),
            self.do_rpcrequest('CreateCacheAnalysisTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cache_analysis_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse(),
            await self.do_rpcrequest_async('CreateCacheAnalysisTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cache_analysis_task(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cache_analysis_task_with_options(request, runtime)

    async def create_cache_analysis_task_async(
        self,
        request: r_kvstore_20150101_models.CreateCacheAnalysisTaskRequest,
    ) -> r_kvstore_20150101_models.CreateCacheAnalysisTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cache_analysis_task_with_options_async(request, runtime)

    def create_global_distribute_cache_with_options(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse(),
            self.do_rpcrequest('CreateGlobalDistributeCache', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_global_distribute_cache_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse(),
            await self.do_rpcrequest_async('CreateGlobalDistributeCache', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_global_distribute_cache(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_global_distribute_cache_with_options(request, runtime)

    async def create_global_distribute_cache_async(
        self,
        request: r_kvstore_20150101_models.CreateGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.CreateGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_global_distribute_cache_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstanceResponse(),
            await self.do_rpcrequest_async('CreateInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: r_kvstore_20150101_models.CreateInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instances_with_options(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstancesResponse(),
            self.do_rpcrequest('CreateInstances', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instances_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateInstancesResponse(),
            await self.do_rpcrequest_async('CreateInstances', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instances(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instances_with_options(request, runtime)

    async def create_instances_async(
        self,
        request: r_kvstore_20150101_models.CreateInstancesRequest,
    ) -> r_kvstore_20150101_models.CreateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instances_with_options_async(request, runtime)

    def create_tair_instance_with_options(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateTairInstanceResponse(),
            self.do_rpcrequest('CreateTairInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_tair_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateTairInstanceResponse(),
            await self.do_rpcrequest_async('CreateTairInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tair_instance(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tair_instance_with_options(request, runtime)

    async def create_tair_instance_async(
        self,
        request: r_kvstore_20150101_models.CreateTairInstanceRequest,
    ) -> r_kvstore_20150101_models.CreateTairInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tair_instance_with_options_async(request, runtime)

    def create_user_cluster_host_with_options(
        self,
        request: r_kvstore_20150101_models.CreateUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateUserClusterHostResponse(),
            self.do_rpcrequest('CreateUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_cluster_host_with_options_async(
        self,
        request: r_kvstore_20150101_models.CreateUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.CreateUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.CreateUserClusterHostResponse(),
            await self.do_rpcrequest_async('CreateUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user_cluster_host(
        self,
        request: r_kvstore_20150101_models.CreateUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.CreateUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_cluster_host_with_options(request, runtime)

    async def create_user_cluster_host_async(
        self,
        request: r_kvstore_20150101_models.CreateUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.CreateUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_cluster_host_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteAccountResponse(),
            self.do_rpcrequest('DeleteAccount', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteAccountResponse(),
            await self.do_rpcrequest_async('DeleteAccount', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: r_kvstore_20150101_models.DeleteAccountRequest,
    ) -> r_kvstore_20150101_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteInstanceResponse(),
            await self.do_rpcrequest_async('DeleteInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: r_kvstore_20150101_models.DeleteInstanceRequest,
    ) -> r_kvstore_20150101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_sharding_node_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteShardingNodeResponse(),
            self.do_rpcrequest('DeleteShardingNode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sharding_node_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteShardingNodeResponse(),
            await self.do_rpcrequest_async('DeleteShardingNode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sharding_node(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sharding_node_with_options(request, runtime)

    async def delete_sharding_node_async(
        self,
        request: r_kvstore_20150101_models.DeleteShardingNodeRequest,
    ) -> r_kvstore_20150101_models.DeleteShardingNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sharding_node_with_options_async(request, runtime)

    def delete_user_cluster_host_with_options(
        self,
        request: r_kvstore_20150101_models.DeleteUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteUserClusterHostResponse(),
            self.do_rpcrequest('DeleteUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_cluster_host_with_options_async(
        self,
        request: r_kvstore_20150101_models.DeleteUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DeleteUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DeleteUserClusterHostResponse(),
            await self.do_rpcrequest_async('DeleteUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_cluster_host(
        self,
        request: r_kvstore_20150101_models.DeleteUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.DeleteUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_cluster_host_with_options(request, runtime)

    async def delete_user_cluster_host_async(
        self,
        request: r_kvstore_20150101_models.DeleteUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.DeleteUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_cluster_host_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAccountsResponse(),
            await self.do_rpcrequest_async('DescribeAccounts', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: r_kvstore_20150101_models.DescribeAccountsRequest,
    ) -> r_kvstore_20150101_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_task_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTaskResponse(),
            self.do_rpcrequest('DescribeActiveOperationTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_active_operation_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeActiveOperationTaskResponse(),
            await self.do_rpcrequest_async('DescribeActiveOperationTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_with_options(request, runtime)

    async def describe_active_operation_task_async(
        self,
        request: r_kvstore_20150101_models.DescribeActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.DescribeActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_with_options_async(request, runtime)

    def describe_audit_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditRecordsResponse(),
            self.do_rpcrequest('DescribeAuditRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAuditRecordsResponse(),
            await self.do_rpcrequest_async('DescribeAuditRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_records(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    async def describe_audit_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeAuditRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeAuditRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_records_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeAvailableResourceResponse(),
            await self.do_rpcrequest_async('DescribeAvailableResource', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: r_kvstore_20150101_models.DescribeAvailableResourceRequest,
    ) -> r_kvstore_20150101_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupPolicyResponse(),
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupsResponse(),
            self.do_rpcrequest('DescribeBackups', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupsResponse(),
            await self.do_rpcrequest_async('DescribeBackups', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupsRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupTasksResponse(),
            self.do_rpcrequest('DescribeBackupTasks', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeBackupTasksResponse(),
            await self.do_rpcrequest_async('DescribeBackupTasks', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeBackupTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_cache_analysis_report_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisReport', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cache_analysis_report_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse(),
            await self.do_rpcrequest_async('DescribeCacheAnalysisReport', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_report(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_with_options(request, runtime)

    async def describe_cache_analysis_report_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_report_with_options_async(request, runtime)

    def describe_cache_analysis_report_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse(),
            self.do_rpcrequest('DescribeCacheAnalysisReportList', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cache_analysis_report_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse(),
            await self.do_rpcrequest_async('DescribeCacheAnalysisReportList', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cache_analysis_report_list(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cache_analysis_report_list_with_options(request, runtime)

    async def describe_cache_analysis_report_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeCacheAnalysisReportListRequest,
    ) -> r_kvstore_20150101_models.DescribeCacheAnalysisReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cache_analysis_report_list_with_options_async(request, runtime)

    def describe_cluster_member_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterMemberInfoResponse(),
            self.do_rpcrequest('DescribeClusterMemberInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_member_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeClusterMemberInfoResponse(),
            await self.do_rpcrequest_async('DescribeClusterMemberInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_member_info(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_member_info_with_options(request, runtime)

    async def describe_cluster_member_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeClusterMemberInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeClusterMemberInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_member_info_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse(),
            self.do_rpcrequest('DescribeDBInstanceNetInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceNetInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeDBInstanceNetInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dedicated_cluster_instance_list_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse(),
            self.do_rpcrequest('DescribeDedicatedClusterInstanceList', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_cluster_instance_list_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedClusterInstanceList', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_cluster_instance_list(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_instance_list_with_options(request, runtime)

    async def describe_dedicated_cluster_instance_list_async(
        self,
        request: r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> r_kvstore_20150101_models.DescribeDedicatedClusterInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_cluster_instance_list_with_options_async(request, runtime)

    def describe_engine_version_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEngineVersionResponse(),
            self.do_rpcrequest('DescribeEngineVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_engine_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeEngineVersionResponse(),
            await self.do_rpcrequest_async('DescribeEngineVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_engine_version(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_engine_version_with_options(request, runtime)

    async def describe_engine_version_async(
        self,
        request: r_kvstore_20150101_models.DescribeEngineVersionRequest,
    ) -> r_kvstore_20150101_models.DescribeEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_engine_version_with_options_async(request, runtime)

    def describe_global_distribute_cache_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse(),
            self.do_rpcrequest('DescribeGlobalDistributeCache', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_global_distribute_cache_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse(),
            await self.do_rpcrequest_async('DescribeGlobalDistributeCache', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_global_distribute_cache(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_global_distribute_cache_with_options(request, runtime)

    async def describe_global_distribute_cache_async(
        self,
        request: r_kvstore_20150101_models.DescribeGlobalDistributeCacheRequest,
    ) -> r_kvstore_20150101_models.DescribeGlobalDistributeCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_distribute_cache_with_options_async(request, runtime)

    def describe_history_monitor_values_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse(),
            self.do_rpcrequest('DescribeHistoryMonitorValues', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_history_monitor_values_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse(),
            await self.do_rpcrequest_async('DescribeHistoryMonitorValues', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_history_monitor_values(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_monitor_values_with_options(request, runtime)

    async def describe_history_monitor_values_async(
        self,
        request: r_kvstore_20150101_models.DescribeHistoryMonitorValuesRequest,
    ) -> r_kvstore_20150101_models.DescribeHistoryMonitorValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_monitor_values_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeInstanceAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAutoRenewalAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse(),
            await self.do_rpcrequest_async('DescribeInstanceAutoRenewalAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_instance_config_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceConfigResponse(),
            self.do_rpcrequest('DescribeInstanceConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceConfigResponse(),
            await self.do_rpcrequest_async('DescribeInstanceConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_config(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_config_with_options(request, runtime)

    async def describe_instance_config_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_config_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstancesResponse(),
            await self.do_rpcrequest_async('DescribeInstances', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstancesRequest,
    ) -> r_kvstore_20150101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceSSLResponse(),
            self.do_rpcrequest('DescribeInstanceSSL', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_sslwith_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeInstanceSSLResponse(),
            await self.do_rpcrequest_async('DescribeInstanceSSL', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_ssl(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: r_kvstore_20150101_models.DescribeInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.DescribeInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_intranet_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeIntranetAttributeResponse(),
            self.do_rpcrequest('DescribeIntranetAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_intranet_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeIntranetAttributeResponse(),
            await self.do_rpcrequest_async('DescribeIntranetAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_intranet_attribute(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_intranet_attribute_with_options(request, runtime)

    async def describe_intranet_attribute_async(
        self,
        request: r_kvstore_20150101_models.DescribeIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.DescribeIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_intranet_attribute_with_options_async(request, runtime)

    def describe_logic_instance_topology_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse(),
            self.do_rpcrequest('DescribeLogicInstanceTopology', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_logic_instance_topology_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse(),
            await self.do_rpcrequest_async('DescribeLogicInstanceTopology', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_logic_instance_topology(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_logic_instance_topology_with_options(request, runtime)

    async def describe_logic_instance_topology_async(
        self,
        request: r_kvstore_20150101_models.DescribeLogicInstanceTopologyRequest,
    ) -> r_kvstore_20150101_models.DescribeLogicInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_logic_instance_topology_with_options_async(request, runtime)

    def describe_monitor_items_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeMonitorItemsResponse(),
            self.do_rpcrequest('DescribeMonitorItems', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_items_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeMonitorItemsResponse(),
            await self.do_rpcrequest_async('DescribeMonitorItems', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_monitor_items(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_items_with_options(request, runtime)

    async def describe_monitor_items_async(
        self,
        request: r_kvstore_20150101_models.DescribeMonitorItemsRequest,
    ) -> r_kvstore_20150101_models.DescribeMonitorItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_items_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParametersResponse(),
            self.do_rpcrequest('DescribeParameters', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParametersResponse(),
            await self.do_rpcrequest_async('DescribeParameters', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: r_kvstore_20150101_models.DescribeParametersRequest,
    ) -> r_kvstore_20150101_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterTemplatesResponse(),
            self.do_rpcrequest('DescribeParameterTemplates', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeParameterTemplatesResponse(),
            await self.do_rpcrequest_async('DescribeParameterTemplates', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: r_kvstore_20150101_models.DescribeParameterTemplatesRequest,
    ) -> r_kvstore_20150101_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribePriceResponse(),
            await self.do_rpcrequest_async('DescribePrice', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: r_kvstore_20150101_models.DescribePriceRequest,
    ) -> r_kvstore_20150101_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: r_kvstore_20150101_models.DescribeRegionsRequest,
    ) -> r_kvstore_20150101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_role_zone_info_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRoleZoneInfoResponse(),
            self.do_rpcrequest('DescribeRoleZoneInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_role_zone_info_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRoleZoneInfoResponse(),
            await self.do_rpcrequest_async('DescribeRoleZoneInfo', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_role_zone_info(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    async def describe_role_zone_info_async(
        self,
        request: r_kvstore_20150101_models.DescribeRoleZoneInfoRequest,
    ) -> r_kvstore_20150101_models.DescribeRoleZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_role_zone_info_with_options_async(request, runtime)

    def describe_running_log_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRunningLogRecordsResponse(),
            self.do_rpcrequest('DescribeRunningLogRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_running_log_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeRunningLogRecordsResponse(),
            await self.do_rpcrequest_async('DescribeRunningLogRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_running_log_records(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    async def describe_running_log_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeRunningLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeRunningLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_running_log_records_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse(),
            self.do_rpcrequest('DescribeSecurityGroupConfiguration', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse(),
            await self.do_rpcrequest_async('DescribeSecurityGroupConfiguration', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityIpsResponse(),
            self.do_rpcrequest('DescribeSecurityIps', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSecurityIpsResponse(),
            await self.do_rpcrequest_async('DescribeSecurityIps', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_ips(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: r_kvstore_20150101_models.DescribeSecurityIpsRequest,
    ) -> r_kvstore_20150101_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSlowLogRecordsResponse(),
            self.do_rpcrequest('DescribeSlowLogRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeSlowLogRecordsResponse(),
            await self.do_rpcrequest_async('DescribeSlowLogRecords', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: r_kvstore_20150101_models.DescribeSlowLogRecordsRequest,
    ) -> r_kvstore_20150101_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeTasksResponse(),
            self.do_rpcrequest('DescribeTasks', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeTasksResponse(),
            await self.do_rpcrequest_async('DescribeTasks', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: r_kvstore_20150101_models.DescribeTasksRequest,
    ) -> r_kvstore_20150101_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_user_cluster_host_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeUserClusterHostResponse(),
            self.do_rpcrequest('DescribeUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_cluster_host_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeUserClusterHostResponse(),
            await self.do_rpcrequest_async('DescribeUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_cluster_host(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_cluster_host_with_options(request, runtime)

    async def describe_user_cluster_host_async(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_cluster_host_with_options_async(request, runtime)

    def describe_user_cluster_host_instance_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeUserClusterHostInstanceResponse(),
            self.do_rpcrequest('DescribeUserClusterHostInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_cluster_host_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeUserClusterHostInstanceResponse(),
            await self.do_rpcrequest_async('DescribeUserClusterHostInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_cluster_host_instance(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostInstanceRequest,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_cluster_host_instance_with_options(request, runtime)

    async def describe_user_cluster_host_instance_async(
        self,
        request: r_kvstore_20150101_models.DescribeUserClusterHostInstanceRequest,
    ) -> r_kvstore_20150101_models.DescribeUserClusterHostInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_cluster_host_instance_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.DescribeZonesResponse(),
            await self.do_rpcrequest_async('DescribeZones', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: r_kvstore_20150101_models.DescribeZonesRequest,
    ) -> r_kvstore_20150101_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def enable_additional_bandwidth_with_options(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.EnableAdditionalBandwidthResponse(),
            self.do_rpcrequest('EnableAdditionalBandwidth', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_additional_bandwidth_with_options_async(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.EnableAdditionalBandwidthResponse(),
            await self.do_rpcrequest_async('EnableAdditionalBandwidth', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_additional_bandwidth(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_additional_bandwidth_with_options(request, runtime)

    async def enable_additional_bandwidth_async(
        self,
        request: r_kvstore_20150101_models.EnableAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.EnableAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_additional_bandwidth_with_options_async(request, runtime)

    def flush_expire_keys_with_options(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushExpireKeysResponse(),
            self.do_rpcrequest('FlushExpireKeys', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def flush_expire_keys_with_options_async(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushExpireKeysResponse(),
            await self.do_rpcrequest_async('FlushExpireKeys', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def flush_expire_keys(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.flush_expire_keys_with_options(request, runtime)

    async def flush_expire_keys_async(
        self,
        request: r_kvstore_20150101_models.FlushExpireKeysRequest,
    ) -> r_kvstore_20150101_models.FlushExpireKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.flush_expire_keys_with_options_async(request, runtime)

    def flush_instance_with_options(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceResponse(),
            self.do_rpcrequest('FlushInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def flush_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.FlushInstanceResponse(),
            await self.do_rpcrequest_async('FlushInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def flush_instance(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.flush_instance_with_options(request, runtime)

    async def flush_instance_async(
        self,
        request: r_kvstore_20150101_models.FlushInstanceRequest,
    ) -> r_kvstore_20150101_models.FlushInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.flush_instance_with_options_async(request, runtime)

    def grant_account_privilege_with_options(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.GrantAccountPrivilegeResponse(),
            self.do_rpcrequest('GrantAccountPrivilege', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_account_privilege_with_options_async(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.GrantAccountPrivilegeResponse(),
            await self.do_rpcrequest_async('GrantAccountPrivilege', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_account_privilege(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    async def grant_account_privilege_async(
        self,
        request: r_kvstore_20150101_models.GrantAccountPrivilegeRequest,
    ) -> r_kvstore_20150101_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_account_privilege_with_options_async(request, runtime)

    def initialize_kvstore_permission_with_options(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.InitializeKvstorePermissionResponse(),
            self.do_rpcrequest('InitializeKvstorePermission', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def initialize_kvstore_permission_with_options_async(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.InitializeKvstorePermissionResponse(),
            await self.do_rpcrequest_async('InitializeKvstorePermission', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def initialize_kvstore_permission(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_kvstore_permission_with_options(request, runtime)

    async def initialize_kvstore_permission_async(
        self,
        request: r_kvstore_20150101_models.InitializeKvstorePermissionRequest,
    ) -> r_kvstore_20150101_models.InitializeKvstorePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_kvstore_permission_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: r_kvstore_20150101_models.ListTagResourcesRequest,
    ) -> r_kvstore_20150101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.MigrateToOtherZoneResponse(),
            self.do_rpcrequest('MigrateToOtherZone', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.MigrateToOtherZoneResponse(),
            await self.do_rpcrequest_async('MigrateToOtherZone', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: r_kvstore_20150101_models.MigrateToOtherZoneRequest,
    ) -> r_kvstore_20150101_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyAccountDescription', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountDescriptionRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_password_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountPasswordResponse(),
            self.do_rpcrequest('ModifyAccountPassword', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_password_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAccountPasswordResponse(),
            await self.do_rpcrequest_async('ModifyAccountPassword', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_password(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    async def modify_account_password_async(
        self,
        request: r_kvstore_20150101_models.ModifyAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_password_with_options_async(request, runtime)

    def modify_active_operation_task_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTaskResponse(),
            self.do_rpcrequest('ModifyActiveOperationTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_active_operation_task_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyActiveOperationTaskResponse(),
            await self.do_rpcrequest_async('ModifyActiveOperationTask', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_active_operation_task(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_task_with_options(request, runtime)

    async def modify_active_operation_task_async(
        self,
        request: r_kvstore_20150101_models.ModifyActiveOperationTaskRequest,
    ) -> r_kvstore_20150101_models.ModifyActiveOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_task_with_options_async(request, runtime)

    def modify_audit_log_config_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAuditLogConfigResponse(),
            self.do_rpcrequest('ModifyAuditLogConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_audit_log_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyAuditLogConfigResponse(),
            await self.do_rpcrequest_async('ModifyAuditLogConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_audit_log_config(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    async def modify_audit_log_config_async(
        self,
        request: r_kvstore_20150101_models.ModifyAuditLogConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_config_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyBackupPolicyResponse(),
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: r_kvstore_20150101_models.ModifyBackupPolicyRequest,
    ) -> r_kvstore_20150101_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse(),
            self.do_rpcrequest('ModifyDBInstanceConnectionString', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceConnectionString', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: r_kvstore_20150101_models.ModifyDBInstanceConnectionStringRequest,
    ) -> r_kvstore_20150101_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAttributeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAutoRenewalAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceAutoRenewalAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_config_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceConfigResponse(),
            self.do_rpcrequest('ModifyInstanceConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceConfigResponse(),
            await self.do_rpcrequest_async('ModifyInstanceConfig', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_config(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_config_with_options(request, runtime)

    async def modify_instance_config_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceConfigRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_config_with_options_async(request, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse(),
            self.do_rpcrequest('ModifyInstanceMaintainTime', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceMaintainTime', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    async def modify_instance_maintain_time_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMaintainTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintain_time_with_options_async(request, runtime)

    def modify_instance_major_version_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse(),
            self.do_rpcrequest('ModifyInstanceMajorVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_major_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse(),
            await self.do_rpcrequest_async('ModifyInstanceMajorVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_major_version(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_major_version_with_options(request, runtime)

    async def modify_instance_major_version_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMajorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMajorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_major_version_with_options_async(request, runtime)

    def modify_instance_minor_version_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse(),
            self.do_rpcrequest('ModifyInstanceMinorVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_minor_version_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse(),
            await self.do_rpcrequest_async('ModifyInstanceMinorVersion', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_minor_version(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_minor_version_with_options(request, runtime)

    async def modify_instance_minor_version_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceMinorVersionRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_minor_version_with_options_async(request, runtime)

    def modify_instance_net_expire_time_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse(),
            self.do_rpcrequest('ModifyInstanceNetExpireTime', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_net_expire_time_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceNetExpireTime', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_net_expire_time(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_net_expire_time_with_options(request, runtime)

    async def modify_instance_net_expire_time_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceNetExpireTimeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceNetExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_net_expire_time_with_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSpecResponse(),
            self.do_rpcrequest('ModifyInstanceSpec', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSpecResponse(),
            await self.do_rpcrequest_async('ModifyInstanceSpec', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_spec(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_sslwith_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSSLResponse(),
            self.do_rpcrequest('ModifyInstanceSSL', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_sslwith_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceSSLResponse(),
            await self.do_rpcrequest_async('ModifyInstanceSSL', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_ssl(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    async def modify_instance_ssl_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceSSLRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_sslwith_options_async(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse(),
            self.do_rpcrequest('ModifyInstanceVpcAuthMode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_vpc_auth_mode_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse(),
            await self.do_rpcrequest_async('ModifyInstanceVpcAuthMode', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vpc_auth_mode(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    async def modify_instance_vpc_auth_mode_async(
        self,
        request: r_kvstore_20150101_models.ModifyInstanceVpcAuthModeRequest,
    ) -> r_kvstore_20150101_models.ModifyInstanceVpcAuthModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_auth_mode_with_options_async(request, runtime)

    def modify_intranet_attribute_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyIntranetAttributeResponse(),
            self.do_rpcrequest('ModifyIntranetAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_intranet_attribute_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyIntranetAttributeResponse(),
            await self.do_rpcrequest_async('ModifyIntranetAttribute', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_intranet_attribute(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_intranet_attribute_with_options(request, runtime)

    async def modify_intranet_attribute_async(
        self,
        request: r_kvstore_20150101_models.ModifyIntranetAttributeRequest,
    ) -> r_kvstore_20150101_models.ModifyIntranetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_intranet_attribute_with_options_async(request, runtime)

    def modify_node_spec_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyNodeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyNodeSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyNodeSpecResponse(),
            self.do_rpcrequest('ModifyNodeSpec', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_node_spec_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyNodeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyNodeSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyNodeSpecResponse(),
            await self.do_rpcrequest_async('ModifyNodeSpec', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_node_spec(
        self,
        request: r_kvstore_20150101_models.ModifyNodeSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyNodeSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_node_spec_with_options(request, runtime)

    async def modify_node_spec_async(
        self,
        request: r_kvstore_20150101_models.ModifyNodeSpecRequest,
    ) -> r_kvstore_20150101_models.ModifyNodeSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_node_spec_with_options_async(request, runtime)

    def modify_resource_group_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyResourceGroupResponse(),
            self.do_rpcrequest('ModifyResourceGroup', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_resource_group_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyResourceGroupResponse(),
            await self.do_rpcrequest_async('ModifyResourceGroup', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_group(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    async def modify_resource_group_async(
        self,
        request: r_kvstore_20150101_models.ModifyResourceGroupRequest,
    ) -> r_kvstore_20150101_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_group_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse(),
            self.do_rpcrequest('ModifySecurityGroupConfiguration', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse(),
            await self.do_rpcrequest_async('ModifySecurityGroupConfiguration', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityGroupConfigurationRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityIpsResponse(),
            self.do_rpcrequest('ModifySecurityIps', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifySecurityIpsResponse(),
            await self.do_rpcrequest_async('ModifySecurityIps', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: r_kvstore_20150101_models.ModifySecurityIpsRequest,
    ) -> r_kvstore_20150101_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_user_cluster_host_with_options(
        self,
        request: r_kvstore_20150101_models.ModifyUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyUserClusterHostResponse(),
            self.do_rpcrequest('ModifyUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_cluster_host_with_options_async(
        self,
        request: r_kvstore_20150101_models.ModifyUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ModifyUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ModifyUserClusterHostResponse(),
            await self.do_rpcrequest_async('ModifyUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_cluster_host(
        self,
        request: r_kvstore_20150101_models.ModifyUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.ModifyUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_cluster_host_with_options(request, runtime)

    async def modify_user_cluster_host_async(
        self,
        request: r_kvstore_20150101_models.ModifyUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.ModifyUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_cluster_host_with_options_async(request, runtime)

    def release_direct_connection_with_options(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseDirectConnectionResponse(),
            self.do_rpcrequest('ReleaseDirectConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_direct_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseDirectConnectionResponse(),
            await self.do_rpcrequest_async('ReleaseDirectConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_direct_connection(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_direct_connection_with_options(request, runtime)

    async def release_direct_connection_async(
        self,
        request: r_kvstore_20150101_models.ReleaseDirectConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseDirectConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_direct_connection_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse(),
            self.do_rpcrequest('ReleaseInstancePublicConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse(),
            await self.do_rpcrequest_async('ReleaseInstancePublicConnection', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: r_kvstore_20150101_models.ReleaseInstancePublicConnectionRequest,
    ) -> r_kvstore_20150101_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def renew_additional_bandwidth_with_options(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewAdditionalBandwidthResponse(),
            self.do_rpcrequest('RenewAdditionalBandwidth', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_additional_bandwidth_with_options_async(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewAdditionalBandwidthResponse(),
            await self.do_rpcrequest_async('RenewAdditionalBandwidth', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_additional_bandwidth(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_additional_bandwidth_with_options(request, runtime)

    async def renew_additional_bandwidth_async(
        self,
        request: r_kvstore_20150101_models.RenewAdditionalBandwidthRequest,
    ) -> r_kvstore_20150101_models.RenewAdditionalBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_additional_bandwidth_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewInstanceResponse(),
            self.do_rpcrequest('RenewInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RenewInstanceResponse(),
            await self.do_rpcrequest_async('RenewInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: r_kvstore_20150101_models.RenewInstanceRequest,
    ) -> r_kvstore_20150101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def replace_user_cluster_host_with_options(
        self,
        request: r_kvstore_20150101_models.ReplaceUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReplaceUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReplaceUserClusterHostResponse(),
            self.do_rpcrequest('ReplaceUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_user_cluster_host_with_options_async(
        self,
        request: r_kvstore_20150101_models.ReplaceUserClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ReplaceUserClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ReplaceUserClusterHostResponse(),
            await self.do_rpcrequest_async('ReplaceUserClusterHost', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_user_cluster_host(
        self,
        request: r_kvstore_20150101_models.ReplaceUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.ReplaceUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_user_cluster_host_with_options(request, runtime)

    async def replace_user_cluster_host_async(
        self,
        request: r_kvstore_20150101_models.ReplaceUserClusterHostRequest,
    ) -> r_kvstore_20150101_models.ReplaceUserClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_user_cluster_host_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.ResetAccountPasswordResponse(),
            await self.do_rpcrequest_async('ResetAccountPassword', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: r_kvstore_20150101_models.ResetAccountPasswordRequest,
    ) -> r_kvstore_20150101_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestartInstanceResponse(),
            self.do_rpcrequest('RestartInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestartInstanceResponse(),
            await self.do_rpcrequest_async('RestartInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_instance(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: r_kvstore_20150101_models.RestartInstanceRequest,
    ) -> r_kvstore_20150101_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def restore_instance_with_options(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestoreInstanceResponse(),
            self.do_rpcrequest('RestoreInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_instance_with_options_async(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.RestoreInstanceResponse(),
            await self.do_rpcrequest_async('RestoreInstance', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_instance(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_instance_with_options(request, runtime)

    async def restore_instance_async(
        self,
        request: r_kvstore_20150101_models.RestoreInstanceRequest,
    ) -> r_kvstore_20150101_models.RestoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_instance_with_options_async(request, runtime)

    def switch_instance_hawith_options(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceHAResponse(),
            self.do_rpcrequest('SwitchInstanceHA', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_instance_hawith_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceHAResponse(),
            await self.do_rpcrequest_async('SwitchInstanceHA', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_instance_ha(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_instance_hawith_options(request, runtime)

    async def switch_instance_ha_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceHARequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_instance_hawith_options_async(request, runtime)

    def switch_instance_proxy_with_options(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceProxyResponse(),
            self.do_rpcrequest('SwitchInstanceProxy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_instance_proxy_with_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchInstanceProxyResponse(),
            await self.do_rpcrequest_async('SwitchInstanceProxy', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_instance_proxy(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_instance_proxy_with_options(request, runtime)

    async def switch_instance_proxy_async(
        self,
        request: r_kvstore_20150101_models.SwitchInstanceProxyRequest,
    ) -> r_kvstore_20150101_models.SwitchInstanceProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_instance_proxy_with_options_async(request, runtime)

    def switch_network_with_options(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchNetworkResponse(),
            self.do_rpcrequest('SwitchNetwork', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_network_with_options_async(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SwitchNetworkResponse(),
            await self.do_rpcrequest_async('SwitchNetwork', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_network(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_network_with_options(request, runtime)

    async def switch_network_async(
        self,
        request: r_kvstore_20150101_models.SwitchNetworkRequest,
    ) -> r_kvstore_20150101_models.SwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_network_with_options_async(request, runtime)

    def sync_dts_status_with_options(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SyncDtsStatusResponse(),
            self.do_rpcrequest('SyncDtsStatus', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_dts_status_with_options_async(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.SyncDtsStatusResponse(),
            await self.do_rpcrequest_async('SyncDtsStatus', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_dts_status(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_dts_status_with_options(request, runtime)

    async def sync_dts_status_async(
        self,
        request: r_kvstore_20150101_models.SyncDtsStatusRequest,
    ) -> r_kvstore_20150101_models.SyncDtsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_dts_status_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: r_kvstore_20150101_models.TagResourcesRequest,
    ) -> r_kvstore_20150101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transform_instance_charge_type_with_options(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformInstanceChargeTypeResponse(),
            self.do_rpcrequest('TransformInstanceChargeType', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transform_instance_charge_type_with_options_async(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformInstanceChargeTypeResponse(),
            await self.do_rpcrequest_async('TransformInstanceChargeType', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transform_instance_charge_type(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_instance_charge_type_with_options(request, runtime)

    async def transform_instance_charge_type_async(
        self,
        request: r_kvstore_20150101_models.TransformInstanceChargeTypeRequest,
    ) -> r_kvstore_20150101_models.TransformInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_instance_charge_type_with_options_async(request, runtime)

    def transform_to_pre_paid_with_options(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformToPrePaidResponse(),
            self.do_rpcrequest('TransformToPrePaid', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transform_to_pre_paid_with_options_async(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.TransformToPrePaidResponse(),
            await self.do_rpcrequest_async('TransformToPrePaid', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transform_to_pre_paid(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    async def transform_to_pre_paid_async(
        self,
        request: r_kvstore_20150101_models.TransformToPrePaidRequest,
    ) -> r_kvstore_20150101_models.TransformToPrePaidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_to_pre_paid_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            r_kvstore_20150101_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2015-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: r_kvstore_20150101_models.UntagResourcesRequest,
    ) -> r_kvstore_20150101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
