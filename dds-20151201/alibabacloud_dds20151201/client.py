# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dds20151201 import models as dds_20151201_models
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
            'cn-qingdao': 'mongodb.aliyuncs.com',
            'cn-beijing': 'mongodb.aliyuncs.com',
            'cn-zhangjiakou': 'mongodb.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'mongodb.cn-huhehaote.aliyuncs.com',
            'cn-wulanchabu': 'mongodb.aliyuncs.com',
            'cn-hangzhou': 'mongodb.aliyuncs.com',
            'cn-shanghai': 'mongodb.aliyuncs.com',
            'cn-shenzhen': 'mongodb.aliyuncs.com',
            'cn-heyuan': 'mongodb.aliyuncs.com',
            'cn-guangzhou': 'mongodb.aliyuncs.com',
            'cn-chengdu': 'mongodb.cn-chengdu.aliyuncs.com',
            'cn-hongkong': 'mongodb.cn-hongkong.aliyuncs.com',
            'ap-northeast-1': 'mongodb.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'mongodb.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'mongodb.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'mongodb.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'mongodb.ap-southeast-5.aliyuncs.com',
            'us-east-1': 'mongodb.us-east-1.aliyuncs.com',
            'us-west-1': 'mongodb.us-west-1.aliyuncs.com',
            'eu-west-1': 'mongodb.eu-west-1.aliyuncs.com',
            'eu-central-1': 'mongodb.eu-central-1.aliyuncs.com',
            'ap-south-1': 'mongodb.ap-south-1.aliyuncs.com',
            'me-east-1': 'mongodb.me-east-1.aliyuncs.com',
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
            'cn-yushanfang': 'mongodb.aliyuncs.com',
            'cn-zhangbei': 'mongodb.aliyuncs.com',
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
        """
        @summary Applies for an internal endpoint for a shard or Configserver node in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances. For more information, see [Apply for an endpoint for a shard or Configserver node](https://help.aliyun.com/document_detail/134037.html).
        >  The allocated endpoints can be used only for internal access. To gain Internet access, you must call the [AllocatePublicNetworkAddress](https://help.aliyun.com/document_detail/67602.html) operation to apply for public endpoints.
        
        @param request: AllocateNodePrivateNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateNodePrivateNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateNodePrivateNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.AllocateNodePrivateNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_node_private_network_address_with_options_async(
        self,
        request: dds_20151201_models.AllocateNodePrivateNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.AllocateNodePrivateNetworkAddressResponse:
        """
        @summary Applies for an internal endpoint for a shard or Configserver node in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances. For more information, see [Apply for an endpoint for a shard or Configserver node](https://help.aliyun.com/document_detail/134037.html).
        >  The allocated endpoints can be used only for internal access. To gain Internet access, you must call the [AllocatePublicNetworkAddress](https://help.aliyun.com/document_detail/67602.html) operation to apply for public endpoints.
        
        @param request: AllocateNodePrivateNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateNodePrivateNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateNodePrivateNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.AllocateNodePrivateNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_node_private_network_address(
        self,
        request: dds_20151201_models.AllocateNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.AllocateNodePrivateNetworkAddressResponse:
        """
        @summary Applies for an internal endpoint for a shard or Configserver node in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances. For more information, see [Apply for an endpoint for a shard or Configserver node](https://help.aliyun.com/document_detail/134037.html).
        >  The allocated endpoints can be used only for internal access. To gain Internet access, you must call the [AllocatePublicNetworkAddress](https://help.aliyun.com/document_detail/67602.html) operation to apply for public endpoints.
        
        @param request: AllocateNodePrivateNetworkAddressRequest
        @return: AllocateNodePrivateNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_node_private_network_address_with_options(request, runtime)

    async def allocate_node_private_network_address_async(
        self,
        request: dds_20151201_models.AllocateNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.AllocateNodePrivateNetworkAddressResponse:
        """
        @summary Applies for an internal endpoint for a shard or Configserver node in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances. For more information, see [Apply for an endpoint for a shard or Configserver node](https://help.aliyun.com/document_detail/134037.html).
        >  The allocated endpoints can be used only for internal access. To gain Internet access, you must call the [AllocatePublicNetworkAddress](https://help.aliyun.com/document_detail/67602.html) operation to apply for public endpoints.
        
        @param request: AllocateNodePrivateNetworkAddressRequest
        @return: AllocateNodePrivateNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_node_private_network_address_with_options_async(request, runtime)

    def allocate_public_network_address_with_options(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        """
        @summary Allocates a public endpoint to an instance.
        
        @param request: AllocatePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocatePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.AllocatePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_public_network_address_with_options_async(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        """
        @summary Allocates a public endpoint to an instance.
        
        @param request: AllocatePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocatePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.AllocatePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_public_network_address(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        """
        @summary Allocates a public endpoint to an instance.
        
        @param request: AllocatePublicNetworkAddressRequest
        @return: AllocatePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_network_address_with_options(request, runtime)

    async def allocate_public_network_address_async(
        self,
        request: dds_20151201_models.AllocatePublicNetworkAddressRequest,
    ) -> dds_20151201_models.AllocatePublicNetworkAddressResponse:
        """
        @summary Allocates a public endpoint to an instance.
        
        @param request: AllocatePublicNetworkAddressRequest
        @return: AllocatePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_network_address_with_options_async(request, runtime)

    def check_cloud_resource_authorized_with_options(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary You can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @description Before you enable Transparent Data Encryption (TDE) by calling the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation, you can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCloudResourceAuthorizedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary You can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @description Before you enable Transparent Data Encryption (TDE) by calling the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation, you can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCloudResourceAuthorizedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CheckCloudResourceAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary You can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @description Before you enable Transparent Data Encryption (TDE) by calling the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation, you can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @return: CheckCloudResourceAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: dds_20151201_models.CheckCloudResourceAuthorizedRequest,
    ) -> dds_20151201_models.CheckCloudResourceAuthorizedResponse:
        """
        @summary You can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @description Before you enable Transparent Data Encryption (TDE) by calling the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation, you can call this operation to check whether KMS keys are authorized to ApsaraDB for MongoDB instances.
        
        @param request: CheckCloudResourceAuthorizedRequest
        @return: CheckCloudResourceAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def check_recovery_condition_with_options(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        """
        @summary Queries whether the data of an ApsaraDB for MongoDB instance can be restored.
        
        @description This operation is applicable to replica set instances and sharded cluster instances.
        >  After you call this operation to confirm that the data of the instance can be restored, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore data to a new instance.
        
        @param request: CheckRecoveryConditionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRecoveryConditionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRecoveryCondition',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CheckRecoveryConditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_recovery_condition_with_options_async(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        """
        @summary Queries whether the data of an ApsaraDB for MongoDB instance can be restored.
        
        @description This operation is applicable to replica set instances and sharded cluster instances.
        >  After you call this operation to confirm that the data of the instance can be restored, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore data to a new instance.
        
        @param request: CheckRecoveryConditionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRecoveryConditionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRecoveryCondition',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CheckRecoveryConditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_recovery_condition(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        """
        @summary Queries whether the data of an ApsaraDB for MongoDB instance can be restored.
        
        @description This operation is applicable to replica set instances and sharded cluster instances.
        >  After you call this operation to confirm that the data of the instance can be restored, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore data to a new instance.
        
        @param request: CheckRecoveryConditionRequest
        @return: CheckRecoveryConditionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_recovery_condition_with_options(request, runtime)

    async def check_recovery_condition_async(
        self,
        request: dds_20151201_models.CheckRecoveryConditionRequest,
    ) -> dds_20151201_models.CheckRecoveryConditionResponse:
        """
        @summary Queries whether the data of an ApsaraDB for MongoDB instance can be restored.
        
        @description This operation is applicable to replica set instances and sharded cluster instances.
        >  After you call this operation to confirm that the data of the instance can be restored, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore data to a new instance.
        
        @param request: CheckRecoveryConditionRequest
        @return: CheckRecoveryConditionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_recovery_condition_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: dds_20151201_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateAccountResponse:
        """
        @summary Creates an account that is granted read-only permissions for shard nodes in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    You can create an account for shard nodes only in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        The account is granted read-only permissions.
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: dds_20151201_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateAccountResponse:
        """
        @summary Creates an account that is granted read-only permissions for shard nodes in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    You can create an account for shard nodes only in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        The account is granted read-only permissions.
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: dds_20151201_models.CreateAccountRequest,
    ) -> dds_20151201_models.CreateAccountResponse:
        """
        @summary Creates an account that is granted read-only permissions for shard nodes in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    You can create an account for shard nodes only in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        The account is granted read-only permissions.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: dds_20151201_models.CreateAccountRequest,
    ) -> dds_20151201_models.CreateAccountResponse:
        """
        @summary Creates an account that is granted read-only permissions for shard nodes in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    You can create an account for shard nodes only in an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        The account is granted read-only permissions.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: dds_20151201_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateBackupResponse:
        """
        @summary Creates a backup set for an ApsaraDB for MongoDB instance.
        
        @description When you call this operation, the instance must be in the Running state.
        
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: dds_20151201_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateBackupResponse:
        """
        @summary Creates a backup set for an ApsaraDB for MongoDB instance.
        
        @description When you call this operation, the instance must be in the Running state.
        
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: dds_20151201_models.CreateBackupRequest,
    ) -> dds_20151201_models.CreateBackupResponse:
        """
        @summary Creates a backup set for an ApsaraDB for MongoDB instance.
        
        @description When you call this operation, the instance must be in the Running state.
        
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: dds_20151201_models.CreateBackupRequest,
    ) -> dds_20151201_models.CreateBackupResponse:
        """
        @summary Creates a backup set for an ApsaraDB for MongoDB instance.
        
        @description When you call this operation, the instance must be in the Running state.
        
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB replica set instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB instances, see [Instance types](https://www.alibabacloud.com/help/en/mongodb/product-overview/instance-types-1).
        To create sharded cluster instances, you can call the [CreateShardingDBInstance](~~CreateShardingDBInstance~~) operation.
        
        @param request: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB replica set instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB instances, see [Instance types](https://www.alibabacloud.com/help/en/mongodb/product-overview/instance-types-1).
        To create sharded cluster instances, you can call the [CreateShardingDBInstance](~~CreateShardingDBInstance~~) operation.
        
        @param request: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB replica set instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB instances, see [Instance types](https://www.alibabacloud.com/help/en/mongodb/product-overview/instance-types-1).
        To create sharded cluster instances, you can call the [CreateShardingDBInstance](~~CreateShardingDBInstance~~) operation.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: dds_20151201_models.CreateDBInstanceRequest,
    ) -> dds_20151201_models.CreateDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB replica set instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB instances, see [Instance types](https://www.alibabacloud.com/help/en/mongodb/product-overview/instance-types-1).
        To create sharded cluster instances, you can call the [CreateShardingDBInstance](~~CreateShardingDBInstance~~) operation.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_global_security_ipgroup_with_options(
        self,
        request: dds_20151201_models.CreateGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_security_ipgroup_with_options_async(
        self,
        request: dds_20151201_models.CreateGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_security_ipgroup(
        self,
        request: dds_20151201_models.CreateGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @return: CreateGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_global_security_ipgroup_with_options(request, runtime)

    async def create_global_security_ipgroup_async(
        self,
        request: dds_20151201_models.CreateGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @return: CreateGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_global_security_ipgroup_with_options_async(request, runtime)

    def create_node_with_options(
        self,
        request: dds_20151201_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateNodeResponse:
        """
        @summary Adds a shard or mongos node to an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to sharded cluster instances.
        
        @param request: CreateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_class):
            query['NodeClass'] = request.node_class
        if not UtilClient.is_unset(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_with_options_async(
        self,
        request: dds_20151201_models.CreateNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateNodeResponse:
        """
        @summary Adds a shard or mongos node to an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to sharded cluster instances.
        
        @param request: CreateNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_class):
            query['NodeClass'] = request.node_class
        if not UtilClient.is_unset(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node(
        self,
        request: dds_20151201_models.CreateNodeRequest,
    ) -> dds_20151201_models.CreateNodeResponse:
        """
        @summary Adds a shard or mongos node to an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to sharded cluster instances.
        
        @param request: CreateNodeRequest
        @return: CreateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_with_options(request, runtime)

    async def create_node_async(
        self,
        request: dds_20151201_models.CreateNodeRequest,
    ) -> dds_20151201_models.CreateNodeResponse:
        """
        @summary Adds a shard or mongos node to an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to sharded cluster instances.
        
        @param request: CreateNodeRequest
        @return: CreateNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_node_with_options_async(request, runtime)

    def create_node_batch_with_options(
        self,
        request: dds_20151201_models.CreateNodeBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateNodeBatchResponse:
        """
        @summary Batch adds mongos or shard nodes for a sharded cluster instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation is applicable only to sharded cluster instances.
        
        @param request: CreateNodeBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodeBatch',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateNodeBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_batch_with_options_async(
        self,
        request: dds_20151201_models.CreateNodeBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateNodeBatchResponse:
        """
        @summary Batch adds mongos or shard nodes for a sharded cluster instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation is applicable only to sharded cluster instances.
        
        @param request: CreateNodeBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodeBatch',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateNodeBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_batch(
        self,
        request: dds_20151201_models.CreateNodeBatchRequest,
    ) -> dds_20151201_models.CreateNodeBatchResponse:
        """
        @summary Batch adds mongos or shard nodes for a sharded cluster instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation is applicable only to sharded cluster instances.
        
        @param request: CreateNodeBatchRequest
        @return: CreateNodeBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_batch_with_options(request, runtime)

    async def create_node_batch_async(
        self,
        request: dds_20151201_models.CreateNodeBatchRequest,
    ) -> dds_20151201_models.CreateNodeBatchResponse:
        """
        @summary Batch adds mongos or shard nodes for a sharded cluster instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation is applicable only to sharded cluster instances.
        
        @param request: CreateNodeBatchRequest
        @return: CreateNodeBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_node_batch_with_options_async(request, runtime)

    def create_sharding_dbinstance_with_options(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB sharded cluster instance.
        
        @description    Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        To create standalone instances and replica set instances, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation.
        
        @param request: CreateShardingDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShardingDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_server):
            query['ConfigServer'] = request.config_server
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not UtilClient.is_unset(request.mongos):
            query['Mongos'] = request.mongos
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_set):
            query['ReplicaSet'] = request.replica_set
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateShardingDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateShardingDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sharding_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB sharded cluster instance.
        
        @description    Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        To create standalone instances and replica set instances, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation.
        
        @param request: CreateShardingDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShardingDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_server):
            query['ConfigServer'] = request.config_server
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not UtilClient.is_unset(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not UtilClient.is_unset(request.mongos):
            query['Mongos'] = request.mongos
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_set):
            query['ReplicaSet'] = request.replica_set
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateShardingDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.CreateShardingDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sharding_dbinstance(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB sharded cluster instance.
        
        @description    Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        To create standalone instances and replica set instances, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation.
        
        @param request: CreateShardingDBInstanceRequest
        @return: CreateShardingDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sharding_dbinstance_with_options(request, runtime)

    async def create_sharding_dbinstance_async(
        self,
        request: dds_20151201_models.CreateShardingDBInstanceRequest,
    ) -> dds_20151201_models.CreateShardingDBInstanceResponse:
        """
        @summary Creates or clones an ApsaraDB for MongoDB sharded cluster instance.
        
        @description    Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        For more information about the instance types of ApsaraDB for MongoDB, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        To create standalone instances and replica set instances, you can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation.
        
        @param request: CreateShardingDBInstanceRequest
        @return: CreateShardingDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sharding_dbinstance_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements
        The instance is in the Running state.
        The billing method of the instance is pay-as-you-go.
        > After an instance is released, all data in the instance is cleared and cannot be recovered. Proceed with caution.
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements
        The instance is in the Running state.
        The billing method of the instance is pay-as-you-go.
        > After an instance is released, all data in the instance is cleared and cannot be recovered. Proceed with caution.
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements
        The instance is in the Running state.
        The billing method of the instance is pay-as-you-go.
        > After an instance is released, all data in the instance is cleared and cannot be recovered. Proceed with caution.
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: dds_20151201_models.DeleteDBInstanceRequest,
    ) -> dds_20151201_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements
        The instance is in the Running state.
        The billing method of the instance is pay-as-you-go.
        > After an instance is released, all data in the instance is cleared and cannot be recovered. Proceed with caution.
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_global_security_ipgroup_with_options(
        self,
        request: dds_20151201_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_security_ipgroup_with_options_async(
        self,
        request: dds_20151201_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_security_ipgroup(
        self,
        request: dds_20151201_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_global_security_ipgroup_with_options(request, runtime)

    async def delete_global_security_ipgroup_async(
        self,
        request: dds_20151201_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_security_ipgroup_with_options_async(request, runtime)

    def delete_node_with_options(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteNodeResponse:
        """
        @summary Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The instance is a sharded cluster instance.
        The billing method of the instance is pay-as-you-go.
        The number of the shard or mongos nodes in the instance is greater than two.
        
        @param request: DeleteNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_with_options_async(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DeleteNodeResponse:
        """
        @summary Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The instance is a sharded cluster instance.
        The billing method of the instance is pay-as-you-go.
        The number of the shard or mongos nodes in the instance is greater than two.
        
        @param request: DeleteNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DeleteNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
    ) -> dds_20151201_models.DeleteNodeResponse:
        """
        @summary Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The instance is a sharded cluster instance.
        The billing method of the instance is pay-as-you-go.
        The number of the shard or mongos nodes in the instance is greater than two.
        
        @param request: DeleteNodeRequest
        @return: DeleteNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    async def delete_node_async(
        self,
        request: dds_20151201_models.DeleteNodeRequest,
    ) -> dds_20151201_models.DeleteNodeResponse:
        """
        @summary Deletes a shard or mongos node from an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The instance is a sharded cluster instance.
        The billing method of the instance is pay-as-you-go.
        The number of the shard or mongos nodes in the instance is greater than two.
        
        @param request: DeleteNodeRequest
        @return: DeleteNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_node_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to query only the information of the root account.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to query only the information of the root account.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to query only the information of the root account.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: dds_20151201_models.DescribeAccountsRequest,
    ) -> dds_20151201_models.DescribeAccountsResponse:
        """
        @summary Queries the database accounts of an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to query only the information of the root account.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_task_count_with_options(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary Queries the number of operation and maintenance tasks on an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTaskCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTaskCount',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTaskCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_count_with_options_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary Queries the number of operation and maintenance tasks on an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTaskCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTaskCount',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTaskCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task_count(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary Queries the number of operation and maintenance tasks on an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTaskCountRequest
        @return: DescribeActiveOperationTaskCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_count_with_options(request, runtime)

    async def describe_active_operation_task_count_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskCountRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskCountResponse:
        """
        @summary Queries the number of operation and maintenance tasks on an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTaskCountRequest
        @return: DescribeActiveOperationTaskCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_count_with_options_async(request, runtime)

    def describe_active_operation_task_type_with_options(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        """
        @summary Queries the types of Operation and Maintenance tasks and the number of tasks of each type for an ApsaraDB for MongoDB instance.
        
        @description This operation is no longer updated and will be unavailable.
        
        @param request: DescribeActiveOperationTaskTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTaskType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTaskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_type_with_options_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        """
        @summary Queries the types of Operation and Maintenance tasks and the number of tasks of each type for an ApsaraDB for MongoDB instance.
        
        @description This operation is no longer updated and will be unavailable.
        
        @param request: DescribeActiveOperationTaskTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTaskTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTaskType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTaskTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task_type(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        """
        @summary Queries the types of Operation and Maintenance tasks and the number of tasks of each type for an ApsaraDB for MongoDB instance.
        
        @description This operation is no longer updated and will be unavailable.
        
        @param request: DescribeActiveOperationTaskTypeRequest
        @return: DescribeActiveOperationTaskTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_type_with_options(request, runtime)

    async def describe_active_operation_task_type_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTaskTypeRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTaskTypeResponse:
        """
        @summary Queries the types of Operation and Maintenance tasks and the number of tasks of each type for an ApsaraDB for MongoDB instance.
        
        @description This operation is no longer updated and will be unavailable.
        
        @param request: DescribeActiveOperationTaskTypeRequest
        @return: DescribeActiveOperationTaskTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_type_with_options_async(request, runtime)

    def describe_active_operation_tasks_with_options(
        self,
        request: dds_20151201_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries a list of operation and maintenance tasks initiated for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not UtilClient.is_unset(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not UtilClient.is_unset(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_tasks_with_options_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries a list of operation and maintenance tasks initiated for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not UtilClient.is_unset(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not UtilClient.is_unset(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_tasks(
        self,
        request: dds_20151201_models.DescribeActiveOperationTasksRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries a list of operation and maintenance tasks initiated for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_tasks_with_options(request, runtime)

    async def describe_active_operation_tasks_async(
        self,
        request: dds_20151201_models.DescribeActiveOperationTasksRequest,
    ) -> dds_20151201_models.DescribeActiveOperationTasksResponse:
        """
        @summary Queries a list of operation and maintenance tasks initiated for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeActiveOperationTasksRequest
        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_tasks_with_options_async(request, runtime)

    def describe_audit_log_filter_with_options(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        """
        @summary Queries the types of entries in the audit log collected for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditLogFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogFilter',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditLogFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_filter_with_options_async(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        """
        @summary Queries the types of entries in the audit log collected for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditLogFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditLogFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogFilter',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditLogFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_filter(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        """
        @summary Queries the types of entries in the audit log collected for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditLogFilterRequest
        @return: DescribeAuditLogFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_filter_with_options(request, runtime)

    async def describe_audit_log_filter_async(
        self,
        request: dds_20151201_models.DescribeAuditLogFilterRequest,
    ) -> dds_20151201_models.DescribeAuditLogFilterResponse:
        """
        @summary Queries the types of entries in the audit log collected for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditLogFilterRequest
        @return: DescribeAuditLogFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_filter_with_options_async(request, runtime)

    def describe_audit_policy_with_options(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        """
        @summary Queries whether the audit log feature is enabled for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_policy_with_options_async(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        """
        @summary Queries whether the audit log feature is enabled for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_policy(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        """
        @summary Queries whether the audit log feature is enabled for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditPolicyRequest
        @return: DescribeAuditPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_policy_with_options(request, runtime)

    async def describe_audit_policy_async(
        self,
        request: dds_20151201_models.DescribeAuditPolicyRequest,
    ) -> dds_20151201_models.DescribeAuditPolicyResponse:
        """
        @summary Queries whether the audit log feature is enabled for an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditPolicyRequest
        @return: DescribeAuditPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_policy_with_options_async(request, runtime)

    def describe_audit_records_with_options(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for MongoDB instance.
        
        @description    When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for MongoDB instance.
        
        @description    When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAuditRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAuditRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_records(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for MongoDB instance.
        
        @description    When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditRecordsRequest
        @return: DescribeAuditRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    async def describe_audit_records_async(
        self,
        request: dds_20151201_models.DescribeAuditRecordsRequest,
    ) -> dds_20151201_models.DescribeAuditRecordsResponse:
        """
        @summary Queries the audit logs of an ApsaraDB for MongoDB instance.
        
        @description    When you call this operation, ensure that the audit log feature of the instance is enabled. Otherwise, the operation returns an empty audit log.
        This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeAuditRecordsRequest
        @return: DescribeAuditRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_records_with_options_async(request, runtime)

    def describe_availability_zones_with_options(
        self,
        request: dds_20151201_models.DescribeAvailabilityZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailabilityZonesResponse:
        """
        @summary Queries a list of the zones that are supported by an ApsaraDB for MongoDB instance.
        
        @description Queries the zones in which an ApsaraDB for MongoDB instance can be deployed under specified purchase conditions. The region ID is required in the purchase condition.
        
        @param request: DescribeAvailabilityZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailabilityZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.exclude_secondary_zone_id):
            query['ExcludeSecondaryZoneId'] = request.exclude_secondary_zone_id
        if not UtilClient.is_unset(request.exclude_zone_id):
            query['ExcludeZoneId'] = request.exclude_zone_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.mongo_type):
            query['MongoType'] = request.mongo_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_support):
            query['StorageSupport'] = request.storage_support
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailabilityZones',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailabilityZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_availability_zones_with_options_async(
        self,
        request: dds_20151201_models.DescribeAvailabilityZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailabilityZonesResponse:
        """
        @summary Queries a list of the zones that are supported by an ApsaraDB for MongoDB instance.
        
        @description Queries the zones in which an ApsaraDB for MongoDB instance can be deployed under specified purchase conditions. The region ID is required in the purchase condition.
        
        @param request: DescribeAvailabilityZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailabilityZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.exclude_secondary_zone_id):
            query['ExcludeSecondaryZoneId'] = request.exclude_secondary_zone_id
        if not UtilClient.is_unset(request.exclude_zone_id):
            query['ExcludeZoneId'] = request.exclude_zone_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.mongo_type):
            query['MongoType'] = request.mongo_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_support):
            query['StorageSupport'] = request.storage_support
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailabilityZones',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailabilityZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_availability_zones(
        self,
        request: dds_20151201_models.DescribeAvailabilityZonesRequest,
    ) -> dds_20151201_models.DescribeAvailabilityZonesResponse:
        """
        @summary Queries a list of the zones that are supported by an ApsaraDB for MongoDB instance.
        
        @description Queries the zones in which an ApsaraDB for MongoDB instance can be deployed under specified purchase conditions. The region ID is required in the purchase condition.
        
        @param request: DescribeAvailabilityZonesRequest
        @return: DescribeAvailabilityZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_availability_zones_with_options(request, runtime)

    async def describe_availability_zones_async(
        self,
        request: dds_20151201_models.DescribeAvailabilityZonesRequest,
    ) -> dds_20151201_models.DescribeAvailabilityZonesResponse:
        """
        @summary Queries a list of the zones that are supported by an ApsaraDB for MongoDB instance.
        
        @description Queries the zones in which an ApsaraDB for MongoDB instance can be deployed under specified purchase conditions. The region ID is required in the purchase condition.
        
        @param request: DescribeAvailabilityZonesRequest
        @return: DescribeAvailabilityZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_availability_zones_with_options_async(request, runtime)

    def describe_available_engine_version_with_options(
        self,
        request: dds_20151201_models.DescribeAvailableEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableEngineVersionResponse:
        """
        @summary You can call this operation to query the engine versions to which an ApsaraDB for MongoDB instance can be upgraded.
        
        @param request: DescribeAvailableEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableEngineVersion',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailableEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_engine_version_with_options_async(
        self,
        request: dds_20151201_models.DescribeAvailableEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableEngineVersionResponse:
        """
        @summary You can call this operation to query the engine versions to which an ApsaraDB for MongoDB instance can be upgraded.
        
        @param request: DescribeAvailableEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableEngineVersion',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailableEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_engine_version(
        self,
        request: dds_20151201_models.DescribeAvailableEngineVersionRequest,
    ) -> dds_20151201_models.DescribeAvailableEngineVersionResponse:
        """
        @summary You can call this operation to query the engine versions to which an ApsaraDB for MongoDB instance can be upgraded.
        
        @param request: DescribeAvailableEngineVersionRequest
        @return: DescribeAvailableEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_engine_version_with_options(request, runtime)

    async def describe_available_engine_version_async(
        self,
        request: dds_20151201_models.DescribeAvailableEngineVersionRequest,
    ) -> dds_20151201_models.DescribeAvailableEngineVersionResponse:
        """
        @summary You can call this operation to query the engine versions to which an ApsaraDB for MongoDB instance can be upgraded.
        
        @param request: DescribeAvailableEngineVersionRequest
        @return: DescribeAvailableEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_engine_version_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the available resources in the specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the available resources in the specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the available resources in the specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: dds_20151201_models.DescribeAvailableResourceRequest,
    ) -> dds_20151201_models.DescribeAvailableResourceResponse:
        """
        @summary Queries the available resources in the specified zone.
        
        @param request: DescribeAvailableResourceRequest
        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_dbs_with_options(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        """
        @summary Queries the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance.
        
        @description You can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore a database for an ApsaraDB for MongoDB instance. For more information, see [Restore one database of an ApsaraDB for MongoDB instance](https://help.aliyun.com/document_detail/112274.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance was created after March 26, 2019.
        The instance is located in the China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Hangzhou), China (Shanghai), China (Shenzhen), or Singapore region. Other regions are not supported.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4, MongoDB 4.0, or MongoDB 4.2. In addition, the instance uses local disks to store data.
        The storage engine of the instance is WiredTiger.
        
        @param request: DescribeBackupDBsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupDBsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupDBs',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupDBsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_dbs_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        """
        @summary Queries the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance.
        
        @description You can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore a database for an ApsaraDB for MongoDB instance. For more information, see [Restore one database of an ApsaraDB for MongoDB instance](https://help.aliyun.com/document_detail/112274.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance was created after March 26, 2019.
        The instance is located in the China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Hangzhou), China (Shanghai), China (Shenzhen), or Singapore region. Other regions are not supported.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4, MongoDB 4.0, or MongoDB 4.2. In addition, the instance uses local disks to store data.
        The storage engine of the instance is WiredTiger.
        
        @param request: DescribeBackupDBsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupDBsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not UtilClient.is_unset(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupDBs',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupDBsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_dbs(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        """
        @summary Queries the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance.
        
        @description You can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore a database for an ApsaraDB for MongoDB instance. For more information, see [Restore one database of an ApsaraDB for MongoDB instance](https://help.aliyun.com/document_detail/112274.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance was created after March 26, 2019.
        The instance is located in the China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Hangzhou), China (Shanghai), China (Shenzhen), or Singapore region. Other regions are not supported.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4, MongoDB 4.0, or MongoDB 4.2. In addition, the instance uses local disks to store data.
        The storage engine of the instance is WiredTiger.
        
        @param request: DescribeBackupDBsRequest
        @return: DescribeBackupDBsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    async def describe_backup_dbs_async(
        self,
        request: dds_20151201_models.DescribeBackupDBsRequest,
    ) -> dds_20151201_models.DescribeBackupDBsResponse:
        """
        @summary Queries the databases at a specified time or the databases in a specified backup set before you restore a database for an ApsaraDB for MongoDB instance.
        
        @description You can call the [CreateDBInstance](https://help.aliyun.com/document_detail/61763.html) operation to restore a database for an ApsaraDB for MongoDB instance. For more information, see [Restore one database of an ApsaraDB for MongoDB instance](https://help.aliyun.com/document_detail/112274.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance was created after March 26, 2019.
        The instance is located in the China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Hangzhou), China (Shanghai), China (Shenzhen), or Singapore region. Other regions are not supported.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4, MongoDB 4.0, or MongoDB 4.2. In addition, the instance uses local disks to store data.
        The storage engine of the instance is WiredTiger.
        
        @param request: DescribeBackupDBsRequest
        @return: DescribeBackupDBsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_dbs_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: dds_20151201_models.DescribeBackupPolicyRequest,
    ) -> dds_20151201_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup policy of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_storage_with_options(
        self,
        request: dds_20151201_models.DescribeBackupStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupStorageResponse:
        """
        @summary Queries the storage used for backup in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks. Note that you are charged only for the backup-used storage of each shard in a sharded cluster instance. You can call this operation only to query the storage used by a single shard in the instance for backup.
        
        @param request: DescribeBackupStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupStorageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupStorage',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_storage_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupStorageResponse:
        """
        @summary Queries the storage used for backup in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks. Note that you are charged only for the backup-used storage of each shard in a sharded cluster instance. You can call this operation only to query the storage used by a single shard in the instance for backup.
        
        @param request: DescribeBackupStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupStorageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupStorage',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_storage(
        self,
        request: dds_20151201_models.DescribeBackupStorageRequest,
    ) -> dds_20151201_models.DescribeBackupStorageResponse:
        """
        @summary Queries the storage used for backup in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks. Note that you are charged only for the backup-used storage of each shard in a sharded cluster instance. You can call this operation only to query the storage used by a single shard in the instance for backup.
        
        @param request: DescribeBackupStorageRequest
        @return: DescribeBackupStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_storage_with_options(request, runtime)

    async def describe_backup_storage_async(
        self,
        request: dds_20151201_models.DescribeBackupStorageRequest,
    ) -> dds_20151201_models.DescribeBackupStorageResponse:
        """
        @summary Queries the storage used for backup in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks. Note that you are charged only for the backup-used storage of each shard in a sharded cluster instance. You can call this operation only to query the storage used by a single shard in the instance for backup.
        
        @param request: DescribeBackupStorageRequest
        @return: DescribeBackupStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_storage_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: dds_20151201_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupTasksResponse:
        """
        @summary Queries backup tasks running in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks.
        
        @param request: DescribeBackupTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupTasksResponse:
        """
        @summary Queries backup tasks running in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks.
        
        @param request: DescribeBackupTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: dds_20151201_models.DescribeBackupTasksRequest,
    ) -> dds_20151201_models.DescribeBackupTasksResponse:
        """
        @summary Queries backup tasks running in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks.
        
        @param request: DescribeBackupTasksRequest
        @return: DescribeBackupTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: dds_20151201_models.DescribeBackupTasksRequest,
    ) -> dds_20151201_models.DescribeBackupTasksResponse:
        """
        @summary Queries backup tasks running in an ApsaraDB for MongoDB replica set or sharded cluster instance that uses cloud disks.
        
        @param request: DescribeBackupTasksRequest
        @return: DescribeBackupTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: dds_20151201_models.DescribeBackupsRequest,
    ) -> dds_20151201_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cluster_backups_with_options(
        self,
        request: dds_20151201_models.DescribeClusterBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeClusterBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description For a sharded cluster instance that is created before October 19, 2023 and uses cloud disks, you must call the [TransferClusterBackup](https://help.aliyun.com/document_detail/2587931.html) operation to switch the instance from the shard backup mode to the cluster backup mode before you call the DescribeClusterBackups operation.
        By default, cloud disk-based sharded cluster instances that are created after October 19, 2023 are in the cluster backup mode.
        
        @param request: DescribeClusterBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_only_get_cluster_back_up):
            query['IsOnlyGetClusterBackUp'] = request.is_only_get_cluster_back_up
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterBackups',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeClusterBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_backups_with_options_async(
        self,
        request: dds_20151201_models.DescribeClusterBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeClusterBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description For a sharded cluster instance that is created before October 19, 2023 and uses cloud disks, you must call the [TransferClusterBackup](https://help.aliyun.com/document_detail/2587931.html) operation to switch the instance from the shard backup mode to the cluster backup mode before you call the DescribeClusterBackups operation.
        By default, cloud disk-based sharded cluster instances that are created after October 19, 2023 are in the cluster backup mode.
        
        @param request: DescribeClusterBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_only_get_cluster_back_up):
            query['IsOnlyGetClusterBackUp'] = request.is_only_get_cluster_back_up
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterBackups',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeClusterBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_backups(
        self,
        request: dds_20151201_models.DescribeClusterBackupsRequest,
    ) -> dds_20151201_models.DescribeClusterBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description For a sharded cluster instance that is created before October 19, 2023 and uses cloud disks, you must call the [TransferClusterBackup](https://help.aliyun.com/document_detail/2587931.html) operation to switch the instance from the shard backup mode to the cluster backup mode before you call the DescribeClusterBackups operation.
        By default, cloud disk-based sharded cluster instances that are created after October 19, 2023 are in the cluster backup mode.
        
        @param request: DescribeClusterBackupsRequest
        @return: DescribeClusterBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_backups_with_options(request, runtime)

    async def describe_cluster_backups_async(
        self,
        request: dds_20151201_models.DescribeClusterBackupsRequest,
    ) -> dds_20151201_models.DescribeClusterBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description For a sharded cluster instance that is created before October 19, 2023 and uses cloud disks, you must call the [TransferClusterBackup](https://help.aliyun.com/document_detail/2587931.html) operation to switch the instance from the shard backup mode to the cluster backup mode before you call the DescribeClusterBackups operation.
        By default, cloud disk-based sharded cluster instances that are created after October 19, 2023 are in the cluster backup mode.
        
        @param request: DescribeClusterBackupsRequest
        @return: DescribeClusterBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_backups_with_options_async(request, runtime)

    def describe_cluster_recover_time_with_options(
        self,
        request: dds_20151201_models.DescribeClusterRecoverTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeClusterRecoverTimeResponse:
        """
        @summary Queries the time range to which you can restore the data of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. The DescribeClusterRecoverTime operation is applicable only to instances that are switched to the cluster backup mode or instances that are created on or after October 19, 2023.
        
        @param request: DescribeClusterRecoverTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterRecoverTimeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterRecoverTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeClusterRecoverTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_recover_time_with_options_async(
        self,
        request: dds_20151201_models.DescribeClusterRecoverTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeClusterRecoverTimeResponse:
        """
        @summary Queries the time range to which you can restore the data of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. The DescribeClusterRecoverTime operation is applicable only to instances that are switched to the cluster backup mode or instances that are created on or after October 19, 2023.
        
        @param request: DescribeClusterRecoverTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterRecoverTimeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterRecoverTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeClusterRecoverTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_recover_time(
        self,
        request: dds_20151201_models.DescribeClusterRecoverTimeRequest,
    ) -> dds_20151201_models.DescribeClusterRecoverTimeResponse:
        """
        @summary Queries the time range to which you can restore the data of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. The DescribeClusterRecoverTime operation is applicable only to instances that are switched to the cluster backup mode or instances that are created on or after October 19, 2023.
        
        @param request: DescribeClusterRecoverTimeRequest
        @return: DescribeClusterRecoverTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_recover_time_with_options(request, runtime)

    async def describe_cluster_recover_time_async(
        self,
        request: dds_20151201_models.DescribeClusterRecoverTimeRequest,
    ) -> dds_20151201_models.DescribeClusterRecoverTimeResponse:
        """
        @summary Queries the time range to which you can restore the data of an ApsaraDB for MongoDB sharded cluster instance that uses cloud disks.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. The DescribeClusterRecoverTime operation is applicable only to instances that are switched to the cluster backup mode or instances that are created on or after October 19, 2023.
        
        @param request: DescribeClusterRecoverTimeRequest
        @return: DescribeClusterRecoverTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_recover_time_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.is_delete):
            query['IsDelete'] = request.is_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.is_delete):
            query['IsDelete'] = request.is_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceAttributeRequest,
    ) -> dds_20151201_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_encryption_key_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        """
        @summary Queries the details of a key for an ApsaraDB for MongoDB instance.
        
        @description When you call the DescribeDBInstanceEncryptionKey operation, the instance must have transparent data encryption (TDE) enabled in BYOK mode. You can call the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation to enable TDE.
        
        @param request: DescribeDBInstanceEncryptionKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceEncryptionKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceEncryptionKey',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_encryption_key_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        """
        @summary Queries the details of a key for an ApsaraDB for MongoDB instance.
        
        @description When you call the DescribeDBInstanceEncryptionKey operation, the instance must have transparent data encryption (TDE) enabled in BYOK mode. You can call the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation to enable TDE.
        
        @param request: DescribeDBInstanceEncryptionKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceEncryptionKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceEncryptionKey',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_encryption_key(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        """
        @summary Queries the details of a key for an ApsaraDB for MongoDB instance.
        
        @description When you call the DescribeDBInstanceEncryptionKey operation, the instance must have transparent data encryption (TDE) enabled in BYOK mode. You can call the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation to enable TDE.
        
        @param request: DescribeDBInstanceEncryptionKeyRequest
        @return: DescribeDBInstanceEncryptionKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_encryption_key_with_options(request, runtime)

    async def describe_dbinstance_encryption_key_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> dds_20151201_models.DescribeDBInstanceEncryptionKeyResponse:
        """
        @summary Queries the details of a key for an ApsaraDB for MongoDB instance.
        
        @description When you call the DescribeDBInstanceEncryptionKey operation, the instance must have transparent data encryption (TDE) enabled in BYOK mode. You can call the [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html) operation to enable TDE.
        
        @param request: DescribeDBInstanceEncryptionKeyRequest
        @return: DescribeDBInstanceEncryptionKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_encryption_key_with_options_async(request, runtime)

    def describe_dbinstance_monitor_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        """
        @summary Queries the collection frequency of monitoring data for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceMonitor',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_monitor_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        """
        @summary Queries the collection frequency of monitoring data for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceMonitor',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_monitor(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        """
        @summary Queries the collection frequency of monitoring data for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceMonitorRequest
        @return: DescribeDBInstanceMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    async def describe_dbinstance_monitor_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceMonitorRequest,
    ) -> dds_20151201_models.DescribeDBInstanceMonitorResponse:
        """
        @summary Queries the collection frequency of monitoring data for an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstanceMonitorRequest
        @return: DescribeDBInstanceMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_monitor_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        """
        @summary Queries the performance data of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstancePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replica_set_role):
            query['ReplicaSetRole'] = request.replica_set_role
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        """
        @summary Queries the performance data of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstancePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replica_set_role):
            query['ReplicaSetRole'] = request.replica_set_role
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        """
        @summary Queries the performance data of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstancePerformanceRequest
        @return: DescribeDBInstancePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: dds_20151201_models.DescribeDBInstancePerformanceRequest,
    ) -> dds_20151201_models.DescribeDBInstancePerformanceResponse:
        """
        @summary Queries the performance data of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeDBInstancePerformanceRequest
        @return: DescribeDBInstancePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The instance is in the Running state.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4 or later.
        
        @param request: DescribeDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The instance is in the Running state.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4 or later.
        
        @param request: DescribeDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The instance is in the Running state.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4 or later.
        
        @param request: DescribeDBInstanceSSLRequest
        @return: DescribeDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceSSLRequest,
    ) -> dds_20151201_models.DescribeDBInstanceSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The instance is in the Running state.
        The instance is a replica set instance.
        The instance runs MongoDB 3.4 or later.
        
        @param request: DescribeDBInstanceSSLRequest
        @return: DescribeDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_switch_log_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceSwitchLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceSwitchLogResponse:
        """
        @summary Queries the primary/secondary switching logs of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The instance uses local physical disks to store data.
        
        @param request: DescribeDBInstanceSwitchLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceSwitchLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSwitchLog',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceSwitchLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_switch_log_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceSwitchLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceSwitchLogResponse:
        """
        @summary Queries the primary/secondary switching logs of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The instance uses local physical disks to store data.
        
        @param request: DescribeDBInstanceSwitchLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceSwitchLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSwitchLog',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceSwitchLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_switch_log(
        self,
        request: dds_20151201_models.DescribeDBInstanceSwitchLogRequest,
    ) -> dds_20151201_models.DescribeDBInstanceSwitchLogResponse:
        """
        @summary Queries the primary/secondary switching logs of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The instance uses local physical disks to store data.
        
        @param request: DescribeDBInstanceSwitchLogRequest
        @return: DescribeDBInstanceSwitchLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_switch_log_with_options(request, runtime)

    async def describe_dbinstance_switch_log_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceSwitchLogRequest,
    ) -> dds_20151201_models.DescribeDBInstanceSwitchLogResponse:
        """
        @summary Queries the primary/secondary switching logs of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The instance uses local physical disks to store data.
        
        @param request: DescribeDBInstanceSwitchLogRequest
        @return: DescribeDBInstanceSwitchLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_switch_log_with_options_async(request, runtime)

    def describe_dbinstance_tdeinfo_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        """
        @summary Queries whether Transparent Data Encryption (TDE) is enabled for an ApsaraDB for MongoDB instance.
        
        @description >  For more information about TDE, see [TDE](https://help.aliyun.com/document_detail/131048.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The storage engine of the instance is WiredTiger.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: DescribeDBInstanceTDEInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceTDEInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDEInfo',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceTDEInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_tdeinfo_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        """
        @summary Queries whether Transparent Data Encryption (TDE) is enabled for an ApsaraDB for MongoDB instance.
        
        @description >  For more information about TDE, see [TDE](https://help.aliyun.com/document_detail/131048.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The storage engine of the instance is WiredTiger.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: DescribeDBInstanceTDEInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceTDEInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDEInfo',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstanceTDEInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_tdeinfo(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        """
        @summary Queries whether Transparent Data Encryption (TDE) is enabled for an ApsaraDB for MongoDB instance.
        
        @description >  For more information about TDE, see [TDE](https://help.aliyun.com/document_detail/131048.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The storage engine of the instance is WiredTiger.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: DescribeDBInstanceTDEInfoRequest
        @return: DescribeDBInstanceTDEInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdeinfo_with_options(request, runtime)

    async def describe_dbinstance_tdeinfo_async(
        self,
        request: dds_20151201_models.DescribeDBInstanceTDEInfoRequest,
    ) -> dds_20151201_models.DescribeDBInstanceTDEInfoResponse:
        """
        @summary Queries whether Transparent Data Encryption (TDE) is enabled for an ApsaraDB for MongoDB instance.
        
        @description >  For more information about TDE, see [TDE](https://help.aliyun.com/document_detail/131048.html).
        Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The storage engine of the instance is WiredTiger.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: DescribeDBInstanceTDEInfoRequest
        @return: DescribeDBInstanceTDEInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_tdeinfo_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for MongoDB instances.
        
        @description The list of replica set and standalone instances is displayed when the *DBInstanceType** parameter uses the default value **replicate**. To query a list of sharded cluster instances, you must set the **DBInstanceType** parameter to **sharding**.
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.connection_domain):
            query['ConnectionDomain'] = request.connection_domain
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for MongoDB instances.
        
        @description The list of replica set and standalone instances is displayed when the *DBInstanceType** parameter uses the default value **replicate**. To query a list of sharded cluster instances, you must set the **DBInstanceType** parameter to **sharding**.
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.connection_domain):
            query['ConnectionDomain'] = request.connection_domain
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for MongoDB instances.
        
        @description The list of replica set and standalone instances is displayed when the *DBInstanceType** parameter uses the default value **replicate**. To query a list of sharded cluster instances, you must set the **DBInstanceType** parameter to **sharding**.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: dds_20151201_models.DescribeDBInstancesRequest,
    ) -> dds_20151201_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for MongoDB instances.
        
        @description The list of replica set and standalone instances is displayed when the *DBInstanceType** parameter uses the default value **replicate**. To query a list of sharded cluster instances, you must set the **DBInstanceType** parameter to **sharding**.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbinstances_overview_with_options(
        self,
        request: dds_20151201_models.DescribeDBInstancesOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for MongoDB instances.
        
        @description    If you do not specify an instance when you call this operation, the overview information of all instances in a specific region within this account is returned.
        Paged query is disabled for this operation.
        
        @param request: DescribeDBInstancesOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesOverview',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancesOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_overview_with_options_async(
        self,
        request: dds_20151201_models.DescribeDBInstancesOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeDBInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for MongoDB instances.
        
        @description    If you do not specify an instance when you call this operation, the overview information of all instances in a specific region within this account is returned.
        Paged query is disabled for this operation.
        
        @param request: DescribeDBInstancesOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesOverview',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeDBInstancesOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances_overview(
        self,
        request: dds_20151201_models.DescribeDBInstancesOverviewRequest,
    ) -> dds_20151201_models.DescribeDBInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for MongoDB instances.
        
        @description    If you do not specify an instance when you call this operation, the overview information of all instances in a specific region within this account is returned.
        Paged query is disabled for this operation.
        
        @param request: DescribeDBInstancesOverviewRequest
        @return: DescribeDBInstancesOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_overview_with_options(request, runtime)

    async def describe_dbinstances_overview_async(
        self,
        request: dds_20151201_models.DescribeDBInstancesOverviewRequest,
    ) -> dds_20151201_models.DescribeDBInstancesOverviewResponse:
        """
        @summary Queries the overview information of one or more ApsaraDB for MongoDB instances.
        
        @description    If you do not specify an instance when you call this operation, the overview information of all instances in a specific region within this account is returned.
        Paged query is disabled for this operation.
        
        @param request: DescribeDBInstancesOverviewRequest
        @return: DescribeDBInstancesOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_overview_with_options_async(request, runtime)

    def describe_error_log_records_with_options(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        """
        @summary Queries entries in error logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeErrorLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeErrorLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeErrorLogRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeErrorLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_error_log_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        """
        @summary Queries entries in error logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeErrorLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeErrorLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeErrorLogRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeErrorLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_error_log_records(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        """
        @summary Queries entries in error logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeErrorLogRecordsRequest
        @return: DescribeErrorLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_error_log_records_with_options(request, runtime)

    async def describe_error_log_records_async(
        self,
        request: dds_20151201_models.DescribeErrorLogRecordsRequest,
    ) -> dds_20151201_models.DescribeErrorLogRecordsResponse:
        """
        @summary Queries entries in error logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeErrorLogRecordsRequest
        @return: DescribeErrorLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_error_log_records_with_options_async(request, runtime)

    def describe_global_security_ipgroup_with_options(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries the global IP whitelist template of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_with_options_async(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries the global IP whitelist template of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries the global IP whitelist template of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_security_ipgroup_with_options(request, runtime)

    async def describe_global_security_ipgroup_async(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries the global IP whitelist template of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_security_ipgroup_with_options_async(request, runtime)

    def describe_global_security_ipgroup_relation_with_options(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the global IP whitelist templates associated with an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroupRelation',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_relation_with_options_async(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the global IP whitelist templates associated with an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroupRelation',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup_relation(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the global IP whitelist templates associated with an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_security_ipgroup_relation_with_options(request, runtime)

    async def describe_global_security_ipgroup_relation_async(
        self,
        request: dds_20151201_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> dds_20151201_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the global IP whitelist templates associated with an ApsaraDB for MongoDB instance.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_security_ipgroup_relation_with_options_async(request, runtime)

    def describe_history_tasks_with_options(
        self,
        request: dds_20151201_models.DescribeHistoryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeHistoryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_tasks_with_options_async(
        self,
        request: dds_20151201_models.DescribeHistoryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeHistoryTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_tasks(
        self,
        request: dds_20151201_models.DescribeHistoryTasksRequest,
    ) -> dds_20151201_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @return: DescribeHistoryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_history_tasks_with_options(request, runtime)

    async def describe_history_tasks_async(
        self,
        request: dds_20151201_models.DescribeHistoryTasksRequest,
    ) -> dds_20151201_models.DescribeHistoryTasksResponse:
        """
        @summary Queries a list of tasks in the task center.
        
        @param request: DescribeHistoryTasksRequest
        @return: DescribeHistoryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_tasks_with_options_async(request, runtime)

    def describe_history_tasks_stat_with_options(
        self,
        request: dds_20151201_models.DescribeHistoryTasksStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeHistoryTasksStatResponse:
        """
        @summary Queries the overview of a task in the task center.
        
        @param request: DescribeHistoryTasksStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryTasksStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryTasksStat',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeHistoryTasksStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_tasks_stat_with_options_async(
        self,
        request: dds_20151201_models.DescribeHistoryTasksStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeHistoryTasksStatResponse:
        """
        @summary Queries the overview of a task in the task center.
        
        @param request: DescribeHistoryTasksStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHistoryTasksStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryTasksStat',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeHistoryTasksStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_tasks_stat(
        self,
        request: dds_20151201_models.DescribeHistoryTasksStatRequest,
    ) -> dds_20151201_models.DescribeHistoryTasksStatResponse:
        """
        @summary Queries the overview of a task in the task center.
        
        @param request: DescribeHistoryTasksStatRequest
        @return: DescribeHistoryTasksStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_history_tasks_stat_with_options(request, runtime)

    async def describe_history_tasks_stat_async(
        self,
        request: dds_20151201_models.DescribeHistoryTasksStatRequest,
    ) -> dds_20151201_models.DescribeHistoryTasksStatResponse:
        """
        @summary Queries the overview of a task in the task center.
        
        @param request: DescribeHistoryTasksStatRequest
        @return: DescribeHistoryTasksStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_tasks_stat_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary You can call this operation to query whether auto-renewal is enabled for an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary You can call this operation to query whether auto-renewal is enabled for an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary You can call this operation to query whether auto-renewal is enabled for an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: dds_20151201_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.DescribeInstanceAutoRenewalAttributeResponse:
        """
        @summary You can call this operation to query whether auto-renewal is enabled for an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeInstanceAutoRenewalAttributeRequest
        @return: DescribeInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_instance_recover_time_with_options(
        self,
        request: dds_20151201_models.DescribeInstanceRecoverTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeInstanceRecoverTimeResponse:
        """
        @summary Queries the time required to restore the data of an ApsaraDB for MongoDB replica set instance that uses cloud disks.
        
        @param request: DescribeInstanceRecoverTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRecoverTimeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRecoverTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeInstanceRecoverTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_recover_time_with_options_async(
        self,
        request: dds_20151201_models.DescribeInstanceRecoverTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeInstanceRecoverTimeResponse:
        """
        @summary Queries the time required to restore the data of an ApsaraDB for MongoDB replica set instance that uses cloud disks.
        
        @param request: DescribeInstanceRecoverTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRecoverTimeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRecoverTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeInstanceRecoverTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_recover_time(
        self,
        request: dds_20151201_models.DescribeInstanceRecoverTimeRequest,
    ) -> dds_20151201_models.DescribeInstanceRecoverTimeResponse:
        """
        @summary Queries the time required to restore the data of an ApsaraDB for MongoDB replica set instance that uses cloud disks.
        
        @param request: DescribeInstanceRecoverTimeRequest
        @return: DescribeInstanceRecoverTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_recover_time_with_options(request, runtime)

    async def describe_instance_recover_time_async(
        self,
        request: dds_20151201_models.DescribeInstanceRecoverTimeRequest,
    ) -> dds_20151201_models.DescribeInstanceRecoverTimeResponse:
        """
        @summary Queries the time required to restore the data of an ApsaraDB for MongoDB replica set instance that uses cloud disks.
        
        @param request: DescribeInstanceRecoverTimeRequest
        @return: DescribeInstanceRecoverTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_recover_time_with_options_async(request, runtime)

    def describe_kernel_release_notes_with_options(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        """
        @summary Queries the release notes of the minor versions of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeKernelReleaseNotesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKernelReleaseNotesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kernel_version):
            query['KernelVersion'] = request.kernel_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKernelReleaseNotes',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeKernelReleaseNotesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kernel_release_notes_with_options_async(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        """
        @summary Queries the release notes of the minor versions of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeKernelReleaseNotesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKernelReleaseNotesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kernel_version):
            query['KernelVersion'] = request.kernel_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKernelReleaseNotes',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeKernelReleaseNotesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kernel_release_notes(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        """
        @summary Queries the release notes of the minor versions of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeKernelReleaseNotesRequest
        @return: DescribeKernelReleaseNotesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_kernel_release_notes_with_options(request, runtime)

    async def describe_kernel_release_notes_async(
        self,
        request: dds_20151201_models.DescribeKernelReleaseNotesRequest,
    ) -> dds_20151201_models.DescribeKernelReleaseNotesResponse:
        """
        @summary Queries the release notes of the minor versions of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeKernelReleaseNotesRequest
        @return: DescribeKernelReleaseNotesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_kernel_release_notes_with_options_async(request, runtime)

    def describe_kms_keys_with_options(
        self,
        request: dds_20151201_models.DescribeKmsKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeKmsKeysResponse:
        """
        @summary Queries Key Management Service (KMS) keys that are available for disk encryption.
        
        @description Queried keys are available only for disk encryption.
        
        @param request: DescribeKmsKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKmsKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKeys',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeKmsKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kms_keys_with_options_async(
        self,
        request: dds_20151201_models.DescribeKmsKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeKmsKeysResponse:
        """
        @summary Queries Key Management Service (KMS) keys that are available for disk encryption.
        
        @description Queried keys are available only for disk encryption.
        
        @param request: DescribeKmsKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKmsKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKeys',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeKmsKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kms_keys(
        self,
        request: dds_20151201_models.DescribeKmsKeysRequest,
    ) -> dds_20151201_models.DescribeKmsKeysResponse:
        """
        @summary Queries Key Management Service (KMS) keys that are available for disk encryption.
        
        @description Queried keys are available only for disk encryption.
        
        @param request: DescribeKmsKeysRequest
        @return: DescribeKmsKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_kms_keys_with_options(request, runtime)

    async def describe_kms_keys_async(
        self,
        request: dds_20151201_models.DescribeKmsKeysRequest,
    ) -> dds_20151201_models.DescribeKmsKeysResponse:
        """
        @summary Queries Key Management Service (KMS) keys that are available for disk encryption.
        
        @description Queried keys are available only for disk encryption.
        
        @param request: DescribeKmsKeysRequest
        @return: DescribeKmsKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_kms_keys_with_options_async(request, runtime)

    def describe_mongo_dblog_config_with_options(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        """
        @summary Queries the logging configurations of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable only to *general-purpose local-disk** and **dedicated local-disk** instances.
        This operation depends on the audit log feature of ApsaraDB for MongoDB. You can enable the audit log feature based on your business requirements. For more information, see [Enable the audit log feature](https://help.aliyun.com/document_detail/59903.html).
        Starting from January 6, 2022, the official edition of the audit log feature has been launched in all regions, and new applications for the free trial edition have ended. For more information, see [Notice on official launch of the pay-as-you-go audit log feature and no more application for the free trial edition](https://help.aliyun.com/document_detail/377480.html)
        You are charged for the official edition of the audit log feature based on the storage capacity that is consumed by audit logs and the retention period of the audit logs. For more information, see [Pricing of ApsaraDB for MongoDB instances](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        
        @param request: DescribeMongoDBLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMongoDBLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMongoDBLogConfig',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeMongoDBLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mongo_dblog_config_with_options_async(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        """
        @summary Queries the logging configurations of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable only to *general-purpose local-disk** and **dedicated local-disk** instances.
        This operation depends on the audit log feature of ApsaraDB for MongoDB. You can enable the audit log feature based on your business requirements. For more information, see [Enable the audit log feature](https://help.aliyun.com/document_detail/59903.html).
        Starting from January 6, 2022, the official edition of the audit log feature has been launched in all regions, and new applications for the free trial edition have ended. For more information, see [Notice on official launch of the pay-as-you-go audit log feature and no more application for the free trial edition](https://help.aliyun.com/document_detail/377480.html)
        You are charged for the official edition of the audit log feature based on the storage capacity that is consumed by audit logs and the retention period of the audit logs. For more information, see [Pricing of ApsaraDB for MongoDB instances](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        
        @param request: DescribeMongoDBLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMongoDBLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMongoDBLogConfig',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeMongoDBLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mongo_dblog_config(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        """
        @summary Queries the logging configurations of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable only to *general-purpose local-disk** and **dedicated local-disk** instances.
        This operation depends on the audit log feature of ApsaraDB for MongoDB. You can enable the audit log feature based on your business requirements. For more information, see [Enable the audit log feature](https://help.aliyun.com/document_detail/59903.html).
        Starting from January 6, 2022, the official edition of the audit log feature has been launched in all regions, and new applications for the free trial edition have ended. For more information, see [Notice on official launch of the pay-as-you-go audit log feature and no more application for the free trial edition](https://help.aliyun.com/document_detail/377480.html)
        You are charged for the official edition of the audit log feature based on the storage capacity that is consumed by audit logs and the retention period of the audit logs. For more information, see [Pricing of ApsaraDB for MongoDB instances](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        
        @param request: DescribeMongoDBLogConfigRequest
        @return: DescribeMongoDBLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mongo_dblog_config_with_options(request, runtime)

    async def describe_mongo_dblog_config_async(
        self,
        request: dds_20151201_models.DescribeMongoDBLogConfigRequest,
    ) -> dds_20151201_models.DescribeMongoDBLogConfigResponse:
        """
        @summary Queries the logging configurations of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable only to *general-purpose local-disk** and **dedicated local-disk** instances.
        This operation depends on the audit log feature of ApsaraDB for MongoDB. You can enable the audit log feature based on your business requirements. For more information, see [Enable the audit log feature](https://help.aliyun.com/document_detail/59903.html).
        Starting from January 6, 2022, the official edition of the audit log feature has been launched in all regions, and new applications for the free trial edition have ended. For more information, see [Notice on official launch of the pay-as-you-go audit log feature and no more application for the free trial edition](https://help.aliyun.com/document_detail/377480.html)
        You are charged for the official edition of the audit log feature based on the storage capacity that is consumed by audit logs and the retention period of the audit logs. For more information, see [Pricing of ApsaraDB for MongoDB instances](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        
        @param request: DescribeMongoDBLogConfigRequest
        @return: DescribeMongoDBLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_mongo_dblog_config_with_options_async(request, runtime)

    def describe_parameter_modification_history_with_options(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification records of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterModificationHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterModificationHistory',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParameterModificationHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_modification_history_with_options_async(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification records of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterModificationHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterModificationHistory',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParameterModificationHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_modification_history(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification records of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @return: DescribeParameterModificationHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_modification_history_with_options(request, runtime)

    async def describe_parameter_modification_history_async(
        self,
        request: dds_20151201_models.DescribeParameterModificationHistoryRequest,
    ) -> dds_20151201_models.DescribeParameterModificationHistoryResponse:
        """
        @summary Queries the parameter modification records of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParameterModificationHistoryRequest
        @return: DescribeParameterModificationHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_modification_history_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the list of default parameter templates for ApsaraDB for MongoDB instances.
        
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the list of default parameter templates for ApsaraDB for MongoDB instances.
        
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParameterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the list of default parameter templates for ApsaraDB for MongoDB instances.
        
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: dds_20151201_models.DescribeParameterTemplatesRequest,
    ) -> dds_20151201_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the list of default parameter templates for ApsaraDB for MongoDB instances.
        
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParametersResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeParametersResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
    ) -> dds_20151201_models.DescribeParametersResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: dds_20151201_models.DescribeParametersRequest,
    ) -> dds_20151201_models.DescribeParametersResponse:
        """
        @summary Queries the parameter settings of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: dds_20151201_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribePriceResponse:
        """
        @summary Queries the fees incurred when you create, upgrade, or renew an ApsaraDB for MongoDB instance.
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: dds_20151201_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribePriceResponse:
        """
        @summary Queries the fees incurred when you create, upgrade, or renew an ApsaraDB for MongoDB instance.
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: dds_20151201_models.DescribePriceRequest,
    ) -> dds_20151201_models.DescribePriceResponse:
        """
        @summary Queries the fees incurred when you create, upgrade, or renew an ApsaraDB for MongoDB instance.
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: dds_20151201_models.DescribePriceRequest,
    ) -> dds_20151201_models.DescribePriceResponse:
        """
        @summary Queries the fees incurred when you create, upgrade, or renew an ApsaraDB for MongoDB instance.
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        """
        @summary Queries all regions and zones supported for an ApsaraDB for MongoDB instance.
        
        @description >  To query available regions and zones in which an ApsaraDB for MongoDB instance can be created, call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        """
        @summary Queries all regions and zones supported for an ApsaraDB for MongoDB instance.
        
        @description >  To query available regions and zones in which an ApsaraDB for MongoDB instance can be created, call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        """
        @summary Queries all regions and zones supported for an ApsaraDB for MongoDB instance.
        
        @description >  To query available regions and zones in which an ApsaraDB for MongoDB instance can be created, call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: dds_20151201_models.DescribeRegionsRequest,
    ) -> dds_20151201_models.DescribeRegionsResponse:
        """
        @summary Queries all regions and zones supported for an ApsaraDB for MongoDB instance.
        
        @description >  To query available regions and zones in which an ApsaraDB for MongoDB instance can be created, call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_renewal_price_with_options(
        self,
        request: dds_20151201_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRenewalPriceResponse:
        """
        @summary Queries the monthly renewal price of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeRenewalPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenewalPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenewalPrice',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRenewalPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_renewal_price_with_options_async(
        self,
        request: dds_20151201_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRenewalPriceResponse:
        """
        @summary Queries the monthly renewal price of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeRenewalPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenewalPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenewalPrice',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRenewalPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_renewal_price(
        self,
        request: dds_20151201_models.DescribeRenewalPriceRequest,
    ) -> dds_20151201_models.DescribeRenewalPriceResponse:
        """
        @summary Queries the monthly renewal price of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeRenewalPriceRequest
        @return: DescribeRenewalPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    async def describe_renewal_price_async(
        self,
        request: dds_20151201_models.DescribeRenewalPriceRequest,
    ) -> dds_20151201_models.DescribeRenewalPriceResponse:
        """
        @summary Queries the monthly renewal price of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to subscription instances.
        
        @param request: DescribeRenewalPriceRequest
        @return: DescribeRenewalPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_renewal_price_with_options_async(request, runtime)

    def describe_replica_set_role_with_options(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        """
        @summary Queries the role and connection information of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and standalone instances, but not to sharded cluster instances.
        
        @param request: DescribeReplicaSetRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeReplicaSetRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReplicaSetRole',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeReplicaSetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_replica_set_role_with_options_async(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        """
        @summary Queries the role and connection information of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and standalone instances, but not to sharded cluster instances.
        
        @param request: DescribeReplicaSetRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeReplicaSetRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReplicaSetRole',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeReplicaSetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_replica_set_role(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        """
        @summary Queries the role and connection information of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and standalone instances, but not to sharded cluster instances.
        
        @param request: DescribeReplicaSetRoleRequest
        @return: DescribeReplicaSetRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_replica_set_role_with_options(request, runtime)

    async def describe_replica_set_role_async(
        self,
        request: dds_20151201_models.DescribeReplicaSetRoleRequest,
    ) -> dds_20151201_models.DescribeReplicaSetRoleResponse:
        """
        @summary Queries the role and connection information of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and standalone instances, but not to sharded cluster instances.
        
        @param request: DescribeReplicaSetRoleRequest
        @return: DescribeReplicaSetRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_replica_set_role_with_options_async(request, runtime)

    def describe_restore_dbinstance_list_with_options(
        self,
        request: dds_20151201_models.DescribeRestoreDBInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRestoreDBInstanceListResponse:
        """
        @summary Queries ApsaraDB for MongoDB instances whose backups are restored within seven days.
        
        @param request: DescribeRestoreDBInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreDBInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_time_after):
            query['CreationTimeAfter'] = request.creation_time_after
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreDBInstanceList',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRestoreDBInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_dbinstance_list_with_options_async(
        self,
        request: dds_20151201_models.DescribeRestoreDBInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRestoreDBInstanceListResponse:
        """
        @summary Queries ApsaraDB for MongoDB instances whose backups are restored within seven days.
        
        @param request: DescribeRestoreDBInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreDBInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_time_after):
            query['CreationTimeAfter'] = request.creation_time_after
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreDBInstanceList',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRestoreDBInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_dbinstance_list(
        self,
        request: dds_20151201_models.DescribeRestoreDBInstanceListRequest,
    ) -> dds_20151201_models.DescribeRestoreDBInstanceListResponse:
        """
        @summary Queries ApsaraDB for MongoDB instances whose backups are restored within seven days.
        
        @param request: DescribeRestoreDBInstanceListRequest
        @return: DescribeRestoreDBInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_dbinstance_list_with_options(request, runtime)

    async def describe_restore_dbinstance_list_async(
        self,
        request: dds_20151201_models.DescribeRestoreDBInstanceListRequest,
    ) -> dds_20151201_models.DescribeRestoreDBInstanceListResponse:
        """
        @summary Queries ApsaraDB for MongoDB instances whose backups are restored within seven days.
        
        @param request: DescribeRestoreDBInstanceListRequest
        @return: DescribeRestoreDBInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_dbinstance_list_with_options_async(request, runtime)

    def describe_role_zone_info_with_options(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role and zone of each node in an ApsaraDB for MongoDB instance.
        
        @description > For more information, see [View the zone of a node](https://help.aliyun.com/document_detail/123825.html).
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        
        @param request: DescribeRoleZoneInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoleZoneInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoleZoneInfo',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRoleZoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_role_zone_info_with_options_async(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role and zone of each node in an ApsaraDB for MongoDB instance.
        
        @description > For more information, see [View the zone of a node](https://help.aliyun.com/document_detail/123825.html).
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        
        @param request: DescribeRoleZoneInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRoleZoneInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoleZoneInfo',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRoleZoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_role_zone_info(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role and zone of each node in an ApsaraDB for MongoDB instance.
        
        @description > For more information, see [View the zone of a node](https://help.aliyun.com/document_detail/123825.html).
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        
        @param request: DescribeRoleZoneInfoRequest
        @return: DescribeRoleZoneInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    async def describe_role_zone_info_async(
        self,
        request: dds_20151201_models.DescribeRoleZoneInfoRequest,
    ) -> dds_20151201_models.DescribeRoleZoneInfoResponse:
        """
        @summary Queries the role and zone of each node in an ApsaraDB for MongoDB instance.
        
        @description > For more information, see [View the zone of a node](https://help.aliyun.com/document_detail/123825.html).
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        
        @param request: DescribeRoleZoneInfoRequest
        @return: DescribeRoleZoneInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_role_zone_info_with_options_async(request, runtime)

    def describe_running_log_records_with_options(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries entries in operational logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeRunningLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRunningLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningLogRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRunningLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_running_log_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries entries in operational logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeRunningLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRunningLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningLogRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeRunningLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_running_log_records(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries entries in operational logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeRunningLogRecordsRequest
        @return: DescribeRunningLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    async def describe_running_log_records_async(
        self,
        request: dds_20151201_models.DescribeRunningLogRecordsRequest,
    ) -> dds_20151201_models.DescribeRunningLogRecordsResponse:
        """
        @summary Queries entries in operational logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeRunningLogRecordsRequest
        @return: DescribeRunningLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_running_log_records_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to query ECS security groups that are bound to an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to query ECS security groups that are bound to an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to query ECS security groups that are bound to an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @return: DescribeSecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: dds_20151201_models.DescribeSecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.DescribeSecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to query ECS security groups that are bound to an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityGroupConfigurationRequest
        @return: DescribeSecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        """
        @summary You can call this operation to query the IP whitelists of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.show_hdmips):
            query['ShowHDMIps'] = request.show_hdmips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIps',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        """
        @summary You can call this operation to query the IP whitelists of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.show_hdmips):
            query['ShowHDMIps'] = request.show_hdmips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIps',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ips(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        """
        @summary You can call this operation to query the IP whitelists of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityIpsRequest
        @return: DescribeSecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: dds_20151201_models.DescribeSecurityIpsRequest,
    ) -> dds_20151201_models.DescribeSecurityIpsResponse:
        """
        @summary You can call this operation to query the IP whitelists of an ApsaraDB for MongoDB instance.
        
        @param request: DescribeSecurityIpsRequest
        @return: DescribeSecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_sharding_network_address_with_options(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        """
        @summary Queries connection information about an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances.
        
        @param request: DescribeShardingNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeShardingNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShardingNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeShardingNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sharding_network_address_with_options_async(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        """
        @summary Queries connection information about an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances.
        
        @param request: DescribeShardingNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeShardingNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShardingNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeShardingNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sharding_network_address(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        """
        @summary Queries connection information about an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances.
        
        @param request: DescribeShardingNetworkAddressRequest
        @return: DescribeShardingNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sharding_network_address_with_options(request, runtime)

    async def describe_sharding_network_address_async(
        self,
        request: dds_20151201_models.DescribeShardingNetworkAddressRequest,
    ) -> dds_20151201_models.DescribeShardingNetworkAddressResponse:
        """
        @summary Queries connection information about an ApsaraDB for MongoDB sharded cluster instance.
        
        @description This operation is applicable only to sharded cluster instances.
        
        @param request: DescribeShardingNetworkAddressRequest
        @return: DescribeShardingNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sharding_network_address_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of entries in slow query logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of entries in slow query logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of entries in slow query logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: dds_20151201_models.DescribeSlowLogRecordsRequest,
    ) -> dds_20151201_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of entries in slow query logs of an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: dds_20151201_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeTagsResponse:
        """
        @summary Queries all tags in a specified region.
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: dds_20151201_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeTagsResponse:
        """
        @summary Queries all tags in a specified region.
        
        @param request: DescribeTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: dds_20151201_models.DescribeTagsRequest,
    ) -> dds_20151201_models.DescribeTagsResponse:
        """
        @summary Queries all tags in a specified region.
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: dds_20151201_models.DescribeTagsRequest,
    ) -> dds_20151201_models.DescribeTagsResponse:
        """
        @summary Queries all tags in a specified region.
        
        @param request: DescribeTagsRequest
        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: dds_20151201_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the list of custom keys for an ApsaraDB for MongoDB instance.
        
        @description You can use the custom key obtained by calling the DescribeUserEncryptionKeyList operation to enable TDE. For more information, see [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html).
        
        @param request: DescribeUserEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserEncryptionKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeUserEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: dds_20151201_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the list of custom keys for an ApsaraDB for MongoDB instance.
        
        @description You can use the custom key obtained by calling the DescribeUserEncryptionKeyList operation to enable TDE. For more information, see [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html).
        
        @param request: DescribeUserEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserEncryptionKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DescribeUserEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_encryption_key_list(
        self,
        request: dds_20151201_models.DescribeUserEncryptionKeyListRequest,
    ) -> dds_20151201_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the list of custom keys for an ApsaraDB for MongoDB instance.
        
        @description You can use the custom key obtained by calling the DescribeUserEncryptionKeyList operation to enable TDE. For more information, see [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html).
        
        @param request: DescribeUserEncryptionKeyListRequest
        @return: DescribeUserEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    async def describe_user_encryption_key_list_async(
        self,
        request: dds_20151201_models.DescribeUserEncryptionKeyListRequest,
    ) -> dds_20151201_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the list of custom keys for an ApsaraDB for MongoDB instance.
        
        @description You can use the custom key obtained by calling the DescribeUserEncryptionKeyList operation to enable TDE. For more information, see [ModifyDBInstanceTDE](https://help.aliyun.com/document_detail/131267.html).
        
        @param request: DescribeUserEncryptionKeyListRequest
        @return: DescribeUserEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_encryption_key_list_with_options_async(request, runtime)

    def destroy_instance_with_options(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        """
        @summary Destroys an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set instance or a sharded cluster instance that uses local disks.
        The billing method of the instance is subscription.
        The instance has expired and is in the **Locking** state.
        *\
        *Warning** Data cannot be restored after the instance is destroyed. Proceed with caution.
        
        @param request: DestroyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DestroyInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DestroyInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DestroyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_instance_with_options_async(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        """
        @summary Destroys an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set instance or a sharded cluster instance that uses local disks.
        The billing method of the instance is subscription.
        The instance has expired and is in the **Locking** state.
        *\
        *Warning** Data cannot be restored after the instance is destroyed. Proceed with caution.
        
        @param request: DestroyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DestroyInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DestroyInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.DestroyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_instance(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        """
        @summary Destroys an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set instance or a sharded cluster instance that uses local disks.
        The billing method of the instance is subscription.
        The instance has expired and is in the **Locking** state.
        *\
        *Warning** Data cannot be restored after the instance is destroyed. Proceed with caution.
        
        @param request: DestroyInstanceRequest
        @return: DestroyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.destroy_instance_with_options(request, runtime)

    async def destroy_instance_async(
        self,
        request: dds_20151201_models.DestroyInstanceRequest,
    ) -> dds_20151201_models.DestroyInstanceResponse:
        """
        @summary Destroys an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is a replica set instance or a sharded cluster instance that uses local disks.
        The billing method of the instance is subscription.
        The instance has expired and is in the **Locking** state.
        *\
        *Warning** Data cannot be restored after the instance is destroyed. Proceed with caution.
        
        @param request: DestroyInstanceRequest
        @return: DestroyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.destroy_instance_with_options_async(request, runtime)

    def evaluate_resource_with_options(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        """
        @summary Checks whether sufficient resources are available in a region in which you want to create or upgrade an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances. You can call this operation to check whether resources are sufficient for creating an instance, upgrading a replica set or sharded cluster instance, or upgrading a single node of the sharded cluster instance.
        > You can call this operation a maximum of 200 times per minute.
        
        @param request: EvaluateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluateResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.shards_info):
            query['ShardsInfo'] = request.shards_info
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EvaluateResource',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.EvaluateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_resource_with_options_async(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        """
        @summary Checks whether sufficient resources are available in a region in which you want to create or upgrade an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances. You can call this operation to check whether resources are sufficient for creating an instance, upgrading a replica set or sharded cluster instance, or upgrading a single node of the sharded cluster instance.
        > You can call this operation a maximum of 200 times per minute.
        
        @param request: EvaluateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluateResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.shards_info):
            query['ShardsInfo'] = request.shards_info
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EvaluateResource',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.EvaluateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_resource(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        """
        @summary Checks whether sufficient resources are available in a region in which you want to create or upgrade an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances. You can call this operation to check whether resources are sufficient for creating an instance, upgrading a replica set or sharded cluster instance, or upgrading a single node of the sharded cluster instance.
        > You can call this operation a maximum of 200 times per minute.
        
        @param request: EvaluateResourceRequest
        @return: EvaluateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.evaluate_resource_with_options(request, runtime)

    async def evaluate_resource_async(
        self,
        request: dds_20151201_models.EvaluateResourceRequest,
    ) -> dds_20151201_models.EvaluateResourceResponse:
        """
        @summary Checks whether sufficient resources are available in a region in which you want to create or upgrade an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances. You can call this operation to check whether resources are sufficient for creating an instance, upgrading a replica set or sharded cluster instance, or upgrading a single node of the sharded cluster instance.
        > You can call this operation a maximum of 200 times per minute.
        
        @param request: EvaluateResourceRequest
        @return: EvaluateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_resource_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        """
        @summary Queries the relationship between ApsaraDB for MongoDB instances and tags.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        """
        @summary Queries the relationship between ApsaraDB for MongoDB instances and tags.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        """
        @summary Queries the relationship between ApsaraDB for MongoDB instances and tags.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dds_20151201_models.ListTagResourcesRequest,
    ) -> dds_20151201_models.ListTagResourcesResponse:
        """
        @summary Queries the relationship between ApsaraDB for MongoDB instances and tags.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def migrate_available_zone_with_options(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        """
        @summary Migrates an ApsaraDB for MongoDB instance to a specific zone.
        
        @description    This operation is available only for replica set instances that run MongoDB 4.2 or earlier and sharded cluster instances.
        If you have applied for a public endpoint for the ApsaraDB for MongoDB instance, you must call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint before you call the MigrateAvailableZone operation.
        Transparent data encryption (TDE) is disabled for the ApsaraDB for MongoDB instance.
        The source zone and the destination zone belong to the same region.
        A vSwitch is created in the destination zone. This prerequisite must be met if the instance resides in a virtual private cloud (VPC). For more information about how to create a vSwitch, see [Work with vSwitches](https://help.aliyun.com/document_detail/65387.html).
        
        @param request: MigrateAvailableZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateAvailableZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.vswitch):
            query['Vswitch'] = request.vswitch
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateAvailableZone',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.MigrateAvailableZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_available_zone_with_options_async(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        """
        @summary Migrates an ApsaraDB for MongoDB instance to a specific zone.
        
        @description    This operation is available only for replica set instances that run MongoDB 4.2 or earlier and sharded cluster instances.
        If you have applied for a public endpoint for the ApsaraDB for MongoDB instance, you must call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint before you call the MigrateAvailableZone operation.
        Transparent data encryption (TDE) is disabled for the ApsaraDB for MongoDB instance.
        The source zone and the destination zone belong to the same region.
        A vSwitch is created in the destination zone. This prerequisite must be met if the instance resides in a virtual private cloud (VPC). For more information about how to create a vSwitch, see [Work with vSwitches](https://help.aliyun.com/document_detail/65387.html).
        
        @param request: MigrateAvailableZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateAvailableZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not UtilClient.is_unset(request.vswitch):
            query['Vswitch'] = request.vswitch
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateAvailableZone',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.MigrateAvailableZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_available_zone(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        """
        @summary Migrates an ApsaraDB for MongoDB instance to a specific zone.
        
        @description    This operation is available only for replica set instances that run MongoDB 4.2 or earlier and sharded cluster instances.
        If you have applied for a public endpoint for the ApsaraDB for MongoDB instance, you must call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint before you call the MigrateAvailableZone operation.
        Transparent data encryption (TDE) is disabled for the ApsaraDB for MongoDB instance.
        The source zone and the destination zone belong to the same region.
        A vSwitch is created in the destination zone. This prerequisite must be met if the instance resides in a virtual private cloud (VPC). For more information about how to create a vSwitch, see [Work with vSwitches](https://help.aliyun.com/document_detail/65387.html).
        
        @param request: MigrateAvailableZoneRequest
        @return: MigrateAvailableZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_available_zone_with_options(request, runtime)

    async def migrate_available_zone_async(
        self,
        request: dds_20151201_models.MigrateAvailableZoneRequest,
    ) -> dds_20151201_models.MigrateAvailableZoneResponse:
        """
        @summary Migrates an ApsaraDB for MongoDB instance to a specific zone.
        
        @description    This operation is available only for replica set instances that run MongoDB 4.2 or earlier and sharded cluster instances.
        If you have applied for a public endpoint for the ApsaraDB for MongoDB instance, you must call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint before you call the MigrateAvailableZone operation.
        Transparent data encryption (TDE) is disabled for the ApsaraDB for MongoDB instance.
        The source zone and the destination zone belong to the same region.
        A vSwitch is created in the destination zone. This prerequisite must be met if the instance resides in a virtual private cloud (VPC). For more information about how to create a vSwitch, see [Work with vSwitches](https://help.aliyun.com/document_detail/65387.html).
        
        @param request: MigrateAvailableZoneRequest
        @return: MigrateAvailableZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.migrate_available_zone_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        """
        @summary You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone.
        
        @description This operation is applicable only to replica set instances, but not to standalone instances or sharded cluster instances.
        >  If you have applied for a public endpoint of the instance, you must first call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint.
        
        @param request: MigrateToOtherZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateToOtherZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        """
        @summary You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone.
        
        @description This operation is applicable only to replica set instances, but not to standalone instances or sharded cluster instances.
        >  If you have applied for a public endpoint of the instance, you must first call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint.
        
        @param request: MigrateToOtherZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateToOtherZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.MigrateToOtherZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        """
        @summary You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone.
        
        @description This operation is applicable only to replica set instances, but not to standalone instances or sharded cluster instances.
        >  If you have applied for a public endpoint of the instance, you must first call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint.
        
        @param request: MigrateToOtherZoneRequest
        @return: MigrateToOtherZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: dds_20151201_models.MigrateToOtherZoneRequest,
    ) -> dds_20151201_models.MigrateToOtherZoneResponse:
        """
        @summary You can call this operation to migrate an ApsaraDB for MongoDB instance to another zone.
        
        @description This operation is applicable only to replica set instances, but not to standalone instances or sharded cluster instances.
        >  If you have applied for a public endpoint of the instance, you must first call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation to release the public endpoint.
        
        @param request: MigrateToOtherZoneRequest
        @return: MigrateToOtherZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of the root account in an ApsaraDB for MongoDB instance.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of the root account in an ApsaraDB for MongoDB instance.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of the root account in an ApsaraDB for MongoDB instance.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: dds_20151201_models.ModifyAccountDescriptionRequest,
    ) -> dds_20151201_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of the root account in an ApsaraDB for MongoDB instance.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_active_operation_tasks_with_options(
        self,
        request: dds_20151201_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyActiveOperationTasksResponse:
        """
        @summary Modifies the switching time of scheduled O\\\\\\&M tasks for an ApsaraDB for MongoDB instance.
        
        @param request: ModifyActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_tasks_with_options_async(
        self,
        request: dds_20151201_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyActiveOperationTasksResponse:
        """
        @summary Modifies the switching time of scheduled O\\\\\\&M tasks for an ApsaraDB for MongoDB instance.
        
        @param request: ModifyActiveOperationTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTasks',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_tasks(
        self,
        request: dds_20151201_models.ModifyActiveOperationTasksRequest,
    ) -> dds_20151201_models.ModifyActiveOperationTasksResponse:
        """
        @summary Modifies the switching time of scheduled O\\\\\\&M tasks for an ApsaraDB for MongoDB instance.
        
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    async def modify_active_operation_tasks_async(
        self,
        request: dds_20151201_models.ModifyActiveOperationTasksRequest,
    ) -> dds_20151201_models.ModifyActiveOperationTasksResponse:
        """
        @summary Modifies the switching time of scheduled O\\\\\\&M tasks for an ApsaraDB for MongoDB instance.
        
        @param request: ModifyActiveOperationTasksRequest
        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_tasks_with_options_async(request, runtime)

    def modify_audit_log_filter_with_options(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        """
        @summary Queries the types of logs collected by the audit log feature of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** or **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditLogFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditLogFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogFilter',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAuditLogFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_filter_with_options_async(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        """
        @summary Queries the types of logs collected by the audit log feature of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** or **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditLogFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditLogFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogFilter',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAuditLogFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_filter(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        """
        @summary Queries the types of logs collected by the audit log feature of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** or **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditLogFilterRequest
        @return: ModifyAuditLogFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_filter_with_options(request, runtime)

    async def modify_audit_log_filter_async(
        self,
        request: dds_20151201_models.ModifyAuditLogFilterRequest,
    ) -> dds_20151201_models.ModifyAuditLogFilterResponse:
        """
        @summary Queries the types of logs collected by the audit log feature of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the running state when you call this operation.
        This operation is applicable only to **general-purpose local-disk** or **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditLogFilterRequest
        @return: ModifyAuditLogFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_filter_with_options_async(request, runtime)

    def modify_audit_policy_with_options(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        """
        @summary Enables or disables the audit log feature or configures the log storage duration for an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_log_switch_source):
            query['AuditLogSwitchSource'] = request.audit_log_switch_source
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.storage_period):
            query['StoragePeriod'] = request.storage_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAuditPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_policy_with_options_async(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        """
        @summary Enables or disables the audit log feature or configures the log storage duration for an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAuditPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_log_switch_source):
            query['AuditLogSwitchSource'] = request.audit_log_switch_source
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.storage_period):
            query['StoragePeriod'] = request.storage_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyAuditPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_policy(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        """
        @summary Enables or disables the audit log feature or configures the log storage duration for an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditPolicyRequest
        @return: ModifyAuditPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_policy_with_options(request, runtime)

    async def modify_audit_policy_async(
        self,
        request: dds_20151201_models.ModifyAuditPolicyRequest,
    ) -> dds_20151201_models.ModifyAuditPolicyResponse:
        """
        @summary Enables or disables the audit log feature or configures the log storage duration for an ApsaraDB for MongoDB instance.
        
        @description    This operation is applicable only to **general-purpose local-disk** and **dedicated local-disk** instances.
        You can call this operation up to 30 times per minute. To call this operation at a higher frequency, use a Logstore. For more information, see [Manage a Logstore](https://help.aliyun.com/document_detail/48990.html).
        
        @param request: ModifyAuditPolicyRequest
        @return: ModifyAuditPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_policy_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies a backup policy for an ApsaraDB for MongoDB instance.
        
        @description Cross-regional backup only supports  MongoDB sharded cluster instance and MongoDB replica set.
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_interval):
            query['BackupInterval'] = request.backup_interval
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not UtilClient.is_unset(request.cross_backup_period):
            query['CrossBackupPeriod'] = request.cross_backup_period
        if not UtilClient.is_unset(request.cross_backup_type):
            query['CrossBackupType'] = request.cross_backup_type
        if not UtilClient.is_unset(request.cross_log_retention_type):
            query['CrossLogRetentionType'] = request.cross_log_retention_type
        if not UtilClient.is_unset(request.cross_log_retention_value):
            query['CrossLogRetentionValue'] = request.cross_log_retention_value
        if not UtilClient.is_unset(request.cross_retention_type):
            query['CrossRetentionType'] = request.cross_retention_type
        if not UtilClient.is_unset(request.cross_retention_value):
            query['CrossRetentionValue'] = request.cross_retention_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.enable_cross_log_backup):
            query['EnableCrossLogBackup'] = request.enable_cross_log_backup
        if not UtilClient.is_unset(request.high_frequency_backup_retention):
            query['HighFrequencyBackupRetention'] = request.high_frequency_backup_retention
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_backup_type):
            query['SnapshotBackupType'] = request.snapshot_backup_type
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies a backup policy for an ApsaraDB for MongoDB instance.
        
        @description Cross-regional backup only supports  MongoDB sharded cluster instance and MongoDB replica set.
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_interval):
            query['BackupInterval'] = request.backup_interval
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not UtilClient.is_unset(request.cross_backup_period):
            query['CrossBackupPeriod'] = request.cross_backup_period
        if not UtilClient.is_unset(request.cross_backup_type):
            query['CrossBackupType'] = request.cross_backup_type
        if not UtilClient.is_unset(request.cross_log_retention_type):
            query['CrossLogRetentionType'] = request.cross_log_retention_type
        if not UtilClient.is_unset(request.cross_log_retention_value):
            query['CrossLogRetentionValue'] = request.cross_log_retention_value
        if not UtilClient.is_unset(request.cross_retention_type):
            query['CrossRetentionType'] = request.cross_retention_type
        if not UtilClient.is_unset(request.cross_retention_value):
            query['CrossRetentionValue'] = request.cross_retention_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.enable_cross_log_backup):
            query['EnableCrossLogBackup'] = request.enable_cross_log_backup
        if not UtilClient.is_unset(request.high_frequency_backup_retention):
            query['HighFrequencyBackupRetention'] = request.high_frequency_backup_retention
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_backup_type):
            query['SnapshotBackupType'] = request.snapshot_backup_type
        if not UtilClient.is_unset(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies a backup policy for an ApsaraDB for MongoDB instance.
        
        @description Cross-regional backup only supports  MongoDB sharded cluster instance and MongoDB replica set.
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: dds_20151201_models.ModifyBackupPolicyRequest,
    ) -> dds_20151201_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies a backup policy for an ApsaraDB for MongoDB instance.
        
        @description Cross-regional backup only supports  MongoDB sharded cluster instance and MongoDB replica set.
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint that is used to connect to an ApsaraDB for MongoDB instance.
        
        @description You can modify the connection strings and ports of the following instances:
        You can modify the connection strings of instances that use local or cloud disks.
        You can only modify the ports of instances that use cloud disks.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
        if not UtilClient.is_unset(request.new_port):
            query['NewPort'] = request.new_port
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint that is used to connect to an ApsaraDB for MongoDB instance.
        
        @description You can modify the connection strings and ports of the following instances:
        You can modify the connection strings of instances that use local or cloud disks.
        You can only modify the ports of instances that use cloud disks.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
        if not UtilClient.is_unset(request.new_port):
            query['NewPort'] = request.new_port
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint that is used to connect to an ApsaraDB for MongoDB instance.
        
        @description You can modify the connection strings and ports of the following instances:
        You can modify the connection strings of instances that use local or cloud disks.
        You can only modify the ports of instances that use cloud disks.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceConnectionStringRequest,
    ) -> dds_20151201_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint that is used to connect to an ApsaraDB for MongoDB instance.
        
        @description You can modify the connection strings and ports of the following instances:
        You can modify the connection strings of instances that use local or cloud disks.
        You can only modify the ports of instances that use cloud disks.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        """
        @summary Modifies the name of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        """
        @summary Modifies the name of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        """
        @summary Modifies the name of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @return: ModifyDBInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceDescriptionRequest,
    ) -> dds_20151201_models.ModifyDBInstanceDescriptionResponse:
        """
        @summary Modifies the name of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @return: ModifyDBInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_disk_type_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceDiskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceDiskTypeResponse:
        """
        @summary Modifies the disk type of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDiskTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDiskTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.db_instance_storage_type):
            query['DbInstanceStorageType'] = request.db_instance_storage_type
        if not UtilClient.is_unset(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDiskType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceDiskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_disk_type_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceDiskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceDiskTypeResponse:
        """
        @summary Modifies the disk type of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDiskTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDiskTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.db_instance_storage_type):
            query['DbInstanceStorageType'] = request.db_instance_storage_type
        if not UtilClient.is_unset(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDiskType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceDiskTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_disk_type(
        self,
        request: dds_20151201_models.ModifyDBInstanceDiskTypeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceDiskTypeResponse:
        """
        @summary Modifies the disk type of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDiskTypeRequest
        @return: ModifyDBInstanceDiskTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_disk_type_with_options(request, runtime)

    async def modify_dbinstance_disk_type_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceDiskTypeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceDiskTypeResponse:
        """
        @summary Modifies the disk type of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceDiskTypeRequest
        @return: ModifyDBInstanceDiskTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_disk_type_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for MongoDB instance.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_monitor_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        """
        @summary You can call this operation to set the monitoring granularity for an ApsaraDB for MongoDB instance.
        
        @description >  This operation is applicable only to the ApsaraDB for MongoDB console of the previous version due to the change in the feature of adjusting collection intervals of monitoring data.
        Before you call this operation, make sure that the following requirements are met:
        A replica set or sharded cluster instance is used.
        MongoDB 3.4 (the latest minor version) or MongoDB 4.0 is selected.
        
        @param request: ModifyDBInstanceMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMonitor',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_monitor_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        """
        @summary You can call this operation to set the monitoring granularity for an ApsaraDB for MongoDB instance.
        
        @description >  This operation is applicable only to the ApsaraDB for MongoDB console of the previous version due to the change in the feature of adjusting collection intervals of monitoring data.
        Before you call this operation, make sure that the following requirements are met:
        A replica set or sharded cluster instance is used.
        MongoDB 3.4 (the latest minor version) or MongoDB 4.0 is selected.
        
        @param request: ModifyDBInstanceMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMonitor',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_monitor(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        """
        @summary You can call this operation to set the monitoring granularity for an ApsaraDB for MongoDB instance.
        
        @description >  This operation is applicable only to the ApsaraDB for MongoDB console of the previous version due to the change in the feature of adjusting collection intervals of monitoring data.
        Before you call this operation, make sure that the following requirements are met:
        A replica set or sharded cluster instance is used.
        MongoDB 3.4 (the latest minor version) or MongoDB 4.0 is selected.
        
        @param request: ModifyDBInstanceMonitorRequest
        @return: ModifyDBInstanceMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    async def modify_dbinstance_monitor_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceMonitorRequest,
    ) -> dds_20151201_models.ModifyDBInstanceMonitorResponse:
        """
        @summary You can call this operation to set the monitoring granularity for an ApsaraDB for MongoDB instance.
        
        @description >  This operation is applicable only to the ApsaraDB for MongoDB console of the previous version due to the change in the feature of adjusting collection intervals of monitoring data.
        Before you call this operation, make sure that the following requirements are met:
        A replica set or sharded cluster instance is used.
        MongoDB 3.4 (the latest minor version) or MongoDB 4.0 is selected.
        
        @param request: ModifyDBInstanceMonitorRequest
        @return: ModifyDBInstanceMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_monitor_with_options_async(request, runtime)

    def modify_dbinstance_net_expire_time_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The network of the instance is in hybrid access mode.
        >  This operation is supported by replica set instances and sharded cluster instances. This operation is not supported by standalone instances.
        
        @param request: ModifyDBInstanceNetExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceNetExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expend_expired_days):
            query['ClassicExpendExpiredDays'] = request.classic_expend_expired_days
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetExpireTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_net_expire_time_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The network of the instance is in hybrid access mode.
        >  This operation is supported by replica set instances and sharded cluster instances. This operation is not supported by standalone instances.
        
        @param request: ModifyDBInstanceNetExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceNetExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expend_expired_days):
            query['ClassicExpendExpiredDays'] = request.classic_expend_expired_days
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetExpireTime',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_net_expire_time(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The network of the instance is in hybrid access mode.
        >  This operation is supported by replica set instances and sharded cluster instances. This operation is not supported by standalone instances.
        
        @param request: ModifyDBInstanceNetExpireTimeRequest
        @return: ModifyDBInstanceNetExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_net_expire_time_with_options(request, runtime)

    async def modify_dbinstance_net_expire_time_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetExpireTimeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetExpireTimeResponse:
        """
        @summary Extends the retention period of the classic network endpoint of an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the instance meets the following requirements:
        The instance is in the Running state.
        The network of the instance is in hybrid access mode.
        >  This operation is supported by replica set instances and sharded cluster instances. This operation is not supported by standalone instances.
        
        @param request: ModifyDBInstanceNetExpireTimeRequest
        @return: ModifyDBInstanceNetExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_net_expire_time_with_options_async(request, runtime)

    def modify_dbinstance_network_type_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        """
        @summary Changes the network type of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances, but not standalone instances. You can call this operation to change the network of an instance from a classic network to a VPC.
        
        @param request: ModifyDBInstanceNetworkTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        """
        @summary Changes the network type of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances, but not standalone instances. You can call this operation to change the network of an instance from a classic network to a VPC.
        
        @param request: ModifyDBInstanceNetworkTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_network_type(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        """
        @summary Changes the network type of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances, but not standalone instances. You can call this operation to change the network of an instance from a classic network to a VPC.
        
        @param request: ModifyDBInstanceNetworkTypeRequest
        @return: ModifyDBInstanceNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    async def modify_dbinstance_network_type_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> dds_20151201_models.ModifyDBInstanceNetworkTypeResponse:
        """
        @summary Changes the network type of an ApsaraDB for MongoDB instance.
        
        @description This operation is applicable to replica set instances and sharded cluster instances, but not standalone instances. You can call this operation to change the network of an instance from a classic network to a VPC.
        
        @param request: ModifyDBInstanceNetworkTypeRequest
        @return: ModifyDBInstanceNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_network_type_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for MongoDB instance.
        
        @description ## Usage
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is a replica set instance.
        The engine version of the instance is 3.4 or 4.0.
        >  When you enable or disable SSL encryption or update the SSL certificate, the instance restarts. We recommend that you call this operation during off-peak hours.
        
        @param request: ModifyDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslaction):
            query['SSLAction'] = request.sslaction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for MongoDB instance.
        
        @description ## Usage
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is a replica set instance.
        The engine version of the instance is 3.4 or 4.0.
        >  When you enable or disable SSL encryption or update the SSL certificate, the instance restarts. We recommend that you call this operation during off-peak hours.
        
        @param request: ModifyDBInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslaction):
            query['SSLAction'] = request.sslaction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_ssl(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for MongoDB instance.
        
        @description ## Usage
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is a replica set instance.
        The engine version of the instance is 3.4 or 4.0.
        >  When you enable or disable SSL encryption or update the SSL certificate, the instance restarts. We recommend that you call this operation during off-peak hours.
        
        @param request: ModifyDBInstanceSSLRequest
        @return: ModifyDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    async def modify_dbinstance_ssl_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSSLRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSSLResponse:
        """
        @summary Modifies the SSL settings of an ApsaraDB for MongoDB instance.
        
        @description ## Usage
        Before you call this operation, make sure that the following requirements are met:
        The instance is in the running state.
        The instance is a replica set instance.
        The engine version of the instance is 3.4 or 4.0.
        >  When you enable or disable SSL encryption or update the SSL certificate, the instance restarts. We recommend that you call this operation during off-peak hours.
        
        @param request: ModifyDBInstanceSSLRequest
        @return: ModifyDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_sslwith_options_async(request, runtime)

    def modify_dbinstance_spec_with_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        """
        @summary Modifies the specifications or storage space of an ApsaraDB for MongoDB standalone, replica set, or serverless instance. Serverless instances are available only on the China site (aliyun.com).
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to standalone and replica set instances. To modify the specifications of sharded cluster instances, you can call the [ModifyNodeSpec](https://help.aliyun.com/document_detail/61911.html), [CreateNode](https://help.aliyun.com/document_detail/61922.html), [DeleteNode](https://help.aliyun.com/document_detail/61816.html), or [ModifyNodeSpecBatch](https://help.aliyun.com/document_detail/61923.html) operation.
        
        @param request: ModifyDBInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSpec',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_spec_with_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        """
        @summary Modifies the specifications or storage space of an ApsaraDB for MongoDB standalone, replica set, or serverless instance. Serverless instances are available only on the China site (aliyun.com).
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to standalone and replica set instances. To modify the specifications of sharded cluster instances, you can call the [ModifyNodeSpec](https://help.aliyun.com/document_detail/61911.html), [CreateNode](https://help.aliyun.com/document_detail/61922.html), [DeleteNode](https://help.aliyun.com/document_detail/61816.html), or [ModifyNodeSpecBatch](https://help.aliyun.com/document_detail/61923.html) operation.
        
        @param request: ModifyDBInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSpec',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_spec(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        """
        @summary Modifies the specifications or storage space of an ApsaraDB for MongoDB standalone, replica set, or serverless instance. Serverless instances are available only on the China site (aliyun.com).
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to standalone and replica set instances. To modify the specifications of sharded cluster instances, you can call the [ModifyNodeSpec](https://help.aliyun.com/document_detail/61911.html), [CreateNode](https://help.aliyun.com/document_detail/61922.html), [DeleteNode](https://help.aliyun.com/document_detail/61816.html), or [ModifyNodeSpecBatch](https://help.aliyun.com/document_detail/61923.html) operation.
        
        @param request: ModifyDBInstanceSpecRequest
        @return: ModifyDBInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    async def modify_dbinstance_spec_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceSpecRequest,
    ) -> dds_20151201_models.ModifyDBInstanceSpecResponse:
        """
        @summary Modifies the specifications or storage space of an ApsaraDB for MongoDB standalone, replica set, or serverless instance. Serverless instances are available only on the China site (aliyun.com).
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        This operation applies only to standalone and replica set instances. To modify the specifications of sharded cluster instances, you can call the [ModifyNodeSpec](https://help.aliyun.com/document_detail/61911.html), [CreateNode](https://help.aliyun.com/document_detail/61922.html), [DeleteNode](https://help.aliyun.com/document_detail/61816.html), or [ModifyNodeSpecBatch](https://help.aliyun.com/document_detail/61923.html) operation.
        
        @param request: ModifyDBInstanceSpecRequest
        @return: ModifyDBInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_spec_with_options_async(request, runtime)

    def modify_dbinstance_tdewith_options(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        """
        @summary Modifies the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance.
        
        @description TDE allows you to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to a disk and is decrypted when it is read from the disk to the memory. For more information, see [Configure TDE](https://help.aliyun.com/document_detail/131048.html).
        >  TDE cannot be disabled after it is enabled.
        Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        A replica set or sharded cluster instance is used.
        The storage engine of the instance is WiredTiger.
        The instance uses local disks to store data.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: ModifyDBInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryptor_name):
            query['EncryptorName'] = request.encryptor_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceTDE',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_tdewith_options_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        """
        @summary Modifies the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance.
        
        @description TDE allows you to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to a disk and is decrypted when it is read from the disk to the memory. For more information, see [Configure TDE](https://help.aliyun.com/document_detail/131048.html).
        >  TDE cannot be disabled after it is enabled.
        Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        A replica set or sharded cluster instance is used.
        The storage engine of the instance is WiredTiger.
        The instance uses local disks to store data.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: ModifyDBInstanceTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryptor_name):
            query['EncryptorName'] = request.encryptor_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceTDE',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_tde(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        """
        @summary Modifies the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance.
        
        @description TDE allows you to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to a disk and is decrypted when it is read from the disk to the memory. For more information, see [Configure TDE](https://help.aliyun.com/document_detail/131048.html).
        >  TDE cannot be disabled after it is enabled.
        Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        A replica set or sharded cluster instance is used.
        The storage engine of the instance is WiredTiger.
        The instance uses local disks to store data.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: ModifyDBInstanceTDERequest
        @return: ModifyDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    async def modify_dbinstance_tde_async(
        self,
        request: dds_20151201_models.ModifyDBInstanceTDERequest,
    ) -> dds_20151201_models.ModifyDBInstanceTDEResponse:
        """
        @summary Modifies the transparent data encryption (TDE) status of an ApsaraDB for MongoDB instance.
        
        @description TDE allows you to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to a disk and is decrypted when it is read from the disk to the memory. For more information, see [Configure TDE](https://help.aliyun.com/document_detail/131048.html).
        >  TDE cannot be disabled after it is enabled.
        Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        A replica set or sharded cluster instance is used.
        The storage engine of the instance is WiredTiger.
        The instance uses local disks to store data.
        The database engine version of the instance is 4.0 or 4.2. If the database engine version is earlier than 4.0, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine.
        
        @param request: ModifyDBInstanceTDERequest
        @return: ModifyDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_tdewith_options_async(request, runtime)

    def modify_global_security_ipgroup_with_options(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies the global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_with_options_async(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies the global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies the global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_with_options(request, runtime)

    async def modify_global_security_ipgroup_async(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies the global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_with_options_async(request, runtime)

    def modify_global_security_ipgroup_name_with_options(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupName',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyGlobalSecurityIPGroupNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_name_with_options_async(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupName',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyGlobalSecurityIPGroupNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_name(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_name_with_options(request, runtime)

    async def modify_global_security_ipgroup_name_async(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template associated with an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_name_with_options_async(request, runtime)

    def modify_global_security_ipgroup_relation_with_options(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the mapping between a global whitelist template and an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupRelation',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_relation_with_options_async(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the mapping between a global whitelist template and an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupRelation',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_relation(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the mapping between a global whitelist template and an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_relation_with_options(request, runtime)

    async def modify_global_security_ipgroup_relation_async(
        self,
        request: dds_20151201_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> dds_20151201_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the mapping between a global whitelist template and an ApsaraDB for MongoDB instance.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_relation_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is applicable to subscription instances.
        >  When auto-renewal is enabled, your payment will be collected nine days before the expiration date of ApsaraDB for MongoDB. Ensure that your account has sufficient balance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is applicable to subscription instances.
        >  When auto-renewal is enabled, your payment will be collected nine days before the expiration date of ApsaraDB for MongoDB. Ensure that your account has sufficient balance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is applicable to subscription instances.
        >  When auto-renewal is enabled, your payment will be collected nine days before the expiration date of ApsaraDB for MongoDB. Ensure that your account has sufficient balance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: dds_20151201_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> dds_20151201_models.ModifyInstanceAutoRenewalAttributeResponse:
        """
        @summary Enables or disables auto-renewal for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is applicable to subscription instances.
        >  When auto-renewal is enabled, your payment will be collected nine days before the expiration date of ApsaraDB for MongoDB. Ensure that your account has sufficient balance.
        
        @param request: ModifyInstanceAutoRenewalAttributeRequest
        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Disables password-free access over Virtual Private Cloud (VPC) for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The database engine version of the instance is 4.0 (with the minor version of mongodb_20190408_3.0.11 or later) or 4.2. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to view the database engine version of the instance. If necessary, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine version of the instance.
        The network type of the instance must be VPC. If the network type of the instance is classic network, you must call the [ModifyDBInstanceNetworkType](https://help.aliyun.com/document_detail/62138.html) operation to change the network type to VPC.
        You can only disable but not enable password-free access over VPC.
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVpcAuthModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAuthMode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyInstanceVpcAuthModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vpc_auth_mode_with_options_async(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Disables password-free access over Virtual Private Cloud (VPC) for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The database engine version of the instance is 4.0 (with the minor version of mongodb_20190408_3.0.11 or later) or 4.2. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to view the database engine version of the instance. If necessary, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine version of the instance.
        The network type of the instance must be VPC. If the network type of the instance is classic network, you must call the [ModifyDBInstanceNetworkType](https://help.aliyun.com/document_detail/62138.html) operation to change the network type to VPC.
        You can only disable but not enable password-free access over VPC.
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVpcAuthModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAuthMode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyInstanceVpcAuthModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vpc_auth_mode(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Disables password-free access over Virtual Private Cloud (VPC) for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The database engine version of the instance is 4.0 (with the minor version of mongodb_20190408_3.0.11 or later) or 4.2. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to view the database engine version of the instance. If necessary, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine version of the instance.
        The network type of the instance must be VPC. If the network type of the instance is classic network, you must call the [ModifyDBInstanceNetworkType](https://help.aliyun.com/document_detail/62138.html) operation to change the network type to VPC.
        You can only disable but not enable password-free access over VPC.
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @return: ModifyInstanceVpcAuthModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    async def modify_instance_vpc_auth_mode_async(
        self,
        request: dds_20151201_models.ModifyInstanceVpcAuthModeRequest,
    ) -> dds_20151201_models.ModifyInstanceVpcAuthModeResponse:
        """
        @summary Disables password-free access over Virtual Private Cloud (VPC) for an ApsaraDB for MongoDB instance.
        
        @description Before you call this operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is a replica set or sharded cluster instance.
        The database engine version of the instance is 4.0 (with the minor version of mongodb_20190408_3.0.11 or later) or 4.2. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to view the database engine version of the instance. If necessary, you can call the [UpgradeDBInstanceEngineVersion](https://help.aliyun.com/document_detail/67608.html) operation to upgrade the database engine version of the instance.
        The network type of the instance must be VPC. If the network type of the instance is classic network, you must call the [ModifyDBInstanceNetworkType](https://help.aliyun.com/document_detail/62138.html) operation to change the network type to VPC.
        You can only disable but not enable password-free access over VPC.
        
        @param request: ModifyInstanceVpcAuthModeRequest
        @return: ModifyInstanceVpcAuthModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_auth_mode_with_options_async(request, runtime)

    def modify_node_spec_with_options(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        """
        @summary Changes the specifications and storage capacity of a node of an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        > This operation is applicable only to sharded cluster instances.
        
        @param request: ModifyNodeSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.node_class):
            query['NodeClass'] = request.node_class
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeSpec',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyNodeSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_spec_with_options_async(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        """
        @summary Changes the specifications and storage capacity of a node of an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        > This operation is applicable only to sharded cluster instances.
        
        @param request: ModifyNodeSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.node_class):
            query['NodeClass'] = request.node_class
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeSpec',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyNodeSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_spec(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        """
        @summary Changes the specifications and storage capacity of a node of an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        > This operation is applicable only to sharded cluster instances.
        
        @param request: ModifyNodeSpecRequest
        @return: ModifyNodeSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_node_spec_with_options(request, runtime)

    async def modify_node_spec_async(
        self,
        request: dds_20151201_models.ModifyNodeSpecRequest,
    ) -> dds_20151201_models.ModifyNodeSpecResponse:
        """
        @summary Changes the specifications and storage capacity of a node of an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB.
        > This operation is applicable only to sharded cluster instances.
        
        @param request: ModifyNodeSpecRequest
        @return: ModifyNodeSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_node_spec_with_options_async(request, runtime)

    def modify_node_spec_batch_with_options(
        self,
        request: dds_20151201_models.ModifyNodeSpecBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyNodeSpecBatchResponse:
        """
        @summary Changes the configurations of mongos or shard nodes in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        This operation is applicable only to sharded cluster instances.
        When you upgrade or downgrade the configurations of multiple sharded cluster instances in batches, the specifications of the instances are limited. For example, if you want to expand the storage capacity of the instances, the storage capacity of the instances after expansion must be greater than the current capacity. When the specifications of multiple sharded cluster instances are different, limits are defined based on the specifications of a random sharded cluster instance. In this case, you may be unable to upgrade or downgrade the configurations of the instances. In this case, we recommend that you call the ModifyNodeSpec operation to individually change the configurations of each sharded cluster instance.
        
        @param request: ModifyNodeSpecBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeSpecBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeSpecBatch',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyNodeSpecBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_spec_batch_with_options_async(
        self,
        request: dds_20151201_models.ModifyNodeSpecBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyNodeSpecBatchResponse:
        """
        @summary Changes the configurations of mongos or shard nodes in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        This operation is applicable only to sharded cluster instances.
        When you upgrade or downgrade the configurations of multiple sharded cluster instances in batches, the specifications of the instances are limited. For example, if you want to expand the storage capacity of the instances, the storage capacity of the instances after expansion must be greater than the current capacity. When the specifications of multiple sharded cluster instances are different, limits are defined based on the specifications of a random sharded cluster instance. In this case, you may be unable to upgrade or downgrade the configurations of the instances. In this case, we recommend that you call the ModifyNodeSpec operation to individually change the configurations of each sharded cluster instance.
        
        @param request: ModifyNodeSpecBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeSpecBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNodeSpecBatch',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyNodeSpecBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_spec_batch(
        self,
        request: dds_20151201_models.ModifyNodeSpecBatchRequest,
    ) -> dds_20151201_models.ModifyNodeSpecBatchResponse:
        """
        @summary Changes the configurations of mongos or shard nodes in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        This operation is applicable only to sharded cluster instances.
        When you upgrade or downgrade the configurations of multiple sharded cluster instances in batches, the specifications of the instances are limited. For example, if you want to expand the storage capacity of the instances, the storage capacity of the instances after expansion must be greater than the current capacity. When the specifications of multiple sharded cluster instances are different, limits are defined based on the specifications of a random sharded cluster instance. In this case, you may be unable to upgrade or downgrade the configurations of the instances. In this case, we recommend that you call the ModifyNodeSpec operation to individually change the configurations of each sharded cluster instance.
        
        @param request: ModifyNodeSpecBatchRequest
        @return: ModifyNodeSpecBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_node_spec_batch_with_options(request, runtime)

    async def modify_node_spec_batch_async(
        self,
        request: dds_20151201_models.ModifyNodeSpecBatchRequest,
    ) -> dds_20151201_models.ModifyNodeSpecBatchResponse:
        """
        @summary Changes the configurations of mongos or shard nodes in an ApsaraDB for MongoDB sharded cluster instance.
        
        @description Make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB before you call this operation.
        This operation is applicable only to sharded cluster instances.
        When you upgrade or downgrade the configurations of multiple sharded cluster instances in batches, the specifications of the instances are limited. For example, if you want to expand the storage capacity of the instances, the storage capacity of the instances after expansion must be greater than the current capacity. When the specifications of multiple sharded cluster instances are different, limits are defined based on the specifications of a random sharded cluster instance. In this case, you may be unable to upgrade or downgrade the configurations of the instances. In this case, we recommend that you call the ModifyNodeSpec operation to individually change the configurations of each sharded cluster instance.
        
        @param request: ModifyNodeSpecBatchRequest
        @return: ModifyNodeSpecBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_node_spec_batch_with_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyParametersResponse:
        """
        @summary Modifies the parameters of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the Running state when you call this operation.
        If you call this operation to modify specific instance parameters and the modification for part of the parameters can take effect only after an instance restart, the instance is automatically restarted after this operation is called. You can call the [DescribeParameterTemplates](https://help.aliyun.com/document_detail/67618.html) operation to query the parameters that take effect only after the instance is restarted.
        
        @param request: ModifyParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameters_with_options_async(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyParametersResponse:
        """
        @summary Modifies the parameters of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the Running state when you call this operation.
        If you call this operation to modify specific instance parameters and the modification for part of the parameters can take effect only after an instance restart, the instance is automatically restarted after this operation is called. You can call the [DescribeParameterTemplates](https://help.aliyun.com/document_detail/67618.html) operation to query the parameters that take effect only after the instance is restarted.
        
        @param request: ModifyParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameters(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
    ) -> dds_20151201_models.ModifyParametersResponse:
        """
        @summary Modifies the parameters of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the Running state when you call this operation.
        If you call this operation to modify specific instance parameters and the modification for part of the parameters can take effect only after an instance restart, the instance is automatically restarted after this operation is called. You can call the [DescribeParameterTemplates](https://help.aliyun.com/document_detail/67618.html) operation to query the parameters that take effect only after the instance is restarted.
        
        @param request: ModifyParametersRequest
        @return: ModifyParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: dds_20151201_models.ModifyParametersRequest,
    ) -> dds_20151201_models.ModifyParametersResponse:
        """
        @summary Modifies the parameters of an ApsaraDB for MongoDB instance.
        
        @description    The instance must be in the Running state when you call this operation.
        If you call this operation to modify specific instance parameters and the modification for part of the parameters can take effect only after an instance restart, the instance is automatically restarted after this operation is called. You can call the [DescribeParameterTemplates](https://help.aliyun.com/document_detail/67618.html) operation to query the parameters that take effect only after the instance is restarted.
        
        @param request: ModifyParametersRequest
        @return: ModifyParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_resource_group_with_options(
        self,
        request: dds_20151201_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyResourceGroupResponse:
        """
        @summary Moves an ApsaraDB for MongoDB instance to a specified resource group.
        
        @description Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ModifyResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_group_with_options_async(
        self,
        request: dds_20151201_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyResourceGroupResponse:
        """
        @summary Moves an ApsaraDB for MongoDB instance to a specified resource group.
        
        @description Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ModifyResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceGroup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_group(
        self,
        request: dds_20151201_models.ModifyResourceGroupRequest,
    ) -> dds_20151201_models.ModifyResourceGroupResponse:
        """
        @summary Moves an ApsaraDB for MongoDB instance to a specified resource group.
        
        @description Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ModifyResourceGroupRequest
        @return: ModifyResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    async def modify_resource_group_async(
        self,
        request: dds_20151201_models.ModifyResourceGroupRequest,
    ) -> dds_20151201_models.ModifyResourceGroupResponse:
        """
        @summary Moves an ApsaraDB for MongoDB instance to a specified resource group.
        
        @description Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ModifyResourceGroupRequest
        @return: ModifyResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_group_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to modify an ECS Security group that is bound to an ApsaraDB for MongoDB instance.
        
        @description >  For a sharded cluster instance, the bound ECS security group takes effect only for mongos nodes.
        
        @param request: ModifySecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifySecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to modify an ECS Security group that is bound to an ApsaraDB for MongoDB instance.
        
        @description >  For a sharded cluster instance, the bound ECS security group takes effect only for mongos nodes.
        
        @param request: ModifySecurityGroupConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifySecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to modify an ECS Security group that is bound to an ApsaraDB for MongoDB instance.
        
        @description >  For a sharded cluster instance, the bound ECS security group takes effect only for mongos nodes.
        
        @param request: ModifySecurityGroupConfigurationRequest
        @return: ModifySecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: dds_20151201_models.ModifySecurityGroupConfigurationRequest,
    ) -> dds_20151201_models.ModifySecurityGroupConfigurationResponse:
        """
        @summary You can call this operation to modify an ECS Security group that is bound to an ApsaraDB for MongoDB instance.
        
        @description >  For a sharded cluster instance, the bound ECS security group takes effect only for mongos nodes.
        
        @param request: ModifySecurityGroupConfigurationRequest
        @return: ModifySecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for MongoDB instance.
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not UtilClient.is_unset(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for MongoDB instance.
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not UtilClient.is_unset(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for MongoDB instance.
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: dds_20151201_models.ModifySecurityIpsRequest,
    ) -> dds_20151201_models.ModifySecurityIpsResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for MongoDB instance.
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_task_info_with_options(
        self,
        request: dds_20151201_models.ModifyTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyTaskInfoResponse:
        """
        @summary Modifies the information of a task in the task center for an ApsaraDB for MongoDB instance.
        
        @description The actions performed by this operation for a task vary based on the current state of the task. The supported actions for a task can be obtained from the value of the actionInfo parameter in the DescribeHistoryTasks operation.
        
        @param request: ModifyTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_params):
            query['ActionParams'] = request.action_params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.step_name):
            query['StepName'] = request.step_name
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTaskInfo',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_task_info_with_options_async(
        self,
        request: dds_20151201_models.ModifyTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ModifyTaskInfoResponse:
        """
        @summary Modifies the information of a task in the task center for an ApsaraDB for MongoDB instance.
        
        @description The actions performed by this operation for a task vary based on the current state of the task. The supported actions for a task can be obtained from the value of the actionInfo parameter in the DescribeHistoryTasks operation.
        
        @param request: ModifyTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_params):
            query['ActionParams'] = request.action_params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.step_name):
            query['StepName'] = request.step_name
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTaskInfo',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ModifyTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_task_info(
        self,
        request: dds_20151201_models.ModifyTaskInfoRequest,
    ) -> dds_20151201_models.ModifyTaskInfoResponse:
        """
        @summary Modifies the information of a task in the task center for an ApsaraDB for MongoDB instance.
        
        @description The actions performed by this operation for a task vary based on the current state of the task. The supported actions for a task can be obtained from the value of the actionInfo parameter in the DescribeHistoryTasks operation.
        
        @param request: ModifyTaskInfoRequest
        @return: ModifyTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_task_info_with_options(request, runtime)

    async def modify_task_info_async(
        self,
        request: dds_20151201_models.ModifyTaskInfoRequest,
    ) -> dds_20151201_models.ModifyTaskInfoResponse:
        """
        @summary Modifies the information of a task in the task center for an ApsaraDB for MongoDB instance.
        
        @description The actions performed by this operation for a task vary based on the current state of the task. The supported actions for a task can be obtained from the value of the actionInfo parameter in the DescribeHistoryTasks operation.
        
        @param request: ModifyTaskInfoRequest
        @return: ModifyTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_task_info_with_options_async(request, runtime)

    def release_node_private_network_address_with_options(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        """
        @summary Releases the internal endpoint of a shard or Configserver node in a sharded cluster instance.
        
        @description    This operation can be used to release the internal endpoint of a shard or Configserver node in a sharded cluster instance. For more information, see [Release the endpoint of a shard or Configserver node](https://help.aliyun.com/document_detail/134067.html).
        To release the public endpoint of a shard or Configserver node in a sharded cluster instance, you can call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation.
        
        @param request: ReleaseNodePrivateNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseNodePrivateNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseNodePrivateNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_node_private_network_address_with_options_async(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        """
        @summary Releases the internal endpoint of a shard or Configserver node in a sharded cluster instance.
        
        @description    This operation can be used to release the internal endpoint of a shard or Configserver node in a sharded cluster instance. For more information, see [Release the endpoint of a shard or Configserver node](https://help.aliyun.com/document_detail/134067.html).
        To release the public endpoint of a shard or Configserver node in a sharded cluster instance, you can call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation.
        
        @param request: ReleaseNodePrivateNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseNodePrivateNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseNodePrivateNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_node_private_network_address(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        """
        @summary Releases the internal endpoint of a shard or Configserver node in a sharded cluster instance.
        
        @description    This operation can be used to release the internal endpoint of a shard or Configserver node in a sharded cluster instance. For more information, see [Release the endpoint of a shard or Configserver node](https://help.aliyun.com/document_detail/134067.html).
        To release the public endpoint of a shard or Configserver node in a sharded cluster instance, you can call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation.
        
        @param request: ReleaseNodePrivateNetworkAddressRequest
        @return: ReleaseNodePrivateNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_node_private_network_address_with_options(request, runtime)

    async def release_node_private_network_address_async(
        self,
        request: dds_20151201_models.ReleaseNodePrivateNetworkAddressRequest,
    ) -> dds_20151201_models.ReleaseNodePrivateNetworkAddressResponse:
        """
        @summary Releases the internal endpoint of a shard or Configserver node in a sharded cluster instance.
        
        @description    This operation can be used to release the internal endpoint of a shard or Configserver node in a sharded cluster instance. For more information, see [Release the endpoint of a shard or Configserver node](https://help.aliyun.com/document_detail/134067.html).
        To release the public endpoint of a shard or Configserver node in a sharded cluster instance, you can call the [ReleasePublicNetworkAddress](https://help.aliyun.com/document_detail/67604.html) operation.
        
        @param request: ReleaseNodePrivateNetworkAddressRequest
        @return: ReleaseNodePrivateNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_node_private_network_address_with_options_async(request, runtime)

    def release_public_network_address_with_options(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for MongoDB instance.
        
        @param request: ReleasePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ReleasePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_public_network_address_with_options_async(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for MongoDB instance.
        
        @param request: ReleasePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicNetworkAddress',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ReleasePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_public_network_address(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for MongoDB instance.
        
        @param request: ReleasePublicNetworkAddressRequest
        @return: ReleasePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_public_network_address_with_options(request, runtime)

    async def release_public_network_address_async(
        self,
        request: dds_20151201_models.ReleasePublicNetworkAddressRequest,
    ) -> dds_20151201_models.ReleasePublicNetworkAddressResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for MongoDB instance.
        
        @param request: ReleasePublicNetworkAddressRequest
        @return: ReleasePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_public_network_address_with_options_async(request, runtime)

    def renew_dbinstance_with_options(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        """
        @summary Manually renews an ApsaraDB for MongoDB subscription instance.
        
        @description Make sure that you fully understand the billing methods and pricing of ApsaraDB for MongoDB before you call this operation. For more information about the pricing of ApsaraDB for MongoDB, visit the [pricing tab of the product buy page](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is only applicable to instances that use the subscription billing method.
        
        @param request: RenewDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.RenewDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        """
        @summary Manually renews an ApsaraDB for MongoDB subscription instance.
        
        @description Make sure that you fully understand the billing methods and pricing of ApsaraDB for MongoDB before you call this operation. For more information about the pricing of ApsaraDB for MongoDB, visit the [pricing tab of the product buy page](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is only applicable to instances that use the subscription billing method.
        
        @param request: RenewDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.RenewDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_dbinstance(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        """
        @summary Manually renews an ApsaraDB for MongoDB subscription instance.
        
        @description Make sure that you fully understand the billing methods and pricing of ApsaraDB for MongoDB before you call this operation. For more information about the pricing of ApsaraDB for MongoDB, visit the [pricing tab of the product buy page](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is only applicable to instances that use the subscription billing method.
        
        @param request: RenewDBInstanceRequest
        @return: RenewDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_dbinstance_with_options(request, runtime)

    async def renew_dbinstance_async(
        self,
        request: dds_20151201_models.RenewDBInstanceRequest,
    ) -> dds_20151201_models.RenewDBInstanceResponse:
        """
        @summary Manually renews an ApsaraDB for MongoDB subscription instance.
        
        @description Make sure that you fully understand the billing methods and pricing of ApsaraDB for MongoDB before you call this operation. For more information about the pricing of ApsaraDB for MongoDB, visit the [pricing tab of the product buy page](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        This operation is only applicable to instances that use the subscription billing method.
        
        @param request: RenewDBInstanceRequest
        @return: RenewDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_dbinstance_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of the root account in an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to reset only the password of the root account of an instance.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of the root account in an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to reset only the password of the root account of an instance.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.character_type):
            query['CharacterType'] = request.character_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of the root account in an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to reset only the password of the root account of an instance.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: dds_20151201_models.ResetAccountPasswordRequest,
    ) -> dds_20151201_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of the root account in an ApsaraDB for MongoDB instance.
        
        @description >  This operation can be used to reset only the password of the root account of an instance.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for MongoDB instance.
        
        @description This operation can also be used to restart an instance, or restart a shard or mongos node in a sharded cluster instance.
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for MongoDB instance.
        
        @description This operation can also be used to restart an instance, or restart a shard or mongos node in a sharded cluster instance.
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for MongoDB instance.
        
        @description This operation can also be used to restart an instance, or restart a shard or mongos node in a sharded cluster instance.
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: dds_20151201_models.RestartDBInstanceRequest,
    ) -> dds_20151201_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for MongoDB instance.
        
        @description This operation can also be used to restart an instance, or restart a shard or mongos node in a sharded cluster instance.
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def restart_node_with_options(
        self,
        request: dds_20151201_models.RestartNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestartNodeResponse:
        """
        @summary Restarts a node in an ApsaraDB for MongoDB instance.
        
        @description You can call this operation to restart a node in a replica set instance or a child instance in a sharded cluster instance.
        >  When you call this operation, the instance must meet the following requirements:
        The instance is in the Running state.
        The instance is a replica set or sharded cluster instance of the standard edition.
        
        @param request: RestartNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartNode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.RestartNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_node_with_options_async(
        self,
        request: dds_20151201_models.RestartNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.RestartNodeResponse:
        """
        @summary Restarts a node in an ApsaraDB for MongoDB instance.
        
        @description You can call this operation to restart a node in a replica set instance or a child instance in a sharded cluster instance.
        >  When you call this operation, the instance must meet the following requirements:
        The instance is in the Running state.
        The instance is a replica set or sharded cluster instance of the standard edition.
        
        @param request: RestartNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartNode',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.RestartNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_node(
        self,
        request: dds_20151201_models.RestartNodeRequest,
    ) -> dds_20151201_models.RestartNodeResponse:
        """
        @summary Restarts a node in an ApsaraDB for MongoDB instance.
        
        @description You can call this operation to restart a node in a replica set instance or a child instance in a sharded cluster instance.
        >  When you call this operation, the instance must meet the following requirements:
        The instance is in the Running state.
        The instance is a replica set or sharded cluster instance of the standard edition.
        
        @param request: RestartNodeRequest
        @return: RestartNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_node_with_options(request, runtime)

    async def restart_node_async(
        self,
        request: dds_20151201_models.RestartNodeRequest,
    ) -> dds_20151201_models.RestartNodeResponse:
        """
        @summary Restarts a node in an ApsaraDB for MongoDB instance.
        
        @description You can call this operation to restart a node in a replica set instance or a child instance in a sharded cluster instance.
        >  When you call this operation, the instance must meet the following requirements:
        The instance is in the Running state.
        The instance is a replica set or sharded cluster instance of the standard edition.
        
        @param request: RestartNodeRequest
        @return: RestartNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_node_with_options_async(request, runtime)

    def switch_dbinstance_hawith_options(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        """
        @summary Switches the primary and secondary nodes for an ApsaraDB for MongoDB instance.
        
        @description The instance must be running when you call this operation.
        >
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        On replica set instances, the switch is performed between instances. On sharded cluster instances, the switch is performed between shards.
        
        @param request: SwitchDBInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchDBInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.SwitchDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_hawith_options_async(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        """
        @summary Switches the primary and secondary nodes for an ApsaraDB for MongoDB instance.
        
        @description The instance must be running when you call this operation.
        >
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        On replica set instances, the switch is performed between instances. On sharded cluster instances, the switch is performed between shards.
        
        @param request: SwitchDBInstanceHARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchDBInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.SwitchDBInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dbinstance_ha(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        """
        @summary Switches the primary and secondary nodes for an ApsaraDB for MongoDB instance.
        
        @description The instance must be running when you call this operation.
        >
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        On replica set instances, the switch is performed between instances. On sharded cluster instances, the switch is performed between shards.
        
        @param request: SwitchDBInstanceHARequest
        @return: SwitchDBInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    async def switch_dbinstance_ha_async(
        self,
        request: dds_20151201_models.SwitchDBInstanceHARequest,
    ) -> dds_20151201_models.SwitchDBInstanceHAResponse:
        """
        @summary Switches the primary and secondary nodes for an ApsaraDB for MongoDB instance.
        
        @description The instance must be running when you call this operation.
        >
        This operation is applicable to replica set instances and sharded cluster instances, but cannot be performed on standalone instances.
        On replica set instances, the switch is performed between instances. On sharded cluster instances, the switch is performed between shards.
        
        @param request: SwitchDBInstanceHARequest
        @return: SwitchDBInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_hawith_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dds_20151201_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TagResourcesResponse:
        """
        @summary Binds tags to ApsaraDB for MongoDB instances.
        
        @description If you have a large number of instances, you can create multiple tags, bind the tags to the instances, and filter the instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and bound to the specified instance.
        If a tag that has the same key is already bound to the instance, the new tag overwrites the existing tag.
        You can bind up to 20 tags to each instance.
        You can bind tags to up to 50 instances each time you call the operation.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: dds_20151201_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TagResourcesResponse:
        """
        @summary Binds tags to ApsaraDB for MongoDB instances.
        
        @description If you have a large number of instances, you can create multiple tags, bind the tags to the instances, and filter the instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and bound to the specified instance.
        If a tag that has the same key is already bound to the instance, the new tag overwrites the existing tag.
        You can bind up to 20 tags to each instance.
        You can bind tags to up to 50 instances each time you call the operation.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: dds_20151201_models.TagResourcesRequest,
    ) -> dds_20151201_models.TagResourcesResponse:
        """
        @summary Binds tags to ApsaraDB for MongoDB instances.
        
        @description If you have a large number of instances, you can create multiple tags, bind the tags to the instances, and filter the instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and bound to the specified instance.
        If a tag that has the same key is already bound to the instance, the new tag overwrites the existing tag.
        You can bind up to 20 tags to each instance.
        You can bind tags to up to 50 instances each time you call the operation.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dds_20151201_models.TagResourcesRequest,
    ) -> dds_20151201_models.TagResourcesResponse:
        """
        @summary Binds tags to ApsaraDB for MongoDB instances.
        
        @description If you have a large number of instances, you can create multiple tags, bind the tags to the instances, and filter the instances by tag.
        A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        If the tag that you specify does not exist, this tag is automatically created and bound to the specified instance.
        If a tag that has the same key is already bound to the instance, the new tag overwrites the existing tag.
        You can bind up to 20 tags to each instance.
        You can bind tags to up to 50 instances each time you call the operation.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transfer_cluster_backup_with_options(
        self,
        request: dds_20151201_models.TransferClusterBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransferClusterBackupResponse:
        """
        @summary Switches the backup mode of an ApsaraDB for MongoDB sharded cluster instance to the cluster backup mode. After the instance is switched to the cluster backup mode, the instance supports high-frequency backup.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. Cloud disk-based sharded cluster instances that are created on or after October 19, 2023 are set to the cluster backup mode by default.
        
        @param request: TransferClusterBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferClusterBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferClusterBackup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TransferClusterBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_cluster_backup_with_options_async(
        self,
        request: dds_20151201_models.TransferClusterBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransferClusterBackupResponse:
        """
        @summary Switches the backup mode of an ApsaraDB for MongoDB sharded cluster instance to the cluster backup mode. After the instance is switched to the cluster backup mode, the instance supports high-frequency backup.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. Cloud disk-based sharded cluster instances that are created on or after October 19, 2023 are set to the cluster backup mode by default.
        
        @param request: TransferClusterBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferClusterBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferClusterBackup',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TransferClusterBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_cluster_backup(
        self,
        request: dds_20151201_models.TransferClusterBackupRequest,
    ) -> dds_20151201_models.TransferClusterBackupResponse:
        """
        @summary Switches the backup mode of an ApsaraDB for MongoDB sharded cluster instance to the cluster backup mode. After the instance is switched to the cluster backup mode, the instance supports high-frequency backup.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. Cloud disk-based sharded cluster instances that are created on or after October 19, 2023 are set to the cluster backup mode by default.
        
        @param request: TransferClusterBackupRequest
        @return: TransferClusterBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_cluster_backup_with_options(request, runtime)

    async def transfer_cluster_backup_async(
        self,
        request: dds_20151201_models.TransferClusterBackupRequest,
    ) -> dds_20151201_models.TransferClusterBackupResponse:
        """
        @summary Switches the backup mode of an ApsaraDB for MongoDB sharded cluster instance to the cluster backup mode. After the instance is switched to the cluster backup mode, the instance supports high-frequency backup.
        
        @description    The instance is an ApsaraDB for MongoDB sharded cluster instance that runs MongoDB 4.4 or later and uses enhanced SSDs (ESSDs) to store data.
        You can call the TransferClusterBackup operation only for instances that are created before October 19, 2023 to switch the instances to the cluster backup mode. Cloud disk-based sharded cluster instances that are created on or after October 19, 2023 are set to the cluster backup mode by default.
        
        @param request: TransferClusterBackupRequest
        @return: TransferClusterBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_cluster_backup_with_options_async(request, runtime)

    def transform_instance_charge_type_with_options(
        self,
        request: dds_20151201_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an instance from pay-as-you-go to subscription or from subscription to pay-as-you-go.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the Running state.
        Your instance has no unpaid billing method change orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        > To change the billing method of an instance whose instance type is no longer available to purchase, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to change the instance type first.
        
        @param request: TransformInstanceChargeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformInstanceChargeType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TransformInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_instance_charge_type_with_options_async(
        self,
        request: dds_20151201_models.TransformInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an instance from pay-as-you-go to subscription or from subscription to pay-as-you-go.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the Running state.
        Your instance has no unpaid billing method change orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        > To change the billing method of an instance whose instance type is no longer available to purchase, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to change the instance type first.
        
        @param request: TransformInstanceChargeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformInstanceChargeType',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TransformInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_instance_charge_type(
        self,
        request: dds_20151201_models.TransformInstanceChargeTypeRequest,
    ) -> dds_20151201_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an instance from pay-as-you-go to subscription or from subscription to pay-as-you-go.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the Running state.
        Your instance has no unpaid billing method change orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        > To change the billing method of an instance whose instance type is no longer available to purchase, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to change the instance type first.
        
        @param request: TransformInstanceChargeTypeRequest
        @return: TransformInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transform_instance_charge_type_with_options(request, runtime)

    async def transform_instance_charge_type_async(
        self,
        request: dds_20151201_models.TransformInstanceChargeTypeRequest,
    ) -> dds_20151201_models.TransformInstanceChargeTypeResponse:
        """
        @summary Changes the billing method of an instance from pay-as-you-go to subscription or from subscription to pay-as-you-go.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/product/apsaradb-for-mongodb/pricing) of ApsaraDB for MongoDB
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the Running state.
        Your instance has no unpaid billing method change orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        > To change the billing method of an instance whose instance type is no longer available to purchase, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to change the instance type first.
        
        @param request: TransformInstanceChargeTypeRequest
        @return: TransformInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transform_instance_charge_type_with_options_async(request, runtime)

    def transform_to_pre_paid_with_options(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for MongoDB instance from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        A subscription instance cannot be changed to a pay-as-you-go instance. To avoid wasting resources, proceed with caution.
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the running state.
        The billing method of the instance is pay-as-you-go.
        The instance has no unpaid subscription orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        >  To change the billing method of an instance whose instance type is no longer available to subscription, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to first change the instance type.
        
        @param request: TransformToPrePaidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformToPrePaidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformToPrePaid',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TransformToPrePaidResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_to_pre_paid_with_options_async(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for MongoDB instance from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        A subscription instance cannot be changed to a pay-as-you-go instance. To avoid wasting resources, proceed with caution.
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the running state.
        The billing method of the instance is pay-as-you-go.
        The instance has no unpaid subscription orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        >  To change the billing method of an instance whose instance type is no longer available to subscription, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to first change the instance type.
        
        @param request: TransformToPrePaidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformToPrePaidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformToPrePaid',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.TransformToPrePaidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_to_pre_paid(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for MongoDB instance from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        A subscription instance cannot be changed to a pay-as-you-go instance. To avoid wasting resources, proceed with caution.
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the running state.
        The billing method of the instance is pay-as-you-go.
        The instance has no unpaid subscription orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        >  To change the billing method of an instance whose instance type is no longer available to subscription, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to first change the instance type.
        
        @param request: TransformToPrePaidRequest
        @return: TransformToPrePaidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    async def transform_to_pre_paid_async(
        self,
        request: dds_20151201_models.TransformToPrePaidRequest,
    ) -> dds_20151201_models.TransformToPrePaidResponse:
        """
        @summary Changes the billing method of an ApsaraDB for MongoDB instance from pay-as-you-go to subscription.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing).
        A subscription instance cannot be changed to a pay-as-you-go instance. To avoid wasting resources, proceed with caution.
        Before you call this API operation, make sure that the ApsaraDB for MongoDB instance meets the following requirements:
        The instance is in the running state.
        The billing method of the instance is pay-as-you-go.
        The instance has no unpaid subscription orders.
        The instance type is available for purchase. For more information about unavailable instance types, see [Instance types](https://help.aliyun.com/document_detail/57141.html).
        >  To change the billing method of an instance whose instance type is no longer available to subscription, call the [ModifyDBInstanceSpec](https://help.aliyun.com/document_detail/61816.html) or [ModifyNodeSpec](https://help.aliyun.com/document_detail/61923.html) operation to first change the instance type.
        
        @param request: TransformToPrePaidRequest
        @return: TransformToPrePaidResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transform_to_pre_paid_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UntagResourcesResponse:
        """
        @summary Removes a tag if the tag is not added to another instance.
        
        @description >
        You can remove up to 20 tags at a time.
        If you remove a tag from all instances, the tag is automatically deleted.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UntagResourcesResponse:
        """
        @summary Removes a tag if the tag is not added to another instance.
        
        @description >
        You can remove up to 20 tags at a time.
        If you remove a tag from all instances, the tag is automatically deleted.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
    ) -> dds_20151201_models.UntagResourcesResponse:
        """
        @summary Removes a tag if the tag is not added to another instance.
        
        @description >
        You can remove up to 20 tags at a time.
        If you remove a tag from all instances, the tag is automatically deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dds_20151201_models.UntagResourcesRequest,
    ) -> dds_20151201_models.UntagResourcesResponse:
        """
        @summary Removes a tag if the tag is not added to another instance.
        
        @description >
        You can remove up to 20 tags at a time.
        If you remove a tag from all instances, the tag is automatically deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Upgrades the database version of an ApsaraDB for MongoDB instance.
        
        @description The instance must be in the running state when you call this operation.
        >  The available database versions depend on the storage engine used by the instance. For more information, see [Upgrades of MongoDB major versions](https://help.aliyun.com/document_detail/398673.html). You can also call the [DescribeAvailableEngineVersion](https://help.aliyun.com/document_detail/141355.html) operation to query the available database versions.
        >  You cannot downgrade the MongoDB version of an instance after you upgrade it.
        >  The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.UpgradeDBInstanceEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_engine_version_with_options_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Upgrades the database version of an ApsaraDB for MongoDB instance.
        
        @description The instance must be in the running state when you call this operation.
        >  The available database versions depend on the storage engine used by the instance. For more information, see [Upgrades of MongoDB major versions](https://help.aliyun.com/document_detail/398673.html). You can also call the [DescribeAvailableEngineVersion](https://help.aliyun.com/document_detail/141355.html) operation to query the available database versions.
        >  You cannot downgrade the MongoDB version of an instance after you upgrade it.
        >  The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.UpgradeDBInstanceEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_engine_version(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Upgrades the database version of an ApsaraDB for MongoDB instance.
        
        @description The instance must be in the running state when you call this operation.
        >  The available database versions depend on the storage engine used by the instance. For more information, see [Upgrades of MongoDB major versions](https://help.aliyun.com/document_detail/398673.html). You can also call the [DescribeAvailableEngineVersion](https://help.aliyun.com/document_detail/141355.html) operation to query the available database versions.
        >  You cannot downgrade the MongoDB version of an instance after you upgrade it.
        >  The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    async def upgrade_dbinstance_engine_version_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Upgrades the database version of an ApsaraDB for MongoDB instance.
        
        @description The instance must be in the running state when you call this operation.
        >  The available database versions depend on the storage engine used by the instance. For more information, see [Upgrades of MongoDB major versions](https://help.aliyun.com/document_detail/398673.html). You can also call the [DescribeAvailableEngineVersion](https://help.aliyun.com/document_detail/141355.html) operation to query the available database versions.
        >  You cannot downgrade the MongoDB version of an instance after you upgrade it.
        >  The instance is automatically restarted for two to three times during the upgrade process. Make sure that you upgrade the instance during off-peak hours.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_engine_version_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @summary Upgrades the minor version of an ApsaraDB for MongoDB instance.
        
        @description When you call the UpgradeDBInstanceKernelVersion operation, the instance must be in the Running state.
        >  The UpgradeDBInstanceKernelVersion operation is applicable to replica set and sharded cluster instances, but not to standalone instances.
        >  The instance will be restarted once during the upgrade. Call this operation during off-peak hours.
        
        @param request: UpgradeDBInstanceKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.UpgradeDBInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @summary Upgrades the minor version of an ApsaraDB for MongoDB instance.
        
        @description When you call the UpgradeDBInstanceKernelVersion operation, the instance must be in the Running state.
        >  The UpgradeDBInstanceKernelVersion operation is applicable to replica set and sharded cluster instances, but not to standalone instances.
        >  The instance will be restarted once during the upgrade. Call this operation during off-peak hours.
        
        @param request: UpgradeDBInstanceKernelVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2015-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dds_20151201_models.UpgradeDBInstanceKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @summary Upgrades the minor version of an ApsaraDB for MongoDB instance.
        
        @description When you call the UpgradeDBInstanceKernelVersion operation, the instance must be in the Running state.
        >  The UpgradeDBInstanceKernelVersion operation is applicable to replica set and sharded cluster instances, but not to standalone instances.
        >  The instance will be restarted once during the upgrade. Call this operation during off-peak hours.
        
        @param request: UpgradeDBInstanceKernelVersionRequest
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: dds_20151201_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> dds_20151201_models.UpgradeDBInstanceKernelVersionResponse:
        """
        @summary Upgrades the minor version of an ApsaraDB for MongoDB instance.
        
        @description When you call the UpgradeDBInstanceKernelVersion operation, the instance must be in the Running state.
        >  The UpgradeDBInstanceKernelVersion operation is applicable to replica set and sharded cluster instances, but not to standalone instances.
        >  The instance will be restarted once during the upgrade. Call this operation during off-peak hours.
        
        @param request: UpgradeDBInstanceKernelVersionRequest
        @return: UpgradeDBInstanceKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)
