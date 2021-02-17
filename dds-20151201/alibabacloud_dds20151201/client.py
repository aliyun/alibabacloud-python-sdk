# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dds20151201 import models as dds_20151201_models
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
            'cn-qingdao': 'mongodb.aliyuncs.com',
            'cn-beijing': 'mongodb.aliyuncs.com',
            'cn-chengdu': 'mongodb.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'mongodb.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'mongodb.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'mongodb.aliyuncs.com',
            'cn-shanghai': 'mongodb.aliyuncs.com',
            'cn-shenzhen': 'mongodb.aliyuncs.com',
            'cn-heyuan': 'mongodb.aliyuncs.com',
            'cn-hongkong': 'mongodb.aliyuncs.com',
            'ap-southeast-1': 'mongodb.aliyuncs.com',
            'ap-southeast-2': 'mongodb.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'mongodb.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'mongodb.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'mongodb.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'mongodb.eu-west-1.aliyuncs.com',
            'us-west-1': 'mongodb.aliyuncs.com',
            'us-east-1': 'mongodb.aliyuncs.com',
            'eu-central-1': 'mongodb.eu-central-1.aliyuncs.com',
            'me-east-1': 'mongodb.me-east-1.aliyuncs.com',
            'ap-south-1': 'mongodb.ap-south-1.aliyuncs.com',
            'cn-hangzhou-finance': 'mongodb.aliyuncs.com',
            'cn-shanghai-finance-1': 'mongodb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mongodb.aliyuncs.com',
            'cn-north-2-gov-1': 'mongodb.aliyuncs.com',
            'ap-northeast-2-pop': 'mongodb.aliyuncs.com',
            'cn-beijing-finance-1': 'mongodb.aliyuncs.com',
            'cn-beijing-finance-pop': 'mongodb.aliyuncs.com',
            'cn-beijing-gov-1': 'mongodb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mongodb.aliyuncs.com',
            'cn-edge-1': 'mongodb.aliyuncs.com',
            'cn-fujian': 'mongodb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mongodb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mongodb.aliyuncs.com',
            'cn-hangzhou-test-306': 'mongodb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mongodb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'mongodb.aliyuncs.com',
            'cn-qingdao-nebula': 'mongodb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mongodb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mongodb.aliyuncs.com',
            'cn-shanghai-inner': 'mongodb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mongodb.aliyuncs.com',
            'cn-shenzhen-inner': 'mongodb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mongodb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mongodb.aliyuncs.com',
            'cn-wuhan': 'mongodb.aliyuncs.com',
            'cn-wulanchabu': 'mongodb.aliyuncs.com',
            'cn-yushanfang': 'mongodb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mongodb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mongodb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mongodb.aliyuncs.com',
            'eu-west-1-oxs': 'mongodb.aliyuncs.com',
            'rus-west-1-pop': 'mongodb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_node_private_network_address_with_options(
        self,
        request: dds_20151201_models.AllocateNodePrivateNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.AllocateNodePrivateNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.AllocateNodePrivateNetworkAddressResponse().from_map(
            self.do_rpcrequest('AllocateNodePrivateNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_node_private_network_address_with_options_async(
        self,
        request: dds_20151201_models.AllocateNodePrivateNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.AllocateNodePrivateNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.AllocateNodePrivateNetworkAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocateNodePrivateNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_node_private_network_address(
        self,
        request: dds_20151201_models.AllocateNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.AllocateNodePrivateNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_node_private_network_address_with_options(request, runtime)

    async def allocate_node_private_network_address_async(
        self,
        request: dds_20151201_models.AllocateNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.AllocateNodePrivateNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_node_private_network_address_with_options_async(request, runtime)

    def allocate_public_network_address_with_options(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.AllocatePublicNetworkAddressResponse().from_map(
            self.do_rpcrequest('AllocatePublicNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_public_network_address_with_options_async(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.AllocatePublicNetworkAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocatePublicNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_public_network_address(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_network_address_with_options(request, runtime)

    async def allocate_public_network_address_async(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_network_address_with_options_async(request, runtime)

    def check_cloud_resource_authorized_with_options(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CheckCloudResourceAuthorizedResponse().from_map(
            self.do_rpcrequest('CheckCloudResourceAuthorized', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CheckCloudResourceAuthorizedResponse().from_map(
            await self.do_rpcrequest_async('CheckCloudResourceAuthorized', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def check_recovery_condition_with_options(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CheckRecoveryConditionResponse().from_map(
            self.do_rpcrequest('CheckRecoveryCondition', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_recovery_condition_with_options_async(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CheckRecoveryConditionResponse().from_map(
            await self.do_rpcrequest_async('CheckRecoveryCondition', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_recovery_condition(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_recovery_condition_with_options(request, runtime)

    async def check_recovery_condition_async(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_recovery_condition_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: dds_20151201_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateBackupResponse().from_map(
            self.do_rpcrequest('CreateBackup', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: dds_20151201_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateBackupResponse().from_map(
            await self.do_rpcrequest_async('CreateBackup', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(
        self,
        request: dds_20151201_models.CreateBackupRequest,
    ) -> dds_20151201_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: dds_20151201_models.CreateBackupRequest,
    ) -> dds_20151201_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateDBInstanceResponse().from_map(
            self.do_rpcrequest('CreateDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_node_with_options(
        self,
        request: dds_20151201_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateNodeResponse().from_map(
            self.do_rpcrequest('CreateNode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_node_with_options_async(
        self,
        request: dds_20151201_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateNodeResponse().from_map(
            await self.do_rpcrequest_async('CreateNode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_node(
        self,
        request: dds_20151201_models.CreateNodeRequest,
    ) -> dds_20151201_models.CreateNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_node_with_options(request, runtime)

    async def create_node_async(
        self,
        request: dds_20151201_models.CreateNodeRequest,
    ) -> dds_20151201_models.CreateNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_node_with_options_async(request, runtime)

    def create_recommendation_task_with_options(
        self,
        request: dds_20151201_models.CreateRecommendationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateRecommendationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateRecommendationTaskResponse().from_map(
            self.do_rpcrequest('CreateRecommendationTask', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_recommendation_task_with_options_async(
        self,
        request: dds_20151201_models.CreateRecommendationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateRecommendationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateRecommendationTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateRecommendationTask', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_recommendation_task(
        self,
        request: dds_20151201_models.CreateRecommendationTaskRequest,
    ) -> dds_20151201_models.CreateRecommendationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_recommendation_task_with_options(request, runtime)

    async def create_recommendation_task_async(
        self,
        request: dds_20151201_models.CreateRecommendationTaskRequest,
    ) -> dds_20151201_models.CreateRecommendationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_recommendation_task_with_options_async(request, runtime)

    def create_serverless_dbinstance_with_options(
        self,
        request: dds_20151201_models.CreateServerlessDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateServerlessDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateServerlessDBInstanceResponse().from_map(
            self.do_rpcrequest('CreateServerlessDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_serverless_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.CreateServerlessDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateServerlessDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateServerlessDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateServerlessDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_serverless_dbinstance(
        self,
        request: dds_20151201_models.CreateServerlessDBInstanceRequest,
    ) -> dds_20151201_models.CreateServerlessDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_serverless_dbinstance_with_options(request, runtime)

    async def create_serverless_dbinstance_async(
        self,
        request: dds_20151201_models.CreateServerlessDBInstanceRequest,
    ) -> dds_20151201_models.CreateServerlessDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_serverless_dbinstance_with_options_async(request, runtime)

    def create_sharding_dbinstance_with_options(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateShardingDBInstanceResponse().from_map(
            self.do_rpcrequest('CreateShardingDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sharding_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.CreateShardingDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateShardingDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sharding_dbinstance(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sharding_dbinstance_with_options(request, runtime)

    async def create_sharding_dbinstance_async(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sharding_dbinstance_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DeleteDBInstanceResponse().from_map(
            self.do_rpcrequest('DeleteDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DeleteDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_node_with_options(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DeleteNodeResponse().from_map(
            self.do_rpcrequest('DeleteNode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_node_with_options_async(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DeleteNodeResponse().from_map(
            await self.do_rpcrequest_async('DeleteNode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_node(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
    ) -> dds_20151201_models.DeleteNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    async def delete_node_async(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
    ) -> dds_20151201_models.DeleteNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_node_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAccountsResponse().from_map(
            self.do_rpcrequest('DescribeAccounts', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAccountsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccounts', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_task_count_with_options(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeActiveOperationTaskCountResponse().from_map(
            self.do_rpcrequest('DescribeActiveOperationTaskCount', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_active_operation_task_count_with_options_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeActiveOperationTaskCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeActiveOperationTaskCount', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task_count(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_count_with_options(request, runtime)

    async def describe_active_operation_task_count_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_count_with_options_async(request, runtime)

    def describe_active_operation_task_type_with_options(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeActiveOperationTaskTypeResponse().from_map(
            self.do_rpcrequest('DescribeActiveOperationTaskType', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_active_operation_task_type_with_options_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeActiveOperationTaskTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeActiveOperationTaskType', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task_type(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_type_with_options(request, runtime)

    async def describe_active_operation_task_type_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_type_with_options_async(request, runtime)

    def describe_audit_files_with_options(
        self,
        request: dds_20151201_models.DescribeAuditFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditFilesResponse().from_map(
            self.do_rpcrequest('DescribeAuditFiles', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_files_with_options_async(
        self,
        request: dds_20151201_models.DescribeAuditFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAuditFiles', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_files(
        self,
        request: dds_20151201_models.DescribeAuditFilesRequest,
    ) -> dds_20151201_models.DescribeAuditFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_files_with_options(request, runtime)

    async def describe_audit_files_async(
        self,
        request: dds_20151201_models.DescribeAuditFilesRequest,
    ) -> dds_20151201_models.DescribeAuditFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_files_with_options_async(request, runtime)

    def describe_audit_log_filter_with_options(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditLogFilterResponse().from_map(
            self.do_rpcrequest('DescribeAuditLogFilter', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_log_filter_with_options_async(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditLogFilterResponse().from_map(
            await self.do_rpcrequest_async('DescribeAuditLogFilter', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_log_filter(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_filter_with_options(request, runtime)

    async def describe_audit_log_filter_async(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_filter_with_options_async(request, runtime)

    def describe_audit_policy_with_options(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditPolicyResponse().from_map(
            self.do_rpcrequest('DescribeAuditPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_policy_with_options_async(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeAuditPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_policy(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_policy_with_options(request, runtime)

    async def describe_audit_policy_async(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_policy_with_options_async(request, runtime)

    def describe_audit_records_with_options(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditRecordsResponse().from_map(
            self.do_rpcrequest('DescribeAuditRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAuditRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAuditRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_records(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    async def describe_audit_records_async(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_records_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAvailableResourceResponse().from_map(
            self.do_rpcrequest('DescribeAvailableResource', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAvailableResourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableResource', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_available_time_range_with_options(
        self,
        request: dds_20151201_models.DescribeAvailableTimeRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableTimeRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAvailableTimeRangeResponse().from_map(
            self.do_rpcrequest('DescribeAvailableTimeRange', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_time_range_with_options_async(
        self,
        request: dds_20151201_models.DescribeAvailableTimeRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableTimeRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeAvailableTimeRangeResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableTimeRange', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_time_range(
        self,
        request: dds_20151201_models.DescribeAvailableTimeRangeRequest,
    ) -> dds_20151201_models.DescribeAvailableTimeRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_time_range_with_options(request, runtime)

    async def describe_available_time_range_async(
        self,
        request: dds_20151201_models.DescribeAvailableTimeRangeRequest,
    ) -> dds_20151201_models.DescribeAvailableTimeRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_time_range_with_options_async(request, runtime)

    def describe_backup_dbs_with_options(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeBackupDBsResponse().from_map(
            self.do_rpcrequest('DescribeBackupDBs', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_dbs_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeBackupDBsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupDBs', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_dbs(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    async def describe_backup_dbs_async(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_dbs_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeBackupPolicyResponse().from_map(
            self.do_rpcrequest('DescribeBackupPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeBackupsResponse().from_map(
            self.do_rpcrequest('DescribeBackups', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackups', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_encryption_key_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceEncryptionKey', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_encryption_key_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceEncryptionKey', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_encryption_key(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_encryption_key_with_options(request, runtime)

    async def describe_dbinstance_encryption_key_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_encryption_key_with_options_async(request, runtime)

    def describe_dbinstance_monitor_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceMonitorResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceMonitor', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_monitor_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceMonitorResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceMonitor', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_monitor(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    async def describe_dbinstance_monitor_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_monitor_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstancePerformanceResponse().from_map(
            self.do_rpcrequest('DescribeDBInstancePerformance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstancePerformanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstancePerformance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstancesResponse().from_map(
            self.do_rpcrequest('DescribeDBInstances', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstances', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceSSLResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceSSL', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceSSLResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceSSL', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_tdeinfo_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceTDEInfoResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceTDEInfo', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_tdeinfo_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDBInstanceTDEInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceTDEInfo', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_tdeinfo(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdeinfo_with_options(request, runtime)

    async def describe_dbinstance_tdeinfo_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_tdeinfo_with_options_async(request, runtime)

    def describe_dedicated_cluster_instance_list_with_options(
        self,
        request: dds_20151201_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDedicatedClusterInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDedicatedClusterInstanceListResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedClusterInstanceList', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_cluster_instance_list_with_options_async(
        self,
        request: dds_20151201_models.DescribeDedicatedClusterInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDedicatedClusterInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeDedicatedClusterInstanceListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedClusterInstanceList', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_cluster_instance_list(
        self,
        request: dds_20151201_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> dds_20151201_models.DescribeDedicatedClusterInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_instance_list_with_options(request, runtime)

    async def describe_dedicated_cluster_instance_list_async(
        self,
        request: dds_20151201_models.DescribeDedicatedClusterInstanceListRequest,
    ) -> dds_20151201_models.DescribeDedicatedClusterInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_cluster_instance_list_with_options_async(request, runtime)

    def describe_error_log_records_with_options(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeErrorLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeErrorLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_error_log_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeErrorLogRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeErrorLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_error_log_records(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_error_log_records_with_options(request, runtime)

    async def describe_error_log_records_async(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_error_log_records_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAutoRenewalAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAutoRenewalAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_kernel_release_notes_with_options(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeKernelReleaseNotesResponse().from_map(
            self.do_rpcrequest('DescribeKernelReleaseNotes', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_kernel_release_notes_with_options_async(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeKernelReleaseNotesResponse().from_map(
            await self.do_rpcrequest_async('DescribeKernelReleaseNotes', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_kernel_release_notes(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_kernel_release_notes_with_options(request, runtime)

    async def describe_kernel_release_notes_async(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_kernel_release_notes_with_options_async(request, runtime)

    def describe_mongo_dblog_config_with_options(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeMongoDBLogConfigResponse().from_map(
            self.do_rpcrequest('DescribeMongoDBLogConfig', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mongo_dblog_config_with_options_async(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeMongoDBLogConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeMongoDBLogConfig', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mongo_dblog_config(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mongo_dblog_config_with_options(request, runtime)

    async def describe_mongo_dblog_config_async(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mongo_dblog_config_with_options_async(request, runtime)

    def describe_parameter_modification_history_with_options(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeParameterModificationHistoryResponse().from_map(
            self.do_rpcrequest('DescribeParameterModificationHistory', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_modification_history_with_options_async(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeParameterModificationHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameterModificationHistory', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_modification_history(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_modification_history_with_options(request, runtime)

    async def describe_parameter_modification_history_async(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_modification_history_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeParametersResponse().from_map(
            self.do_rpcrequest('DescribeParameters', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeParametersResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameters', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
    ) -> dds_20151201_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
    ) -> dds_20151201_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeParameterTemplatesResponse().from_map(
            self.do_rpcrequest('DescribeParameterTemplates', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeParameterTemplatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameterTemplates', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: dds_20151201_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribePriceResponse().from_map(
            self.do_rpcrequest('DescribePrice', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: dds_20151201_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribePriceResponse().from_map(
            await self.do_rpcrequest_async('DescribePrice', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(
        self,
        request: dds_20151201_models.DescribePriceRequest,
    ) -> dds_20151201_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: dds_20151201_models.DescribePriceRequest,
    ) -> dds_20151201_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_replica_set_role_with_options(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeReplicaSetRoleResponse().from_map(
            self.do_rpcrequest('DescribeReplicaSetRole', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_replica_set_role_with_options_async(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeReplicaSetRoleResponse().from_map(
            await self.do_rpcrequest_async('DescribeReplicaSetRole', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_replica_set_role(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_replica_set_role_with_options(request, runtime)

    async def describe_replica_set_role_async(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_replica_set_role_with_options_async(request, runtime)

    def describe_role_zone_info_with_options(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeRoleZoneInfoResponse().from_map(
            self.do_rpcrequest('DescribeRoleZoneInfo', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_role_zone_info_with_options_async(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeRoleZoneInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeRoleZoneInfo', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_role_zone_info(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    async def describe_role_zone_info_async(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_role_zone_info_with_options_async(request, runtime)

    def describe_running_log_records_with_options(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeRunningLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeRunningLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_running_log_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeRunningLogRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRunningLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_running_log_records(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    async def describe_running_log_records_async(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_running_log_records_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeSecurityGroupConfigurationResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroupConfiguration', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeSecurityGroupConfigurationResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroupConfiguration', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeSecurityIpsResponse().from_map(
            self.do_rpcrequest('DescribeSecurityIps', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeSecurityIpsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityIps', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_ips(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_sharding_network_address_with_options(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeShardingNetworkAddressResponse().from_map(
            self.do_rpcrequest('DescribeShardingNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sharding_network_address_with_options_async(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeShardingNetworkAddressResponse().from_map(
            await self.do_rpcrequest_async('DescribeShardingNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sharding_network_address(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sharding_network_address_with_options(request, runtime)

    async def describe_sharding_network_address_async(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sharding_network_address_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeSlowLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeSlowLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DescribeSlowLogRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlowLogRecords', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def destroy_instance_with_options(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DestroyInstanceResponse().from_map(
            self.do_rpcrequest('DestroyInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def destroy_instance_with_options_async(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.DestroyInstanceResponse().from_map(
            await self.do_rpcrequest_async('DestroyInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def destroy_instance(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_instance_with_options(request, runtime)

    async def destroy_instance_async(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_instance_with_options_async(request, runtime)

    def evaluate_resource_with_options(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.EvaluateResourceResponse().from_map(
            self.do_rpcrequest('EvaluateResource', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def evaluate_resource_with_options_async(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.EvaluateResourceResponse().from_map(
            await self.do_rpcrequest_async('EvaluateResource', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def evaluate_resource(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.evaluate_resource_with_options(request, runtime)

    async def evaluate_resource_async(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_resource_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def migrate_available_zone_with_options(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.MigrateAvailableZoneResponse().from_map(
            self.do_rpcrequest('MigrateAvailableZone', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_available_zone_with_options_async(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.MigrateAvailableZoneResponse().from_map(
            await self.do_rpcrequest_async('MigrateAvailableZone', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_available_zone(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_available_zone_with_options(request, runtime)

    async def migrate_available_zone_async(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_available_zone_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.MigrateToOtherZoneResponse().from_map(
            self.do_rpcrequest('MigrateToOtherZone', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.MigrateToOtherZoneResponse().from_map(
            await self.do_rpcrequest_async('MigrateToOtherZone', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyAccountDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyAccountDescription', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyAccountDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyAccountDescription', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_audit_log_filter_with_options(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyAuditLogFilterResponse().from_map(
            self.do_rpcrequest('ModifyAuditLogFilter', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_audit_log_filter_with_options_async(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyAuditLogFilterResponse().from_map(
            await self.do_rpcrequest_async('ModifyAuditLogFilter', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_audit_log_filter(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_filter_with_options(request, runtime)

    async def modify_audit_log_filter_async(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_filter_with_options_async(request, runtime)

    def modify_audit_policy_with_options(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyAuditPolicyResponse().from_map(
            self.do_rpcrequest('ModifyAuditPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_audit_policy_with_options_async(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyAuditPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyAuditPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_audit_policy(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_policy_with_options(request, runtime)

    async def modify_audit_policy_async(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_policy_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyBackupPolicyResponse().from_map(
            self.do_rpcrequest('ModifyBackupPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceConnectionStringResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceConnectionString', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceConnectionStringResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceConnectionString', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceDescription', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceDescription', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceMaintainTimeResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceMaintainTime', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceMaintainTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceMaintainTime', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_monitor_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceMonitorResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceMonitor', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_monitor_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceMonitorResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceMonitor', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_monitor(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    async def modify_dbinstance_monitor_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_monitor_with_options_async(request, runtime)

    def modify_dbinstance_net_expire_time_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceNetExpireTime', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_net_expire_time_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceNetExpireTime', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_net_expire_time(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_net_expire_time_with_options(request, runtime)

    async def modify_dbinstance_net_expire_time_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_net_expire_time_with_options_async(request, runtime)

    def modify_dbinstance_network_type_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceNetworkTypeResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceNetworkType', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceNetworkTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceNetworkType', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_network_type(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    async def modify_dbinstance_network_type_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_network_type_with_options_async(request, runtime)

    def modify_dbinstance_spec_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceSpec', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_spec_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceSpec', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_spec(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    async def modify_dbinstance_spec_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_spec_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceSSLResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceSSL', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceSSLResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceSSL', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_ssl(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    async def modify_dbinstance_ssl_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_sslwith_options_async(request, runtime)

    def modify_dbinstance_tdewith_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceTDEResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceTDE', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_tdewith_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyDBInstanceTDEResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceTDE', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_tde(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    async def modify_dbinstance_tde_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_tdewith_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoRenewalAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAutoRenewalAttribute', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyInstanceVpcAuthModeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceVpcAuthMode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_vpc_auth_mode_with_options_async(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyInstanceVpcAuthModeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceVpcAuthMode', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vpc_auth_mode(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    async def modify_instance_vpc_auth_mode_async(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_auth_mode_with_options_async(request, runtime)

    def modify_node_spec_with_options(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyNodeSpecResponse().from_map(
            self.do_rpcrequest('ModifyNodeSpec', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_node_spec_with_options_async(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyNodeSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyNodeSpec', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_node_spec(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_node_spec_with_options(request, runtime)

    async def modify_node_spec_async(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_node_spec_with_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyParametersResponse().from_map(
            self.do_rpcrequest('ModifyParameters', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_parameters_with_options_async(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifyParametersResponse().from_map(
            await self.do_rpcrequest_async('ModifyParameters', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameters(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
    ) -> dds_20151201_models.ModifyParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
    ) -> dds_20151201_models.ModifyParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifySecurityGroupConfigurationResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupConfiguration', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifySecurityGroupConfigurationResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupConfiguration', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifySecurityIpsResponse().from_map(
            self.do_rpcrequest('ModifySecurityIps', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ModifySecurityIpsResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityIps', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def release_node_private_network_address_with_options(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse().from_map(
            self.do_rpcrequest('ReleaseNodePrivateNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_node_private_network_address_with_options_async(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleaseNodePrivateNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_node_private_network_address(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_node_private_network_address_with_options(request, runtime)

    async def release_node_private_network_address_async(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_node_private_network_address_with_options_async(request, runtime)

    def release_public_network_address_with_options(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ReleasePublicNetworkAddressResponse().from_map(
            self.do_rpcrequest('ReleasePublicNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_public_network_address_with_options_async(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ReleasePublicNetworkAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleasePublicNetworkAddress', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_public_network_address(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_public_network_address_with_options(request, runtime)

    async def release_public_network_address_async(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_public_network_address_with_options_async(request, runtime)

    def renew_dbinstance_with_options(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.RenewDBInstanceResponse().from_map(
            self.do_rpcrequest('RenewDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.RenewDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_dbinstance(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_dbinstance_with_options(request, runtime)

    async def renew_dbinstance_async(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_dbinstance_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ResetAccountPasswordResponse().from_map(
            self.do_rpcrequest('ResetAccountPassword', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.ResetAccountPasswordResponse().from_map(
            await self.do_rpcrequest_async('ResetAccountPassword', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.RestartDBInstanceResponse().from_map(
            self.do_rpcrequest('RestartDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.RestartDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('RestartDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def restore_dbinstance_with_options(
        self,
        request: dds_20151201_models.RestoreDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestoreDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.RestoreDBInstanceResponse().from_map(
            self.do_rpcrequest('RestoreDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.RestoreDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestoreDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.RestoreDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('RestoreDBInstance', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_dbinstance(
        self,
        request: dds_20151201_models.RestoreDBInstanceRequest,
    ) -> dds_20151201_models.RestoreDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_dbinstance_with_options(request, runtime)

    async def restore_dbinstance_async(
        self,
        request: dds_20151201_models.RestoreDBInstanceRequest,
    ) -> dds_20151201_models.RestoreDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_dbinstance_with_options_async(request, runtime)

    def switch_dbinstance_hawith_options(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.SwitchDBInstanceHAResponse().from_map(
            self.do_rpcrequest('SwitchDBInstanceHA', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_dbinstance_hawith_options_async(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.SwitchDBInstanceHAResponse().from_map(
            await self.do_rpcrequest_async('SwitchDBInstanceHA', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_ha(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    async def switch_dbinstance_ha_async(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_hawith_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dds_20151201_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: dds_20151201_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: dds_20151201_models.TagResourcesRequest,
    ) -> dds_20151201_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dds_20151201_models.TagResourcesRequest,
    ) -> dds_20151201_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transform_to_pre_paid_with_options(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.TransformToPrePaidResponse().from_map(
            self.do_rpcrequest('TransformToPrePaid', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transform_to_pre_paid_with_options_async(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.TransformToPrePaidResponse().from_map(
            await self.do_rpcrequest_async('TransformToPrePaid', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transform_to_pre_paid(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    async def transform_to_pre_paid_async(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_to_pre_paid_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
    ) -> dds_20151201_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
    ) -> dds_20151201_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.UpgradeDBInstanceEngineVersionResponse().from_map(
            self.do_rpcrequest('UpgradeDBInstanceEngineVersion', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbinstance_engine_version_with_options_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.UpgradeDBInstanceEngineVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeDBInstanceEngineVersion', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_engine_version(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    async def upgrade_dbinstance_engine_version_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_engine_version_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.UpgradeDBInstanceKernelVersionResponse().from_map(
            self.do_rpcrequest('UpgradeDBInstanceKernelVersion', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dds_20151201_models.UpgradeDBInstanceKernelVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeDBInstanceKernelVersion', '2015-12-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)
