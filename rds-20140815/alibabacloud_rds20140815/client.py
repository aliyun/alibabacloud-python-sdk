# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rds20140815 import models as rds_20140815_models
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
            'cn-qingdao': 'rds.aliyuncs.com',
            'cn-beijing': 'rds.aliyuncs.com',
            'cn-hangzhou': 'rds.aliyuncs.com',
            'cn-shanghai': 'rds.aliyuncs.com',
            'cn-shenzhen': 'rds.aliyuncs.com',
            'cn-heyuan': 'rds.aliyuncs.com',
            'cn-hongkong': 'rds.aliyuncs.com',
            'ap-southeast-1': 'rds.aliyuncs.com',
            'us-west-1': 'rds.aliyuncs.com',
            'us-east-1': 'rds.aliyuncs.com',
            'cn-shanghai-finance-1': 'rds.aliyuncs.com',
            'cn-shenzhen-finance-1': 'rds.aliyuncs.com',
            'cn-north-2-gov-1': 'rds.aliyuncs.com',
            'ap-northeast-2-pop': 'rds.aliyuncs.com',
            'cn-beijing-finance-1': 'rds.aliyuncs.com',
            'cn-beijing-finance-pop': 'rds.aliyuncs.com',
            'cn-beijing-gov-1': 'rds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'rds.aliyuncs.com',
            'cn-edge-1': 'rds.aliyuncs.com',
            'cn-fujian': 'rds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'rds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'rds.aliyuncs.com',
            'cn-hangzhou-finance': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'rds.aliyuncs.com',
            'cn-hangzhou-test-306': 'rds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'rds.aliyuncs.com',
            'cn-qingdao-nebula': 'rds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'rds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'rds.aliyuncs.com',
            'cn-shanghai-inner': 'rds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'rds.aliyuncs.com',
            'cn-shenzhen-inner': 'rds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'rds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'rds.aliyuncs.com',
            'cn-wuhan': 'rds.aliyuncs.com',
            'cn-yushanfang': 'rds.aliyuncs.com',
            'cn-zhangbei': 'rds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'rds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'rds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'rds.aliyuncs.com',
            'eu-west-1-oxs': 'rds.aliyuncs.com',
            'rus-west-1-pop': 'rds.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('rds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_tags_to_resource_with_options(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTagsToResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AddTagsToResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_to_resource_with_options_async(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTagsToResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AddTagsToResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags_to_resource(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_resource_with_options(request, runtime)

    async def add_tags_to_resource_async(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_to_resource_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def allocate_read_write_splitting_connection_with_options(
        self,
        request: rds_20140815_models.AllocateReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AllocateReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['MaxDelayTime'] = request.max_delay_time
        query['NetType'] = request.net_type
        query['DistributionType'] = request.distribution_type
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_read_write_splitting_connection_with_options_async(
        self,
        request: rds_20140815_models.AllocateReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AllocateReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['MaxDelayTime'] = request.max_delay_time
        query['NetType'] = request.net_type
        query['DistributionType'] = request.distribution_type
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateReadWriteSplittingConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_read_write_splitting_connection(
        self,
        request: rds_20140815_models.AllocateReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.AllocateReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_read_write_splitting_connection_with_options(request, runtime)

    async def allocate_read_write_splitting_connection_async(
        self,
        request: rds_20140815_models.AllocateReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.AllocateReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_read_write_splitting_connection_with_options_async(request, runtime)

    def calculate_dbinstance_weight_with_options(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CalculateDBInstanceWeight',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CalculateDBInstanceWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def calculate_dbinstance_weight_with_options_async(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CalculateDBInstanceWeight',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CalculateDBInstanceWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def calculate_dbinstance_weight(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.calculate_dbinstance_weight_with_options(request, runtime)

    async def calculate_dbinstance_weight_async(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.calculate_dbinstance_weight_with_options_async(request, runtime)

    def cancel_import_with_options(
        self,
        request: rds_20140815_models.CancelImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CancelImportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ImportId'] = request.import_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelImport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CancelImportResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_import_with_options_async(
        self,
        request: rds_20140815_models.CancelImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CancelImportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ImportId'] = request.import_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelImport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CancelImportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_import(
        self,
        request: rds_20140815_models.CancelImportRequest,
    ) -> rds_20140815_models.CancelImportResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_import_with_options(request, runtime)

    async def cancel_import_async(
        self,
        request: rds_20140815_models.CancelImportRequest,
    ) -> rds_20140815_models.CancelImportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_import_with_options_async(request, runtime)

    def check_account_name_available_with_options(
        self,
        request: rds_20140815_models.CheckAccountNameAvailableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckAccountNameAvailableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckAccountNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckAccountNameAvailableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_name_available_with_options_async(
        self,
        request: rds_20140815_models.CheckAccountNameAvailableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckAccountNameAvailableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckAccountNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckAccountNameAvailableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account_name_available(
        self,
        request: rds_20140815_models.CheckAccountNameAvailableRequest,
    ) -> rds_20140815_models.CheckAccountNameAvailableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_account_name_available_with_options(request, runtime)

    async def check_account_name_available_async(
        self,
        request: rds_20140815_models.CheckAccountNameAvailableRequest,
    ) -> rds_20140815_models.CheckAccountNameAvailableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_account_name_available_with_options_async(request, runtime)

    def check_cloud_resource_authorized_with_options(
        self,
        request: rds_20140815_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: rds_20140815_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCloudResourceAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: rds_20140815_models.CheckCloudResourceAuthorizedRequest,
    ) -> rds_20140815_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: rds_20140815_models.CheckCloudResourceAuthorizedRequest,
    ) -> rds_20140815_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def check_create_ddr_dbinstance_with_options(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['RestoreType'] = request.restore_type
        query['BackupSetId'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['BinlogName'] = request.binlog_name
        query['BinlogPosition'] = request.binlog_position
        query['BinlogRole'] = request.binlog_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckCreateDdrDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCreateDdrDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_create_ddr_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['RestoreType'] = request.restore_type
        query['BackupSetId'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['BinlogName'] = request.binlog_name
        query['BinlogPosition'] = request.binlog_position
        query['BinlogRole'] = request.binlog_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckCreateDdrDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCreateDdrDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_create_ddr_dbinstance(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_create_ddr_dbinstance_with_options(request, runtime)

    async def check_create_ddr_dbinstance_async(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_create_ddr_dbinstance_with_options_async(request, runtime)

    def check_dbname_available_with_options(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckDBNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckDBNameAvailableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_dbname_available_with_options_async(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckDBNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckDBNameAvailableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_dbname_available(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_available_with_options(request, runtime)

    async def check_dbname_available_async(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_dbname_available_with_options_async(request, runtime)

    def check_instance_exist_with_options(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckInstanceExist',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckInstanceExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_exist_with_options_async(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckInstanceExist',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckInstanceExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_exist(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_instance_exist_with_options(request, runtime)

    async def check_instance_exist_async(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_instance_exist_with_options_async(request, runtime)

    def clear_dedicated_host_with_options(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClearDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ClearDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClearDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ClearDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_dedicated_host(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_dedicated_host_with_options(request, runtime)

    async def clear_dedicated_host_async(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_dedicated_host_with_options_async(request, runtime)

    def clone_dbinstance_with_options(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['DbNames'] = request.db_names
        query['PayType'] = request.pay_type
        query['InstanceNetworkType'] = request.instance_network_type
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['Category'] = request.category
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['RestoreTable'] = request.restore_table
        query['TableMeta'] = request.table_meta
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['BackupType'] = request.backup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['DbNames'] = request.db_names
        query['PayType'] = request.pay_type
        query['InstanceNetworkType'] = request.instance_network_type
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['Category'] = request.category
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['RestoreTable'] = request.restore_table
        query['TableMeta'] = request.table_meta
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['BackupType'] = request.backup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_dbinstance(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    async def clone_dbinstance_async(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_dbinstance_with_options_async(request, runtime)

    def clone_parameter_group_with_options(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TargetRegionId'] = request.target_region_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['ParameterGroupDesc'] = request.parameter_group_desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TargetRegionId'] = request.target_region_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['ParameterGroupDesc'] = request.parameter_group_desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_parameter_group(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_parameter_group_with_options(request, runtime)

    async def clone_parameter_group_async(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_parameter_group_with_options_async(request, runtime)

    def copy_database_with_options(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_database_with_options_async(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_database(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_database_with_options(request, runtime)

    async def copy_database_async(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_database_with_options_async(request, runtime)

    def copy_database_between_instances_with_options(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDBInstanceId'] = request.target_dbinstance_id
        query['DbNames'] = request.db_names
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['SyncUserPrivilege'] = request.sync_user_privilege
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseBetweenInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_database_between_instances_with_options_async(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDBInstanceId'] = request.target_dbinstance_id
        query['DbNames'] = request.db_names
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['SyncUserPrivilege'] = request.sync_user_privilege
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CopyDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseBetweenInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_database_between_instances(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_database_between_instances_with_options(request, runtime)

    async def copy_database_between_instances_async(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_database_between_instances_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: rds_20140815_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AccountDescription'] = request.account_description
        query['AccountType'] = request.account_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: rds_20140815_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AccountDescription'] = request.account_description
        query['AccountType'] = request.account_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: rds_20140815_models.CreateAccountRequest,
    ) -> rds_20140815_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: rds_20140815_models.CreateAccountRequest,
    ) -> rds_20140815_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: rds_20140815_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['BackupStrategy'] = request.backup_strategy
        query['BackupMethod'] = request.backup_method
        query['BackupType'] = request.backup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: rds_20140815_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['BackupStrategy'] = request.backup_strategy
        query['BackupMethod'] = request.backup_method
        query['BackupType'] = request.backup_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: rds_20140815_models.CreateBackupRequest,
    ) -> rds_20140815_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: rds_20140815_models.CreateBackupRequest,
    ) -> rds_20140815_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['CharacterSetName'] = request.character_set_name
        query['DBDescription'] = request.dbdescription
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['CharacterSetName'] = request.character_set_name
        query['DBDescription'] = request.dbdescription
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['SystemDBCharset'] = request.system_dbcharset
        query['DBInstanceNetType'] = request.dbinstance_net_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['SecurityIPList'] = request.security_iplist
        query['ClientToken'] = request.client_token
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['ZoneIdSlave1'] = request.zone_id_slave_1
        query['ZoneIdSlave2'] = request.zone_id_slave_2
        query['InstanceNetworkType'] = request.instance_network_type
        query['ConnectionMode'] = request.connection_mode
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['ResourceGroupId'] = request.resource_group_id
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['BusinessInfo'] = request.business_info
        query['EncryptionKey'] = request.encryption_key
        query['RoleARN'] = request.role_arn
        query['AutoRenew'] = request.auto_renew
        query['Category'] = request.category
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        query['DBParamGroupId'] = request.dbparam_group_id
        query['DBTimeZone'] = request.dbtime_zone
        query['DBIsIgnoreCase'] = request.dbis_ignore_case
        query['TargetMinorVersion'] = request.target_minor_version
        query['StorageAutoScale'] = request.storage_auto_scale
        query['StorageThreshold'] = request.storage_threshold
        query['StorageUpperBound'] = request.storage_upper_bound
        query['DryRun'] = request.dry_run
        query['UserBackupId'] = request.user_backup_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['SystemDBCharset'] = request.system_dbcharset
        query['DBInstanceNetType'] = request.dbinstance_net_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['SecurityIPList'] = request.security_iplist
        query['ClientToken'] = request.client_token
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['ZoneIdSlave1'] = request.zone_id_slave_1
        query['ZoneIdSlave2'] = request.zone_id_slave_2
        query['InstanceNetworkType'] = request.instance_network_type
        query['ConnectionMode'] = request.connection_mode
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['ResourceGroupId'] = request.resource_group_id
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['BusinessInfo'] = request.business_info
        query['EncryptionKey'] = request.encryption_key
        query['RoleARN'] = request.role_arn
        query['AutoRenew'] = request.auto_renew
        query['Category'] = request.category
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        query['DBParamGroupId'] = request.dbparam_group_id
        query['DBTimeZone'] = request.dbtime_zone
        query['DBIsIgnoreCase'] = request.dbis_ignore_case
        query['TargetMinorVersion'] = request.target_minor_version
        query['StorageAutoScale'] = request.storage_auto_scale
        query['StorageThreshold'] = request.storage_threshold
        query['StorageUpperBound'] = request.storage_upper_bound
        query['DryRun'] = request.dry_run
        query['UserBackupId'] = request.user_backup_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_dbproxy_endpoint_address_with_options(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbproxy_endpoint_address_with_options_async(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBProxyEndpointAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbproxy_endpoint_address(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbproxy_endpoint_address_with_options(request, runtime)

    async def create_dbproxy_endpoint_address_async(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbproxy_endpoint_address_with_options_async(request, runtime)

    def create_ddr_instance_with_options(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['SystemDBCharset'] = request.system_dbcharset
        query['DBInstanceNetType'] = request.dbinstance_net_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['SecurityIPList'] = request.security_iplist
        query['ClientToken'] = request.client_token
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['InstanceNetworkType'] = request.instance_network_type
        query['ConnectionMode'] = request.connection_mode
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['OwnerAccount'] = request.owner_account
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['ResourceGroupId'] = request.resource_group_id
        query['RestoreType'] = request.restore_type
        query['BackupSetId'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['BinlogName'] = request.binlog_name
        query['BinlogPosition'] = request.binlog_position
        query['BinlogRole'] = request.binlog_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDdrInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDdrInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ddr_instance_with_options_async(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['SystemDBCharset'] = request.system_dbcharset
        query['DBInstanceNetType'] = request.dbinstance_net_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['SecurityIPList'] = request.security_iplist
        query['ClientToken'] = request.client_token
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['InstanceNetworkType'] = request.instance_network_type
        query['ConnectionMode'] = request.connection_mode
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['OwnerAccount'] = request.owner_account
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['ResourceGroupId'] = request.resource_group_id
        query['RestoreType'] = request.restore_type
        query['BackupSetId'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['BinlogName'] = request.binlog_name
        query['BinlogPosition'] = request.binlog_position
        query['BinlogRole'] = request.binlog_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDdrInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDdrInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ddr_instance(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ddr_instance_with_options(request, runtime)

    async def create_ddr_instance_async(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ddr_instance_with_options_async(request, runtime)

    def create_dedicated_host_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['HostName'] = request.host_name
        query['ZoneId'] = request.zone_id
        query['VSwitchId'] = request.v_switch_id
        query['HostClass'] = request.host_class
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['UsedTime'] = request.used_time
        query['ClientToken'] = request.client_token
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['HostName'] = request.host_name
        query['ZoneId'] = request.zone_id
        query['VSwitchId'] = request.v_switch_id
        query['HostClass'] = request.host_class
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['UsedTime'] = request.used_time
        query['ClientToken'] = request.client_token
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    async def create_dedicated_host_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_with_options_async(request, runtime)

    def create_dedicated_host_account_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_account_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host_account(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    async def create_dedicated_host_account_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_account_with_options_async(request, runtime)

    def create_dedicated_host_group_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['AllocationPolicy'] = request.allocation_policy
        query['VPCId'] = request.vpcid
        query['HostReplacePolicy'] = request.host_replace_policy
        query['ClientToken'] = request.client_token
        query['OpenPermission'] = request.open_permission
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_group_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['AllocationPolicy'] = request.allocation_policy
        query['VPCId'] = request.vpcid
        query['HostReplacePolicy'] = request.host_replace_policy
        query['ClientToken'] = request.client_token
        query['OpenPermission'] = request.open_permission
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host_group(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    async def create_dedicated_host_group_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_group_with_options_async(request, runtime)

    def create_dedicated_host_user_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['UserPassword'] = request.user_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_user_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['UserPassword'] = request.user_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDedicatedHostUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host_user(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_user_with_options(request, runtime)

    async def create_dedicated_host_user_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_user_with_options_async(request, runtime)

    def create_diagnostic_report_with_options(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDiagnosticReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnostic_report(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def create_gdn_instance_with_options(
        self,
        request: rds_20140815_models.CreateGdnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateGdnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['PrimaryInstanceName'] = request.primary_instance_name
        query['PrimaryInstanceRegion'] = request.primary_instance_region
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGdnInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateGdnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gdn_instance_with_options_async(
        self,
        request: rds_20140815_models.CreateGdnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateGdnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['PrimaryInstanceName'] = request.primary_instance_name
        query['PrimaryInstanceRegion'] = request.primary_instance_region
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGdnInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateGdnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gdn_instance(
        self,
        request: rds_20140815_models.CreateGdnInstanceRequest,
    ) -> rds_20140815_models.CreateGdnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gdn_instance_with_options(request, runtime)

    async def create_gdn_instance_async(
        self,
        request: rds_20140815_models.CreateGdnInstanceRequest,
    ) -> rds_20140815_models.CreateGdnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gdn_instance_with_options_async(request, runtime)

    def create_migrate_task_with_options(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['BackupMode'] = request.backup_mode
        query['IsOnlineDB'] = request.is_online_db
        query['CheckDBMode'] = request.check_dbmode
        query['OssObjectPositions'] = request.oss_object_positions
        query['OSSUrls'] = request.ossurls
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migrate_task_with_options_async(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['BackupMode'] = request.backup_mode
        query['IsOnlineDB'] = request.is_online_db
        query['CheckDBMode'] = request.check_dbmode
        query['OssObjectPositions'] = request.oss_object_positions
        query['OSSUrls'] = request.ossurls
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migrate_task(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_with_options(request, runtime)

    async def create_migrate_task_async(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migrate_task_with_options_async(request, runtime)

    def create_migrate_task_for_sqlserver_with_options(
        self,
        request: rds_20140815_models.CreateMigrateTaskForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateMigrateTaskForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['TaskType'] = request.task_type
        query['IsOnlineDB'] = request.is_online_db
        query['OSSUrls'] = request.ossurls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMigrateTaskForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migrate_task_for_sqlserver_with_options_async(
        self,
        request: rds_20140815_models.CreateMigrateTaskForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateMigrateTaskForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['TaskType'] = request.task_type
        query['IsOnlineDB'] = request.is_online_db
        query['OSSUrls'] = request.ossurls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMigrateTaskForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskForSQLServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migrate_task_for_sqlserver(
        self,
        request: rds_20140815_models.CreateMigrateTaskForSQLServerRequest,
    ) -> rds_20140815_models.CreateMigrateTaskForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_for_sqlserver_with_options(request, runtime)

    async def create_migrate_task_for_sqlserver_async(
        self,
        request: rds_20140815_models.CreateMigrateTaskForSQLServerRequest,
    ) -> rds_20140815_models.CreateMigrateTaskForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migrate_task_for_sqlserver_with_options_async(request, runtime)

    def create_online_database_task_with_options(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['MigrateTaskId'] = request.migrate_task_id
        query['CheckDBMode'] = request.check_dbmode
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOnlineDatabaseTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateOnlineDatabaseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_online_database_task_with_options_async(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['MigrateTaskId'] = request.migrate_task_id
        query['CheckDBMode'] = request.check_dbmode
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOnlineDatabaseTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateOnlineDatabaseTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_online_database_task(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_online_database_task_with_options(request, runtime)

    async def create_online_database_task_async(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_online_database_task_with_options_async(request, runtime)

    def create_parameter_group_with_options(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['Parameters'] = request.parameters
        query['ParameterGroupDesc'] = request.parameter_group_desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['Parameters'] = request.parameters
        query['ParameterGroupDesc'] = request.parameter_group_desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parameter_group(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    async def create_parameter_group_async(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_parameter_group_with_options_async(request, runtime)

    def create_read_only_dbinstance_with_options(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['EngineVersion'] = request.engine_version
        query['PayType'] = request.pay_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['InstanceNetworkType'] = request.instance_network_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        query['Category'] = request.category
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['GdnInstanceName'] = request.gdn_instance_name
        query['TddlBizType'] = request.tddl_biz_type
        query['TddlRegionConfig'] = request.tddl_region_config
        query['InstructionSetArch'] = request.instruction_set_arch
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateReadOnlyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateReadOnlyDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_read_only_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['EngineVersion'] = request.engine_version
        query['PayType'] = request.pay_type
        query['DBInstanceDescription'] = request.dbinstance_description
        query['InstanceNetworkType'] = request.instance_network_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        query['Category'] = request.category
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['GdnInstanceName'] = request.gdn_instance_name
        query['TddlBizType'] = request.tddl_biz_type
        query['TddlRegionConfig'] = request.tddl_region_config
        query['InstructionSetArch'] = request.instruction_set_arch
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateReadOnlyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateReadOnlyDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_read_only_dbinstance(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_read_only_dbinstance_with_options(request, runtime)

    async def create_read_only_dbinstance_async(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_read_only_dbinstance_with_options_async(request, runtime)

    def create_temp_dbinstance_with_options(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTempDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateTempDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_temp_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTempDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateTempDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_temp_dbinstance(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_temp_dbinstance_with_options(request, runtime)

    async def create_temp_dbinstance_async(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_temp_dbinstance_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
    ) -> rds_20140815_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
    ) -> rds_20140815_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backup_with_options(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
    ) -> rds_20140815_models.DeleteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    async def delete_backup_async(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
    ) -> rds_20140815_models.DeleteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_with_options_async(request, runtime)

    def delete_backup_file_with_options(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['DBName'] = request.dbname
        query['BackupTime'] = request.backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_file_with_options_async(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['DBName'] = request.dbname
        query['BackupTime'] = request.backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_file(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_file_with_options(request, runtime)

    async def delete_backup_file_async(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_file_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_dbproxy_endpoint_address_with_options(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbproxy_endpoint_address_with_options_async(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBProxyEndpointAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbproxy_endpoint_address(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbproxy_endpoint_address_with_options(request, runtime)

    async def delete_dbproxy_endpoint_address_async(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbproxy_endpoint_address_with_options_async(request, runtime)

    def delete_dedicated_host_account_with_options(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dedicated_host_account_with_options_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dedicated_host_account(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    async def delete_dedicated_host_account_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_account_with_options_async(request, runtime)

    def delete_dedicated_host_group_with_options(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedHostGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dedicated_host_group_with_options_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedHostGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDedicatedHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dedicated_host_group(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    async def delete_dedicated_host_group_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_group_with_options_async(request, runtime)

    def delete_parameter_group_with_options(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ParameterGroupId'] = request.parameter_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ParameterGroupId'] = request.parameter_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parameter_group(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    async def delete_parameter_group_async(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_parameter_group_with_options_async(request, runtime)

    def delete_user_backup_file_with_options(
        self,
        request: rds_20140815_models.DeleteUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteUserBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupId'] = request.backup_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_backup_file_with_options_async(
        self,
        request: rds_20140815_models.DeleteUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteUserBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupId'] = request.backup_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteUserBackupFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_backup_file(
        self,
        request: rds_20140815_models.DeleteUserBackupFileRequest,
    ) -> rds_20140815_models.DeleteUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_backup_file_with_options(request, runtime)

    async def delete_user_backup_file_async(
        self,
        request: rds_20140815_models.DeleteUserBackupFileRequest,
    ) -> rds_20140815_models.DeleteUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_backup_file_with_options_async(request, runtime)

    def descibe_imports_from_database_with_options(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Engine'] = request.engine
        query['ImportId'] = request.import_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescibeImportsFromDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescibeImportsFromDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def descibe_imports_from_database_with_options_async(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Engine'] = request.engine
        query['ImportId'] = request.import_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescibeImportsFromDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescibeImportsFromDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def descibe_imports_from_database(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.descibe_imports_from_database_with_options(request, runtime)

    async def descibe_imports_from_database_async(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.descibe_imports_from_database_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_action_event_policy_with_options(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeActionEventPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_action_event_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeActionEventPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_action_event_policy(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_action_event_policy_with_options(request, runtime)

    async def describe_action_event_policy_async(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_action_event_policy_with_options_async(request, runtime)

    def describe_available_classes_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['InstanceChargeType'] = request.instance_charge_type
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceId'] = request.dbinstance_id
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Category'] = request.category
        query['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_classes_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['InstanceChargeType'] = request.instance_charge_type
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceId'] = request.dbinstance_id
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Category'] = request.category
        query['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_classes(
        self,
        request: rds_20140815_models.DescribeAvailableClassesRequest,
    ) -> rds_20140815_models.DescribeAvailableClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_classes_with_options(request, runtime)

    async def describe_available_classes_async(
        self,
        request: rds_20140815_models.DescribeAvailableClassesRequest,
    ) -> rds_20140815_models.DescribeAvailableClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_classes_with_options_async(request, runtime)

    def describe_available_cross_region_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCrossRegion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableCrossRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_cross_region_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCrossRegion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableCrossRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_cross_region(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cross_region_with_options(request, runtime)

    async def describe_available_cross_region_async(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_cross_region_with_options_async(request, runtime)

    def describe_available_dedicated_host_classes_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableDedicatedHostClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_dedicated_host_classes_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableDedicatedHostClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_dedicated_host_classes(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_classes_with_options(request, runtime)

    async def describe_available_dedicated_host_classes_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_dedicated_host_classes_with_options_async(request, runtime)

    def describe_available_dedicated_host_zones_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableDedicatedHostZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_dedicated_host_zones_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableDedicatedHostZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_dedicated_host_zones(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_zones_with_options(request, runtime)

    async def describe_available_dedicated_host_zones_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_dedicated_host_zones_with_options_async(request, runtime)

    def describe_available_recovery_time_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['CrossBackupId'] = request.cross_backup_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_recovery_time_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['CrossBackupId'] = request.cross_backup_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableRecoveryTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_recovery_time(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_recovery_time_with_options(request, runtime)

    async def describe_available_recovery_time_async(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_recovery_time_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['InstanceChargeType'] = request.instance_charge_type
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Category'] = request.category
        query['DispenseMode'] = request.dispense_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['InstanceChargeType'] = request.instance_charge_type
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Category'] = request.category
        query['DispenseMode'] = request.dispense_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: rds_20140815_models.DescribeAvailableResourceRequest,
    ) -> rds_20140815_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: rds_20140815_models.DescribeAvailableResourceRequest,
    ) -> rds_20140815_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_available_zones_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['EngineVersion'] = request.engine_version
        query['CommodityCode'] = request.commodity_code
        query['DispenseMode'] = request.dispense_mode
        query['DBInstanceName'] = request.dbinstance_name
        query['Category'] = request.category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_zones_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['EngineVersion'] = request.engine_version
        query['CommodityCode'] = request.commodity_code
        query['DispenseMode'] = request.dispense_mode
        query['DBInstanceName'] = request.dbinstance_name
        query['Category'] = request.category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_zones(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zones_with_options(request, runtime)

    async def describe_available_zones_async(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_zones_with_options_async(request, runtime)

    def describe_backup_database_with_options(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_database_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_database(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_database_with_options(request, runtime)

    async def describe_backup_database_async(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_database_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupPolicyMode'] = request.backup_policy_mode
        query['OwnerAccount'] = request.owner_account
        query['CompressType'] = request.compress_type
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupPolicyMode'] = request.backup_policy_mode
        query['OwnerAccount'] = request.owner_account
        query['CompressType'] = request.compress_type
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['BackupStatus'] = request.backup_status
        query['BackupMode'] = request.backup_mode
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['BackupStatus'] = request.backup_status
        query['BackupMode'] = request.backup_mode
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['Flag'] = request.flag
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupJobId'] = request.backup_job_id
        query['BackupMode'] = request.backup_mode
        query['BackupJobStatus'] = request.backup_job_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['Flag'] = request.flag
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupJobId'] = request.backup_job_id
        query['BackupMode'] = request.backup_mode
        query['BackupJobStatus'] = request.backup_job_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_binlog_files_with_options(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBinlogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBinlogFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_binlog_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBinlogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBinlogFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_binlog_files(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_binlog_files_with_options(request, runtime)

    async def describe_binlog_files_async(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_binlog_files_with_options_async(request, runtime)

    def describe_character_set_name_with_options(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Engine'] = request.engine
        query['RegionId'] = request.region_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCharacterSetName',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCharacterSetNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_character_set_name_with_options_async(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Engine'] = request.engine
        query['RegionId'] = request.region_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCharacterSetName',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCharacterSetNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_character_set_name(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    async def describe_character_set_name_async(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_character_set_name_with_options_async(request, runtime)

    def describe_collation_time_zones_with_options(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCollationTimeZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCollationTimeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_collation_time_zones_with_options_async(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCollationTimeZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCollationTimeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_collation_time_zones(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_collation_time_zones_with_options(request, runtime)

    async def describe_collation_time_zones_async(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_collation_time_zones_with_options_async(request, runtime)

    def describe_cross_backup_meta_list_with_options(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupSetId'] = request.backup_set_id
        query['GetDbName'] = request.get_db_name
        query['Pattern'] = request.pattern
        query['PageSize'] = request.page_size
        query['PageIndex'] = request.page_index
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossBackupMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossBackupMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cross_backup_meta_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupSetId'] = request.backup_set_id
        query['GetDbName'] = request.get_db_name
        query['Pattern'] = request.pattern
        query['PageSize'] = request.page_size
        query['PageIndex'] = request.page_index
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossBackupMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossBackupMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cross_backup_meta_list(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_backup_meta_list_with_options(request, runtime)

    async def describe_cross_backup_meta_list_async(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_backup_meta_list_with_options_async(request, runtime)

    def describe_cross_region_backup_dbinstance_with_options(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackupDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cross_region_backup_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackupDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cross_region_backup_dbinstance(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backup_dbinstance_with_options(request, runtime)

    async def describe_cross_region_backup_dbinstance_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_region_backup_dbinstance_with_options_async(request, runtime)

    def describe_cross_region_backups_with_options(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupRegion'] = request.cross_backup_region
        query['CrossBackupId'] = request.cross_backup_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cross_region_backups_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupRegion'] = request.cross_backup_region
        query['CrossBackupId'] = request.cross_backup_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cross_region_backups(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backups_with_options(request, runtime)

    async def describe_cross_region_backups_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_region_backups_with_options_async(request, runtime)

    def describe_cross_region_log_backup_files_with_options(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupRegion'] = request.cross_backup_region
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cross_region_log_backup_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupRegion'] = request.cross_backup_region
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cross_region_log_backup_files(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_log_backup_files_with_options(request, runtime)

    async def describe_cross_region_log_backup_files_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_region_log_backup_files_with_options_async(request, runtime)

    def describe_databases_with_options(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['DBStatus'] = request.dbstatus
        query['OwnerAccount'] = request.owner_account
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_databases_with_options_async(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['DBStatus'] = request.dbstatus
        query['OwnerAccount'] = request.owner_account
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_databases(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    async def describe_databases_async(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_databases_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Expired'] = request.expired
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Expired'] = request.expired
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_detail_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDetail',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_detail_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDetail',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_detail(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_detail_with_options(request, runtime)

    async def describe_dbinstance_detail_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_detail_with_options_async(request, runtime)

    def describe_dbinstance_encryption_key_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['EncryptionKey'] = request.encryption_key
        query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceEncryptionKey',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_encryption_key_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['EncryptionKey'] = request.encryption_key
        query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceEncryptionKey',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_encryption_key(
        self,
        request: rds_20140815_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_encryption_key_with_options(request, runtime)

    async def describe_dbinstance_encryption_key_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_encryption_key_with_options_async(request, runtime)

    def describe_dbinstance_haconfig_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceHAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_haconfig_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceHAConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_haconfig(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_haconfig_with_options(request, runtime)

    async def describe_dbinstance_haconfig_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_haconfig_with_options_async(request, runtime)

    def describe_dbinstance_iparray_list_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['WhitelistNetworkType'] = request.whitelist_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIPArrayList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIPArrayListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_iparray_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['WhitelistNetworkType'] = request.whitelist_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIPArrayList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIPArrayListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_iparray_list(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    async def describe_dbinstance_iparray_list_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_iparray_list_with_options_async(request, runtime)

    def describe_dbinstance_ip_hostname_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIpHostname',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIpHostnameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_ip_hostname_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIpHostname',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIpHostnameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ip_hostname(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_ip_hostname_with_options(request, runtime)

    async def describe_dbinstance_ip_hostname_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_ip_hostname_with_options_async(request, runtime)

    def describe_dbinstance_monitor_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_monitor_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_monitor(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    async def describe_dbinstance_monitor_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_monitor_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Flag'] = request.flag
        query['DBInstanceNetRWSplitType'] = request.dbinstance_net_rwsplit_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Flag'] = request.flag
        query['DBInstanceNetRWSplitType'] = request.dbinstance_net_rwsplit_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Key'] = request.key
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Key'] = request.key
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstance_proxy_configuration_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_proxy_configuration_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_proxy_configuration(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_proxy_configuration_with_options(request, runtime)

    async def describe_dbinstance_proxy_configuration_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_proxy_configuration_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['ResourceGroupId'] = request.resource_group_id
        query['DBInstanceStatus'] = request.dbinstance_status
        query['Expired'] = request.expired
        query['SearchKey'] = request.search_key
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceType'] = request.dbinstance_type
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceNetworkType'] = request.instance_network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['PayType'] = request.pay_type
        query['ConnectionMode'] = request.connection_mode
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['InstanceLevel'] = request.instance_level
        query['ConnectionString'] = request.connection_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['ResourceGroupId'] = request.resource_group_id
        query['DBInstanceStatus'] = request.dbinstance_status
        query['Expired'] = request.expired
        query['SearchKey'] = request.search_key
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceType'] = request.dbinstance_type
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceNetworkType'] = request.instance_network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['PayType'] = request.pay_type
        query['ConnectionMode'] = request.connection_mode
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['InstanceLevel'] = request.instance_level
        query['ConnectionString'] = request.connection_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbinstances_as_csv_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesAsCsv',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesAsCsvResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_as_csv_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesAsCsv',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesAsCsvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances_as_csv(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_as_csv_with_options(request, runtime)

    async def describe_dbinstances_as_csv_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_as_csv_with_options_async(request, runtime)

    def describe_dbinstances_by_expire_time_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['proxyId'] = request.proxy_id
        query['ExpirePeriod'] = request.expire_period
        query['Expired'] = request.expired
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_by_expire_time_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['proxyId'] = request.proxy_id
        query['ExpirePeriod'] = request.expire_period
        query['Expired'] = request.expired
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances_by_expire_time(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_expire_time_with_options(request, runtime)

    async def describe_dbinstances_by_expire_time_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_by_expire_time_with_options_async(request, runtime)

    def describe_dbinstances_by_performance_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['SortMethod'] = request.sort_method
        query['SortKey'] = request.sort_key
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_by_performance_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['SortMethod'] = request.sort_method
        query['SortKey'] = request.sort_key
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances_by_performance(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_performance_with_options(request, runtime)

    async def describe_dbinstances_by_performance_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_by_performance_with_options_async(request, runtime)

    def describe_dbinstances_for_clone_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['DBInstanceStatus'] = request.dbinstance_status
        query['Expired'] = request.expired
        query['SearchKey'] = request.search_key
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceType'] = request.dbinstance_type
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceNetworkType'] = request.instance_network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['NodeType'] = request.node_type
        query['PayType'] = request.pay_type
        query['ConnectionMode'] = request.connection_mode
        query['OwnerAccount'] = request.owner_account
        query['CurrentInstanceId'] = request.current_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesForClone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesForCloneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_for_clone_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['Engine'] = request.engine
        query['ZoneId'] = request.zone_id
        query['DBInstanceStatus'] = request.dbinstance_status
        query['Expired'] = request.expired
        query['SearchKey'] = request.search_key
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceType'] = request.dbinstance_type
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['InstanceNetworkType'] = request.instance_network_type
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['NodeType'] = request.node_type
        query['PayType'] = request.pay_type
        query['ConnectionMode'] = request.connection_mode
        query['OwnerAccount'] = request.owner_account
        query['CurrentInstanceId'] = request.current_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesForClone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesForCloneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances_for_clone(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_for_clone_with_options(request, runtime)

    async def describe_dbinstances_for_clone_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_for_clone_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_status_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceStatus',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_status_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceStatus',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_status(
        self,
        request: rds_20140815_models.DescribeDBInstanceStatusRequest,
    ) -> rds_20140815_models.DescribeDBInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_status_with_options(request, runtime)

    async def describe_dbinstance_status_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceStatusRequest,
    ) -> rds_20140815_models.DescribeDBInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_status_with_options_async(request, runtime)

    def describe_dbinstance_tdewith_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_tdewith_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_tde(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    async def describe_dbinstance_tde_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_tdewith_options_async(request, runtime)

    def describe_dbproxy_with_options(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbproxy_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbproxy(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_with_options(request, runtime)

    async def describe_dbproxy_async(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbproxy_with_options_async(request, runtime)

    def describe_dbproxy_endpoint_with_options(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyConnectString'] = request.dbproxy_connect_string
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbproxy_endpoint_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyConnectString'] = request.dbproxy_connect_string
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbproxy_endpoint(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_endpoint_with_options(request, runtime)

    async def describe_dbproxy_endpoint_async(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbproxy_endpoint_with_options_async(request, runtime)

    def describe_dbproxy_performance_with_options(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyInstanceType'] = request.dbproxy_instance_type
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['RegionId'] = request.region_id
        query['MetricsName'] = request.metrics_name
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbproxy_performance_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyInstanceType'] = request.dbproxy_instance_type
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['RegionId'] = request.region_id
        query['MetricsName'] = request.metrics_name
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbproxy_performance(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_performance_with_options(request, runtime)

    async def describe_dbproxy_performance_async(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbproxy_performance_with_options_async(request, runtime)

    def describe_dedicated_host_attribute_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_attribute_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_attribute(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    async def describe_dedicated_host_attribute_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_attribute_with_options_async(request, runtime)

    def describe_dedicated_host_groups_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['ImageCategory'] = request.image_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_groups_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['ImageCategory'] = request.image_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_groups(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    async def describe_dedicated_host_groups_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_groups_with_options_async(request, runtime)

    def describe_dedicated_host_image_categories_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['HostGroup'] = request.host_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostImageCategories',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_image_categories_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['HostGroup'] = request.host_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostImageCategories',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_image_categories(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_image_categories_with_options(request, runtime)

    async def describe_dedicated_host_image_categories_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_image_categories_with_options_async(request, runtime)

    def describe_dedicated_hosts_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['OrderId'] = request.order_id
        query['HostType'] = request.host_type
        query['HostStatus'] = request.host_status
        query['AllocationStatus'] = request.allocation_status
        query['ZoneId'] = request.zone_id
        query['DedicatedHostId'] = request.dedicated_host_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_hosts_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['OrderId'] = request.order_id
        query['HostType'] = request.host_type
        query['HostStatus'] = request.host_status
        query['AllocationStatus'] = request.allocation_status
        query['ZoneId'] = request.zone_id
        query['DedicatedHostId'] = request.dedicated_host_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_hosts(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    async def describe_dedicated_hosts_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_with_options_async(request, runtime)

    def describe_detached_backups_with_options(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['BackupStatus'] = request.backup_status
        query['BackupMode'] = request.backup_mode
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDetachedBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDetachedBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_detached_backups_with_options_async(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['BackupStatus'] = request.backup_status
        query['BackupMode'] = request.backup_mode
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDetachedBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDetachedBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_detached_backups(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    async def describe_detached_backups_async(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_detached_backups_with_options_async(request, runtime)

    def describe_diagnostic_report_list_with_options(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDiagnosticReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDiagnosticReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnostic_report_list(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    async def describe_diagnostic_report_list_async(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_report_list_with_options_async(request, runtime)

    def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dtcsecurity_ip_hosts_for_sqlserver(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    async def describe_dtcsecurity_ip_hosts_for_sqlserver_async(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(request, runtime)

    def describe_error_logs_with_options(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeErrorLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeErrorLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_error_logs_with_options_async(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeErrorLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeErrorLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_error_logs(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_error_logs_with_options(request, runtime)

    async def describe_error_logs_async(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_error_logs_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
    ) -> rds_20140815_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
    ) -> rds_20140815_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_hadiagnose_config_with_options(
        self,
        request: rds_20140815_models.DescribeHADiagnoseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHADiagnoseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHADiagnoseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hadiagnose_config_with_options_async(
        self,
        request: rds_20140815_models.DescribeHADiagnoseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHADiagnoseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHADiagnoseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hadiagnose_config(
        self,
        request: rds_20140815_models.DescribeHADiagnoseConfigRequest,
    ) -> rds_20140815_models.DescribeHADiagnoseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hadiagnose_config_with_options(request, runtime)

    async def describe_hadiagnose_config_async(
        self,
        request: rds_20140815_models.DescribeHADiagnoseConfigRequest,
    ) -> rds_20140815_models.DescribeHADiagnoseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hadiagnose_config_with_options_async(request, runtime)

    def describe_haswitch_config_with_options(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHASwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_haswitch_config_with_options_async(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHASwitchConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_haswitch_config(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_haswitch_config_with_options(request, runtime)

    async def describe_haswitch_config_async(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_haswitch_config_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_instance_cross_backup_policy_with_options(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_cross_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_cross_backup_policy(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_cross_backup_policy_with_options(request, runtime)

    async def describe_instance_cross_backup_policy_async(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_cross_backup_policy_with_options_async(request, runtime)

    def describe_instance_keywords_with_options(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Key'] = request.key
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceKeywords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_keywords_with_options_async(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Key'] = request.key
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceKeywords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceKeywordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_keywords(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_keywords_with_options(request, runtime)

    async def describe_instance_keywords_async(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_keywords_with_options_async(request, runtime)

    def describe_local_available_recovery_time_with_options(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLocalAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_local_available_recovery_time_with_options_async(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLocalAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_local_available_recovery_time(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_local_available_recovery_time_with_options(request, runtime)

    async def describe_local_available_recovery_time_async(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_local_available_recovery_time_with_options_async(request, runtime)

    def describe_log_backup_files_with_options(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLogBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_backup_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLogBackupFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_backup_files(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_files_with_options(request, runtime)

    async def describe_log_backup_files_async(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_backup_files_with_options_async(request, runtime)

    def describe_meta_list_with_options(
        self,
        request: rds_20140815_models.DescribeMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMetaListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['RestoreType'] = request.restore_type
        query['BackupSetID'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['GetDbName'] = request.get_db_name
        query['Pattern'] = request.pattern
        query['PageSize'] = request.page_size
        query['PageIndex'] = request.page_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meta_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMetaListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['RestoreType'] = request.restore_type
        query['BackupSetID'] = request.backup_set_id
        query['RestoreTime'] = request.restore_time
        query['GetDbName'] = request.get_db_name
        query['Pattern'] = request.pattern
        query['PageSize'] = request.page_size
        query['PageIndex'] = request.page_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meta_list(
        self,
        request: rds_20140815_models.DescribeMetaListRequest,
    ) -> rds_20140815_models.DescribeMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_list_with_options(request, runtime)

    async def describe_meta_list_async(
        self,
        request: rds_20140815_models.DescribeMetaListRequest,
    ) -> rds_20140815_models.DescribeMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meta_list_with_options_async(request, runtime)

    def describe_migrate_task_by_id_with_options(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTaskById',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migrate_task_by_id_with_options_async(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTaskById',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTaskByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migrate_task_by_id(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_task_by_id_with_options(request, runtime)

    async def describe_migrate_task_by_id_async(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migrate_task_by_id_with_options_async(request, runtime)

    def describe_migrate_tasks_with_options(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migrate_tasks_with_options_async(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migrate_tasks(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_with_options(request, runtime)

    async def describe_migrate_tasks_async(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migrate_tasks_with_options_async(request, runtime)

    def describe_migrate_tasks_for_sqlserver_with_options(
        self,
        request: rds_20140815_models.DescribeMigrateTasksForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTasksForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTasksForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migrate_tasks_for_sqlserver_with_options_async(
        self,
        request: rds_20140815_models.DescribeMigrateTasksForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTasksForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTasksForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksForSQLServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migrate_tasks_for_sqlserver(
        self,
        request: rds_20140815_models.DescribeMigrateTasksForSQLServerRequest,
    ) -> rds_20140815_models.DescribeMigrateTasksForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_for_sqlserver_with_options(request, runtime)

    async def describe_migrate_tasks_for_sqlserver_async(
        self,
        request: rds_20140815_models.DescribeMigrateTasksForSQLServerRequest,
    ) -> rds_20140815_models.DescribeMigrateTasksForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migrate_tasks_for_sqlserver_with_options_async(request, runtime)

    def describe_modify_parameter_log_with_options(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeModifyParameterLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeModifyParameterLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_modify_parameter_log_with_options_async(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeModifyParameterLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeModifyParameterLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_modify_parameter_log(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    async def describe_modify_parameter_log_async(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_modify_parameter_log_with_options_async(request, runtime)

    def describe_oss_downloads_with_options(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssDownloads',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_downloads_with_options_async(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssDownloads',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_downloads(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_with_options(request, runtime)

    async def describe_oss_downloads_async(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_downloads_with_options_async(request, runtime)

    def describe_oss_downloads_for_sqlserver_with_options(
        self,
        request: rds_20140815_models.DescribeOssDownloadsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeOssDownloadsForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssDownloadsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_downloads_for_sqlserver_with_options_async(
        self,
        request: rds_20140815_models.DescribeOssDownloadsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeOssDownloadsForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssDownloadsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsForSQLServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_downloads_for_sqlserver(
        self,
        request: rds_20140815_models.DescribeOssDownloadsForSQLServerRequest,
    ) -> rds_20140815_models.DescribeOssDownloadsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_for_sqlserver_with_options(request, runtime)

    async def describe_oss_downloads_for_sqlserver_async(
        self,
        request: rds_20140815_models.DescribeOssDownloadsForSQLServerRequest,
    ) -> rds_20140815_models.DescribeOssDownloadsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_downloads_for_sqlserver_with_options_async(request, runtime)

    def describe_parameter_group_with_options(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_group(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    async def describe_parameter_group_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_group_with_options_async(request, runtime)

    def describe_parameter_groups_with_options(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_groups_with_options_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_groups(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    async def describe_parameter_groups_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_groups_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
    ) -> rds_20140815_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
    ) -> rds_20140815_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['OwnerAccount'] = request.owner_account
        query['Category'] = request.category
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['OwnerAccount'] = request.owner_account
        query['Category'] = request.category
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: rds_20140815_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['CommodityCode'] = request.commodity_code
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['UsedTime'] = request.used_time
        query['TimeType'] = request.time_type
        query['Quantity'] = request.quantity
        query['InstanceUsedType'] = request.instance_used_type
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: rds_20140815_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['CommodityCode'] = request.commodity_code
        query['RegionId'] = request.region_id
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['ZoneId'] = request.zone_id
        query['UsedTime'] = request.used_time
        query['TimeType'] = request.time_type
        query['Quantity'] = request.quantity
        query['InstanceUsedType'] = request.instance_used_type
        query['OrderType'] = request.order_type
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: rds_20140815_models.DescribePriceRequest,
    ) -> rds_20140815_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: rds_20140815_models.DescribePriceRequest,
    ) -> rds_20140815_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_rds_resource_settings_with_options(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceNiche'] = request.resource_niche
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsResourceSettings',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRdsResourceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_resource_settings_with_options_async(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceNiche'] = request.resource_niche
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsResourceSettings',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRdsResourceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_resource_settings(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_resource_settings_with_options(request, runtime)

    async def describe_rds_resource_settings_async(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_resource_settings_with_options_async(request, runtime)

    def describe_read_dbinstance_delay_with_options(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ReadInstanceId'] = request.read_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeReadDBInstanceDelay',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeReadDBInstanceDelayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_read_dbinstance_delay_with_options_async(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ReadInstanceId'] = request.read_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeReadDBInstanceDelay',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeReadDBInstanceDelayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_read_dbinstance_delay(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_read_dbinstance_delay_with_options(request, runtime)

    async def describe_read_dbinstance_delay_async(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_read_dbinstance_delay_with_options_async(request, runtime)

    def describe_region_infos_with_options(
        self,
        request: rds_20140815_models.DescribeRegionInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRegionInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['InstanceUsedType'] = request.instance_used_type
        query['SpecifyCount'] = request.specify_count
        query['HostType'] = request.host_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegionInfos',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_region_infos_with_options_async(
        self,
        request: rds_20140815_models.DescribeRegionInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRegionInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['InstanceUsedType'] = request.instance_used_type
        query['SpecifyCount'] = request.specify_count
        query['HostType'] = request.host_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegionInfos',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_region_infos(
        self,
        request: rds_20140815_models.DescribeRegionInfosRequest,
    ) -> rds_20140815_models.DescribeRegionInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_region_infos_with_options(request, runtime)

    async def describe_region_infos_async(
        self,
        request: rds_20140815_models.DescribeRegionInfosRequest,
    ) -> rds_20140815_models.DescribeRegionInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_region_infos_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_renewal_price_with_options(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['PayType'] = request.pay_type
        query['DBInstanceClass'] = request.dbinstance_class
        query['UsedTime'] = request.used_time
        query['TimeType'] = request.time_type
        query['Quantity'] = request.quantity
        query['OrderType'] = request.order_type
        query['BusinessInfo'] = request.business_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRenewalPrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRenewalPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_renewal_price_with_options_async(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['PayType'] = request.pay_type
        query['DBInstanceClass'] = request.dbinstance_class
        query['UsedTime'] = request.used_time
        query['TimeType'] = request.time_type
        query['Quantity'] = request.quantity
        query['OrderType'] = request.order_type
        query['BusinessInfo'] = request.business_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRenewalPrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRenewalPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_renewal_price(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    async def describe_renewal_price_async(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_renewal_price_with_options_async(request, runtime)

    def describe_resource_usage_with_options(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsage',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_usage_with_options_async(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsage',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_usage(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    async def describe_resource_usage_async(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_usage_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLHASH'] = request.sqlhash
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['DBName'] = request.dbname
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLHASH'] = request.sqlhash
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['DBName'] = request.dbname
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_logs_with_options(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['DBName'] = request.dbname
        query['SortKey'] = request.sort_key
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_logs_with_options_async(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['DBName'] = request.dbname
        query['SortKey'] = request.sort_key
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_logs(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_logs_with_options(request, runtime)

    async def describe_slow_logs_async(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_logs_with_options_async(request, runtime)

    def describe_sqlcollector_policy_with_options(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlcollector_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlcollector_policy(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_policy_with_options(request, runtime)

    async def describe_sqlcollector_policy_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlcollector_policy_with_options_async(request, runtime)

    def describe_sqlcollector_retention_with_options(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorRetentionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlcollector_retention_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorRetentionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlcollector_retention(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_retention_with_options(request, runtime)

    async def describe_sqlcollector_retention_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlcollector_retention_with_options_async(request, runtime)

    def describe_sqllog_files_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['FileName'] = request.file_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['FileName'] = request.file_name
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllog_files(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_files_with_options(request, runtime)

    async def describe_sqllog_files_async(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_files_with_options_async(request, runtime)

    def describe_sqllog_records_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLId'] = request.sqlid
        query['QueryKeywords'] = request.query_keywords
        query['StartTime'] = request.start_time
        query['Database'] = request.database
        query['User'] = request.user
        query['Form'] = request.form
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_records_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLId'] = request.sqlid
        query['QueryKeywords'] = request.query_keywords
        query['StartTime'] = request.start_time
        query['Database'] = request.database
        query['User'] = request.user
        query['Form'] = request.form
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllog_records(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    async def describe_sqllog_records_async(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_records_with_options_async(request, runtime)

    def describe_sqllog_report_list_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_report_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllog_report_list(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_report_list_with_options(request, runtime)

    async def describe_sqllog_report_list_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_report_list_with_options_async(request, runtime)

    def describe_sqllog_reports_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogReports',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_reports_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogReports',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllog_reports(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_reports_with_options(request, runtime)

    async def describe_sqllog_reports_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_reports_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
    ) -> rds_20140815_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
    ) -> rds_20140815_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Status'] = request.status
        query['TaskAction'] = request.task_action
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Status'] = request.status
        query['TaskAction'] = request.task_action
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
    ) -> rds_20140815_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
    ) -> rds_20140815_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def destroy_dbinstance_with_options(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DestroyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DestroyDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DestroyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DestroyDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_dbinstance(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_dbinstance_with_options(request, runtime)

    async def destroy_dbinstance_async(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_dbinstance_with_options_async(request, runtime)

    def drop_dedicated_host_user_with_options(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DropDedicatedHostUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_dedicated_host_user_with_options_async(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DropDedicatedHostUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_dedicated_host_user(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_dedicated_host_user_with_options(request, runtime)

    async def drop_dedicated_host_user_async(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_dedicated_host_user_with_options_async(request, runtime)

    def evaluate_dedicated_host_instance_resource_with_options(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DiskType'] = request.disk_type
        query['DiskSize'] = request.disk_size
        query['InstanceClassNames'] = request.instance_class_names
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EvaluateDedicatedHostInstanceResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_dedicated_host_instance_resource_with_options_async(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DiskType'] = request.disk_type
        query['DiskSize'] = request.disk_size
        query['InstanceClassNames'] = request.instance_class_names
        query['Engine'] = request.engine
        query['EngineVersion'] = request.engine_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EvaluateDedicatedHostInstanceResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_dedicated_host_instance_resource(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.evaluate_dedicated_host_instance_resource_with_options(request, runtime)

    async def evaluate_dedicated_host_instance_resource_async(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_dedicated_host_instance_resource_with_options_async(request, runtime)

    def get_db_proxy_instance_ssl_with_options(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbInstanceId'] = request.db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GetDbProxyInstanceSslResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_db_proxy_instance_ssl_with_options_async(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbInstanceId'] = request.db_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GetDbProxyInstanceSslResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_db_proxy_instance_ssl(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_db_proxy_instance_ssl_with_options(request, runtime)

    async def get_db_proxy_instance_ssl_async(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_db_proxy_instance_ssl_with_options_async(request, runtime)

    def grant_account_privilege_with_options(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['DBName'] = request.dbname
        query['AccountPrivilege'] = request.account_privilege
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_account_privilege_with_options_async(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['DBName'] = request.dbname
        query['AccountPrivilege'] = request.account_privilege
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_account_privilege(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    async def grant_account_privilege_async(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_account_privilege_with_options_async(request, runtime)

    def grant_operator_permission_with_options(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ExpiredTime'] = request.expired_time
        query['Privileges'] = request.privileges
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_operator_permission_with_options_async(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ExpiredTime'] = request.expired_time
        query['Privileges'] = request.privileges
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_operator_permission(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    async def grant_operator_permission_async(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_operator_permission_with_options_async(request, runtime)

    def import_database_between_instances_with_options(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SourceDBInstanceId'] = request.source_dbinstance_id
        query['DBInfo'] = request.dbinfo
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportDatabaseBetweenInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_database_between_instances_with_options_async(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SourceDBInstanceId'] = request.source_dbinstance_id
        query['DBInfo'] = request.dbinfo
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportDatabaseBetweenInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_database_between_instances(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_database_between_instances_with_options(request, runtime)

    async def import_database_between_instances_async(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_database_between_instances_with_options_async(request, runtime)

    def import_user_backup_file_with_options(
        self,
        request: rds_20140815_models.ImportUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ImportUserBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EngineVersion'] = request.engine_version
        query['BucketRegion'] = request.bucket_region
        query['BackupFile'] = request.backup_file
        query['Comment'] = request.comment
        query['RestoreSize'] = request.restore_size
        query['Retention'] = request.retention
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_user_backup_file_with_options_async(
        self,
        request: rds_20140815_models.ImportUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ImportUserBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EngineVersion'] = request.engine_version
        query['BucketRegion'] = request.bucket_region
        query['BackupFile'] = request.backup_file
        query['Comment'] = request.comment
        query['RestoreSize'] = request.restore_size
        query['Retention'] = request.retention
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportUserBackupFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_user_backup_file(
        self,
        request: rds_20140815_models.ImportUserBackupFileRequest,
    ) -> rds_20140815_models.ImportUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_user_backup_file_with_options(request, runtime)

    async def import_user_backup_file_async(
        self,
        request: rds_20140815_models.ImportUserBackupFileRequest,
    ) -> rds_20140815_models.ImportUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_user_backup_file_with_options_async(request, runtime)

    def list_classes_with_options(
        self,
        request: rds_20140815_models.ListClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['CommodityCode'] = request.commodity_code
        query['DBInstanceId'] = request.dbinstance_id
        query['OrderType'] = request.order_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_classes_with_options_async(
        self,
        request: rds_20140815_models.ListClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListClassesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['CommodityCode'] = request.commodity_code
        query['DBInstanceId'] = request.dbinstance_id
        query['OrderType'] = request.order_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_classes(
        self,
        request: rds_20140815_models.ListClassesRequest,
    ) -> rds_20140815_models.ListClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_classes_with_options(request, runtime)

    async def list_classes_async(
        self,
        request: rds_20140815_models.ListClassesRequest,
    ) -> rds_20140815_models.ListClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_classes_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_backup_files_with_options(
        self,
        request: rds_20140815_models.ListUserBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListUserBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['BackupId'] = request.backup_id
        query['OssUrl'] = request.oss_url
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUserBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListUserBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_backup_files_with_options_async(
        self,
        request: rds_20140815_models.ListUserBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListUserBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['BackupId'] = request.backup_id
        query['OssUrl'] = request.oss_url
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUserBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListUserBackupFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_backup_files(
        self,
        request: rds_20140815_models.ListUserBackupFilesRequest,
    ) -> rds_20140815_models.ListUserBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_backup_files_with_options(request, runtime)

    async def list_user_backup_files_async(
        self,
        request: rds_20140815_models.ListUserBackupFilesRequest,
    ) -> rds_20140815_models.ListUserBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_backup_files_with_options_async(request, runtime)

    def lock_account_with_options(
        self,
        request: rds_20140815_models.LockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.LockAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.LockAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_account_with_options_async(
        self,
        request: rds_20140815_models.LockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.LockAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.LockAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_account(
        self,
        request: rds_20140815_models.LockAccountRequest,
    ) -> rds_20140815_models.LockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_account_with_options(request, runtime)

    async def lock_account_async(
        self,
        request: rds_20140815_models.LockAccountRequest,
    ) -> rds_20140815_models.LockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_account_with_options_async(request, runtime)

    def migrate_dbinstance_with_options(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['EffectiveTime'] = request.effective_time
        query['SpecifiedTime'] = request.specified_time
        query['ZoneIdForLog'] = request.zone_id_for_log
        query['ZoneIdForFollower'] = request.zone_id_for_follower
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['EffectiveTime'] = request.effective_time
        query['SpecifiedTime'] = request.specified_time
        query['ZoneIdForLog'] = request.zone_id_for_log
        query['ZoneIdForFollower'] = request.zone_id_for_follower
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_dbinstance(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    async def migrate_dbinstance_async(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_dbinstance_with_options_async(request, runtime)

    def migrate_security_ipmode_with_options(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateSecurityIPMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateSecurityIPModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_security_ipmode_with_options_async(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateSecurityIPMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateSecurityIPModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_security_ipmode(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_security_ipmode_with_options(request, runtime)

    async def migrate_security_ipmode_async(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_security_ipmode_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['VPCId'] = request.vpcid
        query['ZoneId'] = request.zone_id
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        query['VSwitchId'] = request.v_switch_id
        query['Category'] = request.category
        query['ZoneIdSlave1'] = request.zone_id_slave_1
        query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['VPCId'] = request.vpcid
        query['ZoneId'] = request.zone_id
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        query['VSwitchId'] = request.v_switch_id
        query['Category'] = request.category
        query['ZoneIdSlave1'] = request.zone_id_slave_1
        query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateToOtherZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountDescription'] = request.account_description
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountDescription'] = request.account_description
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_action_event_policy_with_options(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EnableEventLog'] = request.enable_event_log
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyActionEventPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_action_event_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EnableEventLog'] = request.enable_event_log
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyActionEventPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_action_event_policy(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_policy_with_options(request, runtime)

    async def modify_action_event_policy_async(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_action_event_policy_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupPolicyMode'] = request.backup_policy_mode
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['BackupLog'] = request.backup_log
        query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        query['OwnerAccount'] = request.owner_account
        query['EnableBackupLog'] = request.enable_backup_log
        query['LocalLogRetentionHours'] = request.local_log_retention_hours
        query['LocalLogRetentionSpace'] = request.local_log_retention_space
        query['HighSpaceUsageProtection'] = request.high_space_usage_protection
        query['LogBackupFrequency'] = request.log_backup_frequency
        query['CompressType'] = request.compress_type
        query['ArchiveBackupRetentionPeriod'] = request.archive_backup_retention_period
        query['ArchiveBackupKeepPolicy'] = request.archive_backup_keep_policy
        query['ArchiveBackupKeepCount'] = request.archive_backup_keep_count
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        query['LogBackupLocalRetentionNumber'] = request.log_backup_local_retention_number
        query['Category'] = request.category
        query['BackupInterval'] = request.backup_interval
        query['BackupMethod'] = request.backup_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupPolicyMode'] = request.backup_policy_mode
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['BackupLog'] = request.backup_log
        query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        query['OwnerAccount'] = request.owner_account
        query['EnableBackupLog'] = request.enable_backup_log
        query['LocalLogRetentionHours'] = request.local_log_retention_hours
        query['LocalLogRetentionSpace'] = request.local_log_retention_space
        query['HighSpaceUsageProtection'] = request.high_space_usage_protection
        query['LogBackupFrequency'] = request.log_backup_frequency
        query['CompressType'] = request.compress_type
        query['ArchiveBackupRetentionPeriod'] = request.archive_backup_retention_period
        query['ArchiveBackupKeepPolicy'] = request.archive_backup_keep_policy
        query['ArchiveBackupKeepCount'] = request.archive_backup_keep_count
        query['ReleasedKeepPolicy'] = request.released_keep_policy
        query['LogBackupLocalRetentionNumber'] = request.log_backup_local_retention_number
        query['Category'] = request.category
        query['BackupInterval'] = request.backup_interval
        query['BackupMethod'] = request.backup_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_collation_time_zone_with_options(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Collation'] = request.collation
        query['Timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyCollationTimeZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyCollationTimeZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_collation_time_zone_with_options_async(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Collation'] = request.collation
        query['Timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyCollationTimeZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyCollationTimeZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_collation_time_zone(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_collation_time_zone_with_options(request, runtime)

    async def modify_collation_time_zone_async(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_collation_time_zone_with_options_async(request, runtime)

    def modify_das_instance_config_with_options(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['StorageAutoScale'] = request.storage_auto_scale
        query['StorageThreshold'] = request.storage_threshold
        query['StorageUpperBound'] = request.storage_upper_bound
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDasInstanceConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDasInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_das_instance_config_with_options_async(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['StorageAutoScale'] = request.storage_auto_scale
        query['StorageThreshold'] = request.storage_threshold
        query['StorageUpperBound'] = request.storage_upper_bound
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDasInstanceConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDasInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_das_instance_config(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_das_instance_config_with_options(request, runtime)

    async def modify_das_instance_config_async(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_das_instance_config_with_options_async(request, runtime)

    def modify_dbdescription_with_options(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['DBDescription'] = request.dbdescription
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbdescription_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBName'] = request.dbname
        query['DBDescription'] = request.dbdescription
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbdescription(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    async def modify_dbdescription_async(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbdescription_with_options_async(request, runtime)

    def modify_dbinstance_auto_upgrade_minor_version_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['AutoUpgradeMinorVersion'] = request.auto_upgrade_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAutoUpgradeMinorVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_auto_upgrade_minor_version_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['AutoUpgradeMinorVersion'] = request.auto_upgrade_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAutoUpgradeMinorVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_auto_upgrade_minor_version(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_auto_upgrade_minor_version_with_options(request, runtime)

    async def modify_dbinstance_auto_upgrade_minor_version_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_auto_upgrade_minor_version_with_options_async(request, runtime)

    def modify_dbinstance_connection_mode_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionMode'] = request.connection_mode
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_mode_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionMode'] = request.connection_mode
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_mode(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionModeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_mode_with_options(request, runtime)

    async def modify_dbinstance_connection_mode_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionModeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_mode_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceDescription'] = request.dbinstance_description
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceDescription'] = request.dbinstance_description
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_haconfig_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SyncMode'] = request.sync_mode
        query['HAMode'] = request.hamode
        query['DbInstanceId'] = request.db_instance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceHAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_haconfig_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SyncMode'] = request.sync_mode
        query['HAMode'] = request.hamode
        query['DbInstanceId'] = request.db_instance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceHAConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_haconfig(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_haconfig_with_options(request, runtime)

    async def modify_dbinstance_haconfig_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_haconfig_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['MaintainTime'] = request.maintain_time
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['MaintainTime'] = request.maintain_time
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_monitor_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Period'] = request.period
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_monitor_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Period'] = request.period
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_monitor(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    async def modify_dbinstance_monitor_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_monitor_with_options_async(request, runtime)

    def modify_dbinstance_network_expire_time_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionString'] = request.connection_string
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_network_expire_time_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionString'] = request.connection_string
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_network_expire_time(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_expire_time_with_options(request, runtime)

    async def modify_dbinstance_network_expire_time_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_network_expire_time_with_options_async(request, runtime)

    def modify_dbinstance_network_type_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RetainClassic'] = request.retain_classic
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['InstanceNetworkType'] = request.instance_network_type
        query['ReadWriteSplittingClassicExpiredDays'] = request.read_write_splitting_classic_expired_days
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['ReadWriteSplittingPrivateIpAddress'] = request.read_write_splitting_private_ip_address
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RetainClassic'] = request.retain_classic
        query['ClassicExpiredDays'] = request.classic_expired_days
        query['InstanceNetworkType'] = request.instance_network_type
        query['ReadWriteSplittingClassicExpiredDays'] = request.read_write_splitting_classic_expired_days
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['ReadWriteSplittingPrivateIpAddress'] = request.read_write_splitting_private_ip_address
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_network_type(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    async def modify_dbinstance_network_type_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_network_type_with_options_async(request, runtime)

    def modify_dbinstance_pay_type_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UsedTime'] = request.used_time
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_pay_type_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UsedTime'] = request.used_time
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstancePayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_pay_type(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_pay_type_with_options(request, runtime)

    async def modify_dbinstance_pay_type_async(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_pay_type_with_options_async(request, runtime)

    def modify_dbinstance_proxy_configuration_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ProxyConfigurationKey'] = request.proxy_configuration_key
        query['ProxyConfigurationValue'] = request.proxy_configuration_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_proxy_configuration_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ProxyConfigurationKey'] = request.proxy_configuration_key
        query['ProxyConfigurationValue'] = request.proxy_configuration_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_proxy_configuration(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_proxy_configuration_with_options(request, runtime)

    async def modify_dbinstance_proxy_configuration_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_proxy_configuration_with_options_async(request, runtime)

    def modify_dbinstance_spec_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        query['EngineVersion'] = request.engine_version
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Direction'] = request.direction
        query['SourceBiz'] = request.source_biz
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSpec',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_spec_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        query['EngineVersion'] = request.engine_version
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        query['Direction'] = request.direction
        query['SourceBiz'] = request.source_biz
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSpec',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_spec(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    async def modify_dbinstance_spec_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_spec_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionString'] = request.connection_string
        query['OwnerAccount'] = request.owner_account
        query['SSLEnabled'] = request.sslenabled
        query['CAType'] = request.catype
        query['ServerCert'] = request.server_cert
        query['ServerKey'] = request.server_key
        query['ClientCAEnabled'] = request.client_caenabled
        query['ClientCACert'] = request.client_cacert
        query['ClientCrlEnabled'] = request.client_crl_enabled
        query['ClientCertRevocationList'] = request.client_cert_revocation_list
        query['ACL'] = request.acl
        query['ReplicationACL'] = request.replication_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionString'] = request.connection_string
        query['OwnerAccount'] = request.owner_account
        query['SSLEnabled'] = request.sslenabled
        query['CAType'] = request.catype
        query['ServerCert'] = request.server_cert
        query['ServerKey'] = request.server_key
        query['ClientCAEnabled'] = request.client_caenabled
        query['ClientCACert'] = request.client_cacert
        query['ClientCrlEnabled'] = request.client_crl_enabled
        query['ClientCertRevocationList'] = request.client_cert_revocation_list
        query['ACL'] = request.acl
        query['ReplicationACL'] = request.replication_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_ssl(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    async def modify_dbinstance_ssl_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_sslwith_options_async(request, runtime)

    def modify_dbinstance_tdewith_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TDEStatus'] = request.tdestatus
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        query['EncryptionKey'] = request.encryption_key
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_tdewith_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TDEStatus'] = request.tdestatus
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        query['EncryptionKey'] = request.encryption_key
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_tde(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    async def modify_dbinstance_tde_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_tdewith_options_async(request, runtime)

    def modify_dbproxy_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConfigDBProxyService'] = request.config_dbproxy_service
        query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        query['RegionId'] = request.region_id
        query['InstanceNetworkType'] = request.instance_network_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbproxy_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ConfigDBProxyService'] = request.config_dbproxy_service
        query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        query['RegionId'] = request.region_id
        query['InstanceNetworkType'] = request.instance_network_type
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbproxy(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_with_options(request, runtime)

    async def modify_dbproxy_async(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_with_options_async(request, runtime)

    def modify_dbproxy_endpoint_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['ConfigDBProxyFeatures'] = request.config_dbproxy_features
        query['RegionId'] = request.region_id
        query['ReadOnlyInstanceMaxDelayTime'] = request.read_only_instance_max_delay_time
        query['ReadOnlyInstanceDistributionType'] = request.read_only_instance_distribution_type
        query['ReadOnlyInstanceWeight'] = request.read_only_instance_weight
        query['DBInstanceId'] = request.dbinstance_id
        query['DbEndpointOperator'] = request.db_endpoint_operator
        query['DbEndpointAliases'] = request.db_endpoint_aliases
        query['DbEndpointType'] = request.db_endpoint_type
        query['DbEndpointReadWriteMode'] = request.db_endpoint_read_write_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbproxy_endpoint_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['ConfigDBProxyFeatures'] = request.config_dbproxy_features
        query['RegionId'] = request.region_id
        query['ReadOnlyInstanceMaxDelayTime'] = request.read_only_instance_max_delay_time
        query['ReadOnlyInstanceDistributionType'] = request.read_only_instance_distribution_type
        query['ReadOnlyInstanceWeight'] = request.read_only_instance_weight
        query['DBInstanceId'] = request.dbinstance_id
        query['DbEndpointOperator'] = request.db_endpoint_operator
        query['DbEndpointAliases'] = request.db_endpoint_aliases
        query['DbEndpointType'] = request.db_endpoint_type
        query['DbEndpointReadWriteMode'] = request.db_endpoint_read_write_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbproxy_endpoint(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_with_options(request, runtime)

    async def modify_dbproxy_endpoint_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_endpoint_with_options_async(request, runtime)

    def modify_dbproxy_endpoint_address_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyNewConnectString'] = request.dbproxy_new_connect_string
        query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbproxy_endpoint_address_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        query['DBProxyNewConnectString'] = request.dbproxy_new_connect_string
        query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbproxy_endpoint_address(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_address_with_options(request, runtime)

    async def modify_dbproxy_endpoint_address_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_endpoint_address_with_options_async(request, runtime)

    def modify_dbproxy_instance_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyInstanceType'] = request.dbproxy_instance_type
        query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        query['EffectiveTime'] = request.effective_time
        query['EffectiveSpecificTime'] = request.effective_specific_time
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbproxy_instance_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DBProxyInstanceType'] = request.dbproxy_instance_type
        query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        query['EffectiveTime'] = request.effective_time
        query['EffectiveSpecificTime'] = request.effective_specific_time
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbproxy_instance(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_instance_with_options(request, runtime)

    async def modify_dbproxy_instance_async(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_instance_with_options_async(request, runtime)

    def modify_db_proxy_instance_ssl_with_options(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbProxyEndpointId'] = request.db_proxy_endpoint_id
        query['DbProxyConnectString'] = request.db_proxy_connect_string
        query['DbProxySslEnabled'] = request.db_proxy_ssl_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDbProxyInstanceSslResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_db_proxy_instance_ssl_with_options_async(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbInstanceId'] = request.db_instance_id
        query['DbProxyEndpointId'] = request.db_proxy_endpoint_id
        query['DbProxyConnectString'] = request.db_proxy_connect_string
        query['DbProxySslEnabled'] = request.db_proxy_ssl_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDbProxyInstanceSslResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_db_proxy_instance_ssl(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_db_proxy_instance_ssl_with_options(request, runtime)

    async def modify_db_proxy_instance_ssl_async(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_db_proxy_instance_ssl_with_options_async(request, runtime)

    def modify_dedicated_host_account_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_account_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_account(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    async def modify_dedicated_host_account_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_account_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['HostName'] = request.host_name
        query['AllocationStatus'] = request.allocation_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_attribute_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['HostName'] = request.host_name
        query['AllocationStatus'] = request.allocation_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_attribute(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['AllocationPolicy'] = request.allocation_policy
        query['HostReplacePolicy'] = request.host_replace_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostGroupAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_group_attribute_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['AllocationPolicy'] = request.allocation_policy
        query['HostReplacePolicy'] = request.host_replace_policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostGroupAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_group_attribute(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    async def modify_dedicated_host_group_attribute_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_group_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_user_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['OldPassword'] = request.old_password
        query['NewPassword'] = request.new_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_user_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DedicatedHostName'] = request.dedicated_host_name
        query['UserName'] = request.user_name
        query['OldPassword'] = request.old_password
        query['NewPassword'] = request.new_password
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostUser',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDedicatedHostUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_user(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_user_with_options(request, runtime)

    async def modify_dedicated_host_user_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_user_with_options_async(request, runtime)

    def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityIpHosts'] = request.security_ip_hosts
        query['WhiteListGroupName'] = request.white_list_group_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityIpHosts'] = request.security_ip_hosts
        query['WhiteListGroupName'] = request.white_list_group_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dtcsecurity_ip_hosts_for_sqlserver(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    async def modify_dtcsecurity_ip_hosts_for_sqlserver_async(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(request, runtime)

    def modify_hadiagnose_config_with_options(
        self,
        request: rds_20140815_models.ModifyHADiagnoseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyHADiagnoseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TcpConnectionType'] = request.tcp_connection_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHADiagnoseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hadiagnose_config_with_options_async(
        self,
        request: rds_20140815_models.ModifyHADiagnoseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyHADiagnoseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TcpConnectionType'] = request.tcp_connection_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHADiagnoseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hadiagnose_config(
        self,
        request: rds_20140815_models.ModifyHADiagnoseConfigRequest,
    ) -> rds_20140815_models.ModifyHADiagnoseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_hadiagnose_config_with_options(request, runtime)

    async def modify_hadiagnose_config_async(
        self,
        request: rds_20140815_models.ModifyHADiagnoseConfigRequest,
    ) -> rds_20140815_models.ModifyHADiagnoseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hadiagnose_config_with_options_async(request, runtime)

    def modify_haswitch_config_with_options(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['HAConfig'] = request.haconfig
        query['ManualHATime'] = request.manual_hatime
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHASwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_haswitch_config_with_options_async(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['HAConfig'] = request.haconfig
        query['ManualHATime'] = request.manual_hatime
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHASwitchConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_haswitch_config(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_haswitch_config_with_options(request, runtime)

    async def modify_haswitch_config_async(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_haswitch_config_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['Duration'] = request.duration
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['Duration'] = request.duration
        query['AutoRenew'] = request.auto_renew
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_cross_backup_policy_with_options(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupType'] = request.cross_backup_type
        query['LogBackupEnabled'] = request.log_backup_enabled
        query['BackupEnabled'] = request.backup_enabled
        query['CrossBackupRegion'] = request.cross_backup_region
        query['RetentType'] = request.retent_type
        query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_cross_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['CrossBackupType'] = request.cross_backup_type
        query['LogBackupEnabled'] = request.log_backup_enabled
        query['BackupEnabled'] = request.backup_enabled
        query['CrossBackupRegion'] = request.cross_backup_region
        query['RetentType'] = request.retent_type
        query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_cross_backup_policy(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_cross_backup_policy_with_options(request, runtime)

    async def modify_instance_cross_backup_policy_async(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_cross_backup_policy_with_options_async(request, runtime)

    def modify_parameter_with_options(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Parameters'] = request.parameters
        query['Forcerestart'] = request.forcerestart
        query['OwnerAccount'] = request.owner_account
        query['ParameterGroupId'] = request.parameter_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyParameter',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameter_with_options_async(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Parameters'] = request.parameters
        query['Forcerestart'] = request.forcerestart
        query['OwnerAccount'] = request.owner_account
        query['ParameterGroupId'] = request.parameter_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyParameter',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameter(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
    ) -> rds_20140815_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    async def modify_parameter_async(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
    ) -> rds_20140815_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_with_options_async(request, runtime)

    def modify_parameter_group_with_options(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['ParameterGroupDesc'] = request.parameter_group_desc
        query['Parameters'] = request.parameters
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ParameterGroupId'] = request.parameter_group_id
        query['ParameterGroupName'] = request.parameter_group_name
        query['ParameterGroupDesc'] = request.parameter_group_desc
        query['Parameters'] = request.parameters
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameter_group(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_group_with_options(request, runtime)

    async def modify_parameter_group_async(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_group_with_options_async(request, runtime)

    def modify_readonly_instance_delay_replication_time_with_options(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ReadSQLReplicationTime'] = request.read_sqlreplication_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadonlyInstanceDelayReplicationTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_readonly_instance_delay_replication_time_with_options_async(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['ReadSQLReplicationTime'] = request.read_sqlreplication_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadonlyInstanceDelayReplicationTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_readonly_instance_delay_replication_time(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_readonly_instance_delay_replication_time_with_options(request, runtime)

    async def modify_readonly_instance_delay_replication_time_async(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_readonly_instance_delay_replication_time_with_options_async(request, runtime)

    def modify_read_write_splitting_connection_with_options(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['MaxDelayTime'] = request.max_delay_time
        query['DistributionType'] = request.distribution_type
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_read_write_splitting_connection_with_options_async(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['MaxDelayTime'] = request.max_delay_time
        query['DistributionType'] = request.distribution_type
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadWriteSplittingConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_read_write_splitting_connection(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_read_write_splitting_connection_with_options(request, runtime)

    async def modify_read_write_splitting_connection_async(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_read_write_splitting_connection_with_options_async(request, runtime)

    def modify_resource_group_with_options(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourceGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_group_with_options_async(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourceGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_group(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    async def modify_resource_group_async(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_group_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityIps'] = request.security_ips
        query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        query['SecurityIPType'] = request.security_iptype
        query['WhitelistNetworkType'] = request.whitelist_network_type
        query['ModifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SecurityIps'] = request.security_ips
        query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        query['SecurityIPType'] = request.security_iptype
        query['WhitelistNetworkType'] = request.whitelist_network_type
        query['ModifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_sqlcollector_policy_with_options(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLCollectorStatus'] = request.sqlcollector_status
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sqlcollector_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['SQLCollectorStatus'] = request.sqlcollector_status
        query['OwnerAccount'] = request.owner_account
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sqlcollector_policy(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    async def modify_sqlcollector_policy_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sqlcollector_policy_with_options_async(request, runtime)

    def modify_sqlcollector_retention_with_options(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConfigValue'] = request.config_value
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorRetentionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sqlcollector_retention_with_options_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['ConfigValue'] = request.config_value
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorRetentionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sqlcollector_retention(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_retention_with_options(request, runtime)

    async def modify_sqlcollector_retention_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sqlcollector_retention_with_options_async(request, runtime)

    def purge_dbinstance_log_with_options(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PurgeDBInstanceLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.PurgeDBInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def purge_dbinstance_log_with_options_async(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PurgeDBInstanceLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.PurgeDBInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purge_dbinstance_log(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.purge_dbinstance_log_with_options(request, runtime)

    async def purge_dbinstance_log_async(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purge_dbinstance_log_with_options_async(request, runtime)

    def rebuild_dbinstance_with_options(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['RebuildNodeType'] = request.rebuild_node_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RebuildDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RebuildDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebuild_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['RebuildNodeType'] = request.rebuild_node_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RebuildDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RebuildDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebuild_dbinstance(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebuild_dbinstance_with_options(request, runtime)

    async def rebuild_dbinstance_async(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebuild_dbinstance_with_options_async(request, runtime)

    def recovery_dbinstance_with_options(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['InstanceNetworkType'] = request.instance_network_type
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDBInstanceId'] = request.target_dbinstance_id
        query['DbNames'] = request.db_names
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RecoveryDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RecoveryDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceClass'] = request.dbinstance_class
        query['DBInstanceStorage'] = request.dbinstance_storage
        query['PayType'] = request.pay_type
        query['InstanceNetworkType'] = request.instance_network_type
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDBInstanceId'] = request.target_dbinstance_id
        query['DbNames'] = request.db_names
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        query['UsedTime'] = request.used_time
        query['Period'] = request.period
        query['DBInstanceStorageType'] = request.dbinstance_storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RecoveryDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RecoveryDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_dbinstance(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recovery_dbinstance_with_options(request, runtime)

    async def recovery_dbinstance_async(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recovery_dbinstance_with_options_async(request, runtime)

    def release_instance_connection_with_options(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['InstanceNetworkType'] = request.instance_network_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstanceConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstanceConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_connection_with_options_async(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['InstanceNetworkType'] = request.instance_network_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstanceConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstanceConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_connection(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_connection_with_options(request, runtime)

    async def release_instance_connection_async(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_connection_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['CurrentConnectionString'] = request.current_connection_string
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def release_read_write_splitting_connection_with_options(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_read_write_splitting_connection_with_options_async(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_read_write_splitting_connection(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_read_write_splitting_connection_with_options(request, runtime)

    async def release_read_write_splitting_connection_async(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_read_write_splitting_connection_with_options_async(request, runtime)

    def remove_tags_from_resource_with_options(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTagsFromResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RemoveTagsFromResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tags_from_resource_with_options_async(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['proxyId'] = request.proxy_id
        query['RegionId'] = request.region_id
        query['DBInstanceId'] = request.dbinstance_id
        query['Tags'] = request.tags
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTagsFromResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RemoveTagsFromResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tags_from_resource(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_from_resource_with_options(request, runtime)

    async def remove_tags_from_resource_async(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_from_resource_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Period'] = request.period
        query['AutoPay'] = request.auto_pay
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['Period'] = request.period
        query['AutoPay'] = request.auto_pay
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
    ) -> rds_20140815_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
    ) -> rds_20140815_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def replace_dedicated_host_with_options(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReplaceDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReplaceDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReplaceDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReplaceDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_dedicated_host(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    async def replace_dedicated_host_async(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_dedicated_host_with_options_async(request, runtime)

    def reset_account_with_options(
        self,
        request: rds_20140815_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_with_options_async(
        self,
        request: rds_20140815_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account(
        self,
        request: rds_20140815_models.ResetAccountRequest,
    ) -> rds_20140815_models.ResetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    async def reset_account_async(
        self,
        request: rds_20140815_models.ResetAccountRequest,
    ) -> rds_20140815_models.ResetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def restart_dedicated_host_with_options(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartDedicatedHost',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dedicated_host(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    async def restart_dedicated_host_async(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dedicated_host_with_options_async(request, runtime)

    def restore_ddr_table_with_options(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['RestoreType'] = request.restore_type
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestoreDdrTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreDdrTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_ddr_table_with_options_async(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['RestoreType'] = request.restore_type
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['SourceRegion'] = request.source_region
        query['SourceDBInstanceName'] = request.source_dbinstance_name
        query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestoreDdrTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreDdrTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_ddr_table(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_ddr_table_with_options(request, runtime)

    async def restore_ddr_table_async(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_ddr_table_with_options_async(request, runtime)

    def restore_table_with_options(
        self,
        request: rds_20140815_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['OwnerAccount'] = request.owner_account
        query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestoreTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_table_with_options_async(
        self,
        request: rds_20140815_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['BackupId'] = request.backup_id
        query['RestoreTime'] = request.restore_time
        query['OwnerAccount'] = request.owner_account
        query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestoreTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_table(
        self,
        request: rds_20140815_models.RestoreTableRequest,
    ) -> rds_20140815_models.RestoreTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    async def restore_table_async(
        self,
        request: rds_20140815_models.RestoreTableRequest,
    ) -> rds_20140815_models.RestoreTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_table_with_options_async(request, runtime)

    def revoke_account_privilege_with_options(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokeAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_account_privilege_with_options_async(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        query['DBName'] = request.dbname
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokeAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_account_privilege(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    async def revoke_account_privilege_async(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_account_privilege_with_options_async(request, runtime)

    def revoke_operator_permission_with_options(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokeOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_operator_permission_with_options_async(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokeOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeOperatorPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_operator_permission(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    async def revoke_operator_permission_async(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_operator_permission_with_options_async(request, runtime)

    def start_dbinstance_with_options(
        self,
        request: rds_20140815_models.StartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.StartDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        query['EffectiveTime'] = request.effective_time
        query['SpecifiedTime'] = request.specified_time
        query['TargetDBInstanceClass'] = request.target_dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['DBInstanceTransType'] = request.dbinstance_trans_type
        query['Storage'] = request.storage
        query['VSwitchId'] = request.v_switch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.StartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.StartDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DBInstanceId'] = request.dbinstance_id
        query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        query['EffectiveTime'] = request.effective_time
        query['SpecifiedTime'] = request.specified_time
        query['TargetDBInstanceClass'] = request.target_dbinstance_class
        query['EngineVersion'] = request.engine_version
        query['DBInstanceTransType'] = request.dbinstance_trans_type
        query['Storage'] = request.storage
        query['VSwitchId'] = request.v_switch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dbinstance(
        self,
        request: rds_20140815_models.StartDBInstanceRequest,
    ) -> rds_20140815_models.StartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_dbinstance_with_options(request, runtime)

    async def start_dbinstance_async(
        self,
        request: rds_20140815_models.StartDBInstanceRequest,
    ) -> rds_20140815_models.StartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_dbinstance_with_options_async(request, runtime)

    def stop_dbinstance_with_options(
        self,
        request: rds_20140815_models.StopDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.StopDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StopDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.StopDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.StopDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StopDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dbinstance(
        self,
        request: rds_20140815_models.StopDBInstanceRequest,
    ) -> rds_20140815_models.StopDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_dbinstance_with_options(request, runtime)

    async def stop_dbinstance_async(
        self,
        request: rds_20140815_models.StopDBInstanceRequest,
    ) -> rds_20140815_models.StopDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_dbinstance_with_options_async(request, runtime)

    def switch_dbinstance_hawith_options(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['NodeId'] = request.node_id
        query['Force'] = request.force
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_hawith_options_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['NodeId'] = request.node_id
        query['Force'] = request.force
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dbinstance_ha(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    async def switch_dbinstance_ha_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_hawith_options_async(request, runtime)

    def switch_dbinstance_net_type_with_options(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['ConnectionStringType'] = request.connection_string_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceNetType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceNetTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_net_type_with_options_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['Port'] = request.port
        query['ConnectionStringType'] = request.connection_string_type
        query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceNetType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceNetTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dbinstance_net_type(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    async def switch_dbinstance_net_type_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_net_type_with_options_async(request, runtime)

    def switch_dbinstance_vpc_with_options(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceVpc',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_vpc_with_options_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceVpc',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dbinstance_vpc(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_vpc_with_options(request, runtime)

    async def switch_dbinstance_vpc_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_vpc_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: rds_20140815_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: rds_20140815_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: rds_20140815_models.TagResourcesRequest,
    ) -> rds_20140815_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: rds_20140815_models.TagResourcesRequest,
    ) -> rds_20140815_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def terminate_migrate_task_with_options(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TerminateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TerminateMigrateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_migrate_task_with_options_async(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['MigrateTaskId'] = request.migrate_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TerminateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TerminateMigrateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_migrate_task(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_migrate_task_with_options(request, runtime)

    async def terminate_migrate_task_async(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_migrate_task_with_options_async(request, runtime)

    def transform_dbinstance_pay_type_with_options(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['UsedTime'] = request.used_time
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['BusinessInfo'] = request.business_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransformDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TransformDBInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_dbinstance_pay_type_with_options_async(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['OwnerAccount'] = request.owner_account
        query['DBInstanceId'] = request.dbinstance_id
        query['UsedTime'] = request.used_time
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['BusinessInfo'] = request.business_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransformDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TransformDBInstancePayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_dbinstance_pay_type(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_dbinstance_pay_type_with_options(request, runtime)

    async def transform_dbinstance_pay_type_async(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_dbinstance_pay_type_with_options_async(request, runtime)

    def unlock_account_with_options(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UnlockAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnlockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UnlockAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_account_with_options_async(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UnlockAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['AccountName'] = request.account_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnlockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UnlockAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_account(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
    ) -> rds_20140815_models.UnlockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_account_with_options(request, runtime)

    async def unlock_account_async(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
    ) -> rds_20140815_models.UnlockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_account_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
    ) -> rds_20140815_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
    ) -> rds_20140815_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_user_backup_file_with_options(
        self,
        request: rds_20140815_models.UpdateUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpdateUserBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupId'] = request.backup_id
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpdateUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_backup_file_with_options_async(
        self,
        request: rds_20140815_models.UpdateUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpdateUserBackupFileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BackupId'] = request.backup_id
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpdateUserBackupFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_backup_file(
        self,
        request: rds_20140815_models.UpdateUserBackupFileRequest,
    ) -> rds_20140815_models.UpdateUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_backup_file_with_options(request, runtime)

    async def update_user_backup_file_async(
        self,
        request: rds_20140815_models.UpdateUserBackupFileRequest,
    ) -> rds_20140815_models.UpdateUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_backup_file_with_options_async(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['EngineVersion'] = request.engine_version
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_engine_version_with_options_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClientToken'] = request.client_token
        query['DBInstanceId'] = request.dbinstance_id
        query['EngineVersion'] = request.engine_version
        query['OwnerAccount'] = request.owner_account
        query['EffectiveTime'] = request.effective_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_engine_version(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    async def upgrade_dbinstance_engine_version_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_engine_version_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UpgradeTime'] = request.upgrade_time
        query['SwitchTime'] = request.switch_time
        query['TargetMinorVersion'] = request.target_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UpgradeTime'] = request.upgrade_time
        query['SwitchTime'] = request.switch_time
        query['TargetMinorVersion'] = request.target_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)

    def upgrade_dbproxy_instance_kernel_version_with_options(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UpgradeTime'] = request.upgrade_time
        query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBProxyInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbproxy_instance_kernel_version_with_options_async(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['DBInstanceId'] = request.dbinstance_id
        query['UpgradeTime'] = request.upgrade_time
        query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeDBProxyInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbproxy_instance_kernel_version(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbproxy_instance_kernel_version_with_options(request, runtime)

    async def upgrade_dbproxy_instance_kernel_version_async(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbproxy_instance_kernel_version_with_options_async(request, runtime)
